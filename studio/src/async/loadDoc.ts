import memo from 'memoizee';
import * as Doc from 'studio/foundation/doc';
import {loadDocBlob} from 'studio/async/loadDocs';
import * as Project from 'studio/state/project';
import {BlueprintSettings} from 'studio/state/settings';
import {Value as TheSessionContext} from 'studio/context/SessionContext';
import {stringify, writeString} from 'studio/util/stringifyForPython';
import * as Handle from 'studio/state/handle';

async function onDiskDocFileHandle(
  handle: Handle.t,
  docName: string):
    Promise<Handle.FileHandle>
{
  const subdirHandle = await handle.getDirectoryHandle('ocr');
  return subdirHandle.getFileHandle(`${docName}.json`);
}

async function rawLoadDoc(
  handle: Handle.t,
  docName: string,
  blueprintSettings: BlueprintSettings,
  sessionContext: TheSessionContext):
    Promise<Doc.t>
{
  console.log('Running loadDoc', handle, docName);

  const fileHandle = await onDiskDocFileHandle(handle, docName);
  console.log('Got filehandle for doc', fileHandle);

  const file = await fileHandle.getFile();
  const text = await file.text();
  const googleOCR = JSON.parse(text);
  console.log('Loaded raw Google OCR doc', googleOCR);

  const payload = {'google_ocr': googleOCR};

  const response = await fetch('http://localhost:5000/gen_bp_doc', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const json = await response.json();

  console.log('Got loadDoc response', handle, docName, json);

  const resultText = json.payload.results;
  const result = JSON.parse(resultText) as Doc.t;

  return result;
}

const loadDoc = memo(rawLoadDoc, {max: 500});

export default loadDoc;

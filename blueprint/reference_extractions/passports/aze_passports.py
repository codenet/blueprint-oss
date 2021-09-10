#!/usr/bin/env python3

from bp import *

sn = extract(
  text_equals('Soyadi/Surname')('sn_label'),
  is_top_down_label_value_pair('sn_label', 'sn')
)

fn = extract(
  text_equals('Adi, atasinin adi/Given name, patronymic', taper=4)('fn_label'),
  is_top_down_label_value_pair('fn_label', 'fn')
)

pob = extract(
  text_equals('Doguldugu yer/Place of birth', taper=8)('pob_label'),
  is_top_down_label_value_pair('pob_label', 'pob')
)

dob = extract(
  text_equals('Doguldugu tarix/Date of birth', taper=4)('dob_label'),
  is_date('dob'),
  is_top_down_label_value_pair('dob_label', 'dob')
)

doe = extract(
  is_date('doe'),
  is_top_down_label_value_pair('doe_label', 'doe'),
  text_equals('Etibarliliq muddati/Date of expiry', taper=4)('doe_label')
)

doi  = extract(
  text_equals('Verilma tarixi/Date of issue', taper=4)('doi_label'),
  is_date('doi'),
  is_top_down_label_value_pair('doi_label', 'doi')
)

sex = extract(
  is_top_down_label_value_pair('sex_label', 'sex'),
  text_equals('Cinsi/Sex', taper=3)('sex_label')
)

aze = combine(
  # sn, fn, doe, dob, doi, sex, pob
  pob
  # text_equals('Tip/Type')('type_label'),
  # text_equals('Olkenin kodu/Code of State')('state_label'),
  # text_equals('Pasportun nomrasi/Passport No')('num_label'),
  # text_equals('Vetendasligi/Nationality')('nation_label'),
  # text_equals('Fardi identifikasiya nomrasi/Personal No')('personal_no_label'),
  # text_equals('Pasportu veran orqan/Issuing authority')('auth_label'),


  # text_equals('AZE')('state'),
  # is_top_down_label_value_pair('state_label', 'state'),
  # is_top_down_label_value_pair('num_label', 'num'),

  # is_top_down_label_value_pair('nation_label', 'nation'),

  # is_top_down_label_value_pair('personal_no_label', 'personal_no'),

  # is_top_down_label_value_pair('auth_label', 'auth'),

  # row('type_label', 'state_label', 'num_label'),
  # row('dob_label', 'personal_no_label', 'sex_label'),

  #row('doi_label', 'doe_label'),

  # left_aligned_column('sn_label' 'fn_label', 'dob_label'),
  # left_aligned_column('type_label', 'sn_label' 'fn_label', 'nation_label', 'dob_label', 'pob_label', 'doi_label', 'auth_label'),
  # left_aligned_column('personal_no_label', 'doe_label'),

  # row('state', 'num'),
).with_name('AZE')


# Run on CLI
# ----------

config = Config(num_samples=100)

if __name__ == '__main__':
  bp_cli_main(aze, config=config)

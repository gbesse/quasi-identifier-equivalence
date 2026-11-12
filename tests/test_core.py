import unittest,copy,json
from quasi_identifier_equivalence import run
DEMO={'quasi_identifiers': ['age_band', 'area'], 'sensitive_field': 'condition', 'rows': [{'age_band': '20-29', 'area': 'A', 'condition': 'x'}, {'age_band': '20-29', 'area': 'A', 'condition': 'x'}, {'age_band': '30-39', 'area': 'A', 'condition': 'y'}]}
class DomainTests(unittest.TestCase):
 def test_small_equivalence_class(self):
  x=run(DEMO);self.assertEqual(x['minimum_class_size'],1);self.assertEqual(x['classes'][0]['row_indices'],[0,1])
 def test_large_group_can_have_sensitive_homogeneity(self):
  x=run(dict(DEMO,rows=DEMO['rows'][:2]));self.assertEqual(x['minimum_class_size'],2);self.assertEqual(x['minimum_distinct_sensitive'],1);self.assertFalse(x['anonymity_guaranteed'])
 def test_missing_field_not_imputed(self):
  x=copy.deepcopy(DEMO);del x['rows'][0]['area']
  with self.assertRaises(KeyError):run(x)

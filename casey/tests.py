import os
import unittest
from group_project import *


class TestJsonFile(unittest.TestCase):
    def setUp(self):
        pass

    def test_file_exist(self):
        self.assertTrue(os.path.exists('proposal.json'))

    def test_length_of_data(self):
        infile = read_file('proposal.json')
        self.assertTrue(len(infile['corpus']) >= 5)

    def test_diversity_labels(self):
        infile = read_file('proposal.json')
        lab_cnt = {}
        for dat in infile['corpus']:
            if not dat['label'] in lab_cnt:
                lab_cnt[dat['label']] = 0
            else:
                lab_cnt[dat['label']] += 1
        self.assertTrue(len(lab_cnt.keys()) > 1)
        for k in dat:
            self.assertTrue(dat[k] > 1)

    def test_author_names_emails(self):
        infile = read_file('proposal.json')
        names = infile['authors']
        emails = infile['emails']
        self.assertEqual(len(names), len(emails))
        self.assertFalse(len(names) == 0)


if __name__ == '__main__':
    unittest.main()

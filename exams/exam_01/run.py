#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import unittest


def mock_input_facts():
    facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True)]
    return facts


def mock_input_facts_one_invalid_item():
    facts = [
                ('gabriel', 'endereço', 'av rio branco, 109', True),
                ('gabriel', 'telefone', '98888-1111', True),
                ('gabriel', 'telefone', '56789-1010', False),
                ('joão', 'endereço', 'rua alice, 10', True),
                ('joão', 'endereço', 'rua bob, 88', True),
                ('joão', 'telefone', '234-5678', False),
                ('joão', 'telefone', '91234-5555', True),
                ('joão', 'telefone', '234-5678', False),
                ('spider-man', 'dimension', '32', True)
            ]
    return facts


def mock_input_schema():
    schema = [
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')]

    return schema


class TestFacts(unittest.TestCase):

    def test_return_get_schema(self):
        fact = mock_input_facts()[0]
        schema = utils.get_schema(fact, 1, mock_input_schema(), 0)

        self.assertEqual(schema[0], 'endereço')
        self.assertEqual(schema[1], 'cardinality')
        self.assertEqual(schema[2], 'one')

    def test_return_none_get_schema(self):
        fact = ('spider-man', 'another thing')
        schema = utils.get_schema(fact, 1, mock_input_schema(), 0)

        self.assertEqual(schema, None)

    def test_recent_facts_one_invalid_item(self):
        response = utils.recent_facts(mock_input_facts_one_invalid_item(), mock_input_schema())
        gabriel = response['gabriel']
        joao = response['joão']
        spider_man = response['spider-man']

        self.assertEqual(spider_man, 'the fact has data not mapping in the schema')
        self.assertEqual(gabriel['endereço'], 'av rio branco, 109')
        self.assertEqual(len(gabriel['telefone']), 1)
        self.assertEqual(joao['endereço'], 'rua bob, 88')
        self.assertEqual(len(joao['telefone']), 1)


if __name__ == '__main__':
    unittest.main()
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def recent_facts(facts, schema_list):
    name = 0
    title = 1
    data = 2
    valid = 3

    schema_key = 0
    cardinality = 2

    map_itens = {}

    for fact in facts:
        if fact[valid]:

            obj = map_itens.get(fact[name])
            schema = get_schema(fact, title, schema_list, schema_key)

            if schema is None:
                msg = 'the fact has data not mapping in the schema'
                map_itens[fact[name]] = msg
                print(msg)
                continue

            if obj is None:
                obj = {}
                map_itens[fact[name]] = obj

            if schema[cardinality] == 'one':
                obj[fact[title]] = fact[data]

            if schema[cardinality] == 'many':
                list = obj.get(fact[title])

                if list is None:
                    list = []
                    obj[fact[title]] = list

                list.append(fact[data])

    return map_itens


def get_schema(fact,
               position_title_fact,
               schema_list,
               position_key_schema):

    for schema in schema_list:
        if schema[position_key_schema] == fact[position_title_fact]:
            return schema


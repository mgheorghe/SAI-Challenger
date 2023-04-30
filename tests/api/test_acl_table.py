from pprint import pprint

import pytest


class TestSaiAclTable:
    # object with no parents

    def test_acl_table_create(self, npu):
        commands = [
            {
                'name': 'acl_table_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_acl_table_attr_entry_list_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_table_attr_entry_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'atrribute': 'SAI_ACL_TABLE_ATTR_ENTRY_LIST',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_acl_table_attr_available_acl_entry_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_table_attr_available_acl_entry_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'atrribute': 'SAI_ACL_TABLE_ATTR_AVAILABLE_ACL_ENTRY',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_acl_table_attr_available_acl_counter_get(self, npu):
        commands = [
            {
                'name': 'sai_acl_table_attr_available_acl_counter_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'atrribute': 'SAI_ACL_TABLE_ATTR_AVAILABLE_ACL_COUNTER',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_acl_table_remove(self, npu):
        commands = [
            {
                'name': 'acl_table_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ACL_TABLE',
                'attributes': ['SAI_ACL_TABLE_ATTR_ACL_STAGE', 'SAI_ACL_STAGE_INGRESS'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

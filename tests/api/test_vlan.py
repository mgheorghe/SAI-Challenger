from pprint import pprint

import pytest


class TestSaiVlan:
    # object with no parents

    def test_vlan_create(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    # def test_sai_vlan_attr_vlan_id_get(self, npu):
    #     commands = [
    #         {
    #             'name': 'sai_vlan_attr_vlan_id_get',
    #             'vlan_oid': '$vlan_1',
    #             'op': 'get',
    #             'type': 'SAI_OBJECT_TYPE_VLAN',
    #             'attributes': ['SAI_VLAN_ATTR_VLAN_ID'],
    #         }
    #     ]
    #     pprint(commands)
    #     results = [*npu.process_commands(commands)]
    #     print('======= SAI commands RETURN values get =======')
    #     pprint(results)
    #     assert all([result[1].value() == '10' for result in results]), 'Get error'

    def test_vlan_remove(self, npu):
        commands = [
            {
                'name': 'vlan_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

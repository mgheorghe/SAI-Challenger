from pprint import pprint

import pytest


class TestSaiMcastFdbEntry:
    # object with parent SAI_OBJECT_TYPE_L2MC_GROUP

    def test_mcast_fdb_entry_create(self, npu):
        commands = [
            {
                'name': 'l2mc_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            },
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'attributes': [
                    'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
                    '$l2mc_group_1',
                    'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_mcast_fdb_entry_attr_group_id_set(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mcast_fdb_entry_attr_group_id_set'])
    def test_sai_mcast_fdb_entry_attr_group_id_get(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mcast_fdb_entry_attr_packet_action_set(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mcast_fdb_entry_attr_packet_action_set'])
    def test_sai_mcast_fdb_entry_attr_packet_action_get(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    @pytest.mark.dependency()
    def test_sai_mcast_fdb_entry_attr_meta_data_set(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': ['SAI_MCAST_FDB_ENTRY_ATTR_META_DATA', '0'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_mcast_fdb_entry_attr_meta_data_set'])
    def test_sai_mcast_fdb_entry_attr_meta_data_get(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'atrribute': 'SAI_MCAST_FDB_ENTRY_ATTR_META_DATA',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == '0', (
            'Get error, expected 0 but got %s' % results[1][0].value()
        )

    def test_mcast_fdb_entry_remove(self, npu):
        commands = [
            {
                'name': 'mcast_fdb_entry_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_MCAST_FDB_ENTRY',
                'attributes': [
                    'SAI_MCAST_FDB_ENTRY_ATTR_GROUP_ID',
                    '$l2mc_group_1',
                    'SAI_MCAST_FDB_ENTRY_ATTR_PACKET_ACTION',
                    'SAI_PACKET_ACTION_DROP',
                ],
                'key': {
                    'switch_id': '$SWITCH_ID',
                    'mac_address': 'TODO',
                    'bv_id': 'TODO',
                },
            },
            {
                'name': 'l2mc_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_L2MC_GROUP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

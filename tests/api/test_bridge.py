from pprint import pprint

import pytest


class TestSaiBridge:
    # object with no parents

    @pytest.mark.dependency(scope='session')
    def test_bridge_create(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_bridge_attr_port_list_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_port_list_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_PORT_LIST',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'TODO' for result in results]), 'Get error'

    def test_sai_bridge_attr_max_learned_addresses_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_max_learned_addresses_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': ['SAI_BRIDGE_ATTR_MAX_LEARNED_ADDRESSES', '0'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_max_learned_addresses_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_max_learned_addresses_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_MAX_LEARNED_ADDRESSES',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == '0' for result in results]), 'Get error'

    def test_sai_bridge_attr_learn_disable_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_learn_disable_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': ['SAI_BRIDGE_ATTR_LEARN_DISABLE', 'false'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_learn_disable_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_learn_disable_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_LEARN_DISABLE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'false' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_unicast_flood_control_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_unicast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_unicast_flood_control_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_unicast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS' for result in results]
        ), 'Get error'

    def test_sai_bridge_attr_unknown_unicast_flood_group_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_unicast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_unicast_flood_group_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_unicast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_UNKNOWN_UNICAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_multicast_flood_control_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_multicast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_multicast_flood_control_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_multicast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS' for result in results]
        ), 'Get error'

    def test_sai_bridge_attr_unknown_multicast_flood_group_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_multicast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_unknown_multicast_flood_group_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_unknown_multicast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_UNKNOWN_MULTICAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_sai_bridge_attr_broadcast_flood_control_type_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_broadcast_flood_control_type_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
                    'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_broadcast_flood_control_type_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_broadcast_flood_control_type_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_CONTROL_TYPE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all(
            [result == 'SAI_BRIDGE_FLOOD_CONTROL_TYPE_SUB_PORTS' for result in results]
        ), 'Get error'

    def test_sai_bridge_attr_broadcast_flood_group_set(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_broadcast_flood_group_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': [
                    'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_GROUP',
                    'SAI_NULL_OBJECT_ID',
                ],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_bridge_attr_broadcast_flood_group_get(self, dpu):
        commands = [
            {
                'name': 'sai_bridge_attr_broadcast_flood_group_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'atrribute': 'SAI_BRIDGE_ATTR_BROADCAST_FLOOD_GROUP',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_NULL_OBJECT_ID' for result in results]), 'Get error'

    def test_bridge_remove(self, npu):
        commands = [
            {
                'name': 'bridge_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            }
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

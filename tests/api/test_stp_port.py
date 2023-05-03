from pprint import pprint

import pytest


class TestSaiStpPort:
    # object with parent SAI_OBJECT_TYPE_STP SAI_OBJECT_TYPE_BRIDGE_PORT

    def test_stp_port_create(self, npu):
        commands = [
            {
                'name': 'stp_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_STP',
                'attributes': [],
            },
            {
                'name': 'port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'virtual_router_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'vlan_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'bridge_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'router_interface_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'attributes': [
                    'SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID',
                    '$virtual_router_1',
                    'SAI_ROUTER_INTERFACE_ATTR_TYPE',
                    'SAI_ROUTER_INTERFACE_TYPE_PORT',
                    'SAI_ROUTER_INTERFACE_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'tunnel_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'attributes': [
                    'SAI_TUNNEL_ATTR_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE',
                    '$router_interface_1',
                    'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE',
                    '$router_interface_1',
                ],
            },
            {
                'name': 'bridge_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'attributes': [
                    'SAI_BRIDGE_PORT_ATTR_TYPE',
                    'SAI_BRIDGE_PORT_TYPE_PORT',
                    'SAI_BRIDGE_PORT_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_BRIDGE_PORT_ATTR_VLAN_ID',
                    '10',
                    'SAI_BRIDGE_PORT_ATTR_RIF_ID',
                    '$router_interface_1',
                    'SAI_BRIDGE_PORT_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'stp_port_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_STP_PORT',
                'attributes': [
                    'SAI_STP_PORT_ATTR_STP',
                    '$stp_1',
                    'SAI_STP_PORT_ATTR_BRIDGE_PORT',
                    '$bridge_port_1',
                    'SAI_STP_PORT_ATTR_STATE',
                    'SAI_STP_PORT_STATE_LEARNING',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    @pytest.mark.dependency()
    def test_sai_stp_port_attr_state_set(self, npu):
        commands = [
            {
                'name': 'stp_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_STP_PORT',
                'atrribute': ['SAI_STP_PORT_ATTR_STATE', 'TODO'],
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Set error'

    @pytest.mark.dependency(depends=['test_sai_stp_port_attr_state_set'])
    def test_sai_stp_port_attr_state_get(self, npu):
        commands = [
            {
                'name': 'stp_port_1',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_STP_PORT',
                'atrribute': 'SAI_STP_PORT_ATTR_STATE',
            }
        ]
        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert results[1][0].value() == 'TODO', (
            'Get error, expected TODO but got %s' % results[1][0].value()
        )

    def test_stp_port_remove(self, npu):
        commands = [
            {
                'name': 'stp_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_STP_PORT',
                'attributes': [
                    'SAI_STP_PORT_ATTR_STP',
                    '$stp_1',
                    'SAI_STP_PORT_ATTR_BRIDGE_PORT',
                    '$bridge_port_1',
                    'SAI_STP_PORT_ATTR_STATE',
                    'SAI_STP_PORT_STATE_LEARNING',
                ],
            },
            {
                'name': 'bridge_port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE_PORT',
                'attributes': [
                    'SAI_BRIDGE_PORT_ATTR_TYPE',
                    'SAI_BRIDGE_PORT_TYPE_PORT',
                    'SAI_BRIDGE_PORT_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_BRIDGE_PORT_ATTR_VLAN_ID',
                    '10',
                    'SAI_BRIDGE_PORT_ATTR_RIF_ID',
                    '$router_interface_1',
                    'SAI_BRIDGE_PORT_ATTR_TUNNEL_ID',
                    '$tunnel_1',
                    'SAI_BRIDGE_PORT_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'tunnel_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_TUNNEL',
                'attributes': [
                    'SAI_TUNNEL_ATTR_TYPE',
                    'SAI_TUNNEL_TYPE_IPINIP',
                    'SAI_TUNNEL_ATTR_UNDERLAY_INTERFACE',
                    '$router_interface_1',
                    'SAI_TUNNEL_ATTR_OVERLAY_INTERFACE',
                    '$router_interface_1',
                ],
            },
            {
                'name': 'router_interface_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_ROUTER_INTERFACE',
                'attributes': [
                    'SAI_ROUTER_INTERFACE_ATTR_VIRTUAL_ROUTER_ID',
                    '$virtual_router_1',
                    'SAI_ROUTER_INTERFACE_ATTR_TYPE',
                    'SAI_ROUTER_INTERFACE_TYPE_PORT',
                    'SAI_ROUTER_INTERFACE_ATTR_PORT_ID',
                    '$port_1',
                    'SAI_ROUTER_INTERFACE_ATTR_VLAN_ID',
                    '$vlan_1',
                    'SAI_ROUTER_INTERFACE_ATTR_OUTER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_INNER_VLAN_ID',
                    '10',
                    'SAI_ROUTER_INTERFACE_ATTR_BRIDGE_ID',
                    '$bridge_1',
                ],
            },
            {
                'name': 'bridge_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_BRIDGE',
                'attributes': ['SAI_BRIDGE_ATTR_TYPE', 'SAI_BRIDGE_TYPE_1Q'],
            },
            {
                'name': 'vlan_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VLAN',
                'attributes': ['SAI_VLAN_ATTR_VLAN_ID', '10'],
            },
            {
                'name': 'virtual_router_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_VIRTUAL_ROUTER',
                'attributes': [],
            },
            {
                'name': 'port_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_PORT',
                'attributes': [
                    'SAI_PORT_ATTR_HW_LANE_LIST',
                    '2:10,11',
                    'SAI_PORT_ATTR_SPEED',
                    '10',
                ],
            },
            {
                'name': 'stp_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_STP',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

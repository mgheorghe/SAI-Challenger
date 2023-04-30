from pprint import pprint

import pytest


class TestSaiUdf:
    # object with parent SAI_OBJECT_TYPE_UDF_MATCH SAI_OBJECT_TYPE_UDF_GROUP

    @pytest.mark.dependency(scope='session')
    def test_udf_create(self, npu):
        commands = [
            {
                'name': 'udf_match_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF_MATCH',
                'attributes': [],
            },
            {
                'name': 'udf_group_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            },
            {
                'name': 'udf_1',
                'op': 'create',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'attributes': [
                    'SAI_UDF_ATTR_MATCH_ID',
                    '$udf_match_1',
                    'SAI_UDF_ATTR_GROUP_ID',
                    '$udf_group_1',
                    'SAI_UDF_ATTR_OFFSET',
                    '10',
                ],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values create =======')
        pprint(results)
        assert all(results), 'Create error'

    def test_sai_udf_attr_base_set(self, dpu):
        commands = [
            {
                'name': 'sai_udf_attr_base_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': ['SAI_UDF_ATTR_BASE', 'SAI_UDF_BASE_L2'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_udf_attr_base_get(self, dpu):
        commands = [
            {
                'name': 'sai_udf_attr_base_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': 'SAI_UDF_ATTR_BASE',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_UDF_BASE_L2' for result in results]), 'Get error'

    def test_sai_udf_attr_hash_mask_set(self, dpu):
        commands = [
            {
                'name': 'sai_udf_attr_hash_mask_set',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': ['SAI_UDF_ATTR_HASH_MASK', 'const'],
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'SAI_STATUS_SUCCESS' for result in results]), 'Get error'

    def test_sai_udf_attr_hash_mask_get(self, dpu):
        commands = [
            {
                'name': 'sai_udf_attr_hash_mask_get',
                'op': 'get',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'atrribute': 'SAI_UDF_ATTR_HASH_MASK',
            }
        ]
        results = [*dpu.process_commands(commands)]
        print('======= SAI commands RETURN values get =======')
        pprint(results)
        assert all([result == 'const' for result in results]), 'Get error'

    def test_udf_remove(self, npu):
        commands = [
            {
                'name': 'udf_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF',
                'attributes': [
                    'SAI_UDF_ATTR_MATCH_ID',
                    '$udf_match_1',
                    'SAI_UDF_ATTR_GROUP_ID',
                    '$udf_group_1',
                    'SAI_UDF_ATTR_OFFSET',
                    '10',
                ],
            },
            {
                'name': 'udf_group_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF_GROUP',
                'attributes': ['SAI_UDF_GROUP_ATTR_LENGTH', '10'],
            },
            {
                'name': 'udf_match_1',
                'op': 'remove',
                'type': 'SAI_OBJECT_TYPE_UDF_MATCH',
                'attributes': [],
            },
        ]

        results = [*npu.process_commands(commands)]
        print('======= SAI commands RETURN values remove =======')
        pprint(results)
        assert all(
            [result == 'SAI_STATUS_SUCCESS' for result in results]
        ), 'Remove error'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:05 
# @Author : hesgang
# @File : UpdateFC.py 

import sys
import base64

from typing import List
from Tea.core import TeaCore

from alibabacloud_fc_open20210406.client import Client as FC_Open20210406Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient

AccessKeyId = 'LTAI5tDkX9mJC4JfUoqqKmfF'
AccessKeySecret = '4K3Y1tk0ZbSWMX7hX0c8x45hW2U6G6'


class UpdateFC:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> FC_Open20210406Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = f"{'1371505006329876'}.cn-beijing.fc.aliyuncs.com"
        return FC_Open20210406Client(config)

    @staticmethod
    def main(zipcode):
        client = UpdateFC.create_client(AccessKeyId, AccessKeySecret)
        update_function_headers = fc__open_20210406_models.UpdateFunctionHeaders()
        update_function_request = fc__open_20210406_models.UpdateFunctionRequest(code=zipcode)
        resp = client.update_function_with_options('hepler', 'test', update_function_request, update_function_headers, util_models.RuntimeOptions())
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = UpdateFC.create_client('ACCESS_KEY_ID', 'ACCESS_KEY_SECRET')
        update_function_headers = fc__open_20210406_models.UpdateFunctionHeaders()
        update_function_request = fc__open_20210406_models.UpdateFunctionRequest()
        resp = await client.update_function_with_options_async('hepler', 'test', update_function_request, update_function_headers, util_models.RuntimeOptions())
        ConsoleClient.log(UtilClient.to_jsonstring(TeaCore.to_map(resp)))


if __name__ == '__main__':
    with open("test.zip", "rb") as f:
        by = f.read()
        encoded = base64.b64encode(by)
        f.close()
    aa = fc__open_20210406_models.Code(zip_file=encoded.decode())
    UpdateFC.main(aa)


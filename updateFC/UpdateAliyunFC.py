#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:05 
# @Author : hesgang
# @File : UpdateFC.py
import os
import sys
import base64
import argparse
import yaml
from typing import List
from Tea.core import TeaCore

from alibabacloud_fc_open20210406.client import Client as FC_Open20210406Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient

from mirror import Mirror


def _create_parser():
    with open('/action.yml', 'r') as f:
        action = yaml.safe_load(f)
    _parser = argparse.ArgumentParser(
        description=action['description'])
    inputs = action['inputs']

    for key in inputs:
        if key in ['dst_key']:
            continue
        input_args = inputs[key]
        dft = input_args.get('default', '')
        _parser.add_argument(
            "--" + key.replace('_', '-'),
            # Autofill the `type` according `default`, str by default
            type=str,
            required=input_args.get('required', False),
            default=dft,
            help=input_args.get('description', '')
        )
    return _parser


class UpdateFC:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
        account_id: str,
        region: str,
    ):
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @param account_id:
        @param region
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
        config.endpoint = '''{}.{}.fc.aliyuncs.com'''.format(account_id, region)
        return FC_Open20210406Client(config)

    @staticmethod
    def main(_ak, _sk, _account_id, region, _sever_name, _func_name, zipcode):
        client = UpdateFC.create_client(_ak, _sk, _account_id, region)
        update_function_headers = fc__open_20210406_models.UpdateFunctionHeaders()
        update_function_request = fc__open_20210406_models.UpdateFunctionRequest(code=zipcode)
        resp = client.update_function_with_options(_sever_name, _func_name, update_function_request, update_function_headers, util_models.RuntimeOptions())
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
    print(os.getcwd())
    with open("cache.zip", "rb") as z_file:
        by = z_file.read()
        b_file = base64.b64encode(by)
        z_file.close()
    parser = _create_parser()
    args = parser.parse_args()

    zipfile = fc__open_20210406_models.Code(zip_file=b_file.decode())
    UpdateFC.main(args.access_key_id, args.access_key_secret, args.account_ID, args.region, args.server_name, args.function_name, zipfile)


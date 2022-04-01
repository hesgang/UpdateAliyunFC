#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:05 
# @Author : hesgang
# @File : UpdateFC.py 
import argparse
import yaml
import sys
from typing import List
from Tea.core import TeaCore

from alibabacloud_fc_open20210406.client import Client as FC_Open20210406Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_fc_open20210406 import models as fc__open_20210406_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_console.client import Client as ConsoleClient
from alibabacloud_tea_util.client import Client as UtilClient


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


if __name__ == '__main__':
    print('runs begin')
    parser = _create_parser()
    args = parser.parse_args()
    print(args.region)
    print('runs end')


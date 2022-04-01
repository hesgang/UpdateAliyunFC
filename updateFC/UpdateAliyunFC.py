#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/4/1 15:05 
# @Author : hesgang
# @File : UpdateFC.py 
import argparse
import yaml
import sys


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


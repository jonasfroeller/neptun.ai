#!/bin/bash

cd ../RWKV

pip install -r requirements.txt


cd ../python-scripts


python process_data.py

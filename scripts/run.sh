#!/bin/bash

cd update_score && \
    python -m pip install -r requirements.txt && \
    python ./main.py && \
    cd ..

cd calc_table && \
    python -m pip install -r requirements.txt && \
    python ./calc_table.py && \
    cd ..

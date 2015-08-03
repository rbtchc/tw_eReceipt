#!/usr/bin/env python

import json
import os
import sys

"""
Taiwan eletronic receipt format

CSV row format: Type,Paylod
--
Type: (1) M: metadata (2) D: detail
--
(1) Metadata format: M,status,serial,date,store VAT number,store name,card name,card serial,total amount
    - M: indicates it's metadata
    - status: open or invalidate
    - serial: serial number of the receipt
    - date: receipt date
    - store VAT: value added tax number (or unified biz number)
    - store name: store name
    - card name: name of the card used of the payment
    - card serial: serial number of the card
    - total amount: total amount of the transaction
(2) Detail format: D,serial,amount,item name
    - D: indicates it's detail info.
    - serial: serial number of the receipt
    - amount: amount of the item
    - item name: name of the item
"""

data = {}
with open(sys.argv[1], 'r') as csv:
    for l in csv:
        d = l.decode('big5').encode('utf8').split('|')
        if d[0] == 'M':
            data[d[2]] = {
                'metadata': {
                    'status':       d[1],
                    'date':         d[3],
                    'vat_no':       d[4],
                    'store_name':   d[5],
                    'card_name':    d[6],
                    'card_serial':  d[7],
                    'total_amount': float(d[8])
                }
            }
        elif d[0] == 'D':
            data[d[1]].setdefault('detail', []).append({'amount': float(d[2]), 'item_name': d[3]})

#print json.dumps(data[data.keys()[0]], indent=4)
print json.dumps(data, indent=4)


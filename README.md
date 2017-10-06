# Taiwan eletronic receipt parser

Parser of Taiwan electronic receipt summary
In Taiwan, when you pay with the easycard (an eletronic wallet for small amount payment) or any registered eletronic means,
the ministry of finance will keep the eletronic receipt for each transaction.
And you can ask them to send you the receipt summary each month by mail.
It will be sent with email subject: 財政部電子發票整合服務平台 - 消費發票彙整通知 and an attachment of CSV file.

This project is created to host the scripts that I use to parse the CSV file for now.

# Usage

The input will be the CSV file attached in the mail sent from the ministry of the finance.
The output will be printed in JSON format

Command: `./parser.py xxx.csv`

Sample output format:
```
{
    "Receipt Serial": {
        "detail": [
            {
                "item_name": "<item name 1 in chinese>",
                "amount": <amount of the item>
            },
            {
                "item_name": "<item name 2 in chinese>",
                "amount": <amount of the item, could be negative if there's a promotion>
            }
        ],
        "metadata": {
            "card_name": "<name of the eletronic mean>",
            "total_amount": 40.0,
            "vat_no": <value added tax number of the business>,
            "store_name": "<store name in chinese>",
            "valid": true,
            "card_serial": "<serial number of the card",
            "date": "<date that receipt is created>"
        }
    },
    "WW82147123": {
        "detail": [
            {
                "item_name": "400\u932b\u862d\u7d05\u8336",
                "amount": 21.0
            }
        ],
        "metadata": {
            "card_name": "\u60a0\u904a\u5361",
            "total_amount": 21.0,
            "vat_no": 52500358,
            "store_name": "\u7fa9\u7f8e\u80a1\u4efd\u6709\u9650\u516c\u53f8\u6c50\u6b62\u5206\u516c\u53f8",
            "valid": true,
            "card_serial": "37123123",
            "date": "20170912"
        }
    }
}
```

# References

1. http://www.einvoice.nat.gov.tw/

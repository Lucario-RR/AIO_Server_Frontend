# Repo Intro
This repo provide details on what this server does, how to use, how to handling errors (from user perspective). This server is frontend and backend separated, to find more details please find following repo.

Frontend: (Not available yet)

Backend: (Not available yet)


# What it does
## Blogs?
1. Public view blogs
2. Private edit blogs
3. Comments

### Cooking


## Ledger
### Download Transactions
1. Upload bills from bank or WCP ALP
2. Add new book and link to user
3. Add rules on how to link bills to user and card

### Download Transactions

### Auto Bill Processor
1. Support bills from WeChat Pay, Ali Pay,
2. Automatically converted to DB record when user uploaded
3. Handling error when incorrect file sumbitted

### Parser
HSBCHKHH
Example 1: 16 items  
``` json
{
            "transactionDate": "2026-03-07",
            "transactionType": "UNBILLED",
            "transactionAmount": {
                "amount": 240.00,
                "currencyCode": "CNY"
            },
            "transactionDescriptions": [
                "SALES:   WUHAN TIANHE AIRPORT HOLI WUHAN        CN"
            ],
            "cardNumber": "8383830000319673",
            "cardNumberDisplay": "8383830000319673",
            "cardNumberIdentifier": "VEdTRlNCU0dTQlNHJGSPpGiFTNaocAZNB_min_7FAKy766vbiLfPOCeWlMtndfE=",
            "cardholderName": "REN QIRAN",
            "merchantCategoryCode": "7011",
            "transactionCreditDebitCode": "DEBIT_TRANSACTION",
            "realTimeTransactionDetails": {
                "transactionTime": "125324",
                "merchantName": "WUHAN TIANHE AIRPORT HOLI",
                "merchantCity": "WUHAN",
                "merchantLocation": "CN",
                "merchantCountryCode": "CN"
            },
            "authorizationCode": "590659",
            "uniqueTransactionIdentifier": "VkVkVFJsTkNVMGRUUWxOSFozWFdfbktNWHJEZEpHRXVVcGF4WmhTVmZRTUhydXFFSHVpRk40Y19HbnhPNWdsVXRKMzlGcG5na1FuQTNRWDJvcF9taW5fS0hEZkNTQW5rV0REX2wxM0lrcG9mUW1pZk1EVV94em5KYTZmU3l2RlFuUWxuZndZdWlvekdHZ1lQeEhVSXhXWmRHSF9taW5fWGl3UTJOcVN4RHY2YkxQUDVSX2c5UXFNTW1XVEpnWFZ0bl9taW5fYzZYR1VfbWluX2ZpNzlaaV9uc0dWMGZmcDNCc2ptX21pbl9OTGRnMDkybXduV2dwM1pyenRFYzg2UHlVSmhYZEpXZ184aWxFWDF1X21pbl9faWU2Nm12TDE1YjFiSU44Rzk1RVZ0Q0g2SjVaY3JKQWdOSkxKeDZ1amhsVFRQNmgxblE2YnlzQ1VfMUNoRzdiU0RJZG1wd0RDR2FjMzNjbmhVazRfZ0FQeTI0c0JiS055QjRQMmxOcXBQQ2Jsb1JwU1FzVDBkM19taW5fanFKcF9taW5fTHB5SGM=",
            "transactionEnrichmentIndicator": true,
            "secondaryCardTransactionIndicator": true,
            "transactionStatus": "PENDING"
        },
  ```

Example 2: 21 items
``` json
{
            "transactionDate": "2026-03-06",
            "transactionPostingDate": "2026-03-07",
            "transactionType": "UNBILLED",
            "transactionAmount": {
                "amount": 54.00,
                "currencyCode": "CNY"
            },
            "transactionDescriptions": [
                "QR       CHINA XUNXIAO CO.,LTD     CHN          CN"
            ],
            "cardNumber": "8383830000319673",
            "cardNumberDisplay": "8383830000319673",
            "cardNumberIdentifier": "VEdTRlNCU0dTQlNHJGSPpGiFTNaocAZNB_min_7FAKy766vbiLfPOCeWlMtndfE=",
            "cardholderName": "REN QIRAN",
            "merchantCategoryCode": "5691",
            "transactionCreditDebitCode": "DEBIT_TRANSACTION",
            "realTimeTransactionDetails": {
                "transactionTime": "104240",
                "merchantName": "CHINA XUNXIAO CO.,LTD",
                "merchantCity": "CHN",
                "merchantLocation": "CHINA",
                "authorizationType": "INTERNATIONAL",
                "merchantCountryCode": "CN"
            },
            "authorizationCode": "035972",
            "acquirerReferenceNumber": "00000000000000000000000",
            "uniqueTransactionIdentifier": "VkVkVFJsTkNVMGRUUWxOSFozWFdfbktNWHJEZEpHRXVVcGF4WmhTVmZRTUhydXFFSHVpRk40Y19HbnhPNWdsVXRKMzlGcG5na1FuQTNRWDJvcF9taW5fS0hEZkNTQW5rV0REX2wxM0lrcG9mUW1pZk1EVV94em5KYTZmU3l2RlFuUWxuZndZdWlvekdHZ1lQeEhVSXhXWmRHSF9taW5fWGl3UTJOcVN4RHY2YkxQUDVSX2c5UXFNTW1XVEpnWFZ0bl9taW5fYzZYR1VfbWluX2ZpNzlaaV9uc0dWMGZmcDNCc2ptX21pbl9OTGRnMDkybXduV2dwM1pyenRFYzg2UHlVSmhYZEpXZ184aWxFWDF1X21pbl9faWU2Nm12TDE1YjFiSU44Rzk1RVZ0Q0g2SjVaY3JKQWdOSkxKeDZ1amhsVFRQNmgxblE2YnlzQ2dfMUNnOWtOV1NOY2o2aENLTWVMX21pbl9OWm1ORnhjYXJRYVh5dVk1ckE2bUJyNl9rZUtvaENZZG9IY3BEZHF6WE9tWmoxWDMzeTI1VTFqbFdEdmJPSzlTWGh0aVlISVp3Z3R2RDZ1M2JVZnhyZTd0VGF5eE9ERTd2bUdGX21pbl9fQnZlZG9FaE1EZV9taW5fcUNNWnRRNzU5OUhkRTFyV210cW1Eem1nSVY0N0hHN1VocklKMDlmUjE3SEc1N0FiYWMyU21MSERERVRBM2t5X3NVSno1X21pbl9XcHhYZlNzQkFkMVZ5Tg==",
            "transactionEnrichmentIndicator": true,
            "transactionDisputeIndicator": true,
            "secondaryCardTransactionIndicator": false,
            "transactionStatus": "HISTORIC",
            "transactionEnrichmentTypes": [
                "MERCHANT"
            ],
            "foreignCurrencyTransactionCreditDebitCode": "DEBIT_TRANSACTION"
        },
```

Example 3: 16 items  
``` json
{
            "transactionDate": "2026-03-05",
            "transactionPostingDate": "2026-03-06",
            "transactionType": "BILLED",
            "transactionAmount": {
                "amount": 2000.00,
                "currencyCode": "CNY"
            },
            "transactionDescriptions": [
                "PAYMENT - THANK YOU"
            ],
            "cardNumber": "8383830000319673",
            "cardNumberDisplay": "8383830000319673",
            "cardNumberIdentifier": "VEdTRlNCU0dTQlNHJGSPpGiFTNaocAZNB_min_7FAKy766vbiLfPOCeWlMtndfE=",
            "cardholderName": "REN QIRAN",
            "merchantCategoryCode": "0000",
            "transactionCreditDebitCode": "CREDIT_TRANSACTION",
            "realTimeTransactionDetails": {
                "transactionTime": "000000"
            },
            "uniqueTransactionIdentifier": "VkVkVFJsTkNVMGRUUWxOSFozWFdfbktNWHJEZEpHRXVVcGF4WmhTVmZRTUhydXFFSHVpRk40Y19HbnhPNWdsVXRKMzlGcG5na1FuQTNRWDJvcF9taW5fS0hEZkNTQW5rV0REX2wxM0lrcG9mUW1pZk1EVV94em5KYTZmU3l2RlFuUWxuZndZdWlvekdHZ1lQeEhVSXhXWmRHSF9taW5fWGl3UTJOcVN4RHY2YkxQUDVSX2c5UXFNTW1XVEpnWFZ0bl9taW5fYzZYR1VfbWluX2ZpNzlaaV9uc0dWMGZmcDNCc2ptX21pbl9OTGRnMDkybXduV2dwM1pyenRFYzg2UHlVSmhYZEpXZ184aWxFWDF1X21pbl9faWU2Nm12TDE1YjFiSU44Rzk1RVZ0Q0g2SjVaY3JKQWdOSkxKeDZ1amhsVFRQNmgxblE2YnlzQ2dfMUNnOWtOV1NOY2o2aENLTWVMX21pbl9OWm1ORnhjYXJRYVh5dVk1ckE2bUJyNl9rZUtvaENZZG9IY3BEZHF6WE9tWmoxWDMzeTI1VTFqbFdEdmJjSzlTWGh0aVlISVp3Z3R2UzlKWGJVZnhyZTd0VGF5eE9ERTd2bUdGOF9CdmVkb0VoTURlNHF5Z2N1UTc1OTlIZEUxcldtdHFtRHptZ0lWNDdIRzdVaHJJSjA5ZlIxN0hHNTdBYmFjMlNtTEhERWtiTzNreGFfNGk2VWxCdjFHNE5GTjhydTY2Mw==",
            "transactionEnrichmentIndicator": false,
            "transactionDisputeIndicator": false,
            "secondaryCardTransactionIndicator": false,
            "transactionStatus": "HISTORIC",
            "transactionEnrichmentTypes": [],
            "foreignCurrencyTransactionCreditDebitCode": "CREDIT_TRANSACTION"
        },
```

Example 4: 23 items
``` json
{
            "transactionDate": "2026-01-24",
            "transactionPostingDate": "2026-01-26",
            "transactionType": "BILLED",
            "transactionAmount": {
                "amount": 296.12,
                "currencyCode": "HKD"
            },
            "transactionDescriptions": [
                "SALES:   IH                        MAC          MO"
            ],
            "cardNumber": "6250980000929213",
            "cardNumberDisplay": "6250980000929213",
            "cardNumberIdentifier": "VEdTRlNCU0dTQlNHKmWCp2mOTNaocAxOB_min_rDAAh01_h_min_Hgkm053VTxWlgGs=",
            "cardholderName": "WANG ZIFAN",
            "exchangeRate": 0.97089,
            "merchantCategoryCode": "5812",
            "transactionCreditDebitCode": "DEBIT_TRANSACTION",
            "realTimeTransactionDetails": {
                "transactionTime": "133418",
                "merchantName": "IH",
                "merchantCity": "MAC",
                "merchantLocation": "MACAU",
                "authorizationType": "DOMESTIC",
                "merchantCountryCode": "MO"
            },
            "authorizationCode": "195542",
            "acquirerReferenceNumber": "00000000000000000000000",
            "uniqueTransactionIdentifier": "VkVkVFJsTkNVMGRUUWxOSFozWFdfbktNWHJEZEpHRXVVcGF4WmhTVmZRTUhydXFGTk95V05fSTdFM3hPNWdsVWtwWDlGclA3dmlYWm14UHdqTGVwTEJiUVpUdmJURV9qbDEzSWtwb1JRVlNCT2pzcjRVcUJlWmJ0bnNoYXJRWjdaZ0ZJdWF5aEtod3R4MHd4N1dKQk1uV0VqQmtnWTRPQUlmV2pBdWpSVzhNa2I4TXZrWF9TNW1obTN1VWZRV0pVTERfZVZ5cmlyM1FoWXRoQkhPam05N0RMaEVacGlqZjY4WTYzOTJGYmVmT2ozelFlR2VvMzFLVTN2V2UwcV9taW5fVHNRWl9taW5fNWxiWVJRMmY2QTlmeW1INWxDMWJXX21pbl9yRU5CZ2xNRzk5bjdvM2xfbWluX2lYZDlneGdENmpxOFhBdjJ6bzhtOTJSUGN2emhpdU9lcjJXZkhZVmhNaXpBSTZieDQ0RWI1UFhvYmVsVDhzNUJfbWluX1pmV285RE9LX2ZkQzlnbURQbjNDeFVqMnRBQl9taW5feXJQODJBMHByR0lKRUxtYm5Ea3BMQVRfbWluXzg3UGJWTEttME1VRnJsaVJrQ2xtU19taW5fVWQwMFBTYTZyQ0VhdVE3NTk4SElRQTdXOU5xNkhXcmdlQmcxQkNfNnRwMDNuOW5KbHVYVTdiQUZlNXZIaXJyVGFqU3YzbFZNbk5JQXZnd08yZGdnTU8xNVVTaU9IcjdlMjhvNXpzdTE5VVRHd0c3V2lwNXQ3Q2dvZEVGOUs2ZElIMFpNVmJLcFZUTWlXNTA0ZGZ1Nmh6VFpVb0JkZnhpaTZRPT0=",
            "transactionEnrichmentIndicator": true,
            "transactionDisputeIndicator": true,
            "secondaryCardTransactionIndicator": true,
            "transactionStatus": "HISTORIC",
            "foreignCurrencyTransactionAmount": {
                "amount": 305.00,
                "currencyCode": "MOP"
            },
            "transactionEnrichmentTypes": [
                "MERCHANT"
            ],
            "foreignCurrencyTransactionCreditDebitCode": "DEBIT_TRANSACTION"
        }
```

Example 5 Pay bills/Taxes: 21 lines 
``` json
{
            "transactionDate": "2026-01-16",
            "transactionPostingDate": "2026-01-16",
            "transactionType": "BILLED",
            "transactionAmount": {
                "amount": 72500.00,
                "currencyCode": "HKD"
            },
            "transactionDescriptions": [
                "SALES:   HKPU                      KOWLOON      HK"
            ],
            "cardNumber": "4966040123875015",
            "cardNumberDisplay": "4966040123875015",
            "cardNumberIdentifier": "VEdTRlNCU0dTQlNHKG6BoWCCTNeqcw1LC_min_jDBielJu8i4blZajUYC_5reDk=",
            "cardholderName": "REN QIRAN",
            "merchantCategoryCode": "4900",
            "transactionCreditDebitCode": "DEBIT_TRANSACTION",
            "realTimeTransactionDetails": {
                "transactionTime": "105136",
                "merchantName": "HKPU",
                "merchantCity": "KOWLOON",
                "merchantLocation": "HONG KONG",
                "merchantCountryCode": "HK"
            },
            "authorizationCode": "310726",
            "acquirerReferenceNumber": "26652001171",
            "uniqueTransactionIdentifier": "VkVkVFJsTkNVMGRUUWxOSFozWFdfbktNWHJEZEpHRXVVcGF4WmhTVmZRTUhydXFGSG8yWEtKY1ZIM3hPNGhkVWd2Yl9GNW5na1FuQWdBZjFpSl9taW5fS0hEaktGUW5rV0RuOHZtX21pbl9RcHBvX21pbl9HbHlmSDI0MzJSeWNkNV9taW5fRTFfMWpyUXRTWUJabm82X05OUndNbzIwSjlBSjhJR2IzdGhZbFJaNl9taW5fQzlpR0V0blVZdWdNUjVvbnNVeVFpVlZlM1lnSFpHWlRaZ3Y1WVdYVGwxTTdUTUpSSnRqNjk0M3RtMDlQaXhQVTRLdldyUkUwWTg2MV9taW5fR3hoVGRKU2d0bDNua1gxdV9taW5fX2llNjZtdkwxNWIxYk9aUGF6djNSTUxtZWw0dWNTTkNzdU50ZHRfTnF5bFRUUDZoMW5RNmJ5c0NnXzFDZ3htdHVYUGNfNmhTQ1BjN21CWUdWRHhjYXJRYVh5dVk1Z0JyU0JyNl9rZUtvaENZZG9IY3BEZHF6WE9tWmoxWDMzeTI1VTFqbFdEdmJjSzlTWGh0aVlISVp3Z3R2RDd2TGJVZnhyZTd0VGF5eE9ERTd2bW1CX19CdmVkb0VoTURlNnJ5Y1hzUTc1OTlIZEUxcldtdHFtRHptZ0lWNDdIRzdVaHJJSjA5ZlIxN0hHNTdBYmFjMlNtTEhEREVUQTNreVgwcTJOcDNqYTVMd25MSF9pcWQ4cQ==",
            "transactionEnrichmentIndicator": false,
            "transactionDisputeIndicator": false,
            "secondaryCardTransactionIndicator": false,
            "transactionStatus": "HISTORIC",
            "transactionEnrichmentTypes": [],
            "foreignCurrencyTransactionCreditDebitCode": "DEBIT_TRANSACTION"
        },
```

## Bank Currency Comparing
1. Fetch currency from different bank
2. Find history currency data in DB
3. Plot graphs

## Account Management System
1. Pwd add salt
2. Cookies expiring time
3. 2FA setup
4. Passkey logon

## Bike Management System
### Bike Maintenance Log
1. Store records on each maintenance
2. Add, edit, remove records

### Bike Trip Log
1. Store the basic distence time info and GPS positions (if any) for each trip (automatic upload or manual import)
2. Add, edit, remove records
3. Export statiscical data

## Gallery
Show anime pictures.


# User Interface
## Website


## Mobile and Desktop Application?
Not in the current plan yet.


## iOS Shortcuts


# APIs


# Server Security
## File Virus Check


## DB (SQL) Injection Prevention


# Error Handling, Log and Status Code


# Version History
## 0.0.1 
1. Project created, making detailed requirements.




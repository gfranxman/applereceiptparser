Use
==========================
Use like so::

  from applereceiptparser import parse_receipt
  from pprint import pprint

  receipt = parse_receipt( open("testreceipt.txt").read() )
  pprint( receipt )

The (slightly scrambled) results look like::

  {'environment': 'Sand box',
  'pod': '100',
  'purchase-info': {'bid': 'com.example.prototype',
                   'bvrs': '2006',
                   'expires-date': '1389752699966',
                   'expires-date-formatted': '2014-01-15 02:24:59 Etc/GMT',
                   'expires-date-formatted-pst': '2014-01-14 18:24:59 America/Los_Angeles',
                   'item-id': '778386464',
                   'original-purchase-date': '2014-01-14 01:25:01 Etc/GMT',
                   'original-purchase-date-ms': '1389662701000',
                   'original-purchase-date-pst': '2014-01-13 17:25:01 America/Los_Angeles',
                   'original-transaction-id': '1000000098422197',
                   'product-id': 'com.example.subscription',
                   'purchase-date': '2014-01-15 02:09:59 Etc/GMT',
                   'purchase-date-ms': '1389751799966',
                   'purchase-date-pst': '2014-01-14 18:09:59 America/Los_Angeles',
                   'quantity': '1',
                   'transaction-id': '1000000098546533',
                   'unique-identifier': '9eb0f282b9bf549edaea59749bd1d0c44b641045',
                   'unique-vendor-identifier': '2F9B4BE4-6443-4F22-AB21-7126D7F5945A',
                   'web-order-line-item-id': '1000000027752735'},
  'signature': 'AiYM2lc/Rol+7gx/rt59Row9FgjY3Nr3hchnSs3Ez66ISLRELkPr9rQ3s8OTb2diPy5ERsbrmSDqsF1BwnlFUg+1Pquf+j0dftZsc4S6H7LV49ppTHm5YY58zu4rKiXcrOPIRy83Pnm0k7vqUYN38kXJP/imQVsLIUyNSpjrkYErAAADVzCCA1MwggI7oAMCAQICCGUUkU3ZWAS1MA0GCSqGS1b3DQEBBQUAMH8xCzAJBgNVBAYTAlVTMRMwEQYDVQQKDApBcHBsZSBJbmMuMSYwJAYDVQQLDB1BcHBsZSBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTEzMDEGA1UEAwwqQXBwbGUgaVR1bmVzIFN0b3JlIENlcnRpZmljYXRpb24gQXV0aG9yaXR5MB4XDTA5MDYxNTIyMDU1NloXDTE0MDYxNDIyMDU1NlowZDEjMCEGA1UEAwwaUHVyY2hhc2VSZWNlaXB0Q2VydGlmaWNhdGUxGzAZBgNVBAsMEkFwcGxlIGlUdW5lcyBTdG9yZTETMBEGA1UECgwKQXBwbGUgSW5jLjELMAkGA1UEBhMCVVMwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMrRjF2ct4IrSdiTChaI0g8pwv/cmHs8p/RwV/rt/91XKVhNl4XIBimKjQQNfgHsDs6yju++DrKJE7uKsphMddKYfFE5rGXsAdBEjBwRIxexTevx3HLEFGAt1moKx509dhxtiIdDgJv2YaVs49B0uJvNdy6SMqNNLHsDLzDS9oZHAgMBAAGjcjBwMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUNh3o4p2C0gEYtTJrDtdDC5FYQzowDgYDVR0PAQH/BAQDAgeAMB0GA1UdDgQWBBSpg4PyGUjFPhJXCBTMzaN+mV8k9TAQBgoqhkiG92NkBgUBBAIFADANBgkqhkiG9w0BAQUFAAOCAQEAEaSbPjtmN4C/IB3QEpK32RxacCDXdVXAeVReS5FaZxc+t88pQP93BiAxvdW/3eTSMGY5FbeAYL3etqP5gm8wrFojX0ikyVRStQ+/AQ0KEjtqB07kLs9QUe8czR8UGfdM1EumV/UgvDd4NwNYxLQMg4WTQfgkQQVy8GXZwVHgbE/UC6Y7053pGXBk51NPM3woxhd3gSRLvXj+loHsStcTEqe9pBDpmG5+sk4tw+GK3GMeEN5/+e1QT9np/Kl1nj+aBw7C0xsy0bFnaAd1cSS6xdory/CUvM6gtKsmnOOdqTesbp0bs8sn6Wqs0C9dgcxRHuOMZ2tm8npLUm7argOSzQ==',
  'signing-status': '0'}
 
Credits
-------

- `PyParsing`_
- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _PyParsing: https://pypi.python.org/pypi/pyparsing
.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template

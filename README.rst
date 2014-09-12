Use like so...
==========================
from applereceiptparser import parse_receipt
from pprint import pprint

receipt = parse_receipt( open("testreceipt.txt").read() )
pprint( receipt )

Credits
-------

- `Distribute`_
- `Buildout`_
- `modern-package-template`_

.. _Buildout: http://www.buildout.org/
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _`modern-package-template`: http://pypi.python.org/pypi/modern-package-template

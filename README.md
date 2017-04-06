# CVP configlet builder scripts
---

This repo houses CVP configlet builder scripts that I've created over time.

## lookback-builder.py
---

This script will create loopbacks numbering from 100 to 199.

For switches that start with `spine`, the 2nd octet will be set to `20` and the 3rd octet will be the number after `spine`, for instance it will be `1` for `spine1`.

For switches that start with `leaf`, the 2nd octet will be set to `10` and the 3rd octet will be the number after `leaf`, for instance it will be `1` for `leaf1`.

Examples:

* spine1 = 10.20.1.100-199
* spine4 = 10.20.4.100-199
* leaf6 = 10.10.6.100-199

#! /usr/bin/env python3

import wledpy.wled

s = wledpy.wled.Wled("10.0.0.221")
effect = s.get_effect_name()
print(effect)
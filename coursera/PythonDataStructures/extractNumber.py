text = "X-DSPAM-Confidence:    0.8475";

import re

nums = re.findall('\d+\.\d+', text)

print
float(nums[0])

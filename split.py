
import re

split_list = re.split("[,.]", "100,000,000.000")

#print (split_list)

print("\n".join(re.split("[,.]", "100,000,000.000")))

#string = 'a-bird-in-the-hand-is-worth-two-in-the-bush'

#print(re.split("-", string, maxsplit = 5)) # you split only two times

#string = "myxxxnamexXxisxxXslimXXXshady"

#print(re.split("xxx", string, flags = re.IGNORECASE))


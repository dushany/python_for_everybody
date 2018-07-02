text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(":")
val = text[pos+1:]
num = float(val.lstrip())
print(num)

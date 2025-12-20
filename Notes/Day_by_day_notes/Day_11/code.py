language = "Programming"
print(language)
print(language[9])
print(language[8])
print(language[-2])
print(language[-6])
print(language[0:8])  #e r a m m
print(language[2:9])  # o g r a m m i
print(language[0: ])  # P r o g r a m m i n g
print(language[ : ])  # P r o g r a m m i n g
print(language[ 4: -1])  # r a m m i n
print(language[-8: ])  # g   r   a   m   m   i   n    g
print("with gap the output is", language[0:7:1])
print("without gap the output is ", language[0:7])
# --------------------------------------------------
language[0:7:1]
=> starting point => 0
=> ending point => 7
=> gap => 1 => N-1 => 1-1 = 0
language = "Programming"
print("with gap the output is", language[0:7:1])
print("without gap the output is ", language[0:7])
# —-------------------------------
language2 = "javascript"
print(language2[0:9:2]) # jvsrp
print(language2[0:11:2]) # jvsrp


# Output
# jvsrp
# jvsrp


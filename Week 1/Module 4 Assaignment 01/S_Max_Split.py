s = input()

balance_list = []
cnt_L = 0
cnt_R = 0
st = 0
for i in range(len(s)):
    if 'L' == s[i]:
        cnt_L += 1
    elif 'R' == s[i]:
        cnt_R += 1
    if cnt_L == cnt_R:
        balance_list.append(s[st:i+1])
        cnt_L = 0
        cnt_R = 0
        st = i+1
print(len(balance_list))
for item in balance_list:
    print(item)
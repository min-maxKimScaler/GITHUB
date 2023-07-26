st=[]
for i in range(30):
    a = 0
    a += i+1
    st.append(a)
for i in range(28):
    st_num=int(input())
    if st_num in st:
        st.remove(st_num)
    else:
        st_num=0
sorted(st)
for i in st:
    print(i)
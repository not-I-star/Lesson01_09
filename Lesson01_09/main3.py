m_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m_list2 = [] 
for i in m_list1:
    m_list2.append(i ** 2)

# print(m_list1)
# print(m_list2)

# генератор списков
# 3. выражение / 1.  цикл для выражения / 2. условие (не обяз)
my_list3 = [x ** 2 for x in m_list1 if x % 2 == 0]

print(my_list3)


Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
np.random.seed(12345) left=1
right=21 n=100
ser=np.random.randint(left,right,n) dict_of_elem=count_elements(ser) print(dict_of_elem)
>>>>
3: 5, 6: 12, 2: 5, 5: 2, 10: 5, 18: 5, 15: 6, 17: 2, 19: 8, 12: 9, 14: 3, 11: 2, 7: 4, 8: 4, 1: 7, 16: 2,
4: 3, 20: 3, 9: 6, 13: 7}

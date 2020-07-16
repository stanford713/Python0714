word='She sells sea shell on the seashore'
print(word.count("s"))

passwords="abcABC123".join("xxx")
print(passwords)
print(passwords.isalnum())#是否包含文字或數字
print(passwords.isalpha())#是否只包含文字
print(passwords.isdigit())#是否只包含數字



path = 'C:\nba\tiket.txt'
print(path)
path = r'C:\nba\tiket.txt'
print(path)
path = 'C:\\nba\\tiket.txt'
print(path)
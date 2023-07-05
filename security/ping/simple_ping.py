import os

ip = str(input("Digite o IP ou Host a ser verificado "))

os.system("ping -n 4 {}".format(ip))


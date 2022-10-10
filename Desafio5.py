n = int(input('Digite um número: '))
print("O antecessor de \033[7m{0}\033[m é \033[7m{1}\033[m.\nO sucessor de \033[7;35m{0}\033[m é \033[7;35m{2}\033[m."
      .format(n, (n - 1), (n + 1)))

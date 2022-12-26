def obter_ingredientes(sabor):
  print("Os ingredientes são:")
  if sabor == "c":
    return ['cacau','fermento','ovos', 'leite', 'farinha']
  elif sabor == "b":
    return ['baunilha', 'farinha', 'leite', 'ovos', 'fermento']
  else:
    return ['morangos','fermento','ovos', 'leite', 'farinha']

sabor = 'qualquer'
while(sabor == 'qualquer'):
  print('##########################################\n## Bem vindo a Neco receitas! ## \n##########################################')
  sabor =     input('\n\t\t\tVc quer que bolo?\nPara  Chocolate[c]\t Para Morango[m]\t Para Baunilha[b]')
  print('##########################################\n')
  if sabor.lower() == "c":
    print('Chocolate! Burnyu...\n')
  elif sabor.lower() == "b":
    print('Baunilha! MUITO REAL.\n')
  elif sabor.lower() == "m":
    print('Morango! SHIBABOO.\n')
  else:
    print('Porra bugasse o código!')
    sabor='qualquer'

ingredientes = obter_ingredientes(sabor)
print(ingredientes)
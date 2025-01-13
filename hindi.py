# sh hindi.sh main.hindi
import sys
import os
vars = {}
def hindi(code):
  global vars
  code = code.split('\n')
  newline = False
  def stringoper(code):
    if type(code) == list:
      code = ''.join(code)
    code = code.replace('ओर', '+')
    code = code.replace('बिना', '-')
    code = code.replace('गुना', '*')
    code = code.replace('बांट नीचे', '//')
    code = code.replace('बांट', '/')
    listed = code.split(' ')
    for i in range(len(listed)):
      if listed[i] == 'जर':
        listed[i] = ''
        ad = ''
        if type(vars[listed[i+1]]) == str:
          ad = "'"
        listed[i+1] = ad+str(vars[listed[i+1]])+ad
    code = ''.join(listed)
    return code
  def printnl(stf):
    global newline
    newline = True
    print(stf, end='')
  toexec = True
  compwhile = False
  whilecond = ''
  whilecode = ''
  fwhl = False
  for i in range(len(code)):
    stringed = 1
    line = code[i]
    if line.startswith('बाहर') and toexec:
      if line[5:].startswith('अंक'):
        line = list(line)
        line[5:] = list(stringoper(line[5:]))
        line[8:] = list(str(eval(''.join(line[8:]))))
        line = ''.join(line)
        printnl(line[8:])
      elif line[5:].startswith('जर') and toexec:
        printnl(vars[line[8:].strip()])
      elif line[5:].startswith('नई') and toexec:
        print()
        newline = False
      elif line[5:].startswith('स्प') and toexec:
        printnl(' ')
      else:
        printnl(line[5:])
    elif line.startswith('वार') and toexec:
      newline = line.split(' ')
      ttype = str
      typeset = False
      for j in range(len(newline)):
        if j >= 1 and newline[j-1] == 'वार':
          var = newline[j]
        if j >= 1 and newline[j-1] == 'को':
          if newline[j] == 'अंक':
            ttype = lambda i: int(eval(stringoper(i)))
            typeset = True
          if newline[j] == 'अन्दर':
            val = input(' '.join(newline[j+1:-2])+' ')
          if newline[j] == 'करो':
            val = stringoper(' '.join(newline[j+1:-2]))
        if typeset:
          val = ttype(' '.join(newline[j+1:-2]))
          typeset = False
      vars[var] = val
    elif line.startswith('मत करे:'):
      continue
    elif line.startswith('सब गायब') and toexec:
      os.system('clear')
    elif line.startswith('अगर') and toexec:
      if not eval(stringoper(line[3:])):
        toexec = False
    elif line.startswith('लेकिन अगर') and not toexec:
      if not eval(stringoper(line[9:])):
        toexec = False
    elif line.startswith('तो फ़िर') and not toexec:
      toexec = True
    elif line.startswith('बन्द अगर'):
      toexec = True
    elif line.startswith('जब') and toexec:
      compwhile = True
      toexec = False
      whilecond = line[2:]
      fwhl = True
    elif line.startswith('बन्द जब'):
      while eval(stringoper(whilecond)):
        hindi(whilecode)
      compwhile = False
      toexec = True
    if not stringed:
      line = stringoper(line)
    if compwhile and not fwhl:
      whilecode += line + '\n'
    if fwhl and line.startswith('जब'):
      fwhl = False
  if newline:
    print()
hindi(sys.argv[1])
vars = {}

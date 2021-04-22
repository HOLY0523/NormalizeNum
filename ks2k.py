#!/bin/env python3
import sys

with open(sys.argv[1],mode='w') :
  pass
KAN = {'〇','一','二','三','四','五','六','七','八','九'}

with open(sys.argv[2],mode='r') as input :
  for line in input:
    line.replace('\n','')
    n,m = line.split()
    with open(sys.argv[1],mode='a') as output :
      if len(n) == 24 :
        output.write(line)
      else :
        p = 0
        while p<len(m) :
          if (m[p] in {'千','百','十'}) :
            p += 2
          elif (m[p]=='．' or m[p]=='・') == True :
            if (m[p]=='・' and m[p-1] in KAN) == True :
              src = m[:p] + "．" + m[(p+1):]
              m = src
            p += 1
            while (p<len(m) and m[p] in KAN) :
                p += 1
          elif (m[p] in KAN)==True :
            p += 1
            if (p<len(m) and m[p] in KAN)==True :
              r = p
              p += 1
              while (p<len(m) and m[p] in KAN)==True :
                p += 1
              u = 0
              o = 1
              if (p-r)==3 :
                src = m[:(r+u)] + "千" + m[(r+u):]
                m = src
                u += 2
                o = 3
              if (p-r)!=1 :
                src = m[:(r+u)] + "百" + m[(r+u):]
                m = src
                u += 2
                if o != 3 :
                  o = 2
              src = m[:(r+u)] + "十" + m[(r+u):]
              m = src
              p += o
          else :
            p += 1
        print(n + ' ' + m , file = output)

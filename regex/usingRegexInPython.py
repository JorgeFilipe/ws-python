import re

texto = '0,1,2,3,,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

pattern9 = re.compile('9')
match1 = re.search(pattern9, texto)
print ("Posicoes: %s, %s; Valor: %s." % (match1.start(), match1.end(), match1.group(0)))

valores = re.findall('[a-f]', texto)
print("Valores: %s" % valores)

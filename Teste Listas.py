import re

print(re.search(r'\d+', 'Teste 123').group())
print(re.match(r'\W', 'Teste'))
print(re.findall(r'[a-zA-Z]+', 'Teste 123! Eba @#'))
print(re.sub(r'\s+', '-', 'Teste de substituição de espaços'))
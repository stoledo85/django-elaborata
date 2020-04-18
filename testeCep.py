import pycep_correios

endereco = pycep_correios.get_address_from_cep('89026697')# CEP de Blumenau.
endereco2 = pycep_correios.get_address_from_cep('74393-140')
endereco3 = pycep_correios.get_address_from_cep('83206320')
print(endereco3)
#print(endereco)
#print(endereco['logradouro'])
#print(endereco['bairro'])
#print(endereco['cidade'])
#print(endereco['uf'])
#print(endereco['cep'])
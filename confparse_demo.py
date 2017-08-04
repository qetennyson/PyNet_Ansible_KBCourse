from ciscoconfparse import CiscoConfParse

ipsec_parse = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = ipsec_parse.find_objects(r"crypto map CRYPTO")

for i in crypto_maps:
    print i.text

print '\n'

pfs_maps = ipsec_parse.find_objects_w_child(parentspec=r"crypto map CRYPTO", childspec=r"set pfs group2")

for p in pfs_maps:
    print p.text

print '\n'

no_aes_maps = ipsec_parse.find_objects_wo_child(parentspec=r"crypto map CRYPTO", childspec=r"AES")

for a in no_aes_maps:
    print a.text

print '\n'
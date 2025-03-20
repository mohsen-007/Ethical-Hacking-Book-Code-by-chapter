from ldap3 import Server, Connection, ALL, SUBTREE
server = Server(host = 'ipa.demo1.freeipa.org', use_ssl=True)
conn = Connection(server, user='uid=admin,cn=users,cn=accounts,dc=demo1,dc=freeipa,dc=org', password="Secret123", auto_bind=True)
conn.search(search_base = 'dc=demo1,dc=freeipa,dc=org'
,search_filter = '(objectClass=person)'
,attributes=['cn', 'givenName', 'mail']
,search_scope = SUBTREE)
print(conn.entries)

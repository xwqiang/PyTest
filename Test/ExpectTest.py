import pexpect

child = pexpect.spawn('/usr/local/bin/mysql -u root -p')
child.expect('Enter password:')
child.sendline('xuwuqiang')

child.expect('mysql> ')
child.sendline('use kytv_user;')
child.sendline('select * from kytv_user;')
print child.before
child.interact()


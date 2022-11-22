# import pexpect
# child = pexpect.spawn("echo myworld")
# print(child.expect(["Hello","Welcome","Myworld"]))
import pexpect
child = pexpect.spawn("cat")
child.sendline("welcome world")
print(child.expect(["Hello","Welcome","Myworld"]))
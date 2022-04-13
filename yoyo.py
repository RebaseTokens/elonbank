import json
import subprocess
import sched, time

s = sched.scheduler(time.time, time.sleep)


def elonbank(sc):
    print('Enter')
    with open('/root/Desktop/elonbank/elonbank.json', 'r') as file :
      filedata = file.read()

    filedata = filedata.replace(']\n[', ',')
    filedata = filedata.replace('][', ',')

    with open('/root/Desktop/elonbank/elonbank.json', 'w') as file:
      file.write(filedata)
  
    s.enter(5, 1, commit, (s,))
    

def commit(sc):
    print('Commit')
    
    subprocess.call(['/root/Desktop/elonbank/autocommit.sh'])
    print('Done')
  
    s.enter(60, 1, elonbank, (s,))


s.enter(5, 1, elonbank, (s,))
s.run()

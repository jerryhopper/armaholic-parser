import os,sys,time

sys.stdout.write('Start bidentify server file analysis server \n')
while True:
    try:
        sys.stdout.write('Keeping the container up  :)\n')
        time.sleep(500)
    except Exception as inst:
       print(type(inst))
       print(inst.args)
       print(inst)
       sys.stderr.write('Fatal error!\n')
       time.sleep(5)
       pass

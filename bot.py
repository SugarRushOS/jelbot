from pyomegle import OmegleClient, OmegleHandler
import time, threading
def counter():
    if 'cnt' not in counter.__dict__:
        counter.cnt = 0
    counter.cnt += 1
    return counter.cnt

counter()
class Example(OmegleHandler):
    def connected(self):
        super(Example, self).connected()
        self.omegle.send('19 F')

    def message(self,message):
        print(message)
        
        if counter.cnt == 1:
            c.send('Where are you from?')

        if counter.cnt == 2:
            time.sleep(.742)
            c.send('I\'m from LA')
            time.sleep(3)
            c.send("Add me on insta we can talk there more")
            c.send("@Asseater69")
            time.sleep(1)
            counter.cnt = 0
            time.sleep(2)
            c.next()
        else:
            counter.cnt += 1

    def typing(self):
        print("typing")

    def server_message(message, self):
        print(message)
    
    def disconnected(self):
        print("Other person disconnected")
        c.next()

h = Example()
c = OmegleClient(h, wpm=20, lang='en')
c.start()

time.sleep(0.373)

lokalzeit = time.time()
foligezeit = lokalzeit+30
def resetTime():
    print('too long')
    c.next()
    threading.Timer(30, resetTime).start()

resetTime()

while 1:
    input_str = raw_input('')
    if lokalzeit == foligezeit:
        resetTime()
        c.next()
    if input_str.strip() == '/next' or input_str.strip() == '/n':
        resetTime()
        c.next()
    elif input_str.strip() == '/quit' or input_str.strip() == '/exit' or input_str.strip() == '/q' or input_str.strip() == '/e':
        c.disconnect()
        break
    elif input_str.strip() == '/help' or input_str.strip() == '/h':
        
        print("Usage: [message] or [/command] ")
        print("commands:")
        print("    -/next, /n ............ : Find a new omigle user.")
        print("    -/quit, /exit, /q, /e ... : Self explanitory.")
        print("    -/help, /h ............ : Display this message.")
    else:
        c.send(input_str)

## Originally published under http://wanlinksniper.blogspot.com.es/2014/05/erlang-c-en-python-herramientas-para-el.html
## A few Python routines I put together one evening to compute traffic intensity, agent occupancy, probability of waiting,
## average speed of answer (ASA), service level, agents needed and other Erlang-C related stuff.
## broken link: http://www.mitan.co.uk/erlang/elgcmath.htm
## wayback machine: https://web.archive.org/web/20181209042241/http://www.mitan.co.uk/erlang/elgcmath.htm
## Python3 ported

from math import pow,factorial,log,exp

def PowerFact(b,e):
    ## Returns b^e / e! used everywhere else in the model
    return pow(b,e)/factorial(e)

def erlangC(m,u):
    ## Returns the probability a call waits.
    ## m is the agent count
    ## u is the traffic intensity
    p = u/m  ##  agent occupancy
    suma = 0
    for k in range(0,m):
        suma += PowerFact(u,k)
    erlang = PowerFact(u,m) / ((PowerFact(u,m)) + (1-p)*suma)
    return erlang

def SLA(m,u,T,target):
    ## Returns the average speed of answer
    ## m is the agent count
    ## u is the traffic intensity
    ## T is the average call time
    ## target is the target answer time
    return (1 - erlangC(m, u) * exp(-(m-u) * (target/T)))

def ASA(m,u,T):
    ## Returns the average speed of answer (ASA)
    ## m is the agent counts.
    ## u is the traffic intensity
    ## T is the average call time
    return erlangC(m, u) * (T/(m-u))

def agentsNeeded(u,T,targetSLA,target):
    ## Returns the number of agents needed to reach given SLA
    ## u is the traffic intensity
    ## T is the average call time
    ## target is the target answer time
    ## targetSLA % calls answered under target time
    level=0
    m=1
    while level<targetSLA:
        level = SLA(m,u,T,target)
        m += 1
    return m-1
    

def showStats(calls,interval,T,m,target,level):
    # calls       number of calls in a given time interval
    # interval    the time interval, in secs (1800 s == 30 minutes)
    # landa       calls/interval
    # T           average call duration, in secs
    # m           number of agents
    # u=landa*T   traffic intensity
    # p=u/m       agent occupancy
    landa = calls/interval
    u=landa*T      # traffic intensity
    p=u/m          # agent occupancy

    print('calls: {}   interval: {}   landa: {:.8f} (l = calls/interval)'.format(calls, interval, landa))
    print('traffic intensity: {:.2f}   agents: {}    agent occupancy: {:.2f}'.format(u,m,p))
    print('ErlangC, Probability of waiting: {:.2f}%'.format(erlangC(m,u)*100))
    print('ASA, Average speed of answer: {:.1f} secs'.format(ASA(m,u,T)))
    print('Probability call is answered in less than {} secs: {:.2f}%'.format(target,SLA(m,u,T,target)*100))
    print('Agents needed to reach {:.2f}% calls answered in <{} secs: {}'.format(level*100,target,agentsNeeded(u,T,level,target)))

def main():
    # calls       number of calls in a given time interval
    # interval    the time interval, in secs (1800 s == 30 minutes)
    # landa       calls/interval
    # T           average call duration, in secs
    # m           number of agents
    # u=landa*T   traffic intensity
    # p=u/m       agent occupancy
    TESTS = [
        #calls,interval,T,m,target,level
        [360, 1800,  240, 55,   15, 0.70],
        [300,  900,  180, 65,   45, 0.95],
        [650, 3600,  150, 34,   30, 0.50],
        [20,  3600, 1800, 11, 3600, 0.80]
    ]

    for dataset in TESTS:
        calls,interval,T,m,target,level = dataset
        showStats(calls,interval,T,m,target,level)
        print("-"*10)

if __name__ == "__main__":
    main()
## Originally published under http://wanlinksniper.blogspot.com.es/2014/05/erlang-c-en-python-herramientas-para-el.html
## A few Python routines I put together one evening to compute traffic intensity, agent occupancy, probability of waiting,
## average speed of answer (ASA), service level, agents needed and other Erlang-C related stuff.
## http://www.mitan.co.uk/erlang/elgcmath.htm
## Bitcoins, etc to Antonio Gallego amturing@gmail.com, complaints to /dev/null

from math import pow,factorial,log,exp

def PowerFact(b,e):
    ## Returns b^e / e! used everywhere else in the model
    return pow(b,e)/factorial(e)

def erlangC(m,u):
    ## Returns the probability a call waits.
    ## m is the agent count
    ## u is the traffic intensity
    suma=0
    for k in range(0,m):
        suma+=PowerFact(u,k)
    erlang=PowerFact(u,m)/((PowerFact(u,m))+(1-p)*suma)
    return erlang

def SLA(m,u,T,target):
    ## Returns the average speed of answer
    ## m is the agent count
    ## u is the traffic intensity
    ## T is the average call time
    ## target is the target answer time
    return (1 - erlangC(m, u) * exp(-(m-u)*(target/T)))

def ASA(m,u,T):
    ## Returns the average speed of answer (ASA)
    ## m is the agent counts.
    ## u is the traffic intensity
    ## T is the average call time
    return erlangC(m, u)*(T/(m-u))

def agentsNeeded(u,T,targetSLA,target):
    ## Returns the number of agents needed to reach given SLA
    ## u is the traffic intensity
    ## T is the average call time
    ## target is the target answer time
    ## targetSLA % calls answered under target time
    level=0
    m=1
    while level<targetSLA:
        level=SLA(m,u,T,target)
        m+=1
    return m-1
    

######################################################################################
######################################################################################
######################################################################################

calls=360.     # number of calls in a given time interval
interval=1800. # the time interval, in secs (1800 s == 30 minutes)
landa=calls/interval
T=240.         # average call duration, in secs
m=55           # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'secs, average speed of answer (ASA)'
target=15
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'secs'
nivel=0.7
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'secs'

######################################################################################
######################################################################################
######################################################################################

print "-"*10

calls=300.      # number of calls in a given time interval
interval=900. # the time interval, in secs (1800 s == 30 minutes)
landa=calls/interval
T=180.        # average call duration, in secs
m=65            # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'secs, average speed of answer (ASA)'
target=45
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'secs'
nivel=0.95
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'secs'

######################################################################################

print "-"*10

calls=650.      # number of calls in a given time interval
interval=3600. # the time interval, in secs (1800 s == 30 minutes)
landa=calls/interval
T=150.        # average call duration, in secs
m=34            # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'secs, average speed of answer (ASA)'
target=30
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'secs'
nivel=0.5
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'secs'


######################################################################################

print "-"*16
print "-"*3,"EXAMPLE 1","-"*3
print "-"*16

calls=20.      # number of calls in a given time interval
interval=3600. # the time interval, in secs (1800 s == 30 minutes)
landa=calls/interval
T=1800.        # average call duration, in secs
m=11           # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'secs, average speed of answer (ASA)'
target=3600
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'secs'
nivel=0.8
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'secs'


######################################################################################

print "-"*16
print "-"*3,"EXAMPLE 2","-"*3
print "-"*16

calls=4280.      # number of calls in a given time interval
interval=168.    # the time interval, in hours (7dx24h = 168)
landa=calls/interval
T=1./6           # average call duration, in hours
m=6           # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'hrs, average speed of answer (ASA)'
target=0.5
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'hrs'
nivel=0.87
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'hrs'

######################################################################################

print "-"*16
print "-"*3,"EXAMPLE 3","-"*3
print "-"*16

calls=1282.    # number of calls in a given time interval
interval=60.   # the time interval, in hours (5dx12h = 60)
landa=calls/interval
T=0.75         # average call duration, in hours
m=18           # number of agents
u=landa*T      # traffic intensity
p=u/m          # agent occupancy

print landa,'calls/interval'
print u,'traffic intensity'
print m,'agents'
print p,'agent occupancy'
print erlangC(m,u)*100,'% probability of waiting, ErlangC'
print ASA(m,u,T),'hrs, average speed of answer (ASA)'
target=1
print SLA(m,u,T,target)*100,'% probability call is answered in less than',target,'hrs'
nivel=0.89
print agentsNeeded(u,T,nivel,target),'agents needed to reach',nivel*100,'% calls answered in <',target,'hrs'



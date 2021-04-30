pyErlang
========
Here's a link to a very good explanation about the Erlangs, and a few Python routines I put together one evening to compute traffic intensity, agent occupancy, probability of waiting, average speed of answer (ASA), service level, agents needed and other Erlang-C related stuff. I'm not an expert on this at all, just needed to validate some data and the calculators I came across didn't suit me (or I just didn't know how to use them)  

Aquí dejo una página con una explicación muy buena sobre los Erlangs, y unas rutinas en Python que escribí una tarde para calcular probabilidades de espera, número de agentes, niveles de servicio u temas relacionados con los Erlang. No soy para nada experto en el tema, simplemente necesitaba validar unos números y las calculadoras que encontraba no me servían (o yo no supe usarlas) 

http://www.mitan.co.uk/erlang/elgcmath.htm (as of May 2021 this link is unavailable)
https://web.archive.org/web/20181209042241/http://www.mitan.co.uk/erlang/elgcmath.htm (wayback machine)


Typical Output:

C:\Data\CODE>python pyErlang.py
calls: 360   interval: 1800   landa: 0.20000000 (l = calls/interval)
traffic intensity: 48.00   agents: 55    agent occupancy: 0.87
ErlangC, Probability of waiting: 23.87%
ASA, Average speed of answer: 8.2 secs
Probability call is answered in less than 15 secs: 84.59%
Agents needed to reach 70.00% calls answered in <15 secs: 53
----------
calls: 300   interval: 900   landa: 0.33333333 (l = calls/interval)
traffic intensity: 60.00   agents: 65    agent occupancy: 0.92
ErlangC, Probability of waiting: 42.01%
ASA, Average speed of answer: 15.1 secs
Probability call is answered in less than 45 secs: 87.96%
Agents needed to reach 95.00% calls answered in <45 secs: 67
----------
calls: 650   interval: 3600   landa: 0.18055556 (l = calls/interval)
traffic intensity: 27.08   agents: 34    agent occupancy: 0.80
ErlangC, Probability of waiting: 14.30%
ASA, Average speed of answer: 3.1 secs
Probability call is answered in less than 30 secs: 96.41%
Agents needed to reach 50.00% calls answered in <30 secs: 29
----------
calls: 20   interval: 3600   landa: 0.00555556 (l = calls/interval)
traffic intensity: 10.00   agents: 11    agent occupancy: 0.91
ErlangC, Probability of waiting: 68.21%
ASA, Average speed of answer: 1227.8 secs
Probability call is answered in less than 3600 secs: 90.77%
Agents needed to reach 80.00% calls answered in <3600 secs: 11
----------

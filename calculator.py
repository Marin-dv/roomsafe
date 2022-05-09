
from math import sqrt, pow, pi
import math
from flask import Flask, flash, jsonify, redirect, render_template, request, session


def calc(A, h, Th, Tm, La, Pf, H, Pi, Qb, pm, Cq, Vs, Vt, Nguest, pml, Cql, Qbl, Thl, Tml, outdoor, S, ServHours, ServMinutes, age, outvalue):
    Rc = ((0.00007/60)*pow(float(La)*float(h), 1/2))
    Lc = (float(La)/3600)*(1+(pow(10, -12)/(Rc*Rc)))+((0.6*float(H)/3600))+((float(outdoor)*float(Pf))/3600)
    
    Tnet = 3600*Th+60*Tm
    s=0
    if outvalue == 1:
        for i in range(Nguest):
            s = s+(0.3*float(Qbl[i])*float(Vs)*float(age)*float(Qb)*float(Cql[i])*float(pml[i])*float(pm)/(float(Lc)*float(A)*float(h)*3600*3600))
        l = Lc*Tnet*Tnet
        Rj = (l/(Lc*Tnet+1))*s
        
    else:
        for i in range(Nguest):
            s = s+((3*float(Qbl[i])*math.floor(float(pm))*float(Cq)*sqrt(3.14159269*0.0006))/((3600*2*(float(Nguest)-1))*(3.14159269+0.15*0.15)*float(sqrt(A))))
        Rj = s*Tnet
    

    Rjf = Rj*(Pi/0.1)
    GRj = round(10/(Rjf+1))
    return GRj
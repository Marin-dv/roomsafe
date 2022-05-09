from math import sqrt, pow, pi
import math
from flask import Flask, flash, jsonify, redirect, render_template, request, session


def Hcalc(A, h, Th, Tm, La, Pf, H, Pi, Qb, pm, Cq, Nguest, outdoor, ageAvg, outvalue):
    Rc = ((0.00007/60)*pow(float(La)*float(h), 1/2))
    Lc = (float(La)/3600)*(1+(pow(10, -12)/(Rc*Rc)))+((0.6*float(H)/3600))+((float(outdoor)*float(Pf))/3600)
    print("outvalue", outvalue)
    Tnet = 3600*float(Th)+60*float(Tm)
    if outvalue == 1:
        invalue = 0
    else:
        invalue = 1
    print("values", A, h, Th, Tm, La, Pf, H, Pi, Qb, pm, Cq, Nguest, outdoor, ageAvg, outvalue)
    s=0
    if outvalue == 1:
        for i in range(int(Nguest)):
            s = s+(0.3*float(Qb)*float(Qb)*float(ageAvg)*float(Cq)*float(pm)*float(pm)/(float(Lc)*float(A)*float(h)*3600*3600))
        l = Lc*Tnet*Tnet
        Rj = (l/(Lc*Tnet+1))*s
    else:
        for i in range(int(Nguest)):
            s = s+(3*float(Qb)*math.floor(float(pm))*float(Cq)*float(Tnet)*sqrt(pi*0.0006))/((3600*2*(float(Nguest)-1))*(pi+0.15*0.15)*float(sqrt(A)))
        Rj = s
        
    Rjf0 = Rj*(Pi*(1-Pi)*float(Nguest)/0.1)
    GRj = round(10/(Rjf0+1))
    return GRj

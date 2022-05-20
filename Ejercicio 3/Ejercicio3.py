from pyswip import Prolog 
prolog = Prolog() 
prolog.assertz("papa(gonzalo,beatriz)") 
prolog.assertz("papa(beatriz,gary)") 
prolog.assertz("papa(mario,gary)") 
prolog.assertz("papa(gonzalo,franco)") 
prolog.assertz("papa(franco,abigail)") 
prolog.asserta("abuelo(X,Y):-papa(X,Z),papa(Z,Y)") 
prolog.asserta("nieto(X,Y):-papa(Z,X),papa(Y,Z)") 
prolog.asserta("hermano(X,Y):-papa(Z,X),papa(Z,Y)") 
prolog.asserta("primo(X,Y):-papa(Z,X),papa(W,Y),hermano(Z,W),X\=Y") 
abuelos = list(prolog.query("abuelo(X,Y)"))
for abuelo in abuelos: 
    print (abuelo["X"], " - abuelo - ",abuelo["Y"] ) 
    
nietos= list(prolog.query("nieto(X,Y)")) 
for nieto in nietos: 
    print ( nieto["X"], " - nieto - ",nieto["Y"] ) 
     
primos = list(prolog.query("primo(X,Y)")) 
for primo in primos: 
    print (primo["X"], " - primo - ",primo["Y"] ) 
 
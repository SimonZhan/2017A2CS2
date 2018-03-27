`#ECQ`
`##Task 29.01`
capitalcity(paris).
capitalcity(berlin).
capitalcity(cairo).

`##Task 29.02`

/*Task 29.03*/
male(kevin).
male(fred).
female(alia).
father(F,C) :- male(F),parent(F,C)

`##Task 29.04`
ancestor(A,B) :-parent(A,B).
ancestor(A,B) :-parent(A,X), ancestor(X,B).

`##Task 29.05`
/*answer 120*/
factorial(1, 1).
factorial(N, R) :-
    M is N - 1,
    factorial(M, X),
    R is N * X.

`##Task 29.06`
writelist([]).
writelist([H|T]) :-write(H),nl,writelist([H|T]).
-------------------------------

Question 1.
/*fact*/
capital(vienna). 
capital(london). 
capital(santiago). 
capital(caracas). 
capital(tokyo). 
cityin(vienna, austria). 
cityin(santiago, chile). 
cityin(salzburg, austria). 
cityin(maracaibo, venezuela). 
continent(austria, europe). 
continent (chile, southAmerica). 
continent(uk, europe). 
continent(argentina, southAmerica). 
iVisited(vienna). 
iVisited(tokyo).
/**/ 
/*rule*/
capitalOf(City, Country) :-capital(City),cityin(City, Country). europeanCity(City) :-cityin(City, Country),continent(Country, europe). 
/**/	

a.
i.
cityin(london,UK).
ii.
iVisited(strasbourg).

b.
chile, argentina.

c.
countriesIVisited(Country) :- cityin(City,Country), iVisited(City).

Question2
a.i.For example, Clause 10
 ii. For example, Clause 15

b.i. Who = Jack
 ii. output False. 
iii. output False.

c.i. qualifiedCarDrivers(X) :- qualifiedDriver(X, car). 
 ii. partQualified(X) :- passedTheoryTest(X) AND NOT( passedDrivingTest(X, _)). 

d.Clause 11 should be True.
Clause 01 and Clause 05 are False. The reason is the conflict between the age setting. Also, the Clause 15, rules should be False. The reason is A is smaller than L in this case. 
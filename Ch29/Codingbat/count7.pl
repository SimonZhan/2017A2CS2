count7(0,0).
count7(N,P) :-
    E is N div 10,
    count7(E,X),
    A is N mod 10,
    B is A div 7,
    C is A div 8,
    D is B - C,
    P is X + D.
triangle(0,0).
triangle(1,1).
triangle(R,B) :-
    P is R - 1,
    triangle(P,X),
    B is P + X + 1.
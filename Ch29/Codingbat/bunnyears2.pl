bunnyear(0,0).
oddeven(0, 2).
oddeven(1, 3).
oddeven(N, Y) :-
    M is N - 2,
    oddeven(M, Z),
    Y is Z.

bunnyear(N, X) :-
    M is N - 1,
    bunnyear(M, P),
    oddeven(M, Y), 
    X is Y + P.
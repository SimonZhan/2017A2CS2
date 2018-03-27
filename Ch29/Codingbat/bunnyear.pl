bunnyear(0, 0).
bunnyear(N, E) :-
    M is N - 1, 
    bunnyear(M, X),
    E is X + 2.
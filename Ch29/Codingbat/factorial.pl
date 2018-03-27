factorial(1, 1).
factorial(N, R) :-
    M is N - 1,
    factorial(M, X),
    R is N * X.
fibonacci(0, 0).
fibonacci(1, 1). 
fibonacci(N, R) :-
    P is N - 1,
    Q is N - 2,
    fibonacci(P, X),
    fibonacci(Q, Y), 
    R is X + Y. 
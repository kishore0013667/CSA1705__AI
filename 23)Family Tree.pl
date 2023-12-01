female(pam). %clauses
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(peter).

parent(pam,bob).
parent(tom,bob).
parent(tom,liz).
parent(bob,ann).
parent(bob,pat).
parent(pat,jim).
parent(bob,peter).
parent(peter,jim).

mother(X,Y):- parent(X,Y), female(X).
father(X,Y):- parent(X,Y), male(X).
sister(X,Y):- parent(Z,X), parent(Z,Y), female(X), X\==Y.
brother(X,Y):- parent(Z,X), parent(Z,Y), male(X), X\==Y.sum_integers(N, Sum) :-
    N > 1,
    N1 is N - 1,
    sum_integers(N1, Sum1),
    Sum is Sum1 + N.)

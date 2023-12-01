% Base case: Sum of integers from 1 to 1 is 1.
sum_integers(1, 1).

% Recursive case: Sum integers from 1 to N is the sum of N and the sum of integers from 1 to N-1.
sum_integers(N, Sum) :-
    N > 1,
    Prev is N - 1,
    sum_integers(Prev, PrevSum),
    Sum is N + PrevSum.

% Example usage:
% To find the sum of integers from 1 to 5, use: sum_integers(5, Result).

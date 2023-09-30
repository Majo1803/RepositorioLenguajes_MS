subconj([], _).
subconj([X|Y], S) :- member(X, S), subconj(Y, S).%Si X es miembro de S,revisa que Y tambien sea subconjunto de S



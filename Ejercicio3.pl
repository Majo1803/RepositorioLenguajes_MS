aplanar([],[]).

aplanar([X|Xs],L2):-
   \+ is_list(X),
   aplanar(Xs,ColaXs),
   L2=[X|ColaXs].
aplanar([X|Xs],L2):-
   is_list(X),
   aplanar(X,CabezaX),
   aplanar(Xs,ColaXs),
   append(CabezaX,ColaXs,L2).











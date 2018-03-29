# Task3
## 3.1, 3.2, 3.3
character(jim).
character(jenny).
character(habib).
character(Michael).
character_type(jim,prince).
character_type(jenny,princess).
character_type(habib,explorer).
character_type(Michael,king).
hasskill(jim,fly).
hasskill(jenny,invisibility).
hasskill(habib,timetravel).
asskill(Michael,sing).
pet(jim,horse).
pet(jenny,bird).
pet(habib,fish).
pet(Michael,dog).
animal(horse).
animal(bird).
animal(fish).
animal(dog).
skill(fly).
skill(invisibility).
skill(timetravel).
skill(sing).

has_skill(X,Y):-
	character(X),
	skill(Y).

haspet(X,Y):-
	character(X),
	animal(Y).
	
	
## task 3.4
True
pricess
jim
invisibility
jim

## task 3.5
pet(jim,X).
has_skill(X,fly).
skill(X).
pet(X,Y),character_type(X,princess).
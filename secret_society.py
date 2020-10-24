def society_name(l):
    return ''.join(n[0] for n in sorted(l))



print(society_name(["Adam", "Sarah", "Malcolm"]) == "AMS")
print(society_name(["Harry", "Newt", "Luna", "Cho"]) == "CHLN")
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) == "CJMPRR")

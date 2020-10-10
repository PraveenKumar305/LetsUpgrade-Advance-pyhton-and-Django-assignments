input = """Nick Fury : Tony Stark, Maria Hill, Norman Osborn
Hulk : Tony Stark, HawkEye, Rogers
Rogers : Thor
Tony Stark: Pepper Potts, Nick Fury
Agent_13 : Agent-X, Nick Fury, Hitler
Thor: HawkEye, BlackWidow
BlackWidow:Hawkeye
Maria Hill : Hulk, Rogers, Nick Fury
Agent-X : Agent_13, Rogers
Norman Osborn: Tony Stark, Thor"""
lvlO= "Nick Fury"
dataset = {}
for each in input.split("\n"):
    tmp = each.split(":")
    dataset[tmp[0].strip()] = tmp[1].strip()
SHIELD_members = []
HYDRA_memebrs = []


def traverse(name):
	if dataset.get(name, None):
		for each in dataset.get(name).split(","):
			if each.strip() not in SHIELD_members:
				SHIELD_members.append(each.strip())
				traverse(each.strip())
SHIELD_members.append(lvlO)
traverse(lvlO)
print(dataset)

values = [i.strip() for each in dataset.values() for i in each.split(",") ]
All_members = list(dataset.keys())+ values
All_members = list(set(All_members))
print(All_members)

hydra = set(All_members) -set(SHIELD_members)
print(hydra)

class Party:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def __len__(self):
        return self.members

    def __eq__(self, other):
        return self.members == other.members

    def __lt__(self, other):
        return self.members < other.members


communist_party = Party("People's Party", 130)
libertarian_party = Party("Selfish Pricks", 10)
philatelists_party = Party("Stamps are our passion", 10)
neoliberal_party = Party("BY ŻYŁO SIĘ .LEPIEJ", 200)


print(len(communist_party))  # 130
print(len(philatelists_party))  # 10
print(communist_party == libertarian_party)  # False
print(communist_party > neoliberal_party)  # False
print(communist_party < neoliberal_party)  # True
print(communist_party == libertarian_party)  # False
print(philatelists_party == libertarian_party)  # True
print(philatelists_party == libertarian_party)  # True
print(neoliberal_party > communist_party)  # True
print(neoliberal_party != communist_party)  # True
parties = [communist_party, libertarian_party, philatelists_party, neoliberal_party]
print(max(parties).name)  # BY ŻYŁO SIĘ .LEPIEJ
print(min(parties).name)  # Selfish Pricks

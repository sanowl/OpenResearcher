import fickling

with open("example_history/multimodal.pkl", 'rb') as file:
    multimodal = fickling.load(file)

with open("example_history/wizard lm.pkl", 'rb') as file:
    wizard_lm = fickling.load(file)

with open("example_history/what is ppo.pkl", 'rb') as file:
    what_is_ppo = fickling.load(file)

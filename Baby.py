from random import choice

questons = ["Why is the sky blue?:", "Why is there a face on the moon?:","Where are all the dinosaurs gone?:"]

question = choice(questons)
answer = input(question).strip().lower()

while answer != "just because":
	answer = input("Why?:").strip().lower()

	print("Oh okay")
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    combined_name = name1 + name2
    combined_true = combined_name.count("t") + combined_name.count("r") + combined_name.count("u")+ combined_name.count("e")
    combined_love = combined_name.count("l") + combined_name.count("o") + combined_name.count("v")+ combined_name.count("e")
    combined_score = str(combined_true) + str(combined_love) 
    print(f"your love score is {combined_score}")
calculate_love_score("antar", "kenzy")
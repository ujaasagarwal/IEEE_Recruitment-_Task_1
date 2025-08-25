cutoff_list = [
    ("Pilani", "CS", 327),
    ("Pilani", "Chemical", 280),
    ("Pilani", "MSc Eco", 271),
    ("Pilani", "MSc Bio", 265),
    
    ("Goa", "CS", 310),
    ("Goa", "Chemical", 239),
    ("Goa", "MSc Eco", 230),
    ("Goa", "MSc Bio", 225),
    
    ("Hyderabad", "CS", 295),
    ("Hyderabad", "Chemical", 250),
    ("Hyderabad", "MSc Eco", 240),
    ("Hyderabad", "MSc Bio", 235),
]
cutoff_dict={}

for campus, branch, cutoff in cutoff_list:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = cutoff

print(cutoff_dict)

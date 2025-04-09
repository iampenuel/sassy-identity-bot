# ============================================
# DATA ENTRY BOT: The Identity Protocol
# ============================================

print("Welcome to the system...\n\nPlease remain calm.\n")
print("Let's get this party started!\n")

print("============================================")
print("   DATA ENTRY BOT: The Identity Protocol")
print("============================================\n")

# === NAME ===
first_name = input("What's your first name?: ")
last_name = input("What's your last name?: ")
full_name = first_name + " " + last_name
print(f"Apparently you are {full_name}. Hi {first_name}!\n")

# === AGE ===
while True:
    try:
        age = int(input("How old are you?: "))
        break
    except ValueError:
        print("Bruhhh I said a NUMBER. Not letters ahhh. Try again, I forgive you.")

future_age = age + 5
print(f"Projected age in 5 years: {str(future_age)}\n")

# === HEIGHT ===
while True:
    try:
        height = float(input("How tall are you (in cm)?: "))
        break
    except ValueError:
        print("Use digits...DIGITSSS! Give me your height in NUMBERS. *sigh* try again dear")

if height >= 186:
    print("Dang, my guyyyy...You better be modelling or in the NBA with this height haha. Jk Jk")
    print("You are tall!")
elif 145 <= height <= 179:
    print("Awwww I could literally fit you into my pocket...so cute! You're short not 'average'")
    print("and that's okay! ")
elif height <= 136:
    print("Ummmm...thanks for telling me your height?? Are you even real? 😭")
print(f"You are {str(height)} cm tall\n")

# === HUMAN STATUS ===
human_status = input("CraZZYYY question but...are you a human being? (yes/no): ").lower()
if human_status == "yes":
    print("You are a human being!\n")
else:
    print("You are probably an alien or robot...or something. You can't be an animal...I think")
    print("but you're definitely NOT a human.\n")

print(f"Well there's your identity report {first_name}!")

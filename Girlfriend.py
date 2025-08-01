from datetime import datetime

def wish_girlfriend(name):
    today = datetime.now().strftime("%B %d, %Y")
    message = f"""
    💖 Happy Girlfriend Day, {name}! 💖
    Date: {today}
    You are amazing, and I feel so lucky to have you in my life.
    Thank you for being my best friend and my love.
    Have a wonderful day, beautiful! 🌹
    """
    print(message)

# Replace 'HerName' with your girlfriend's name
wish_girlfriend("HerName")

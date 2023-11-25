def identify_situation(feeling):
    global output
    global situation

    if feeling == "happy":
        situation = "You are feeling happy! This is a great feeling. Enjoy it!"
        output = "Spend time with loved ones, do something you enjoy, or simply take some time for yourself to relax and recharge."
    elif feeling == "sad":
        situation = "You are feeling sad. It's okay to feel this way sometimes. Allow yourself to feel your emotions, but don't let them control you."
        output = "Talk to someone you trust, watch a comforting movie, or listen to good music."
    elif feeling == "angry":
        situation = "You are feeling angry. It's important to express your anger in a healthy way."
        output = "Exercise, write in a journal, or take a deep breath and count to ten."
    elif feeling == "scared":
        situation = "You are feeling scared. It's natural to feel scared sometimes, but it's important to face your fears."
        output = "Talk to someone you trust, read a self-help book, or face your fears gradually."
    elif feeling == "excited":
        situation = "You are feeling excited! This is a positive emotion that can motivate you to achieve great things."
        output = "Channel your excitement into productive activities, such as pursuing a hobby or learning a new skill."
    elif feeling == "frustrated":
        situation = "You are feeling frustrated. It's okay to feel this way sometimes, but it's important to find healthy ways to cope with frustration."
        output = "Take a break from whatever is frustrating you, practice relaxation techniques, or talk to someone you trust."
    elif feeling == "anxious":
        situation = "You are feeling anxious. Anxiety is a normal emotion, but it can become overwhelming if not managed properly."
        output = "Practice relaxation techniques, such as deep breathing or meditation, and seek professional help if your anxiety is severe."
    elif feeling == "stressed":
        situation = "You are feeling stressed. Stress is a normal response to pressure, but it can be harmful if it becomes chronic."
        output = "Identify the sources of your stress and take steps to manage them, such as delegating tasks, learning to say no, or taking breaks throughout the day."
    elif feeling == "overwhelmed":
        situation = "You are feeling overwhelmed. It's okay to feel this way sometimes, but it's important to break down tasks into smaller, more manageable steps."
        output = "Prioritize your tasks, delegate what you can, and take breaks when needed."
    elif feeling == "bored":
        situation = "You are feeling bored. Boredom can be a sign that you need some mental stimulation."
        output = "Try something new, learn a new skill, or connect with friends or family."
    elif feeling == "lonely":
        situation = "You are feeling lonely. Loneliness is a common emotion, but it can be isolating and depressing."
        output = "Connect with friends or family, join a club or group, or volunteer in your community."
    elif feeling == "insecure":
        situation = "You are feeling insecure. Insecurity can be a source of anxiety and self-doubt."
        output = "Focus on your strengths and accomplishments, challenge your negative thoughts, and build your self-esteem."
    elif feeling == "guilty":
        situation = "You are feeling guilty. Guilt can be a burden, but it can also be an opportunity for growth."
        output = "Learn from your mistakes, make amends if necessary, and forgive yourself."
    elif feeling == "ashamed":
        situation = "You are feeling ashamed. Shame can be a powerful emotion, but it doesn't have to define you."
        output = "Accept yourself for who you are, learn from your mistakes, and move on."
    elif feeling == "jealous":
        situation = "You are feeling jealous. Jealousy is a normal emotion, but it can be destructive if not managed properly."
        output = "Focus on your own blessings, avoid comparing yourself to others, and celebrate the successes of others."
    elif feeling == "disappointed":
        situation = "You are feeling disappointed. Disappointment is a natural reaction to setbacks, but it's important not to dwell on it."
        output = "Learn from your mistakes, pick yourself up, and keep moving forward."
    elif feeling == "nervous":
        situation = "You are feeling nervous. It's a natural feeling to experience when you're facing something new or challenging."
        output = "Take deep breaths, focus on the present moment, and visualize yourself doing well. Remind yourself that you've prepared for this, and you have the skills and abilities to succeed."
    else:
        situation = "I'm not sure how you're feeling. Can you please try to describe your feeling?"
        output = "please describe properly:"


feeling = input("How are you feeling today? ")
identify_situation(feeling)
print("Your situation right now :-" + situation)
print("Advice:-"+ output)

while True:
    more_feelings = input("Do you have any other feelings you'd like to identify? (yes/no) ")
    if more_feelings.lower() == "yes":
        feeling = input("How are you feeling now? ")
        identify_situation(feeling)
        print("Your situation right now :-" + situation)
        print("Advice:-"+ output)
    else:
        print("Thank you for using our emotional identification tool. We hope you have a great day!")
        break



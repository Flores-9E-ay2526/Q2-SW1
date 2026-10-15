# Club checker

from pyscript import display, document

def view_members(e):
    First_name = document.getElementById('First_name').value.strip()
    Last_name = document.getElementById('Last_name').value.strip()

    Full_name = f"{First_name} {Last_name}".title()

    Club_members = ["Lebwrong James", "Jalen brunson", "Lamelo ball", "James Harden", "Lucas Flores", "Andrew E"]
    Is_member = Full_name in Club_members

    if Is_member:
        display_message = f"Congratulations {Full_name}, you are now part of this team!"
    else:
        display_message = f"Sorry, {Full_name}, you are not included in the school's basketball varsity team."

    document.getElementById('result').innerHTML = ""
    display(display_message, target='result')
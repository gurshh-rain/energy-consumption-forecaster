with open("household_power_consumption.txt", "r") as file:
    content = file.read()


new_content = content.replace(";", ",")

with open("household_power_consumption.txt", "w") as file:
    file.write(new_content)
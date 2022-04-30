with open("nums.html", "a") as html:
    html.write("<!DOCTYPE html>\n<html>\n   <body>\n")

    for num in range(1, 1000001):
        line = str(num)

        # If the number is divisible by 10 into a whole number.
        if num % 10 == 0:
            # Add the bold tag.
            line = "<b>" + line + "</b>"

        # If the number is divisible by 3 into a whole number.
        if num % 3 == 0:
            # Add the italic tag.
            line = "<i>" + line + "</i>"

        # If the number is prime.
        if num > 1 and (num == 2 or num % 2 != 0) and all(
                num % divisor != 0 for divisor in range(3, int(num ** 0.5) + 1, 2)):
            # Add the underline tag.
            line = "<u>" + line + "</u>"

        # Write HTML to the file.
        html.write("    " + line + "<br>\n")

    html.write("    </body>\n</html>")

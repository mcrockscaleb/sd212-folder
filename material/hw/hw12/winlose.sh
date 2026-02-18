# Put your sed command (or commands) here
# I'll get you started - this command changes lead into gold.
# (You need to change it of course to be about win/lose stuff.)

sed 's/charwin/lose/g' input.txt | sed 's/charlose/win/g'


# Remember you will probably need to do *multiple* sed's in a pipeline
# to complete this HW!

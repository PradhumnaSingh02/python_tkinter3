from tkinter import *
root = Tk()
root.geometry('945x267')
root.title('Pradhumna')

# import levels different options
# text  - add the text
# bd - background
# fg - foreground
# font - sets the font
# padx - x padding
# pady - y padding
# relief - border stylish

paragraph = Label(text='''
India, officially the Republic of India (Hindi: Bhārat Gaṇarājya),[23] is a country 
in South Asia. It is the seventh-largest country by area, the second-most populous country, and th
e most populous democracy in the world. Bounded by the Indian Ocean on the south, the Arabian Sea on the 
southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[f] 
China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, 
India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime
 border with Thailand, Myanmar and Indonesia.''', bg="red" , fg='blue',padx=45, pady=56, font=("comicsansms", 20, ' bold'))
paragraph.pack(side=TOP, fill=Y)

title = Label(text="Credit goes to Pradhumna Singh", bg="green", fg="Yellow")
title.pack(side=BOTTOM, anchor='ne')

heading = Label(text="INDIAN HISTORY", bg='grey', fg="White", padx=89, pady=47, borderwidth=12, relief=SUNKEN)
heading.pack()
root.mainloop()

# important pack options
# anchor = nw,ne,se,sw (north east,west)..
# side=top,bottom,left,right

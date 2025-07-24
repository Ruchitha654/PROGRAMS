import qrcode
a=qrcode.QRCode()
text_mg="Hi students bye"
a.add_data(text_mg)
a.make(fit=True)
abijith=a.make_image(fill_color="black", back_color="white")
abijith.save("abhyu.png")
print("Save successfully")
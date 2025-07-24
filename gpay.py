import qrcode
upi_id="ambikajayashanthi@okaxis"
name="Ruchitha's Ambika "
amount="1"
note="Payment bcoz why not?"
upi_link=f"ambikajayashanthi@okaxis"
qr=qrcode.make(upi_link)
qr.save("upi_payment_qr.png")
print("done ya")
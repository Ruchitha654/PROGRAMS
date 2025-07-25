import qrcode
upi_id="ambikajayashanthi@okaxis"
name="Ruchitha's Ambika "
amount="1"
currency="INR"
note="Payment bcoz why not?"
upi_link= f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu={currency}"
qr=qrcode.make(upi_link)
qr.save("upi_payment_qr.png")
print("done ya")





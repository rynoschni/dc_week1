phonebook_dict = {
    'Alice': "703-493-1834",
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}
print(phonebook_dict)
print(phonebook_dict['Elizabeth'])

if "Kareem" in phonebook_dict:
    None
else:
    phonebook_dict["Kareem"] = "938-489-1234"
if "Alice" in phonebook_dict:
    del phonebook_dict["Alice"]
elif "Bob" in phonebook_dict:
    phonebook_dict["Bob"] = "968-345-2345"

    
print(phonebook_dict)

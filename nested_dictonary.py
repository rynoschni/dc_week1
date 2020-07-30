digitalcrafts = {
    'US': {
        'Georgia': {
            'Atlanta': '3423 Piedmont Road NE #420'
        },
        'Texas': {
            'Houston': '1334 Brittmoore Rd, Houston, TX 77043'
        }
    } 
}

print(digitalcrafts['US'])

print(digitalcrafts['US']['Texas']['Houston'])

digitalcrafts['US']["Florida"] = {
    'Tampa': '123 Jake Stogle House'
}
print(digitalcrafts['US'])

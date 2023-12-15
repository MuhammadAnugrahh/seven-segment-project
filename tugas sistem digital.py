segments = {
    0: [
        " aaaa ",
        "f    b",
        "f    b",
        "e    c",
        "e    c",
        " dddd "
    ],
    1: [
        "     b",
        "     b",
        "     b",
        "     c",
        "     c",
        "     c"
    ],
    2: [
        " aaaa",
        "     b",
        " gggg",
        "e     ",
        " dddd"
    ],
    3: [
        " aaaa",
        "     b",
        " gggg",
        "     c",
        " dddd"
    ],
    4: [
        "f    b",
        "f    b",
        " gggg ",
        "     #",
        "     #"
    ],
    5: [
        " aaaa",
        "f     ",
        " gggg",
        "     c",
        " dddd"
    ],
    6: [
        " aaaa ",
        "f     ",
        " gggg ",
        "e    c",
        " dddd "
    ],
    7: [
        " aaaa",
        "     b",
        "     b",
        "     c",
        "     c"
    ],
    8: [
        " aaaa ",
        "f    b",
        " gggg ",
        "e    c",
        " dddd "
    ],
    9: [
        " aaaa ",
        "f    b",
        " gggg ",
        "     c",
        " dddd"
    ]
}


def main(): 
  while True:
    x = int(input("Masukkan x: "))
    if x == 0 or x == 1:
      break
    else:
      print("Masukkan 0 atau 1!")
      continue
  while True:
    y = int(input("Masukkan y: "))
    if y == 0 or y == 1:
      break
    else:
      print("Masukkan 0 atau 1!")
      continue
  while True:
    z = int(input("Masukkan z: "))
    if z == 0 or z == 1:
      break
    else:
      print("Masukkan 0 atau 1!")
      continue

  if x == 0 and y == 0 and z == 0:
    segments_to_display = segments[0]
    print("\nBiner ke- 0: 1,1,1,1,1,1,0")
  elif x == 0 and y == 0 and z == 1:
    segments_to_display = segments[1]
    print("\nBiner ke- 1: 0,1,1,0,0,0,0")
  elif x == 0 and y == 1 and z == 0:
    segments_to_display = segments[2]
    print("\nBiner ke- 2: 1,1,0,1,1,0,1")
  elif x == 0 and y == 1 and z == 1:
    segments_to_display = segments[3]
    print("\nBiner ke- 3: 1,1,1,1,0,0,1")
  elif x == 1 and y == 0 and z == 0:
    segments_to_display = segments[4]
    print("\nBiner ke- 4: 0,1,1,0,0,1,1")
  elif x == 1 and y == 0 and z == 1:
    segments_to_display = segments[5]
    print("\nBiner ke- 5: 1,0,1,1,0,0,1")
  elif x == 1 and y == 1 and z == 0:
    segments_to_display = segments[6]
    print("\nBiner ke- 6: 1,0,1,1,1,1,1")
  elif x == 1 and y == 1 and z == 1:
    segments_to_display = segments[7]
    print("\nBiner ke- 7: 1,1,1,0,0,0,0")
  
  
  print("\nSeven segment display:\n")  
  for segment in segments_to_display:
    print(segment)
main()

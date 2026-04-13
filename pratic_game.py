print("🏰 Welcome to Treasure Hunt Escape!")
print("You are trapped in a dungeon... Find your way out!\n")

choice1 = input("You see two doors: LEFT or RIGHT? ").lower()

if choice1 == "left":
    print("\nYou enter a dark room...")
    choice2 = input("You see a chest and a tunnel. Open CHEST or go TUNNEL? ").lower()

    if choice2 == "chest":
        print("\n💀 BOOM! The chest was trapped. Game Over.")
    
    elif choice2 == "tunnel":
        print("\nYou crawl through the tunnel...")
        choice3 = input("You find a river. SWIM or BUILD a raft? ").lower()

        if choice3 == "swim":
            print("\n💀 A monster in the water eats you. Game Over.")
        
        elif choice3 == "build":
            print("\n🏆 You safely cross the river and find TREASURE! YOU WIN!")
        
        else:
            print("\nInvalid choice. Game Over.")

    else:
        print("\nInvalid choice. Game Over.")

elif choice1 == "right":
    print("\nYou walk into a room full of snakes...")
    print("💀 You got bitten. Game Over.")

else:
    print("\nInvalid choice. Game Over.")
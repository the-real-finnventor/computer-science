from base import *


class Item:
    def __init__(self, itemName, attackDamage, enchantments, durability):
        self.itemName = itemName
        self.attackDamage = attackDamage
        self.enchantments = enchantments
        self.durability = durability


def printHotbar(ll):
    itemNum = 0
    for item in ll:
        itemNum += 1
        enchantments = ""
        enchanmentNum = 0
        for enchanment in item.enchantments:
            enchantments += enchanment
            if enchanmentNum != len(item.enchantments) - 1:
                enchantments += ", "
            enchanmentNum += 1
        print(f"""Item Number: {itemNum}
Item Name: {item.itemName}
Attack Damage: {item.attackDamage}
Enchanments: {enchantments}
Durability: {item.durability}\n""")


items = [
    Item("Sword of the Ender", 7, ["Sharpness V", "Unbreaking III"], 1561),
    Item("Warforged Battleaxe", 9, ["Smite IV", "Efficiency III"], 250),
    Item("Midas Pickaxe", 4, ["Fortune III", "Unbreaking III"], 33),
    Item("Inferno Spade", 6, ["Fire Aspect II", "Silk Touch"], 2031),
    Item("Stormcaster Bow", 5, ["Power V", "Punch II", "Infinity"], 384),
    Item("Precision Crossbow", 6, ["Multishot",
         "Quick Charge III", "Piercing IV"], 326),
    Item("Ocean's Wrath Trident", 9, [
         "Impaling V", "Loyalty III", "Channeling"], 250),
    Item("Harvestmoon Reaver", 2, ["Fortune III", "Mending"], 1561),
    Item("Draconic Cleaver", 8, ["Sharpness IV", "Efficiency IV"], 1561)
]

ll = insertItems(items)

hotbar = ll.getLL()

printHotbar(hotbar)

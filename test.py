
import pyrebase

config = {
    "apiKey": "AIzaSyAPFjcbSU9AcY3pVaUpsr5t-Fai-PPS3KI",
    "authDomain": "kellog-s-recipe-api.firebaseapp.com",
    "databaseURL": "https://kellogg-s-recipe-api.firebaseio.com/",
    "storageBucket": "kellogg-s-recipe-api",
}


firebase = pyrebase.initialize_app(config)


db = firebase.database()
st = firebase.storage()

cereal = {
    "cerealList": [
                   {
                   "title": "Apple Jacks",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Chocolate Frosted Flakes",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Corn Flakes",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Corn Pops",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Froot Loops",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Frosted Flakes",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Frosted Mini-Wheats",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Honey Smacks",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Krave",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Raisin Bran",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Rice Krispies",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   },
                   {
                   "title": "Special K",
                   "amount": "null",
                   "volume": "null",
                   "imageUrl": "null"
                   }
                   ]
}

recipe = {
    "recipeList": [
                   {
                   "ingredientList": [
                                      {
                                      "name": "Cinnamon Roasted Apples",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salted Caramel",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Brown Sugar Cinnamon Pop-Tart Crumble",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Apple Pie",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1tqRTXAgWboGvFDKcWrU-Us6kZaJPbW71"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Cooked Cranberries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Oat Streusel",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Cran Apple Crisp",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1WfQAFERUIWNp87zxgvx9WumQUVljOf3X"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Chocolate Cake Mix",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Rainbow Sprinkles",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Vanilla Syrup",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Chocolate Birthday Cake",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1Uvy28gKJOKBXtALQF0n3N5lnYnkEMDGt"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "White Chocolate Chips",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Dried Blueberries",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Blueberry and Cream",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1oJekuc8uOqWIJ3JW6lCJvtYPzOuFW7n3"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Powdered Milk",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Honey Comb Candy",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Bee Pollen",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Milk and Honey",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1OAXMwthacuzHMko7x_eBv6EnKyxfKWZm"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Rice Krispies",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Toasted Coconut Flakes",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Sesame Seeds",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Fresh Pineapple",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Tropical Mermaid",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1iSr2OWZWN_DEKeWIzaa_udfGoW6EDtrN"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Maple Bacon",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Strawberry Jam",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Eggo Croutons",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "What's Shakin Bacon",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1wuG4lOIuUjm9NdcJsOGE0e_x8P0X8sNn"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Blueberry Jam (or Blueberry Lemon Jam)",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Lemon Zest ",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Corny Blues",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1YWu-9lCSijtitY6NqYJzssid1fkEPlqE"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Corn Flakes",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Half-Popped Popcorn",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Super Corny",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1LiHL4Wgqc2B3hjkWatt7ZnrtrEWG0Ebb"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Passion Fruit Jam",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Lime Zest",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Mini Marshmallows",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Life in Color",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1LzdTv3sNWAydZCM2KM1C4_mKv9itkp2P"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Mochi",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Fresh or Dried Mango",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Pacific Loop",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1dCIkmrjEM-CEiB8ybgXuGZIrrJ5DGF3g"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Special K",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Rum Bananas",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Candied Cashews",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cajeta",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Bananas Foster",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=18nQe_DAlyxu8LLqlOGDvJZ21lYwgCwvl"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Yellow Cake Mix",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Rainbow Sprinkles",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Vanilla Syrup",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Birthday Cake",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1JVwzM_GfdNSbyoHsCMqtf0uPIZPz-c_u"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Caramel or Salted Popcorn",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Reese's Pieces",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Whoppers",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "M&Ms",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Chocolate Covered Raisins",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Movie Time",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1Lw-Vuetcgyjk4s12-hyJrwrF9x6B2WIt"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Special K",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pistachios",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Lemon Zest ",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Thyme",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Pistachio Lemon",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1xQenSSGMkcNl00Pj8WopcXxNPcWr_Opd"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Marshmallows",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Chocolate Chips",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Graham Crackers",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "S'mores",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1XZis0te3Jf-wdzGjs7snA9mmsJ76Pfm5"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Toasted Walnuts",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Toasted Pistachios",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Honey ",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Baklava",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1Qsp3-Uj06H-aMa3er4cKY-Bi9r2uN4dT"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Raspberries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Instant Espresso Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Berry Au Lait",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1CBK7K9MmKAJYDt_YPihm1C6PyRqVbaZW"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Poached Pears",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cinnamon Roll Croutons",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Crystallized Ginger",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Toasted Marshmallow",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Christmas Morning",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1ioGK1b1yCLBuLZsgl4Jk3Bhj16HU5x02"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Fresh Pear",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Ground Ginger",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cinnamon",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Harvest Swoon",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1uULv4G0SFCEBbF4HqhPrDRGBdenRS3rl"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Grapefruit Segments",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Tarragon",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Sugar in the Raw",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Kosher Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Pucker Up",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1SXemZbvPOKloB56uR6SIgh8HBbTGl17U"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Raisins",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Chopped Walnuts",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Frosting Drizzle",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cinnamon",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Sticky Bun",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1gHZT2FOZUmghM6tzsGBGKjfbsd3kVPOQ"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Cajeta",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Diced or Dried Mango ",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cinnamon",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salt",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Churro",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1hG9_rsf3Rkeu6_hsaMqyts6apk4ziKEm"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Banana Chips",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pecans",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Honey",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Honey Buzz",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1AcozgttG8ABmp0WWTOGoxD7yvoPvDxlX"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Banana",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Hazelnuts",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Malted Milk Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Malted Nutty Banana",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1JjmS1LnwSwKVzilsiiA1J49FOVnAYCkt"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Chocolate Covered Pretzels",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Peanut Butter",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Salted Caramel",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Nutty Buddy",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1_b6rn9mbuSG9wEI3Oh8ejAI666W6_bGu"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Mini Coffee Meringues",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Luxardo Maraschino Cherries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Toasted Coconut Flakes",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Coffee Meringue",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=14N6hL-NIWqA0IKajAVgth0C_XKGlcU4A"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Graham Cracker ",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Chocolate Chips",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Butterscotch Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pecans",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Dulce de Leche",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Hello Dolly",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1YUuNhmpb1nO_NsRivRDeutZIzD4j_iOR"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Toasted Peanuts",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Banana Chips",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "The Circus",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1WWhKOfniKsOqpoChlIeRmppyC6B2nuLS"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Chocolate Covered Oranges",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Candied Slivered Almonds",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "The Sicilian",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1U5W4P3ReBeNG_BmOVOyZhYmAY3fCpZEb"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Fresh Strawberries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Green Tea Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Berry Me in Green Tea",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1FsEcpZfGbwv8QabRyqpgT6o2yRBiMp-o"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Lemon Curd",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Torched Marshmallow Fluff",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pie Crust Crumble",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Lemon Meringue Pie",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1mEXlE6-sFpi3N2ysQAvw1RC0c4qTMlcm"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Fresh Kiwi",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Dehydrated Pineapple",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Fresh Pinapple",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Mango Jam",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Tropicalia",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1_r6MTTDXg6TgMidnnfjORt4tFziqYMwE"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Instant Espresso Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Sweetened Condensed Milk",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Vietnamese Coffee",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1EEau1bvsEqiA6dXfwfkP3kP29V2Acclc"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Banana",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Almond Butter",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Banana Nut",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1ZYnp3rNSGbvhkQqCQ5xj6nkuZRMua3Kl"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Fresh Strawberries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Cocoa Nibs",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "White Chocolate Sauce",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Chocolate-Covered Strawberry",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1msmurz8ZpHXzQmpKFXn4wYHoXwFlDwJr"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Dried Goji Berries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Blueberries",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Acai Powder",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Duper Super",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1KjzPGuTWCN-uHKhw1mYkIfMoYjz4Ea7x"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Peanut Butter",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Toasted Peanuts",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Strawberry Jam",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Fresh Strawberries",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Peanut Butter Jelly Time",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1JFwbUTrhHKgl72QjNfpndzDVoupYz96O"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Frosted Flakes",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pistachio",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Lemon Zest",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Thyme",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Pistachio Lemon",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1xQenSSGMkcNl00Pj8WopcXxNPcWr_Opd"
                   },
                   {
                   "ingredientList": [
                                      {
                                      "name": "Dried Apricots",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Pistachio",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Almond Nougat",
                                      "amount": "null",
                                      "volume": "null"
                                      },
                                      {
                                      "name": "Apricot Jam",
                                      "amount": "null",
                                      "volume": "null"
                                      }
                                      ],
                   "title": "Turkish Delight",
                   "imageUrl": "https://drive.google.com/a/iteo.com/uc?authuser=0&id=1RcHF_F2ovhMhD4CkyVGYhRNMZQbt-NCo"
                   }
                   ]
}


name = "Sticky Bun"

link = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Sticky%20Bun.png?alt=media&token=661b2e43-92d2-4458-95c7-cdd2018979b7"

name2 = "Super Corny"

link2 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Super%20Corny.png?alt=media&token=b7c1d3e9-c76c-4a8b-a254-1329f5407cef"

name3 = "The Circus"

link3 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/The%20Circus.png?alt=media&token=e113b594-4439-44a1-a857-a594ac556528"

name4 = "The Sicilian"

link4 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/The%20Sicilian.png?alt=media&token=454defc8-53e2-4e8e-a1c6-c68331aeb3cc"

name5 = "Tropical Mermaid"

link5 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Tropical%20Mermaid.png?alt=media&token=807a791e-842b-4833-ab6c-20e273c19901"

name6 = "Tropicalia"

link6 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Tropicalia.png?alt=media&token=c4f27947-90ed-412c-8170-7dd8df428fa4"

name7 = "Turkish Delight"

link7 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Turkish%20Delight.png?alt=media&token=fc4e46a1-4d57-4d5f-a10f-852213ba501c"

name8 = "Vietnamese Coffee"

link8 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Vietnamese%20Coffee.png?alt=media&token=da2b7655-cb3b-446c-a9da-3969a575b537"

name9 = "Whats Shakin Bacon"

link9 = "https://firebasestorage.googleapis.com/v0/b/kellogg-s-recipe-api.appspot.com/o/Whats%20Shakin%20Bacon.png?alt=media&token=630a53f9-1b91-437d-8e15-0f6eed78d1a9"




db.child("images").child(name).set(link)
db.child("images").child(name2).set(link2)
db.child("images").child(name3).set(link3)
db.child("images").child(name4).set(link4)
db.child("images").child(name5).set(link5)
db.child("images").child(name6).set(link6)
db.child("images").child(name7).set(link7)
db.child("images").child(name8).set(link8)
db.child("images").child(name9).set(link9)


#image = st.child("gs://kellogg-s-recipe-api.appspot.com").download("baklava.png")




#db.child("recipe-list").set(recipe)
#db.child("cereal-list").set(cereal)



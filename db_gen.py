import sqlite3
#import mysql.connector

Loc = {
    "images": [
      {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/a02022.png",
            "label": "apple;red",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/b02022.png",
            "label": "ball;white",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/c02022.png",
            "label": "cherry;two;red",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/d02022.png",
            "label": "drum;sound;large",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/e02022.png",
            "label": "egg;white;raw",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/f02022.png",
            "label": "food;cuisins;restaurants",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/g02022.png",
            "label": "glares;sunglass;black;cool",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/h02022.png",
            "label": "house;beatiful;",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/i02022.png",
            "label": "icecream;tasty",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/j02022.png",
            "label": "jug;water;5 Liter",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/k02022.png",
            "label": "kite;orange;",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/l02022.png",
            "label": "lemons;yellow",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/m02022.png",
            "label": "mountains;green",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/n02022.png",
            "label": "nature;beach",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/o02022.png",
            "label": "orange;colour;fruit",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/p02022.png",
            "label": "pen;write;light",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/q02022.png",
            "label": "people;festival;enjoy",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/r02022.png",
            "label": "sun;bright;nature",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/u02022.png",
            "label": "moon;night;dark",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/w02022.png",
            "label": "watermelon;red;green;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/s02022.png",
            "label": "snacks;tasty;crunch",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/t02022.png",
            "label": "television;tv",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/z02022.png",
            "label": "zoo;animals",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/v02022.png",
            "label": "vase;flower;decor",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/x02022.png",
            "label": "ride;bike;car;drive",
            "date": "02-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/y02022.png",
            "label": "king;rule;power",
            "date": "02-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/a12022.png",
            "label": "apple;red;big",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/b12022.png",
            "label": "ball;white;black",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/c12022.png",
            "label": "cherry;two;red;tasty",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/d12022.png",
            "label": "drum;sound;large;2",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/e12022.png",
            "label": "egg;white;ripe",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/f12022.png",
            "label": "food;cuisins;hotels;restaurants",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/g12022.png",
            "label": "glares;sunglass;cool",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/h12022.png",
            "label": "house;beautiful;large;",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/i12022.png",
            "label": "icecream;tasty;cool",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/j12022.png",
            "label": "jug;water;10 Liter;empty",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/k12022.png",
            "label": "kite;orange;sky;",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/l12022.png",
            "label": "lemons;yellow;small",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/m12022.png",
            "label": "mountains;greeny;hills",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/n12022.png",
            "label": "nature;beach;warm",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/o12022.png",
            "label": "orange;colour;red-yellow",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/p12022.png",
            "label": "pen;write;thick",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/q12022.png",
            "label": "people;mall;shop",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/r12022.png",
            "label": "sun;heat;hot",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/u12022.png",
            "label": "moon;cool;light",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/w12022.png",
            "label": "watermelon;juicy;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/s12022.png",
            "label": "snacks;salty;munchy",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/t12022.png",
            "label": "telescope;universe",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/z12022.png",
            "label": "zebra;animal;white black",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/v12022.png",
            "label": "violin;music;opera",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/x12022.png",
            "label": "exibition;art;artist",
            "date": "02-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/y12022.png",
            "label": "king;rule;power;strict",
            "date": "02-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/a22022.png",
            "label": "almond;nuts;health",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/b22022.png",
            "label": "ball;white;small",
            "date": "23-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/c22022.png",
            "label": "chesse;milk;fat",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/d22022.png",
            "label": "disco;party;people",
            "date": "24-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/e22022.png",
            "label": "egg;white;raw;yolk",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/f22022.png",
            "label": "food;cuisins;nutrients",
            "date": "25-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/g22022.png",
            "label": "glares;sunglass;protect;;cool",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/h22022.png",
            "label": "house;expensive;asthetic;",
            "date": "26-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/i22022.png",
            "label": "ice;cream;tea;coffee;juice",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/j22022.png",
            "label": "jug;water;5 Liter;full",
            "date": "27-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/k22022.png",
            "label": "kimono;dress;beautiful",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/l22022.png",
            "label": "lemons;yellow;small",
            "date": "28-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/m22022.png",
            "label": "mountains;large;senere",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/n22022.png",
            "label": "nature;beach;waves;fun",
            "date": "29-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/o22022.png",
            "label": "orange;fruit;Vit C;juice",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/p22022.png",
            "label": "pancake;write;light",
            "date": "30-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/q22022.png",
            "label": "people;festival;enjoy",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/r22022.png",
            "label": "sun;bright;nature",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/u22022.png",
            "label": "moon;night;dark",
            "date": "01-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/w22022.png",
            "label": "watermelon;red;green;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/s22022.png",
            "label": "snacks;tasty;crunch",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/t22022.png",
            "label": "television;tv",
            "date": "22-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/z22022.png",
            "label": "zoo;animals",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/v22022.png",
            "label": "vase;flower;decor",
            "date": "21-01-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/x22022.png",
            "label": "ride;bike;car;drive",
            "date": "02-02-2022"
        },
        {
            "location": "Root/private/var/mobile/Media/DCMI/100/APPLE/y22022.png",
            "label": "king;rule;power",
            "date": "02-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/a02022.png",
            "label": "apple;red",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/b02022.png",
            "label": "ball;white",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/c02022.png",
            "label": "cherry;two;red",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/d02022.png",
            "label": "drum;sound;large",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/e02022.png",
            "label": "egg;white;raw",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/f02022.png",
            "label": "food;cuisins;restaurants",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/g02022.png",
            "label": "glares;sunglass;black;cool",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/h02022.png",
            "label": "house;beatiful;",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/i02022.png",
            "label": "icecream;tasty",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/j02022.png",
            "label": "jug;water;5 Liter",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/k02022.png",
            "label": "kite;orange;",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/l02022.png",
            "label": "lemons;yellow",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/m02022.png",
            "label": "mountains;green",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/n02022.png",
            "label": "nature;beach",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/o02022.png",
            "label": "orange;colour;fruit",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/p02022.png",
            "label": "pen;write;light",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/q02022.png",
            "label": "queen;beatiful",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/w002022.png",
            "label": "watermelon;red;green;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/s02022.png",
            "label": "snacks;tasty;crunch",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/t02022.png",
            "label": "television;tv",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/z02022.png",
            "label": "zoo;animals",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/v02022.png",
            "label": "vase;flower;decor",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/u02022.png",
            "label": "bright;sun;nature",
            "date": "01-02-2022"
        },{
            "location": "storage/DCIM/Camera/r02022.png",
            "label": "travel;tour;world",
            "date": "01-02-2022"
        },{
            "location": "storage/DCIM/Camera/x02022.png",
            "label": "people;festival;enjoy",
            "date": "02-02-2022"
        },{
            "location": "storage/DCIM/Camera/y02022.png",
            "label": "robot;machine;work",
            "date": "02-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/a12022.png",
            "label": "apple;red",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/b12022.png",
            "label": "ball;white",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/c12022.png",
            "label": "cherry;two;red",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/d12022.png",
            "label": "drum;sound;large",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/e12022.png",
            "label": "egg;white;raw",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/f12022.png",
            "label": "food;cuisins;restaurants",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/g12022.png",
            "label": "glares;sunglass;black;cool",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/h12022.png",
            "label": "house;beatiful;",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/i12022.png",
            "label": "icecream;tasty",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/j12022.png",
            "label": "jug;water;5 Liter",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/k12022.png",
            "label": "kite;orange;",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/l12022.png",
            "label": "lemons;yellow",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/m12022.png",
            "label": "mountains;green",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/n12022.png",
            "label": "nature;beach",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/o12022.png",
            "label": "orange;colour;fruit",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/p12022.png",
            "label": "pen;write;light",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/q12022.png",
            "label": "queen;beatiful",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/w12022.png",
            "label": "watermelon;red;green;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/s12022.png",
            "label": "snacks;tasty;crunch",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/t12022.png",
            "label": "television;tv",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/z12022.png",
            "label": "zoo;animals",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/v12022.png",
            "label": "vase;flower;decor",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/u12022.png",
            "label": "bright;sun;nature",
            "date": "01-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/r12022.png",
            "label": "travel;tour;world",
            "date": "01-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/x12022.png",
            "label": "people;festival;enjoy",
            "date": "02-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/y12022.png",
            "label": "robot;machine;work",
            "date": "02-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/a22022.png",
            "label": "apple;red",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/b22022.png",
            "label": "ball;white",
            "date": "23-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/c22022.png",
            "label": "cherry;two;red",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/d22022.png",
            "label": "drum;sound;large",
            "date": "24-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/e22022.png",
            "label": "egg;white;raw",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/f22022.png",
            "label": "food;cuisins;restaurants",
            "date": "25-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/g22022.png",
            "label": "glares;sunglass;black;cool",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/h22022.png",
            "label": "house;beatiful;",
            "date": "26-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/i22022.png",
            "label": "icecream;tasty",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/j22022.png",
            "label": "jug;water;5 Liter",
            "date": "27-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/k22022.png",
            "label": "kite;orange;",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/l22022.png",
            "label": "lemons;yellow",
            "date": "28-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/m22022.png",
            "label": "mountains;green",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/n22022.png",
            "label": "nature;beach",
            "date": "29-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/o22022.png",
            "label": "orange;colour;fruit",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/p22022.png",
            "label": "pen;write;light",
            "date": "30-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/q22022.png",
            "label": "queen;beatiful",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/w22022.png",
            "label": "watermelon;red;green;tasty",
            "date": "31-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/s22022.png",
            "label": "snacks;tasty;crunch",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/t22022.png",
            "label": "television;tv",
            "date": "22-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/z22022.png",
            "label": "zoo;animals",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/v22022.png",
            "label": "vase;flower;decor",
            "date": "21-01-2022"
        },
        {
            "location": "storage/DCIM/Camera/u22022.png",
            "label": "bright;sun;nature",
            "date": "01-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/r22022.png",
            "label": "travel;tour;world",
            "date": "01-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/x22022.png",
            "label": "people;festival;enjoy",
            "date": "02-02-2022"
        },
        {
            "location": "storage/DCIM/Camera/y22022.png",
            "label": "robot;machine;work",
            "date": "02-02-2022"
        }
    ]
}
conn = sqlite3.connect('db_img.db')
cursor = conn.cursor()


# Creating table
table ="""CREATE TABLE if not exists Images(location VARCHAR(255) not null, label VARCHAR(255) not null, date VARCHAR(10) not null);"""
cursor.execute(table)

'''
dataBase = mysql.connector.connect(host ="localhost",
  user ="user",
  passwd ="password")
db_cur = dataBase.cursor()
db_cur.excute(table)
'''

for i in range(len(Loc["images"])):
  # cursor.execute(""" INSERT INTO Images(location,label,varchar) VALUES (?,?,?)""", (input("Enter Location"),input("Enter Labels"),input("Enter Date")))
  data = Loc["images"][i]
  cursor.execute(""" INSERT INTO Images(location,label,date) VALUES (?,?,?)""", (data["location"],data["label"],data["date"]))
  #db_cur.execute(""" INSERT INTO Images(location,label,date) VALUES (?,?,?)""", (data["location"],data["label"],data["date"]))
# Queries to INSERT records.
# cursor.execute('''INSERT INTO Images VALUES ('Raju', '7th', 'A')''')
  
# Display data inserted
print("Data Inserted in the table: ")
#data=db_cur.execute('''SELECT * FROM Images''')
print("('location','label','date')")
for row in cursor.execute('''SELECT * FROM Images'''):
    print(row)
  
# Commit your changes in the database    
conn.commit() 
# # Closing the connection
conn.close()

'''
dataBase.commit()
dataBase.close()
'''
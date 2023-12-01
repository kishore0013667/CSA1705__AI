fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).
fruit_color(plum, purple).
fruit_color(strawberry, red).
fruit_color(blueberry, blue).

get_fruit_color(Fruit, Color) :- fruit_color(Fruit, Color).

fruits_of_color(Color, Fruits) :- findall(Fruit, fruit_color(Fruit, Color), Fruits).

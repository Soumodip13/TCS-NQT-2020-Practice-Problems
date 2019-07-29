capital = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
lower = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
res_capital = capital.split()
res_lower = lower.split()
for i in res_capital:
    print ord(i),
print " "
for i in res_lower:
    print ord(i),

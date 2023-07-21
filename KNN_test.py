import pandas as pd
import matplotlib.pyplot as plt
x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# lista com as classes dos pontos
classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]
plt.scatter(x,y, c=classes)
print("CU\n")
plt.show()

dados = pd.DataFrame({'x': x, 'y': y, 'classe':classes})
dados = dados.sort_values(by='classe')
print(dados)
from sklearn.neighbors import KNeighborsClassifier
features= dados[['x','y']]
label = dados['classe']
print("As features são: ")
print(features)
print("A label é: ")
print(label)

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(features, label)


new_x = int(input("x: "))
new_y = int(input("y: "))

new_point = [[new_x, new_y]]

#o modelo prediz a classe do novo ponto
prediction = knn.predict(new_point)

plt.scatter(x + [new_x], y + [new_y], c=classes + [prediction[0]])
plt.text(x=new_x-1.7, y=new_y-0.7, s=f"new point, class: {prediction[0]}")
plt.show()
plt.savefig('Sla.png')
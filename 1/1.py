import pulp

# Створення моделі
model = pulp.LpProblem("Maximization_Production", pulp.LpMaximize)

# Змінні для кількості вироблених одиниць Лимонаду та Фруктового соку
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')  # Лимонад
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat='Continuous')  # Фруктовий сік

# Цільова функція - максимізація загальної кількості продуктів
model += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
model += 2 * lemonade + 0 * fruit_juice <= 100, "Water"
model += 1 * lemonade + 0 * fruit_juice <= 50, "Sugar"
model += 1 * lemonade <= 30, "LemonJuice"
model += 0 * lemonade + 2 * fruit_juice <= 40, "FruitPuree"

# Розв'язання задачі
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Optimal number of Lemonades to produce: {lemonade.varValue}")
print(f"Optimal number of Fruit Juices to produce: {fruit_juice.varValue}")
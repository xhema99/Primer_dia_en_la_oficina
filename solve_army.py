from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Crear el problema de maximización
prob = LpProblem("Maximize_Army_Power", LpMaximize)

# Variables de decisión: número de espadachines, arqueros, jinetes
x = LpVariable("Espadachines", lowBound=0, cat='Integer')
y = LpVariable("Arqueros", lowBound=0, cat='Integer')
z = LpVariable("Jinetes", lowBound=0, cat='Integer')

# Función objetivo: maximizar poder
prob += 70*x + 95*y + 230*z

# Restricciones de recursos
prob += 60*x + 80*y + 140*z <= 1200  # Comida
prob += 20*x + 10*y <= 800  # Madera
prob += 40*y + 100*z <= 600  # Oro

# Resolver el problema
prob.solve()

# Resultados
print("Estado de la solución:", prob.status)
print("Número óptimo de Espadachines:", x.varValue)
print("Número óptimo de Arqueros:", y.varValue)
print("Número óptimo de Jinetes:", z.varValue)
print("Poder máximo:", prob.objective.value())
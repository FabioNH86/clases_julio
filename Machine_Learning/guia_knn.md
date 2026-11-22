# 📘 Guía de apoyo: K-Vecinos Más Cercanos (KNN)

Esta guía acompaña al cuaderno `01_knn_flores_iris.ipynb`. Úsala cuando no recuerdes qué hace una función o por qué hacemos algún paso. No hace falta leerla de corrido: busca la sección que necesites.

---

## 1. Ideas clave (el "mapa" del Machine Learning)

| Concepto | Qué significa | En nuestro proyecto |
|---|---|---|
| **Aprendizaje supervisado** | Le damos a la IA ejemplos **con la respuesta correcta** para que aprenda a adivinar la respuesta de ejemplos nuevos. | Flores con sus medidas **y** su especie. |
| **Características (`X`)** | Los datos que la IA puede "ver" para decidir. Por convención se escribe con **mayúscula** porque es una tabla. | Las 4 medidas: largo/ancho de sépalo y pétalo. |
| **Etiqueta (`y`)** | La respuesta que queremos adivinar. Va con **minúscula** porque es una sola columna. | La especie (0, 1 o 2). |
| **Clasificación** | Cuando la respuesta es una **categoría** (no un número cualquiera). | ¿Setosa, Versicolor o Virginica? |
| **Entrenamiento (train)** | Los datos con los que la IA estudia. | 120 flores (80 %). |
| **Prueba (test)** | Datos escondidos para el examen final. La IA **nunca** los ve al estudiar. | 30 flores (20 %). |
| **Hiperparámetro** | Una perilla del modelo que elegimos **nosotros**, no la IA. | `k` = número de vecinos. |

### ¿Por qué separar train y test?
Si le pones a alguien un examen con **las mismas preguntas** que estudió, puede sacar 100 solo por memoria, sin entender nada. El examen oculto nos dice si el modelo **generaliza**, es decir, si funciona con flores que nunca vio.

---

## 2. ¿Cómo piensa KNN?

KNN clasifica un objeto nuevo **según la clasificación de los objetos que tiene más cerca**. Siempre hace 3 pasos:

1. **Mide la distancia** entre el objeto nuevo y todos los objetos que memorizó.
2. **Elige los `k` más cercanos** (los vecinos).
3. **Votación**: la etiqueta más repetida entre los vecinos gana.

### La distancia
Con 2 características es la distancia "con regla" en un plano:

```
distancia = raíz( (x2 - x1)² + (y2 - y1)² )
```

Con 4 características (como Iris) es la misma idea, solo que sumando 4 términos en vez de 2. Se llama **distancia euclidiana** y es la que usa Scikit-Learn por defecto.

### ¿Cómo elegir `k`?
- **`k` muy chico (ej. 1):** el modelo le hace caso a **un solo** vecino. Si ese vecino es raro o un error, la predicción falla. Es "muy nervioso".
- **`k` muy grande (ej. 120):** escucha a **todos**, así que siempre gana la especie más común. Es "muy flojo".
- **Lo normal:** probar varios valores (como en el Bonus del cuaderno) y quedarse con uno intermedio.
- **¿Por qué impar?** Para evitar empates en la votación (2 contra 2).

### ⚠️ Cuidado con las escalas
En el calentamiento de las frutas, el **peso** (cientos de gramos) pesa mucho más en la distancia que la **acidez** (del 1 al 10). Una diferencia de 10 g "cuenta" igual que 10 puntos de acidez, ¡que es toda la escala! En proyectos reales se suelen **escalar** las características (ponerlas en rangos parecidos) antes de usar KNN. En Iris no es tan grave porque todas las medidas están en centímetros y en rangos similares.

### Ventajas y desventajas de KNN
- ✅ Muy fácil de entender y de explicar.
- ✅ "Entrenar" es instantáneo: solo memoriza.
- ❌ Predecir es lento con muchos datos (tiene que medir la distancia contra **todos**).
- ❌ Sensible a la escala de las características y a datos raros.

---

## 3. Funciones y herramientas que usamos

### Pandas (tablas)

| Función | Qué hace | Por qué la usamos |
|---|---|---|
| `pd.DataFrame(data=..., columns=...)` | Crea una tabla con filas y columnas con nombre. | Para ver los datos como en Excel, no como una lista de números sin nombre. |
| `tabla.head()` | Muestra las primeras 5 filas. | Echar un vistazo rápido sin imprimir 150 filas. |
| `tabla.shape` | Devuelve `(filas, columnas)`. **Sin paréntesis**: es un atributo, no una función. | Saber cuántos datos tenemos. |
| `tabla['columna'].value_counts()` | Cuenta cuántas veces aparece cada valor. | Revisar si las especies están balanceadas (50 de cada una). |
| `tabla.drop('columna', axis=1)` | Devuelve la tabla **sin** esa columna. `axis=1` = columna, `axis=0` = fila. | Sacar la respuesta (`especie`) de las características `X`. ¡Si la dejáramos, sería hacer trampa! |
| `tabla['columna']` | Toma una sola columna. | Para obtener `y`. |
| `tabla.iloc[posiciones]` | Toma filas por su **posición** (0, 1, 2...). | Para ver quiénes son los vecinos de la flor misteriosa. |

### Scikit-Learn (Machine Learning)

| Función | Qué hace | Por qué es importante |
|---|---|---|
| `load_iris()` | Carga el dataset de flores Iris. Trae `.data` (medidas), `.target` (especie en número), `.feature_names` (nombres de las medidas) y `.target_names` (nombres de las especies). | Tener datos limpios y listos para practicar sin descargar nada. |
| `train_test_split(X, y, test_size=0.2, random_state=42)` | Revuelve los datos y los parte en 4: `X_train, X_test, y_train, y_test`. | Crear el examen oculto. **El orden de las 4 variables importa.** |
| ↳ `test_size=0.2` | Qué fracción va al examen (0.2 = 20 %). | 80/20 es una división muy común. |
| ↳ `random_state=42` | Fija la "semilla" del revuelto para que **siempre** salga la misma división. | Que tú y yo obtengamos el mismo resultado. El 42 no tiene nada de especial: puede ser cualquier número. |
| `KNeighborsClassifier(n_neighbors=3)` | Crea un modelo KNN que consulta a 3 vecinos. | Es el "cerebro" de nuestro proyecto. |
| `modelo.fit(X_train, y_train)` | Entrena el modelo. En KNN, solo **memoriza** los datos. | Sin `fit`, el modelo no sabe nada y `predict` da error. |
| `modelo.predict(X)` | Devuelve la predicción para cada fila de `X`. Siempre devuelve una **lista** (array), aunque le des una sola flor; por eso usamos `[0]` para sacar el primer resultado. | Es como el modelo "responde el examen". |
| `modelo.kneighbors(X)` | Devuelve `(distancias, posiciones)` de los vecinos más cercanos. | Para espiar al "chismoso" y ver a quién le preguntó. |
| `accuracy_score(y_real, y_predicho)` | Porcentaje de aciertos (de 0 a 1). | Es la "calificación" del examen. 1.0 = 100 %. |

### El patrón que se repite en TODO Scikit-Learn
Casi todos los modelos funcionan igual, así que lo que aprendes con KNN te sirve para los demás:

```python
modelo = AlgunModelo(parametros)   # 1. Crear
modelo.fit(X_train, y_train)       # 2. Entrenar
predicciones = modelo.predict(X_test)  # 3. Predecir
accuracy_score(y_test, predicciones)   # 4. Evaluar
```

---

## 4. Errores comunes y cómo arreglarlos

| Error / síntoma | Causa probable | Solución |
|---|---|---|
| `NameError: name '___' is not defined` | Hay un hueco sin completar. | Busca los `___` en la celda y rellénalos. |
| `NameError: name 'modelo_vecinos' is not defined` (u otra variable) | Ejecutaste una celda sin haber ejecutado las anteriores, o reiniciaste el kernel. | Ejecuta todo desde arriba: menú *Run → Run All* (o *Ejecutar todo*). |
| `NotFittedError` | Llamaste a `predict` antes de `fit`. | Ejecuta primero la celda de entrenamiento. |
| `ValueError: ... expected 2D array` | Le diste a `predict` una sola lista `[5.1, 3.5, 1.4, 0.2]`. | El modelo espera una **tabla** (lista de filas): `[[5.1, 3.5, 1.4, 0.2]]` o un DataFrame. |
| Aviso amarillo `X does not have valid feature names` | Entrenaste con un DataFrame (con nombres de columna) y predices con una lista simple. | No es un error grave, pero se evita usando `pd.DataFrame([medidas], columns=iris.feature_names)`, como en el cuaderno. |
| `KeyError: 'especie'` | La columna no existe o está mal escrita. | Revisa mayúsculas, acentos y comillas. |

---

## 5. Para seguir aprendiendo (cuando termines)

- Prueba `train_test_split(..., stratify=y)` para que el examen tenga la misma proporción de cada especie.
- Usa solo 2 características (ej. largo y ancho del pétalo) y dibuja las flores con `plt.scatter`, coloreando por especie. ¡Verás los "barrios" de cada especie!
- Prueba otro dataset de juguete: `from sklearn.datasets import load_wine`.

---

<details>
<summary>🔑 <b>Respuestas de los huecos (solo para el profe, o para revisar al final)</b></summary>

| Sección | Huecos |
|---|---|
| Calentamiento 1 | `((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5` |
| Calentamiento 2 | `distancias[:k]` |
| 1. Cargar datos | `load_iris()`, `iris.target` |
| 1. Explorar | `datos_flores.shape` |
| 2. Separar | `datos_flores['especie']`, `test_size=0.2` |
| 3. Entrenar | `n_neighbors=3`, `fit(X_train, y_train)` |
| 4. Evaluar | `predict(X_test)`, `accuracy_score(y_test, predicciones)` |
| 5. Flor misteriosa | `predict(flor_misteriosa)` |
| 5. Reto | Ejemplos: Versicolor `[6.0, 2.8, 4.5, 1.4]`, Virginica `[6.8, 3.0, 5.8, 2.2]` |

**Resultados esperados** (con `random_state=42`): 120 flores de entrenamiento, 30 de examen, precisión de **100 %** con `k=3`, y la flor `[5.1, 3.5, 1.4, 0.2]` sale **Setosa**.

**Preguntas de reflexión:**
- *k impar:* evita empates en la votación.
- *Clases balanceadas:* si hubiera muchas más flores de una especie, el modelo tendería a votar por ella.
- *¿100 % = perfecto?* No: solo acertó en **esas 30** flores. Con flores reales (otras condiciones, errores de medición) puede fallar.
- *k = 1 vs k = 120:* con 1 depende de un solo vecino (muy sensible); con 120 siempre gana la especie más común en el entrenamiento.

</details>

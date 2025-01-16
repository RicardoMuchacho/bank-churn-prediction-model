- Predicción de Abandono de Clientes en Bancos - Proyecto TFM -

Predicting Customer Churn in Banking - TFM Project

Tabla de Contenidos

- Descripción del Proyecto
- Estructura del Proyecto
- Conjunto de Datos
- Detalles del Modelo
- Resultados
- Reconocimientos
- Información de Contacto

- Descripción del Proyecto -

Este proyecto tiene como objetivo predecir el abandono de clientes en el sector bancario utilizando técnicas de aprendizaje automático. A través del análisis de datos demográficos, información de cuentas y transacciones, identificamos clientes con riesgo de abandonar el banco. El flujo de trabajo incluye preprocesamiento de datos, ingeniería de características, modelado inicial y mejoras incrementales con algoritmos como Random Forest y Gradient Boosting.

Summary

This project focuses on predicting customer churn in the banking sector using machine learning techniques. 
By analyzing customer demographics, account information, and transaction data, the objective is to identify clients at risk of leaving the bank. 
The workflow includes data preprocessing, feature engineering, baseline modeling, and incremental improvements using algorithms like Random Forest and Gradient Boosting. 
Cross-validation ensures robust evaluation, and hyperparameter tuning is automated using tools like GridSearchCV.

Evaluation metrics such as AUC, Accuracy, and MAE are carefully selected and justified based on the business context. 
This approach provides actionable insights for retention strategies to enhance customer satisfaction and reduce churn.

- Estructura del Proyecto -

├── data/                   # Archivos de datos crudos y procesados
├── models/                 # Modelos entrenados
├── notebooks/              # Notebooks Jupyter para exploración y análisis
├── src/                    # Código fuente para preprocesamiento, entrenamiento y predicción
├── tests/                  # Pruebas unitarias del proyecto
├── README.md               # Documentación del proyecto
└── TFM_instructions.pdf    # Instrucciones y lineamientos del proyecto

Conjunto de Datos
El conjunto de datos incluye información de clientes, como datos demográficos, detalles de cuentas e historial de transacciones.

- Características -

CustomerID: Identificador único de cada cliente
CreditScore: Puntuación crediticia del cliente
Geography: Ubicación del cliente
Gender: Género del cliente
Age: Edad del cliente
Tenure: Años que el cliente lleva con el banco
Balance: Saldo de la cuenta
NumOfProducts: Número de productos bancarios que usa el cliente
HasCrCard: Si el cliente tiene una tarjeta de crédito (1: Sí, 0: No)
IsActiveMember: Si el cliente es un miembro activo (1: Sí, 0: No)
EstimatedSalary: Salario estimado del cliente
Exited: Si el cliente ha abandonado el banco (1: Sí, 0: No) [Variable objetivo]
Preprocesamiento de Datos:

Manejo de valores faltantes
Codificación de variables categóricas
Escalado de características

- Detalles del Modelo -

Implementamos varios modelos de aprendizaje automático para predecir el abandono de clientes:

Random Forest:

Método de conjunto que combina múltiples árboles de decisión
Maneja el sobreajuste y mejora la precisión
Gradient Boosting:

Técnica de conjunto secuencial
Se enfoca en corregir los errores de modelos previos
Ajuste de Hiperparámetros:

Utilizamos GridSearchCV para seleccionar los mejores parámetros

- Resultados -
Los modelos se evaluaron utilizando las siguientes métricas:

Precisión: Proporción de instancias correctamente predichas
AUC (Área Bajo la Curva): Mide la capacidad del modelo para distinguir entre clases
MAE (Error Absoluto Medio): Diferencia promedio entre los valores predichos y reales
El modelo Random Forest logró la mayor precisión y AUC, indicando su efectividad en la predicción del abandono de clientes.

 - Reconocimientos -
   
Queremos agradecer a los colaboradores siguientes por su invaluable apoyo:
- Ricardo Muchacho
- Antoine Daniel Maisonhaute
- Julio Eliu Camacho Orozco
- Sergio Gómez Cárdenas

- Información de Contacto - 

Para cualquier consulta o problema, contacta al equipo quien maneja a este proyecto en ricardomuchacho.developer@gmail.com, o sergio19959@gmail.com o antoinemaisonhaute59@gmail.com.

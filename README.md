## Predicción de Abandono de Clientes en Bancos – Proyecto TFM

**Predicting Customer Churn in Banking – TFM Project**

---

### Tabla de Contenidos

- [Predicción de Abandono de Clientes en Bancos – Proyecto TFM](#predicción-de-abandono-de-clientes-en-bancos--proyecto-tfm)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción del Proyecto](#descripción-del-proyecto)
    - [Summary (EN)](#summary-en)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Conjunto de Datos](#conjunto-de-datos)
    - [Características principales:](#características-principales)
    - [Preprocesamiento de datos:](#preprocesamiento-de-datos)
  - [Detalles del Modelo](#detalles-del-modelo)
    - [Ajuste de hiperparámetros:](#ajuste-de-hiperparámetros)
  - [Resultados](#resultados)
  - [Reconocimientos](#reconocimientos)
  - [Información de Contacto](#información-de-contacto)

---

### Descripción del Proyecto

Este proyecto tiene como objetivo predecir el abandono de clientes en el sector bancario utilizando técnicas de aprendizaje automático. A través del análisis de datos demográficos, información de cuentas e historial de transacciones, se identifican clientes con riesgo de abandonar el banco.  
El flujo de trabajo incluye preprocesamiento de datos, ingeniería de características, modelado inicial y mejoras incrementales mediante algoritmos de machine learning.

#### Summary (EN)

This project focuses on predicting customer churn in the banking sector using machine learning techniques.  
By analyzing customer demographics, account information, and transaction history, the goal is to identify clients at risk of leaving the bank.  
The workflow includes data preprocessing, feature engineering, baseline modeling, and incremental improvements using algorithms like Random Forest and Gradient Boosting.  
Cross-validation ensures robust evaluation, and hyperparameter tuning is automated using tools like GridSearchCV.
This approach provides actionable insights for retention strategies to enhance customer satisfaction and reduce churn.

---

### Estructura del Proyecto

```
├── data/                   # Archivos de datos crudos y procesados
├── models/                 # Modelos entrenados
├── notebooks/              # Notebooks Jupyter para exploración y análisis
├── src/                    # Código fuente para preprocesamiento, entrenamiento y predicción
├── tests/                  # Pruebas unitarias del proyecto
├── README.md               # Documentación del proyecto
└── TFM_instructions.pdf    # Instrucciones y lineamientos del proyecto
```

---

### Conjunto de Datos

El conjunto de datos incluye información de clientes como datos demográficos, detalles de cuentas e historial de transacciones.

#### Características principales:

- `CustomerID`: Identificador único del cliente  
- `CreditScore`: Puntuación crediticia  
- `Geography`: Ubicación geográfica  
- `Gender`: Género  
- `Age`: Edad  
- `Tenure`: Años con el banco  
- `Balance`: Saldo en la cuenta  
- `NumOfProducts`: Número de productos contratados  
- `HasCrCard`: Posee tarjeta de crédito (1: Sí, 0: No)  
- `IsActiveMember`: Es miembro activo (1: Sí, 0: No)  
- `EstimatedSalary`: Salario estimado  
- `Exited`: Ha abandonado el banco (1: Sí, 0: No) [**Variable objetivo**]

#### Preprocesamiento de datos:

- Manejo de valores faltantes  
- Codificación de variables categóricas  
- Escalado de características  

---

### Detalles del Modelo

Se implementaron distintos modelos de machine learning para predecir el abandono de clientes:

- **Random Forest**  
  - Técnica de ensamblado que combina múltiples árboles de decisión  
  - Robusto frente al sobreajuste y con buena capacidad predictiva  

- **Gradient Boosting**  
  - Modelo secuencial que corrige errores de predicciones anteriores  
  - Alta precisión en clasificación de casos complejos  

#### Ajuste de hiperparámetros:
- Uso de **GridSearchCV** para encontrar la mejor combinación de parámetros en cada modelo.

---

### Resultados

Los modelos fueron evaluados mediante las siguiente métrica:

- **AUC (Área Bajo la Curva):** Capacidad del modelo para distinguir entre clases  

> El modelo **XGBoost** obtuvo los mejores resultados en precisión y AUC, demostrando una alta efectividad para predecir el abandono de clientes.

---

### Reconocimientos

Queremos agradecer a los siguientes colaboradores por su invaluable apoyo:

- Ricardo Muchacho  
- Antoine Daniel Maisonhaute  
- Julio Eliu Camacho Orozco  
- Sergio Gómez Cárdenas  

---

### Información de Contacto

Para cualquier consulta o sugerencia relacionada con el proyecto, por favor contacta a cualquiera de los miembros del equipo:

- ricardomuchacho.developer@gmail.com  
- sergio19959@gmail.com  
- antoinemaisonhaute59@gmail.com  
- jcamachoo@student.eae.es  
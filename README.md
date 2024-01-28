# Data Scientist - Prueba técnica
Dentro de una campaña de ventas se quiere incrementar y optimizar el número de ventas efectivas, en este sentido y como propuesta del área de analítica queremos realizar un modelo el cual prediga cuales son los clientes que tienen mayor probabilidad de pago. 

Contamos con una base de datos con las siguientes variables, demográficas y de gestiones del cliente (Excel adjunto **Sales_outbound.xlsx**):


* **Client_ID:**   El Id del Clinete
* **Name:** Nombre del cliente
* **Age:** Edad del Cliente
* **Location:** Estado donde vivel el Cliente
* **Income:** ingresos del Cliente
* **TAX:** impuestos que paga el cliente
* **previous sales_#:** Cantidad de compras que ha realizado en el pasado
* **Type_of_Products:** Tipo de producto que ha comprado
* **Contact_Channel:** Canal por el que se ha contactado al cliente
* **Contact_hour:** Hora de contacto
* **Num_Contacts:** # de intentos que se han realizado para el contacto
* **Satisfaction_Score:** Medida de satisfacción (CSAT) 1 a 5 siendo 5 muy satisfecho
* **Sales:** si la venta fue efectiva o no (1 Si, 0 No)               


## Desarrollo
1.	Realice un análisis exploratorio de los datos y explique que transformaciones son necesarias para preparar los datos.
2.	Genere un análisis descriptivo, ¿qué puede concluir de este análisis? ¿Y qué recomendaciones entregaría para mejorar la campaña de ventas?
3.	¿Qué tipo de modelos y técnicas de analítica avanzada aplican para generar la predicción?
4.	Desarrolle varios modelos y compare los resultados ¿cuál tiene mejor desempeño? Explique e interprete los resultados.
5.	Implemente el modelo y generar predicciones en una nueva base de datos (**Sales_outbound_New**).
    * ¿Qué resultados encuentra?
    * ¿Que recomendaciones puede entregar al área de operaciones quienes son los que implementan la estrategia? 
6.	Realice una presentación en donde resuma los puntos anteriores (Es una presentación dirigida a un área de negocio).

# Repository structure
The current structure of the repository is essentially the structure recommended by the event organizers with some minor additions:

```
Shimoku_Technical_Test_DS
|   .env
|   .gitignore
|   README.md
|   requirements.txt
|
+---data
|       Sales_outbound.xlsx
|       Sales_outbound_New.xlsx
|
+---src
|
\---venv
```
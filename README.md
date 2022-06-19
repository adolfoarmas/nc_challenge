# Desafio Back-end - API REST - Servicios de Pago

El proyecto consiste en una version simplificada de un proveedor de servicios de pago de impuestos.

### Pre-requisitos 📋

* Python 3.10

* Instalar requerimientos en archivo requirements.txt:

```
asgiref==3.5.2
Django==4.0.5
djangorestframework==3.13.1
pytz==2022.1
sqlparse==0.4.2
tzdata==2022.1

```

### Instalación 🔧

Nota: Este proyecto fue desarrollado en Windows en servidor de desarrollo nativo de Django (127.0.0.1:8000)

* Clonar el repositorio
* En un nivel superior al directorio del proyecto crear entorno virtual y activarlo

```
python -m venv env
```
en Windows ejecutar los comandos:

```
cd env/Scripts
activate

```

en Linux

```
source env/bin/activate

```

* Con el entorno virtual activado, instalar requerimientos:

```
pip install -r requirementes.txt
```

* En el directorio superior de nombre api_project, ejecutar los siguientes comandos sobre manage.py

```
python manage.py migrate
python manage.pu ruunserver
```

### Estructura del proyecto 📦

```
+---api_project     ---> Directorio del proyecto
|   +---api_app     ---> Directorio de aplicacion con codigo relacionado a la API
|   +---api_project ---> Directorio de configuracion del proyecto
|   +---base_app    ---> Directorio de aplicacion principal donde se encuentran declarados los modelos Payables y Transactions
|---db.sqlite3
|---manage.py
|---requirements.txt
```

### Test de la Aplicacion ⌨️

La aplicacion cuenta con dos endpoints de consulta:

```
{
    "payables": "http://127.0.0.1:8000/payables/",
    "transactions": "http://127.0.0.1:8000/transactions/"
}
```

* Una consulta a http://127.0.0.1:8000/payables/ entregara los todos los Payables con status "Pendiente de Pago" ordenados por fecha de vencimiento (due_date)

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "bar_code": "123456789012",
        "service_type": "Luz",
        "due_date": "2022-07-07",
        "service_cost": "2000.00"
    },
    {
        "bar_code": "123456789019",
        "service_type": "COM",
        "due_date": "2022-07-05",
        "service_cost": "60.50"
    },
    {
        "bar_code": "123456789018",
        "service_type": "TLL",
        "due_date": "2022-05-31",
        "service_cost": "394.45"
    },
    {
        "bar_code": "123456789015",
        "service_type": "COM",
        "due_date": "2022-05-17",
        "service_cost": "3569.45"
    },
    {
        "bar_code": "123456789016",
        "service_type": "COM",
        "due_date": "2022-01-31",
        "service_cost": "3956.45"
    },
    {
        "bar_code": "123456789017",
        "service_type": "ELE",
        "due_date": "2022-01-31",
        "service_cost": "394.45"
    }
]
```

* Una consulta filtrando por tipo de servicio, por ejemplo: http://127.0.0.1:8000/payables/?service_type=COM entregara todas las boletas con con status "Pendiente de Pago" filtradas por el servicio indicado.

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "bar_code": "123456789019",
        "due_date": "2022-07-05",
        "service_cost": "60.50"
    },
    {
        "bar_code": "123456789015",
        "due_date": "2022-05-17",
        "service_cost": "3569.45"
    },
    {
        "bar_code": "123456789016",
        "due_date": "2022-01-31",
        "service_cost": "3956.45"
    }
]
```

* El endpoint http://127.0.0.1:8000/payables/ soporta la funcion POST, se debe enviar un objeto en formato json como el del siguiente ejemplo:

_Nota1: bar_code es primary key_
_Nota2: el archivo apy_project/base_app/choices.py contiene diccionarios usados para los choices de 'service_type', 'payment_status'

```
{
"bar_code": "123456789016",
"service_type":"COM",
"service_description":"Internet Service June",
"due_date": "2022-07-05",
"service_cost": "60.5",
"payment_status": "PG"
}
```

* Una consulta a http://127.0.0.1:8000/transactions/ entregara los todas las transacciones de pago realizadas ordenadas por id de transaccion (transaction_id)

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "transaction_id": 3,
        "payment_method": "DC",
        "card_number": "5572883244125700",
        "payment_ammount": "200.00",
        "payment_date": "2022-03-18",
        "bar_code": "123456789017"
    },
    {
        "transaction_id": 2,
        "payment_method": "DC",
        "card_number": "5572883244125700",
        "payment_ammount": "3956.45",
        "payment_date": "2022-06-18",
        "bar_code": "123456789016"
    },
    {
        "transaction_id": 1,
        "payment_method": "CS",
        "card_number": null,
        "payment_ammount": "1000.00",
        "payment_date": "2022-06-18",
        "bar_code": "123456789012"
    }
]

```

*  Una consulta filtrando por fecha inicial (date_min) y fecha final (date_max), por ejemplo:  http://127.0.0.1:8000/transactions/?date_min=2022-06-18&date_max=2022-06-18 entregara un resumen de todas las transacciones realizadas en ese rango de fechas dia a dia (payment_date), sumando el monto de todas las transacciones (sum_payment_ammount) y haciendo un conteo de las mismas (total_transaction_ids). 

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "payment_date": "2022-06-18",
        "sum_payment_ammount": "4956.45",
        "total_transaction_ids": 2
    }
]

```

* El endpoint http://127.0.0.1:8000/transactions/ soporta la funcion POST, se debe enviar un objeto en formato json como el del siguiente ejemplo:

_Nota1: bar_code debe estar asociado a una boleta existente_
_Nota2: el archivo apy_project/base_app/choices.py contiene diccionarios usados para los choices de 'payment_method'

```
{
"bar_code":"123456789016",
"payment_method":"DC",
"card_number":"5572883244125698",
"payment_ammount":"3956.45",
"payment_date":"2022-06-18"
}
```






# vehicles-sales-dashboard

Proyecto Sprint 7 (TripleTen - Bootcamp de Analitica de Datos): analisis exploratorio
de datos y dashboard web interactivo construido con **Streamlit** para un conjunto de
datos de anuncios de venta de vehiculos en EE. UU.

## Contenido del proyecto

```
.
├── README.md
├── app.py                 # Aplicacion web (Streamlit)
├── vehicles_us.csv         # Conjunto de datos de anuncios de coches
├── requirements.txt
└── notebooks
    └── EDA.ipynb           # Analisis exploratorio de datos
```

## Que hace la app

`app.py` carga el conjunto de datos `vehicles_us.csv` y permite:

- Ver una vista previa de los datos.
- Generar un **histograma** del kilometraje (odometer) al presionar un boton.
- Generar un **grafico de dispersion** de precio vs. kilometraje al marcar una casilla
  de verificacion.

## Como ejecutarlo localmente

```bash
python -m venv vehicles_env
source vehicles_env/bin/activate   # En Windows: vehicles_env\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Analisis exploratorio

El notebook `notebooks/EDA.ipynb` documenta el analisis exploratorio: distribucion del
precio, distribucion del kilometraje, relacion precio-kilometraje, precio por tipo de
vehiculo y precio segun el anio del modelo.

## Despliegue

La aplicacion esta desplegada en Render: *(agregar aqui la URL una vez desplegada,
por ejemplo `https://vehicles-sales-dashboard.onrender.com/`)*.

# Entrega-nuevas-tecnologias-2
# 📊 Proyecto Nuevas Tecnologías - Análisis de Datos

## 🧠 Descripción del proyecto

Este proyecto realiza el procesamiento y análisis de datos provenientes de archivos CSV relacionados con ciudades y eventos. Se estructura en módulos para la limpieza, transformación y análisis de datos, utilizando Python y pandas.

El objetivo es relacionar eventos con ciudades a través del identificador `id_ciudad` y generar un resumen final por ciudad.

---

## 🗂️ Estructura del proyecto

```text id="structure_final_readme"
Entrega-nuevas-tecnologias-2/
│
├── data/
│   ├── raw/
│   │   ├── ciudades.csv
│   │   └── eventos.csv
│   ├── clean/
│   │   └── cleanData.py
│   ├── analisis.py
│   └── funciones.py
│
├── venv/
├── main.py
├── requirements.txt
├── README.md
```

---

## ⚙️ Funcionamiento del sistema

1. **Carga de datos (raw):**
   Se leen los archivos CSV originales de ciudades y eventos.

2. **Limpieza de datos (clean):**
   Se utiliza pandas para eliminar valores nulos, limpiar espacios y normalizar los datos.

3. **Análisis (analysis):**
   Se relacionan los eventos con las ciudades usando el campo `id_ciudad` y se genera un conteo por ciudad.

4. **Ejecución (main.py):**
   Ejecuta todo el flujo y muestra el resultado final en consola.

---

## 🚀 Cómo ejecutar el proyecto

### 1. Activar entorno virtual

```bash id="venv_run"
venv\Scripts\activate
```

### 2. Instalar dependencias

```bash id="pip_install"
pip install pandas
```

### 3. Ejecutar el proyecto

```bash id="run_project"
python main.py
```

---

## 🧪 Entorno virtual y pip

Este proyecto utiliza un entorno virtual (`venv`) para aislar las dependencias del sistema.

Se utilizó `pip` para la instalación de librerías externas, principalmente:

* pandas

Las dependencias están registradas en el archivo:

```text id="req_ref"
requirements.txt
```

---

## 📌 Resultado final

El sistema genera un resumen de eventos agrupados por ciudad, conectando los datos de ambos archivos CSV.

Ejemplo de salida:

```text id="output_example"
EVENTOS POR CIUDAD: {
  'Bogota': 4,
  'Medellin': 4,
  'CALI': 4
}
```

---

## 🤖 Uso de herramientas de apoyo (IA)

Durante el desarrollo del proyecto se utilizaron herramientas de inteligencia artificial como apoyo para:

* Corrección de errores en el código
* Optimización de la estructura del proyecto
* Mejora del procesamiento de datos con pandas
* Documentación del proyecto (README)

Estas herramientas se usaron como apoyo al aprendizaje y no reemplazan el trabajo realizado en clase.

---

## 👨‍💻 Autor

Proyecto desarrollado por: **Emanuel, Julián y Miguel**

# Calculadora del Índice de Calidad del Agua (ICA)

## Descripción del Proyecto
Este proyecto fue desarrollado como parte del curso "MANEJO DE RESIDUOS DE APARATOS ELÉCTRICOS Y ELECTRÓNICOS (RAEE) - GRUPO 01" de la Universidad Francisco Gavidia. Consiste en una aplicación web que implementa la metodología del Ministerio de Medio Ambiente y Recursos Naturales (MARN) para calcular el Índice de Calidad del Agua (ICA).

## Características Principales
- Cálculo del ICA basado en 9 parámetros fundamentales
- Visualización interactiva mediante gráfico de indicador
- Desglose detallado de subíndices
- Interpretación automática de resultados

## Parámetros Evaluados
1. Coliformes Fecales (NMP/100mL)
2. pH (unidades)
3. DBO5 (mg/L)
4. Nitratos (mg/L)
5. Fosfatos (mg/L)
6. Cambio de Temperatura (°C)
7. Turbidez (NTU)
8. Sólidos Disueltos Totales (mg/L)
9. Oxígeno Disuelto (% saturación)

## Categorías de Calidad del Agua
- **Excelente:** 91-100
- **Buena:** 71-90
- **Regular:** 51-70
- **Mala:** 26-50
- **Pésima:** 0-25

## Tecnologías Utilizadas
- Python
- Streamlit
- Pandas
- Plotly

## Requisitos de Instalación y Configuración del Entorno

### 1. Instalar Python
Asegúrate de tener instalado Python 3.8 o superior. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### 2. Clonar el Repositorio
Clona el repositorio en tu máquina:
```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```
> **Nota:** Reemplaza `tu-usuario` y `tu-repositorio` por los valores correspondientes.

### 3. Crear un Entorno Virtual
Crea un entorno virtual para aislar las dependencias del proyecto:

- **Windows:**
  ```bash
  python -m venv venv
  ```
- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  ```

### 4. Activar el Entorno Virtual
Activa el entorno virtual antes de instalar las dependencias:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### 5. Instalar las Dependencias
Con el entorno virtual activado, instala las dependencias necesarias:
```bash
pip install streamlit pandas plotly
```

### 6. Ejecutar la Aplicación
Finalmente, ejecuta la aplicación:
```bash
streamlit run app.py
```

## Metodología
La aplicación implementa la metodología oficial del MARN para el cálculo del ICA, que incluye:
- Ponderación de parámetros
- Cálculo de subíndices
- Agregación de resultados
- Interpretación según rangos establecidos

## Interpretación de Resultados
- **Excelente/Buena:** Alta diversidad de vida acuática y apta para contacto directo
- **Regular:** Menor diversidad de organismos y posible crecimiento de algas
- **Mala:** Baja diversidad de vida acuática y problemas de contaminación
- **Pésima:** Capacidad muy limitada para sustentar vida acuática

## Desarrollado por
Wilmer Salazar  
Universidad Francisco Gavidia  
Curso: MANEJO DE RESIDUOS DE APARATOS ELÉCTRICOS Y ELECTRÓNICOS (RAEE) - GRUPO 01

## Licencia
Este proyecto está bajo la Licencia MIT.

# Calculadora del Índice de Calidad del Agua (ICA)

## Descripción del Proyecto
Este proyecto fue desarrollado como parte del curso "MANEJO DE RESIDUOS DE APARATOS ELECTRICOS Y ELECTRONICOS (RAEE) - GRUPO 01" de la Universidad Francisco Gavidia. Consiste en una aplicación web que implementa la metodología del Ministerio de Medio Ambiente y Recursos Naturales (MARN) para calcular el Índice de Calidad del Agua (ICA).

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
- Excelente (91-100)
- Buena (71-90)
- Regular (51-70)
- Mala (26-50)
- Pésima (0-25)

## Tecnologías Utilizadas
- Python
- Streamlit
- Pandas
- Plotly

## Requisitos de Instalación
```bash
pip install streamlit pandas plotly
```

## Instrucciones de Uso
1. Clone el repositorio
2. Instale las dependencias
3. Ejecute la aplicación:
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
- **Excelente/Buena**: Alta diversidad de vida acuática y apta para contacto directo
- **Regular**: Menor diversidad de organismos y posible crecimiento de algas
- **Mala**: Baja diversidad de vida acuática y problemas de contaminación
- **Pésima**: Capacidad muy limitada para sustentar vida acuática

## Desarrollado por
Wilmer Salazar
Universidad Francisco Gavidia
Curso: MANEJO DE RESIDUOS DE APARATOS ELECTRICOS Y ELECTRONICOS (RAEE) - GRUPO 01

## Licencia
Este proyecto está bajo la Licencia MIT.
import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def calculate_sub_coliform(value):
    """Calculate Sub-index for Fecal Coliforms"""
    if value > 100000:
        return 3
    # Use interpolation based on the graph
    if value <= 1:
        return 97
    elif value <= 10:
        return 90
    elif value <= 100:
        return 75
    elif value <= 1000:
        return 50
    elif value <= 10000:
        return 25
    else:
        return 15


def calculate_sub_ph(value):
    """Calculate Sub-index for pH"""
    if value <= 2:
        return 2
    elif value >= 10:
        return 3
    # Interpolation based on the graph
    if 7 <= value <= 7.5:
        return 100
    elif 7.5 < value <= 8:
        return 90
    elif 6.5 <= value < 7:
        return 90
    elif 8 < value <= 8.5:
        return 70
    elif 6 <= value < 6.5:
        return 70
    else:
        return 50


def calculate_sub_dbo5(value):
    """Calculate Sub-index for DBO5"""
    if value > 30:
        return 2
    # Interpolation based on the graph
    if value <= 3:
        return 100
    elif value <= 5:
        return 85
    elif value <= 10:
        return 60
    else:
        return 30


def calculate_sub_nitrates(value):
    """Calculate Sub-index for Nitrates"""
    if value > 100:
        return 2
    # Interpolation based on the graph
    if value <= 10:
        return 100
    elif value <= 20:
        return 85
    elif value <= 50:
        return 55
    else:
        return 25


def calculate_sub_phosphates(value):
    """Calculate Sub-index for Phosphates"""
    if value > 10:
        return 5
    # Interpolation based on the graph
    if value <= 0.5:
        return 100
    elif value <= 1:
        return 90
    elif value <= 2:
        return 80
    elif value <= 4:
        return 70
    else:
        return 60


def calculate_sub_temperature(value):
    """Calculate Sub-index for Temperature Change"""
    if value > 15:
        return 9
    # Interpolation based on the graph
    if value <= 2:
        return 93
    elif value <= 5:
        return 85
    elif value <= 10:
        return 65
    else:
        return 30


def calculate_sub_turbidity(value):
    """Calculate Sub-index for Turbidity"""
    if value > 100:
        return 5
    # Interpolation based on the graph
    if value <= 5:
        return 95
    elif value <= 10:
        return 85
    elif value <= 20:
        return 70
    elif value <= 50:
        return 50
    else:
        return 30


def calculate_sub_solids(value):
    """Calculate Sub-index for Total Dissolved Solids"""
    if value > 500:
        return 3
    # Interpolation based on the graph
    if value <= 50:
        return 100
    elif value <= 100:
        return 95
    elif value <= 200:
        return 85
    elif value <= 400:
        return 70
    else:
        return 50


def calculate_sub_oxygen(value):
    """Calculate Sub-index for Dissolved Oxygen"""
    if value > 140:
        return 47
    # Interpolation based on the graph
    if value <= 40:
        return 30
    elif value <= 60:
        return 50
    elif value <= 80:
        return 70
    elif value <= 100:
        return 90
    else:
        return 85


def get_water_quality_category(ica_value):
    """Get water quality category based on ICA value"""
    if ica_value >= 91:
        return "Excelente", "#000080"  # Navy Blue
    elif ica_value >= 71:
        return "Buena", "#0000FF"  # Blue
    elif ica_value >= 51:
        return "Regular", "#808080"  # Gray
    elif ica_value >= 26:
        return "Mala", "#FFFF00"  # Yellow
    else:
        return "Pésima", "#FF0000"  # Red


def create_gauge_chart(ica_value, category, color):
    """Create a gauge chart for ICA value visualization"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=ica_value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': f"Índice de Calidad del Agua (ICA)<br><span style='font-size:0.8em;color:{color}'>{category}</span>"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'steps': [
                {'range': [0, 25], 'color': '#FF0000'},
                {'range': [26, 50], 'color': '#FFFF00'},
                {'range': [51, 70], 'color': '#808080'},
                {'range': [71, 90], 'color': '#0000FF'},
                {'range': [91, 100], 'color': '#000080'}
            ]
        }
    ))
    fig.update_layout(height=400)
    return fig


def main():
    st.set_page_config(page_title="Calculadora ICA", page_icon="💧", layout="wide")

    st.title("Calculadora del Índice de Calidad del Agua (ICA)")
    st.markdown("""
    Esta aplicación calcula el Índice de Calidad del Agua (ICA) basado en la metodología del MARN.
    Ingrese los valores de los parámetros medidos para obtener el índice de calidad del agua.
    """)

    # Add session state initialization for all parameters
    if 'initialized' not in st.session_state:
        st.session_state.initialized = True
        st.session_state.coliform = 0.0
        st.session_state.ph = 0.0
        st.session_state.dbo5 = 0.0
        st.session_state.nitrates = 0.0
        st.session_state.phosphates = 0.0
        st.session_state.temp_change = 0.0
        st.session_state.turbidity = 0.0
        st.session_state.solids = 0.0
        st.session_state.oxygen = 0.0

    def reset_values():
        st.session_state.coliform = 0.0
        st.session_state.ph = 0.0
        st.session_state.dbo5 = 0.0
        st.session_state.nitrates = 0.0
        st.session_state.phosphates = 0.0
        st.session_state.temp_change = 0.0
        st.session_state.turbidity = 0.0
        st.session_state.solids = 0.0
        st.session_state.oxygen = 0.0

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Parámetros de entrada")
        coliform = st.number_input("Coliformes Fecales (NMP/100mL)",
                                   min_value=0.0,
                                   format="%.2f",
                                   key="coliform")
        ph = st.number_input("pH (unidades)",
                             min_value=0.0,
                             max_value=14.0,
                             format="%.2f",
                             key="ph")
        dbo5 = st.number_input("DBO5 (mg/L)",
                               min_value=0.0,
                               format="%.2f",
                               key="dbo5")
        nitrates = st.number_input("Nitratos (mg/L)",
                                   min_value=0.0,
                                   format="%.2f",
                                   key="nitrates")
        phosphates = st.number_input("Fosfatos (mg/L)",
                                     min_value=0.0,
                                     format="%.2f",
                                     key="phosphates")

    with col2:
        temp_change = st.number_input("Cambio de Temperatura (°C)",
                                      min_value=-50.0,  # Allow negative values
                                      format="%.2f",
                                      key="temp_change")
        turbidity = st.number_input("Turbidez (NTU)",
                                    min_value=0.0,
                                    format="%.2f",
                                    key="turbidity")
        solids = st.number_input("Sólidos Disueltos Totales (mg/L)",
                                 min_value=0.0,
                                 format="%.2f",
                                 key="solids")
        oxygen = st.number_input("Oxígeno Disuelto (% saturación)",
                                 min_value=0.0,
                                 format="%.2f",
                                 key="oxygen")

    # Create a row of buttons using columns
    button_col1, button_col2 = st.columns(2)

    with button_col1:
        calculate_button = st.button("Calcular ICA")

    with button_col2:
        reset_button = st.button("Limpiar Campos", on_click=reset_values)

    if calculate_button:
        # Calculate sub-indices
        subs = {
            'Coliformes Fecales': (calculate_sub_coliform(coliform), 0.15),
            'pH': (calculate_sub_ph(ph), 0.12),
            'DBO5': (calculate_sub_dbo5(dbo5), 0.10),
            'Nitratos': (calculate_sub_nitrates(nitrates), 0.10),
            'Fosfatos': (calculate_sub_phosphates(phosphates), 0.10),
            'Temperatura': (calculate_sub_temperature(abs(temp_change)), 0.10),
            'Turbidez': (calculate_sub_turbidity(turbidity), 0.08),
            'Sólidos Disueltos': (calculate_sub_solids(solids), 0.08),
            'Oxígeno Disuelto': (calculate_sub_oxygen(oxygen), 0.17)
        }

        # Calculate ICA
        ica = sum(sub * weight for sub, weight in subs.values())
        category, color = get_water_quality_category(ica)

        # Display results
        st.markdown("---")
        st.subheader("Resultados")

        # Display gauge chart
        st.plotly_chart(create_gauge_chart(ica, category, color), use_container_width=True)

        # Display sub-indices table
        st.subheader("Desglose de subíndices")
        sub_data = [(param, sub, weight, sub * weight)
                    for param, (sub, weight) in subs.items()]
        df = pd.DataFrame(sub_data,
                          columns=['Parámetro', 'Subíndice', 'Peso', 'Contribución'])
        st.dataframe(df.style.format({
            'Subíndice': '{:.2f}',
            'Peso': '{:.2f}',
            'Contribución': '{:.2f}'
        }))

        # Display interpretation
        st.markdown("---")
        st.subheader("Interpretación")
        interpretations = {
            'Excelente': "Las aguas son capaces de poseer una alta diversidad de vida acuática. Además, el agua también sería conveniente para todas las formas de contacto directo con ella.",
            'Buena': "Las aguas son capaces de poseer una alta diversidad de vida acuática. Además, el agua también sería conveniente para todas las formas de contacto directo con ella.",
            'Regular': "Las aguas tienen generalmente menos diversidad de organismos acuáticos y han aumentado con frecuencia el crecimiento de las algas.",
            'Mala': "Las aguas pueden solamente apoyar una diversidad baja de la vida acuática y están experimentando probablemente problemas con la contaminación.",
            'Pésima': "Las aguas pueden solamente poder apoyar un número limitado de las formas acuáticas de la vida."
        }
        st.markdown(f"**Categoría de calidad del agua:** {category}")
        st.markdown(f"**Interpretación:** {interpretations[category]}")


if __name__ == "__main__":
    main()
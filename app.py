import streamlit as st
import plotly.express as px
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Dashboard Interactivo", layout="wide")

# Crear datos de ejemplo para los gráficos
data = {
    "Product": ["Producto A", "Producto B", "Producto C", "Producto D"],
    "Region": ["Norte", "Sur", "Este", "Oeste"],
    "Sales": [3128, 3033, 3375, 3138],
    "Discount": [16.89, 18.11, 20.65, 20.29],
    "Profit": [1104, 1260, 1027, 983],
    "Quantity": [50, 60, 55, 65]
}

df = pd.DataFrame(data)

# Título del dashboard
st.title("Dashboard Interactivo con Streamlit")
st.markdown("Explora diferentes tipos de gráficos interactivos usando datos de ejemplo.")

# Selector principal
option = st.sidebar.selectbox(
    "Selecciona una opción:",
    ("Exploración del Dataset", "Visualización Gráfica")
)

if option == "Exploración del Dataset":
    st.subheader("Exploración del Dataset")
    st.write("Vista previa de los datos:")
    st.dataframe(df)
    st.write("Estadísticas descriptivas:")
    st.write(df.describe())

elif option == "Visualización Gráfica":
    # Tabs principales
    main_tabs = st.tabs(["Gráficos Básicos", "Gráficos Avanzados"])

    # Gráficos Básicos
    with main_tabs[0]:
        st.subheader("Gráficos Básicos")
        basic_tabs = st.tabs(["Gráfico de Líneas", "Gráfico de Barras", "Gráfico de Dispersión", "Gráfico de Pastel"])

        # Gráfico de Líneas
        with basic_tabs[0]:
            st.header("Gráfico de Líneas")
            fig_line = px.line(
                df, 
                x=df.index, 
                y="Sales", 
                title="Tendencias de Ventas",
                labels={"x": "Fecha", "Sales": "Ventas"}
            )
            st.plotly_chart(fig_line, use_container_width=True)

        # Gráfico de Barras
        with basic_tabs[1]:
            st.header("Gráfico de Barras")
            fig_bar = px.bar(
                df, 
                x="Product", 
                y="Sales", 
                color="Region", 
                title="Ventas por Producto y Región"
            )
            st.plotly_chart(fig_bar, use_container_width=True)

        # Gráfico de Dispersión
        with basic_tabs[2]:
            st.header("Gráfico de Dispersión")
            fig_scatter = px.scatter(
                df, 
                x="Quantity", 
                y="Sales", 
                color="Product", 
                size="Profit", 
                title="Relación entre Cantidad y Ventas",
                labels={"Quantity": "Cantidad", "Sales": "Ventas"}
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

        # Gráfico de Pastel
        with basic_tabs[3]:
            st.header("Gráfico de Pastel")
            fig_pie = px.pie(
                df, 
                names="Region", 
                values="Sales", 
                title="Distribución de Ventas por Región"
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    # Gráficos Avanzados
    with main_tabs[1]:
        st.subheader("Gráficos Avanzados")
        advanced_tabs = st.tabs(["Box Plot", "Heatmap", "Bubble Chart", "Radar Chart"])

        # Box Plot
        with advanced_tabs[0]:
            st.header("Box Plot")
            fig_box = px.box(
                df, 
                x="Region", 
                y="Profit", 
                color="Region", 
                title="Variabilidad de Ganancias por Región"
            )
            st.write(fig_box)

        # Heatmap
        with advanced_tabs[1]:
            st.header("Heatmap")
            corr = df[["Sales", "Discount", "Profit"]].corr()
            fig_heatmap = px.imshow(
                corr, 
                text_auto=True, 
                color_continuous_scale="Viridis", 
                title="Correlaciones entre Ventas, Descuentos y Ganancias"
            )
            st.plotly_chart(fig_heatmap, use_container_width=True)

        # Bubble Chart
        with advanced_tabs[2]:
            st.header("Bubble Chart")
            fig_bubble = px.scatter(
                df, 
                x="Quantity", 
                y="Profit", 
                size="Sales", 
                color="Product", 
                title="Cantidad vs Ganancias (Tamaño por Ventas)",
                labels={"Quantity": "Cantidad", "Profit": "Ganancias"}
            )
            st.plotly_chart(fig_bubble, use_container_width=True)

        # Radar Chart
        with advanced_tabs[3]:
            st.header("Radar Chart")
            radar_data_long = df.melt(id_vars="Product", var_name="Metric", value_name="Value")
            fig_radar = px.line_polar(
                radar_data_long,
                r="Value",
                theta="Metric",
                color="Product",
                title="Comparación Multivariante por Producto",
                line_close=True
            )
            fig_radar.update_traces(fill="toself")
            st.plotly_chart(fig_radar, use_container_width=True)

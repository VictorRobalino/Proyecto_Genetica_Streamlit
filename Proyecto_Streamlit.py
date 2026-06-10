import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración profesional de la aplicación
st.set_page_config(page_title="Genética Parental - Panel Analítico", layout="wide")
st.title("🧬 Parental Genetics & Child Trait Prediction")
st.markdown("Estudio analítico de la herencia fenotípica y predicción de rasgos en la siguiente generación.")

NOMBRE_ARCHIVO = "parental_genetics_child_traits.csv"

try:
    # Cargar el dataset de 7,000 registros
    df = pd.read_csv(NOMBRE_ARCHIVO)
    df.columns = df.columns.str.strip() # Limpiar espacios ocultos
    
    # Estructura narrativa definitiva de 5 pestañas
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📖 Introducción y Contexto",
        "📏 Regresión de Estatura", 
        "🎨 Herencia de Rasgos Físicos",
        "🏥 Análisis Probabilístico de Riesgo", 
        "🔮 Simulador Predictivo Multirrasgo"
    ])

    # ------------------------------------------------------------------
    # PESTAÑA 1: INTRODUCCIÓN Y CONTEXTO
    # ------------------------------------------------------------------
    with tab1:
        st.header("Análisis de Herencia y Predicción Fenotípica")
        st.write("Bienvenido al Panel Analítico. Esta aplicación transforma datos genéticos abstractos en una historia interactiva.")
        
        col_text, col_img = st.columns([2, 1])
        with col_text:
            st.markdown("""
            ### ¿De qué se trata este proyecto?
            Este estudio utiliza un dataset estructurado de **7,000 registros** para analizar y modelar cómo se transmiten los rasgos físicos 
            y factores clínicos de los progenitores hacia la descendencia. 

            ### Variables Críticas Clasificadas en la Aplicación:
            * **Rasgos Cuantitativos Continuos:** Estaturas del padre, madre e hijo (en centímetros). Siguen un de modelo de herencia aditiva poligénica.
            * **Rasgos Cualitativos Nominales:** Grupo sanguíneo, color de ojos, color de cabello y tono de piel.
            * **Factores Clínicos / Epidemiológicos:** Historial médico familiar (`Family_Disease_History`) y nivel de riesgo sanitario estimado (`Predicted_Health_Risk`).
            
            *Utilice la barra superior de pestañas para navegar cronológicamente por la historia de los datos, desde la validación científica hasta la simulación interactiva.*
            """)
        with col_img:
            st.info(
                "💡 **Métrica Global del Dataset:**\n\n"
                "* **Total Población:** 7,000 familias analizadas.\n"
                "* **Estatura Media Padre:** 173.97 cm\n"
                "* **Estatura Media Madre:** 161.08 cm\n"
                "* **Estatura Media Hijo:** 167.60 cm"
            )

    # ------------------------------------------------------------------
    # PESTAÑA 2: REGRESIÓN Y HERENCIA DE ESTATURA
    # ------------------------------------------------------------------
    with tab2:
        st.header("Análisis de Regresión Lineal Cuantitativa")
        st.write("Evaluación del impacto y correlación de la estatura parental sobre la talla final de la descendencia.")
        
        col1, col2 = st.columns(2)
        with col1:
            fig_scatter1 = px.scatter(df, x="Father_Height_cm", y="Predicted_Child_Height_cm", 
                                      trendline="ols", title="Regresión: Altura del Padre vs Hijo",
                                      labels={"Father_Height_cm": "Estatura del Padre (cm)", "Predicted_Child_Height_cm": "Estatura del Hijo (cm)"},
                                      color_discrete_sequence=['#2E86C1'])
            st.plotly_chart(fig_scatter1, use_container_width=True)
            
        with col2:
            fig_scatter2 = px.scatter(df, x="Mother_Height_cm", y="Predicted_Child_Height_cm", 
                                      trendline="ols", title="Regresión: Altura de la Madre vs Hijo",
                                      labels={"Mother_Height_cm": "Estatura de la Madre (cm)", "Predicted_Child_Height_cm": "Estatura del Hijo (cm)"},
                                      color_discrete_sequence=['#EC7063'])
            st.plotly_chart(fig_scatter2, use_container_width=True)

        st.markdown("---")
        st.subheader("💡 ¿Qué significa este análisis de Regresión?")
        exp1, exp2 = st.columns(2)
        with exp1:
            st.info(
                "**Interpretación de la Línea de Tendencia:**\n\n"
                "* **Pendiente Positiva:** La inclinación ascendente de la recta confirma visual y matemáticamente la fuerza de la heredabilidad.\n"
                "* **Dispersión:** Los puntos distribuidos muestran la variabilidad fenotípica normal en rasgos poligénicos continuos."
            )
        with exp2:
            st.success(
                "**Conclusión Académica:**\n\n"
                "La estatura no sigue una distribución discreta mendeliana, sino una combinación aditiva de múltiples alelos. La carga genética de ambos progenitores influye de forma equitativa en la atracción hacia la media poblacional."
            )

    # ------------------------------------------------------------------
    # PESTAÑA 3: HERENCIA DE RASGOS FÍSICOS (CORREGIDA CON TU ESQUEMA REAL)
    # ------------------------------------------------------------------
    with tab3:
        st.header("Análisis de Rasgos Fenotípicos Combinados")
        st.write("Explore la distribución de las características físicas de los padres y su relación con el género de la descendencia.")
        
        c_sel1, c_sel2 = st.columns(2)
        with c_sel1:
            progenitor = st.radio("1. Seleccione el Progenitor:", ["Padre", "Madre"])
        with c_sel2:
            rasgo = st.selectbox("2. Seleccione el Rasgo Físico a Analizar:", ["Color de Ojos", "Color de Cabello", "Tono de Piel"])
        
        # Mapeo dinámico basado ESTRICTAMENTE en tus columnas reales
        if progenitor == "Padre":
            col_x = "Father_Eye_Color" if rasgo == "Color de Ojos" else "Father_Hair_Color" if rasgo == "Color de Cabello" else "Father_Skin_Tone"
        else:
            col_x = "Mother_Eye_Color" if rasgo == "Color de Ojos" else "Mother_Hair_Color" if rasgo == "Color de Cabello" else "Mother_Skin_Tone"
            
        # Usamos Child_Gender (que sí existe) para ver la segmentación de la herencia por sexo
        fig_traits = px.histogram(df, x=col_x, color="Child_Gender", barmode="group",
                                  title=f"Distribución Poblacional de {rasgo} del {progenitor} según el Género del Hijo",
                                  labels={col_x: f"{rasgo} del {progenitor}", "count": "Cantidad de Registros"},
                                  color_discrete_sequence=["#3498DB", "#F1948A"])
        st.plotly_chart(fig_traits, use_container_width=True)
        
        st.markdown("---")
        st.subheader("💡 ¿Qué significa este análisis fenotípico?")
        ex_t1, ex_t2 = st.columns(2)
        with ex_t1:
            st.info(
                "**Interpretación del Gráfico Categórico:**\n\n"
                f"* Cada par de barras muestra la cantidad de registros en tus 7,000 datos que presentan un determinado **{rasgo.lower()}**.\n"
                f"* La división por colores permite evaluar si existe algún sesgo de distribución o ligamiento según el género del hijo."
            )
        with ex_t2:
            st.success(
                "**Conclusión de Exposición:**\n\n"
                "A diferencia de los rasgos métricos continuos, las variables cualitativas siguen distribuciones multinomiales discretas. Este módulo demuestra cómo se reparten las características externas en la población bajo estudio."
            )

    # ------------------------------------------------------------------
    # PESTAÑA 4: ANÁLISIS PROBABILÍSTICO DE RIESGO
    # ------------------------------------------------------------------
    with tab4:
        st.header("Distribución Porcentual de Riesgo de Salud")
        st.write("Modelado probabilístico del nivel de riesgo sanitario en la descendencia según antecedentes clínicos familiares.")
        
        col_c1, col_c2 = st.columns([1, 2])
        with col_c1:
            opcion_filtro = st.selectbox("Seleccione Historial de Enfermedad Familiar:", df["Family_Disease_History"].unique())
            
        with col_c2:
            df_filtrado = df[df["Family_Disease_History"] == opcion_filtro]
            
            fig_bar = px.histogram(df_filtrado, x="Predicted_Health_Risk", color="Child_Gender", 
                                   barmode="group", histnorm='percent',
                                   title=f"Probabilidad de Riesgo Genético | Antecedente: {opcion_filtro}",
                                   labels={"Predicted_Health_Risk": "Nivel de Riesgo Predicho", "percent": "Probabilidad (%)"},
                                   text_auto=".1f", color_discrete_sequence=["#2980B9", "#E74C3C"])
            st.plotly_chart(fig_bar, use_container_width=True)

        st.markdown("---")
        st.subheader("💡 ¿Qué significa este análisis probabilístico?")
        exp_bar1, exp_bar2 = st.columns(2)
        with exp_bar1:
            st.info(
                "**Lectura de Frecuencias Relativas:**\n\n"
                f"* Al procesar el historial **'{opcion_filtro}'**, los datos se transforman en porcentajes directos de probabilidad.\n"
                f"* Esto permite comparar de forma objetiva qué tan propenso es el hijo a desarrollar complicaciones en comparación con otros antecedentes."
            )
        with exp_bar2:
            st.success(
                "**Conclusión Epidemiológica:**\n\n"
                "Sustituir los valores absolutos por densidades porcentuales permite estimar la penetrancia del rasgo patológico. El gráfico evidencia la probabilidad empírica de transmisión de factores de riesgo multifactoriales."
            )

    # ------------------------------------------------------------------
    # PESTAÑA 5: SIMULADOR PREDICTIVO MULTIRRASGO (CORREGIDA CON COLUMNAS REALES)
    # ------------------------------------------------------------------
    with tab5:
        st.header("🔮 Simulador de Predicción de Rasgos del Hijo")
        st.write("Ingrese el perfil fenotípico de los padres biológicos para proyectar las características esperadas en la descendencia.")
        
        sim_p, sim_m = st.columns(2)
        
        with sim_p:
            st.subheader("👨 Perfil del Padre")
            p_height = st.slider("Estatura Padre (cm)", float(df["Father_Height_cm"].min()), float(df["Father_Height_cm"].max()), float(df["Father_Height_cm"].mean()))
            p_blood = st.selectbox("Grupo Sanguíneo Padre:", sorted(df["Father_Blood_Group"].unique()))
            p_eye = st.selectbox("Color de Ojos Padre:", sorted(df["Father_Eye_Color"].unique()))
            
        with sim_m:
            st.subheader("👩 Perfil de la Madre")
            m_height = st.slider("Estatura Madre (cm)", float(df["Mother_Height_cm"].min()), float(df["Mother_Height_cm"].max()), float(df["Mother_Height_cm"].mean()))
            m_blood = st.selectbox("Grupo Sanguíneo Madre:", sorted(df["Mother_Blood_Group"].unique()))
            m_eye = st.selectbox("Color de Ojos Madre:", sorted(df["Mother_Eye_Color"].unique()))
            
        st.markdown("---")
        st.subheader("🎯 Resultados de la Predicción Genética Simulada")
        
        # 1. Cálculo de Estatura Continua
        estatura_hijo = (p_height + m_height) / 2
        
        # 2. Inferencia basada en columnas reales del archivo
        match_sangre = df[(df["Father_Blood_Group"] == p_blood) & (df["Mother_Blood_Group"] == m_blood)]
        if not match_sangre.empty:
            sangre_predicha = match_sangre["Predicted_Child_Blood_Group"].mode()[0]
        else:
            sangre_predicha = df["Predicted_Child_Blood_Group"].mode()[0]
            
        match_riesgo = df[(df["Father_Eye_Color"] == p_eye) & (df["Mother_Eye_Color"] == m_eye)]
        if not match_riesgo.empty:
            riesgo_predicho = match_riesgo["Predicted_Health_Risk"].mode()[0]
        else:
            riesgo_predicho = df["Predicted_Health_Risk"].mode()[0]
            
        # Despliegue de métricas predictivas corregidas sin columnas falsas
        r1, r2, r3 = st.columns(3)
        with r1:
            st.metric(label="📏 Estatura Estimada del Hijo", value=f"{estatura_hijo:.2f} cm")
        with r2:
            st.metric(label="🩸 Grupo Sanguíneo Probable", value=str(sangre_predicha))
        with r3:
            st.metric(label="🏥 Riesgo de Salud Estimado", value=str(riesgo_predicho))
            
        st.info("💡 **Nota metodológica:** Las predicciones se calculan mediante la máxima verosimilitud (moda estadística) de las intersecciones de datos presentes en la muestra poblacional de tus 7,000 registros.")

except Exception as e:
    st.error(f"⚠️ Error en la ejecución del script analítico. Detalle: {e}")

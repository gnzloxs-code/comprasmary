import streamlit as st

st.set_page_config(page_title="Compras Mary", page_icon="👗", layout="wide")

# Catálogo de productos (sin base de datos, todo en memoria)
productos = [
    {"nombre": "Camisa Blanca Clásica", "categoria": "Camisas", "precio": 15990, "imagen": "https://placehold.co/300x300?text=Camisa+Blanca"},
    {"nombre": "Camisa a Cuadros", "categoria": "Camisas", "precio": 17990, "imagen": "https://placehold.co/300x300?text=Camisa+Cuadros"},
    {"nombre": "Pantalón Jeans Azul", "categoria": "Pantalones", "precio": 24990, "imagen": "https://placehold.co/300x300?text=Jeans+Azul"},
    {"nombre": "Pantalón de Vestir Negro", "categoria": "Pantalones", "precio": 22990, "imagen": "https://placehold.co/300x300?text=Pantalon+Negro"},
    {"nombre": "Polera Básica Blanca", "categoria": "Poleras", "precio": 9990, "imagen": "https://placehold.co/300x300?text=Polera+Blanca"},
    {"nombre": "Polera Estampada", "categoria": "Poleras", "precio": 11990, "imagen": "https://placehold.co/300x300?text=Polera+Estampada"},
    {"nombre": "Abrigo de Lana Beige", "categoria": "Abrigos", "precio": 39990, "imagen": "https://placehold.co/300x300?text=Abrigo+Beige"},
    {"nombre": "Abrigo Acolchado Negro", "categoria": "Abrigos", "precio": 44990, "imagen": "https://placehold.co/300x300?text=Abrigo+Negro"},
    {"nombre": "Zapatos Casuales Cuero", "categoria": "Zapatos", "precio": 34990, "imagen": "https://placehold.co/300x300?text=Zapatos+Cuero"},
    {"nombre": "Zapatillas Deportivas", "categoria": "Zapatos", "precio": 29990, "imagen": "https://placehold.co/300x300?text=Zapatillas"},
    {"nombre": "Falda Plisada", "categoria": "Faldas", "precio": 18990, "imagen": "https://placehold.co/300x300?text=Falda+Plisada"},
    {"nombre": "Chaqueta de Cuero", "categoria": "Abrigos", "precio": 49990, "imagen": "https://placehold.co/300x300?text=Chaqueta+Cuero"},
]

# Inicializar carrito en sesión
if "carrito" not in st.session_state:
    st.session_state.carrito = []

# ---------- ENCABEZADO ----------
st.title("👗 Compras Mary")
st.subheader("Tu tienda de ropa online: camisas, pantalones, poleras, abrigos, zapatos y más")
st.markdown("---")

# ---------- BARRA LATERAL: FILTRO Y CARRITO ----------
st.sidebar.header("Filtrar por categoría")
categorias = ["Todas"] + sorted(set(p["categoria"] for p in productos))
categoria_seleccionada = st.sidebar.selectbox("Categoría", categorias)

st.sidebar.markdown("---")
st.sidebar.header("🛒 Carrito de compras")

if st.session_state.carrito:
    total = 0
    for item in st.session_state.carrito:
        st.sidebar.write(f"- {item['nombre']} — ${item['precio']:,}")
        total += item["precio"]
    st.sidebar.markdown(f"**Total: ${total:,}**")
    if st.sidebar.button("Vaciar carrito"):
        st.session_state.carrito = []
        st.rerun()
else:
    st.sidebar.write("El carrito está vacío.")

# ---------- CATÁLOGO ----------
st.header("Catálogo de productos")

if categoria_seleccionada != "Todas":
    productos_filtrados = [p for p in productos if p["categoria"] == categoria_seleccionada]
else:
    productos_filtrados = productos

# Mostrar productos en columnas (grid de 3)
cols_por_fila = 3
for i in range(0, len(productos_filtrados), cols_por_fila):
    fila = productos_filtrados[i:i + cols_por_fila]
    columnas = st.columns(cols_por_fila)
    for col, producto in zip(columnas, fila):
        with col:
            st.image(producto["imagen"], use_container_width=True)
            st.markdown(f"**{producto['nombre']}**")
            st.write(f"Categoría: {producto['categoria']}")
            st.write(f"Precio: ${producto['precio']:,}")
            if st.button("Agregar al carrito", key=producto["nombre"]):
                st.session_state.carrito.append(producto)
                st.success(f"{producto['nombre']} agregado al carrito ✅")

# ---------- PIE DE PÁGINA ----------
st.markdown("---")
st.markdown("### 📍 Contacto")
st.write("📞 Teléfono: +56 9 1234 5678")
st.write("📧 Email: contacto@comprasmary.cl")
st.write("📷 Instagram: @comprasmary")

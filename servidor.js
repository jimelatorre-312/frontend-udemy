// server.js
const express = require("express");
const productos = require("./productos");

const app = express();
const PORT = 3000;

// Ruta para obtener todos los productos
app.get("/productos", (req, res) => {
  res.json(productos);
});

// Ruta para obtener un producto por su id
app.get("/productos/:id", (req, res) => {
  const { id } = req.params;
  const producto = productos.find(p => p.id === parseInt(id));

  if (!producto) {
    return res.status(404).json({ mensaje: "Producto no encontrado" });
  }
  res.json(producto);
});

// Levantar el servidor
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});

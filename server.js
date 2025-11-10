const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

const a = 2.9524892816519372;
const b = 75.71791057835327;

app.get("/prever", (req, res) => {
  const area = Number(req.query.area);
  if (!area) return res.json({ erro: "Envie ?area=valor" });
  prever(area).then(preco => {
    priceText.textContent = preco;
  });
  

  const preco = a * area + b;
  res.json({ preco });
});

app.listen(3000, () => console.log("API rodando na porta 3000"));

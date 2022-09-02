import React from "react";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";
const Layout = React.lazy(() => import("./pages/Layout/Layout"));
const Home = React.lazy(() => import("./pages/Home/Home"));
const ProductSingle = React.lazy(() =>
  import("./pages/ProductSingle/ProductSingle")
);
const Category = React.lazy(() => import("./pages/Category/Category"));
function App() {
  return (
    <BrowserRouter>
      <React.Suspense fallback={<>hello ali komijani</>}>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="products/:slug" element={<ProductSingle />} />
            <Route path="categories/:id" element={<Category />} />
          </Route>
        </Routes>
      </React.Suspense>
    </BrowserRouter>
  );
}

export default App;

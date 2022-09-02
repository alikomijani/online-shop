import axios from "./axios";

export const getProductList = async (query="") => {
  const response = await axios.get("/api/products/?" + query);
  return response;
};

export const getCategoriesList = async () => {
  const response = await axios.get("/api/categories/");
  return response;
};

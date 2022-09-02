import React from "react";
import './categoriesList.style.css'
import { Link } from "react-router-dom";
const CategoriesList = ({ categories = [] }) => {
  return (
    <div className="CategoriesList">
      {categories.map((category) => (
        <Link key={category.slug} to={'/categories/' + category.id}>
          <div className="CategoriesList__item" >{category.name}</div>
        </Link>

      ))}
    </div>
  );
};

export default CategoriesList;

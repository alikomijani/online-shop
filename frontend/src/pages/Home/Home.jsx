import React, { useEffect, useState } from 'react'
import { getCategoriesList, getProductList } from '../../services/api'
import { CategoriesList ,Container } from '../../components'
const Home = () => {
  const [products, setProducts] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  useEffect(() => {
    Promise.all([getProductList(), getCategoriesList()]).then(values => {
      setProducts(values[0].data.results)
      setCategories(values[1].data.results)
      setLoading(false)
    }).catch(e => {
      setError(true)
    })
  }, [])
  if(loading){
    return<div>...loading</div>
  }
  if(error){
    return <div>ERROR</div>
  }
  return (
    <Container>
      <CategoriesList categories={categories}/>
    </Container>
  )
}

export default Home
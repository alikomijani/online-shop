import React, { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import { getProductList } from '../../services/api'
const Category = () => {
    const { id } = useParams()
    const [productList, setProductList] = useState([])
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(false)
    useEffect(() => {
        setLoading(true)
        getProductList(`category=${id}`)
            .then(response => setProductList(response.data.results))
            .catch(e => {
                console.log(e)
                setError(true)
            })
            .finally(() => {
                setLoading(false)
            })
    }, [id])
    return (
        <div>{productList.map(item => (
            <div key={item.slug}>{item.name}</div>
        ))}</div>
    )
}

export default Category
import React from 'react'
import './container.style.css'
const Container = (props) => {
    return (
        <div className='Container'>{props.children}</div>
    )
}

export default Container
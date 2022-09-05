import axios from 'axios'


const api = axios.create({
 
    baseURL: 'http://82.115.20.92/',
    headers: {
        'Content-type': 'application/json',
        Accept: 'application/json',
    },
});


export default api
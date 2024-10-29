// import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
// import axios from 'axios'
function App() {
    //   const [Keyvalue, SetKey] = useState[""];

    //   const handleChat = () =>{
    //     useEffect(() => {
    //       const fetchData = async () =>{
    //         try{
    //           const response = await axios.post("",{
    //             key:"value",
    //             enpoint:"value"
    //           })
    //         }catch(error){
    //           console.log('Request response error',error);
    //         }
    //       }
          
    //     }
    //   )
    // }
  return (
    <>
      <div>
      <p className="read-the-docs">
        Chat With Open AI
      </p>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
    </>
    )
  }

export default App

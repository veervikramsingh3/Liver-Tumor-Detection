import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './App.css'
import { Toaster } from 'react-hot-toast'
import { BrowserRouter } from 'react-router-dom'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <App />
      <Toaster
        position="top-center"
        reverseOrder={false}
        toastOptions={{
          className: "bg-gray-800 text-base text-white font-['Poppins']"
        }}
      />
    </BrowserRouter>
  </React.StrictMode>
)

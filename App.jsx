import { useEffect, useState } from 'react'
import { Routes, Route, useLocation } from 'react-router-dom'
import Navbar from './components/Navbar'
import Sidebar from './components/Sidebar'
import Home from './pages/Home'
import About from './pages/About'
import Contact from './pages/Contact'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import Cases from './pages/Cases'
import AddCase from './components/AddCase'
import ViewCase from './components/ViewCase'
import Loading from './pages/Loading'
import ProtectedRoute from './routes/ProtectedRoute'

function App() {
  // Load login status directly from localStorage
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    return localStorage.getItem('isLoggedIn') === 'true'
  })
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)

  const location = useLocation()

  useEffect(() => {
    const loggedIn = localStorage.getItem('isLoggedIn') === 'true'
    setIsLoggedIn(loggedIn)
  }, [location.pathname])

  // Show sidebar only for specific routes
  const showSidebar =
    location.pathname.startsWith('/prediction/dashboard') ||
    location.pathname.startsWith('/prediction/cases')

  const hideNavbar = location.pathname === '/prediction/loading'

  return (
    <>
      {!hideNavbar && !showSidebar && <Navbar />}
      {showSidebar && <Sidebar setIsLoggedIn={setIsLoggedIn} onCollapseChange={setSidebarCollapsed} />}

      <div className={`${showSidebar ? (sidebarCollapsed ? 'ml-20' : 'ml-72') : 'mt-[0px]'} p-0 transition-all duration-300 ease-in-out`}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/prediction/login" element={<Login setIsLoggedIn={setIsLoggedIn} />} />
          <Route path="/prediction/register" element={<Register setIsLoggedIn={setIsLoggedIn} />} />
          <Route path="/prediction/loading" element={<Loading />} />

          <Route
            path="/prediction/dashboard"
            element={
              <ProtectedRoute isLoggedIn={isLoggedIn}>
                <Dashboard />
              </ProtectedRoute>
            }
          />
          <Route
            path="/prediction/cases"
            element={
              <ProtectedRoute isLoggedIn={isLoggedIn}>
                <Cases />
              </ProtectedRoute>
            }
          />
          <Route
            path="/prediction/cases/add"
            element={
              <ProtectedRoute isLoggedIn={isLoggedIn}>
                <AddCase />
              </ProtectedRoute>
            }
          />
          <Route
            path="/prediction/cases/view"
            element={
              <ProtectedRoute isLoggedIn={isLoggedIn}>
                <ViewCase />
              </ProtectedRoute>
            }
          />
        </Routes>
      </div>
    </>
  )
}

export default App

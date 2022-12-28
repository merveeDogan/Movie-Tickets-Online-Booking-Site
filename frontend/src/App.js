import "./App.css";
import { HelmetProvider } from "react-helmet-async";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
import "bootstrap/dist/js/bootstrap.min.js";
import Mainpage from "./components/mainpage/Mainpage";
import MovieDetailPage from "./components/movie-details/MovieDetailPage.jsx";
import Login from "./components/login-page/Login";
import Signup from "./components/signup-page/Signup";
import BookTicketPage from "./components/booking/BookTicketPage";
import PaymentPage from "./components/payment/PaymentPage";
import Navbar from "./components/navbar/Navbar";
import { AuthProvider } from "./context/AuthContext";
export default function App() {
  const helmetContext = {};
  return (
    <HelmetProvider context={helmetContext}>
      <BrowserRouter>
        <AuthProvider>
          <Navbar />
          <Routes>
            <Route path="/" element={<Mainpage />} />
            <Route path="film-details/*" element={<MovieDetailPage />} />
            <Route path="log-in" element={<Login />} />
            <Route path="sign-up" element={<Signup />} />
            <Route
              path="/film-details/film-name/book-ticket"
              element={<BookTicketPage />}
            />
            <Route path="/film-details/film-name/book-ticket/payment" element={<PaymentPage />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </HelmetProvider>
  );
}

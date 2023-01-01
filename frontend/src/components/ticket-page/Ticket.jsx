import { useContext } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import AuthContext from "../../context/AuthContext";
import "./ticket.css";
const Ticket = () => {
  let { user, logoutUser } = useContext(AuthContext);
  let { authTokens } = useContext(AuthContext);
  let [tickets, setTickets] = useState([
    {
      ticket_id: 1234,
      price: 50,
      show_id: 1,
      seat_id: "A1",
      user: "X",
    },
    {
      ticket_id: 1235,
      price: 50,
      show_id: 2,
      seat_id: "A2",
      user: "T",
    },
  ]);

  let getTickets = async () => {
    let response = await fetch("http://127.0.0.1:8000/Tickets/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + String(authTokens.access),
      },
    });
    let data = await response.json();

    if (response.status === 200) {
      setTickets(data);
      console.log(data);
    } else if (response.statusText === "Unauthorized") {
      logoutUser();
    }
  };
  return (
    <div>
      <div className="ticket-list">
        <p className="my-tickets">My Tickets</p>
        {tickets.map((ticket) => (
          <div key={ticket.ticket_id}>
            <img
              src="https://img.freepik.com/premium-vector/vector-drawing-cinema-ticket-cinema-ticket-icon_606226-42.jpg?w=2000"
              className="card-img-top ticket-pngg"
              alt="..."
            />
            <div className="ticket-info">
              <div>Ticket ID: {ticket.ticket_id}</div>
              <div>Price: {ticket.price}</div>
              <div>Show ID: {ticket.show_id}</div>
              <div>Seat ID: {ticket.seat_id}</div>
              <div>User: {ticket.user}</div>
              <p></p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Ticket;

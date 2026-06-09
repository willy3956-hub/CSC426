import { useState } from "react";
import "./App.css";

function App() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = (e) => {
    e.preventDefault();

    if (!username || !password) {
      setMessage("Please fill in all fields");
      return;
    }

    if (username === "admin" && password === "12345") {
      setMessage("Login Successful!");
    } else {
      setMessage("Invalid Username or Password");
    }
  };

  const handleReset = () => {
    setUsername("");
    setPassword("");
    setMessage("");
  };

  return (
    <div className="container">
      <form className="login-box" onSubmit={handleLogin}>
        <h2>Login Authentication</h2>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <p>{message}</p>

        <div className="buttons">
          <button type="submit">Login</button>
          <button type="button" onClick={handleReset}>
            Reset
          </button>
        </div>
      </form>
    </div>
  );
}

export default App;
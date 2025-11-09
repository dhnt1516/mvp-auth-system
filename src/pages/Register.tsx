import React, { useState } from "react";

export default function Register() {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setMsg(null);
    try {
      const res = await fetch(`/api/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ login, password }),
      });
      const data = await res.json();
      if (res.ok) {
        setMsg(data.message || "User created");
      } else {
        setMsg(data.detail || JSON.stringify(data));
      }
    } catch (err) {
      setMsg("Network error");
    }
  };

  return (
    <div style={{ maxWidth: 480, margin: "40px auto" }}>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Login</label>
          <input value={login} onChange={(e) => setLogin(e.target.value)} />
        </div>
        <div>
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </div>
        <button type="submit">Register</button>
      </form>
      {msg && <div style={{ marginTop: 12 }}>{msg}</div>}
    </div>
  );
}

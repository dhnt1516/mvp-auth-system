import React from "react";
import Register from "./pages/Register";

const App: React.FC = () => {
  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>Регистрация пользователя</h1>
      <Register />
    </div>
  );
};

export default App;

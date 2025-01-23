import { Route, Routes } from "react-router-dom";
import Layout from "./components/shared/Layout";
import Dashboard from "./pages/Dashboard";
import Client from "./pages/Client";

function App() {
  return (
    <Routes> 
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="gabin" element={<Client />} />
      </Route>
      <Route path="/login" element={<h1>this is login page</h1>} />
    </Routes>
  );
}

export default App;

import React, { useEffect, useState } from "react";
import NavBar from "./NavBar";
import Login from "../pages/Login";
import { Switch, Route } from "react-router-dom";
import EntriesList from "../pages/EntriesList";
import NewEntry from "../pages/NewEntry";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch("/check_session").then((r) => {
      if (r.ok) {
        r.json().then((user) => setUser(user));
      }
    });
  }, []);

  if (!user) return <Login onLogin={setUser} />;

  return (
    <>
      <NavBar user={user} setUser={setUser} />
      <main>
        <Switch>
          <Route path="/new">
            <NewEntry user={user} />
          </Route>
          <Route path="/">
            <EntriesList />
          </Route>
        </Switch>
      </main>
    </>
  );
}

export default App;

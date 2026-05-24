import { useEffect, useState } from "react"
import ReactMarkdown from "react-markdown";
import { Link } from "react-router-dom";
import styled from "styled-components";
import { Box, Button } from "../styles";

function EntriesList() {
  const [entries, setEntries] = useState([]);

  useEffect(() => {
    fetch("/entries")
      .then((r) => r.json())
      .then(setEntries);
  }, []);

  return (
    <Wrapper>
      {entries.length > 0 ? (
        entries.map((entry) => (
          <Entry key={entry.id}>
            <Box>
              <h2>{entry.first_line}</h2>
              <p>{entry.date}</p>
              <ReactMarkdown>{entry.text}</ReactMarkdown>
            </Box>
          </Entry>
        ))
      ) : (
        <p>No entries yet.</p>
      )}
    </Wrapper>
  );
}

const Wrapper = styled.section`
  max-width: 800px;
  margin: 40px auto;
`;

const Entry = styled.article`
  margin-bottom: 24px;
`;

export default EntriesList;
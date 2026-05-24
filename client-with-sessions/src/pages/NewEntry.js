import { useState } from "react";
import { useHistory } from "react-router-dom";
import styled from "styled-components";
import ReactMarkdown from "react-markdown";
import { Button, Error, FormField, Input, Label, Textarea } from "../styles";

function NewEntry({ user }) {
  const [formData, setFormData] = useState({
    date: new Date().toISOString().split("T")[0],
    first_line: "",
    mood: "Reflective",
    text: "Enter your journal entry here...",
  });
  const [errors, setErrors] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const history = useHistory();

  function handleSubmit(e) {
    e.preventDefault();
    setIsLoading(true);
    fetch("/recipes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ ...formData, user_id: user.id }),
    })
      .then((r) => {
        setIsLoading(false);
        if (r.ok) {
          r.json().then((newEntry) => history.push(`/entries/${newEntry.id}`));
        }
        else {
          r.json().then((err) => setErrors(err.errors));
        }
      });
  }

  return (
    <Wrapper>
      <WrapperChild>
        <h2>New Journal Entry</h2>
        <form onSubmit={handleSubmit}>
          <FormField>
            <Label htmlFor="date">Date</Label>
            <Input
              type="date"
              id="date"
              value={formData.date}
              onChange={(e) => setFormData({ ...formData, date: e.target.value })}
            />
          </FormField>
          <FormField>
            <Label htmlFor="first_line">First Line</Label>
            <Input
              type="text"
              id="first_line"
              value={formData.first_line}
              onChange={(e) => setFormData({ ...formData, first_line: e.target.value })}
            />
          </FormField>
          <FormField>
            <Label htmlFor="mood">Mood</Label>
            <Input
              type="text"
              id="mood"
              value={formData.mood}
              onChange={(e) => setFormData({ ...formData, mood: e.target.value })}
            />
          </FormField>
          <FormField>
            <Label htmlFor="text">Entry Text</Label>
            <Textarea
              id="text"
              rows="10"
              value={formData.text}
              onChange={(e) => setFormData({ ...formData, text: e.target.value })}
            />
          </FormField>
          <Button type="submit" disabled={isLoading}>
            {isLoading ? "Saving..." : "Save Entry"}
          </Button>
          {errors.length > 0 && (
            <Error>
              {errors.map((err) => (<p key={err}>{err}</p>
              ))}
            </Error>
          )}
        </form>
      </WrapperChild>
      <WrapperChild>
        <h2>Live Preview</h2>
        <h3>{formData.first_line}</h3>
        <p><em>{formData.mood}</em></p>
        <ReactMarkdown>{formData.text}</ReactMarkdown>
      </WrapperChild>
    </Wrapper>
  );

}

const Wrapper = styled.section`
  max-width: 1000px;
  margin: 40px auto;
  padding: 16px;
  display: flex;
  gap: 24px;
`;

const WrapperChild = styled.div`
  flex: 1;
`;

export default NewEntry;
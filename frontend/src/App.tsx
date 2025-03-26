import { Box, Button, TextField } from "@mui/material";
import { Header } from "./components/common/Header";
import { useState } from "react";
import { getGeminiText } from "./components/api/getGeminiText";

export const App = () => {
  const [text1, setText1] = useState("");
  const [text2, setText2] = useState("");
  const [text3, setText3] = useState("");

  const [geminiText, setGeminiText] = useState("");

  const handleClick = async () => {
    getGeminiText([text1, text2, text3])
      .then((text) => {
        setGeminiText(text);
      })
      .catch((e) => {
        console.error(e);
      });
  };

  const handleClear = () => {
    setText1("");
    setText2("");
    setText3("");
  };

  return (
    <>
      <Header />
      <Box component="main">
        <Box>
          <TextField value={text1} onChange={(e) => setText1(e.target.value)} />
          <TextField value={text2} onChange={(e) => setText2(e.target.value)} />
          <TextField value={text3} onChange={(e) => setText3(e.target.value)} />
          <Button variant="contained" onClick={handleClear}>
            clear
          </Button>
          <Button variant="contained" onClick={handleClick}>
            生成
          </Button>
        </Box>
        <Box>
          <Box>{geminiText === "" ? "blank" : geminiText}</Box>
        </Box>
      </Box>
    </>
  );
};

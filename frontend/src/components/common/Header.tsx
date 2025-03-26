import { AppBar, Typography } from "@mui/material";

export const Header = () => {
  return (
    <AppBar position="static" sx={{ px: 2 }}>
      <Typography component="h1" sx={{ fontSize: 40 }}>
        OKR Helper
      </Typography>
    </AppBar>
  );
};

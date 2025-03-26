export const getGeminiText = async (texts: string[]) => {
  const res = await fetch(`${import.meta.env.VITE_API_BASE_URL}objectives`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ texts }),
  });
  const json = await res.json();
  return json;
};

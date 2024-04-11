const aiEndpoint = "http://localhost:5000";

export const AIService = {
  getPersonalityTypes: (data) => {
    return fetch(aiEndpoint + "/process", {
      method: "POST",
      body: JSON.stringify({ sentences: data }),
      headers: {
        "Content-Type": "application/json"
      }
    });
  }
};

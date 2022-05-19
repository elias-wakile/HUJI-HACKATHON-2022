export function performLogin({ email, password }) {
  const delay = (0.5 + Math.random() * 2) * 1000;
  return new Promise((resolve, reject) => {
    setTimeout(function () {
      if (password === "correct" && !!email) {
        resolve({
          data: {
            username: "Meir",
            weight: null,
            height: 175,
            bodyType: "skinny",
          },
        });
      } else {
        reject(new Error("Invalid credentials"));
      }
    }, delay);
  });
}

import { useState } from "preact/hooks";

function SignUpForm() {
  const [responseMessage, setResponseMessage] = useState("");
  const [responseError, setResponseError] = useState(false);

  const createUser = async (event) => {
    const signUpData = new FormData(event.target);
    const username = signUpData.get("username");
    const password = signUpData.get("password");

    const response = await fetch("http://127.0.0.1:5000/api/users", {
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({ username, password }),
    });

    const data = await response.json();

    if (response.status !== 201) {
      setResponseError(true);
      setResponseMessage(data.message);
    } else {
      setResponseError(false);
      setResponseMessage(data.message);
    }
  };

  const handleOnSubmit = (event) => {
    event.preventDefault();

    createUser(event);
  };

  return (
    <form onSubmit={handleOnSubmit} class="grid w-[500px] gap-y-6">
      <div>
        <input
          class="w-full py-3 pl-6 rounded-lg font-semibold text-lg outline-none text-slate-800"
          type="text"
          placeholder="Username"
          autocomplete="off"
          name="username"
          id="username"
          required
        />
      </div>
      <div>
        <input
          class="w-full py-3 pl-6 rounded-lg font-semibold text-lg outline-none text-slate-800"
          type="password"
          placeholder="Password"
          autocomplete="off"
          name="password"
          id="password"
          required
        />
      </div>
      <button
        type="submit"
        class="bg-emerald-500 text-slate-800 rounded-lg py-3 font-semibold text-lg hover:bg-emerald-600"
      >
        Sign Up
      </button>
      {responseMessage && (
        <p
          class={`text-center text-xl font-medium ${
            responseError ? "text-red-500" : "text-emerald-500"
          }`}
        >
          {responseMessage}
        </p>
      )}
    </form>
  );
}

export default SignUpForm;

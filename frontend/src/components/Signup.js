import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Signup = () => {
  const navigate = useNavigate();

  const handleSignup = (e) => {
    e.preventDefault();
    navigate("/dashboard");
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-r from-purple-500 to-indigo-600">
      <div className="bg-white p-8 rounded-lg shadow-xl max-w-md w-full">
        <h2 className="text-3xl font-bold text-center text-gray-800">Sign Up</h2>
        <p className="text-center text-gray-500">Create an account or <Link to="/" className="text-blue-600">Sign in</Link></p>
        <form className="mt-6 space-y-4" onSubmit={handleSignup}>
          <input type="text" placeholder="Full Name" className="input-field" required />
          <input type="email" placeholder="Email Address" className="input-field" required />
          <input type="password" placeholder="Password" className="input-field" required />

          <button type="submit" className="btn-primary">Sign Up</button>
        </form>
      </div>
    </div>
  );
};

export default Signup;

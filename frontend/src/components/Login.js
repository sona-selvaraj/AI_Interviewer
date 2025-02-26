import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    navigate("/dashboard");
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-r from-purple-500 to-indigo-600">
      <div className="bg-white p-8 rounded-lg shadow-xl max-w-md w-full">
        <h2 className="text-3xl font-bold text-center text-gray-800">Welcome Back!</h2>
        <p className="text-center text-gray-500">Enter your credentials to sign in</p>
        <form className="mt-6 space-y-4" onSubmit={handleLogin}>
          <input type="email" placeholder="Email" className="input-field" required />
          <input type="password" placeholder="Password" className="input-field" required />

          <button type="submit" className="btn-primary">Sign In</button>

          <div className="text-center">
            <p className="text-gray-500">Don't have an account? <Link to="/signup" className="text-blue-600">Sign up</Link></p>
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;

import React, { useState } from 'react';

const StudentForm = () => {
  const [student, setStudent] = useState({
    name: '',
    age: '',
    email: '',
    course: ''
  });

  const handleChange = (e) => {
    setStudent({
      ...student,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch('http://127.0.0.1:5000/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(student)
    });

    const result = await response.json();
    alert(result.message);
    setStudent({ name: '', age: '', email: '', course: '' });
  };

  return (
    <div>
      <h2>Register Student</h2>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" value={student.name} onChange={handleChange} required />
        <input type="number" name="age" placeholder="Age" value={student.age} onChange={handleChange} required />
        <input type="email" name="email" placeholder="Email" value={student.email} onChange={handleChange} required />
        <select name="course" value={student.course} onChange={handleChange}>
          <option value="">Select Course</option>
          <option value="Computer Science">Computer Science</option>
          <option value="Business Administration">Business Administration</option>
        </select>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default StudentForm;

import React from 'react';
import StudentForm from './components/StudentForm';
import StudentList from './components/StudentList';

function App() {
  return (
    <div style={{ textAlign: "center", marginTop: "20px" }}>
      <h1>Student Management Portal</h1>
      <StudentForm />
      <hr />
      <StudentList />
    </div>
  );
}

export default App;

export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') throw TypeError('Name must be a string');
    if (typeof length !== 'number') throw TypeError('Length must be a sumber');
    if (!Array.isArray(students)) throw TypeError('Students must be an array');
    students.forEach((student) => {
      if (typeof student !== 'string') throw TypeError('Student must be a string');
    });
    this._name = name; // string
    this._length = length; // number
    this._students = students; // array
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('Name must be a string');
    } else {
      this._name = value;
    }
  }

  get name() {
    return this._name;
  }

  set length(value) {
    if (typeof value !== 'number') {
      throw TypeError('Length must be a number');
    } else {
      this._length = value;
    }
  }

  get length() {
    return this._length;
  }

  set students(value) {
    if (!Array.isArray(value) && value.forEach((student) => typeof student !== 'string')) {
      throw TypeError('Students must be an array of strings');
    } else {
      this._students = value;
    }
  }

  get students() {
    return this._students;
  }
}

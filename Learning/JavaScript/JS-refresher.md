# JavaScript Refresher

- [Introduction](#introduction)
- [var,let and const](#varlet-and-const)
  - [var](#var)
  - [let](#let)
  - [const](#const)
  - [Difference Between var, let and const](#difference-between-var-let-and-const)
- [Functions](#functions)
  - [Regular Function & its Syntax](#regular-function--its-syntax)
  - [Arrow Function & its Syntax](#arrow-function--its-syntax)

#### Introduction

- It is `weakly typed programming language` which means that we have no explicit type assignment.
- Data types can be switched dynamically means you can convert number to text.
- `Object oriented language` means that data can be organized in logical objects.
- `Primitive and reference type`

  - Primitive type values are : `String`,`Number`,`Boolean`, `Undefined`, `Null` and `Symbol` (introducted in ES6)
  - `Primitive type` values are copied by value
  - `Primitive type` values are stored in `Stack`
  - Stack is a small (limited in space) and fast memory and it does not hold more data
  - Reference type value are `Objects` such as `Array`
  - `Reference type` values are copied by value reference
  - `Reference type` values are stored in `Heap`
  - Heap can hold more data that changes dynamically. Therefore, it is slow
  - Watch https://www.youtube.com/watch?v=9ooYYRLdg_g for more details

- It is a `Versatile language` that runs in browser on a PC/server and can be used to do broad variety of tasks such as listen to user events in browser, rerender the DOM, work with files, databases etc.
-

#### var,let and const

var,const and let are keywords used to create variables.

##### var

- `var` is outdated use `let` instead of `var`
- Variables defined with `var` can be Redeclared
- Scoping of `let` and `var` are different
- Variables defined with `var` are hoisted to the top and can be initialized at any time. Meaning: You can use the variable before it is declared.

##### let

- The `let` & `const` keyword was introduced in ES6 (2015)
- const is used to create constant values that does not gets changed throughout the process.
- Variables defined with `let` & `const` cannot be Redeclared
- Variables defined with `let` & `const` must be Declared before use (Means they are not hoisted)
- Variables defined with `let` & `const` have Block Scope

##### const

- The ` `const` keyword was introduced in ES6 (2015)
- const is used to create constant variables that does not gets changed throughout the process.
- Variables defined with `const` cannot be Redeclared
- Variables defined with `const` must be Declared before use (Means they are not hoisted)
- Variables defined with `const` have Block Scope
- You can change the properties of a constant object

  ```
  // You can create a const object:
  const car = {type:"Fiat", model:"500", color:"white"};

  // You can change a property:
  car.color = "red";

  // You can add a property:
  car.owner = "Johnson";
  ```

  But you can NOT reassign the object:

  ```
  const car = {type:"Fiat", model:"500", color:"white"};

  car = {type:"Volvo", model:"EX60", color:"red"};    // ERROR

  ```

##### Difference Between var, let and const

|       | Scope | Redeclare | Reassign | Hoisted | Binds this |
| ----- | ----- | --------- | -------- | ------- | ---------- |
| var   | No    | Yes       | Yes      | Yes     | Yes        |
| let   | Yes   | No        | Yes      | No      | No         |
| const | Yes   | No        | No       | No      | No         |

#### Functions

- A JavaScript function is a block of code designed to perform a particular task.
- A JavaScript function is executed when "something" invokes it (calls it).
  ```
  // Function to compute the product of p1 and p2
  function myFunction(p1, p2) {
  return p1 \* p2;
  }
  ```

##### Regular Function & its Syntax

- A JavaScript function is defined with the function keyword, followed by a name, followed by parentheses ().
- Function names can contain letters, digits, underscores, and dollar signs (same rules as variables).
- The parentheses may include parameter names separated by commas: `(parameter1, parameter2, ...)`
- Regular functions are hoisted means you can use it before declaration
- The code to be executed, by the function, is placed inside curly brackets: {}

  ```
  function name(parameter1, parameter2, parameter3) {
  // code to be executed
  }
  ```

- Function parameters are listed inside the parentheses () in the function definition.
- Function arguments are the values received by the function when it is invoked.
- Inside the function, the arguments (the parameters) behave as local variables.

##### Arrow Function & its Syntax

- Arrow functions were introduced in ES6.
- Arrow functions allow us to write shorter function syntax:
  ```
  let myFunction = (a, b) => a * b;
  ```
- If the function has only one statement, and the statement returns a value, you can remove the brackets and the return keyword:

  ```
  hello = () => "Hello World!";

  ```

  **Note:** This works only if the function has only one statement.

- If you have only one parameter, you can skip the parentheses as well

  ```
  hello = val => "Hello " + val;
  ```

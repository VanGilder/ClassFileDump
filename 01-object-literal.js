//====================================================================
// object literal
//====================================================================
let person = {
    // properties
    first: "John",
    last: "Doe",
    "full name": "John Doe",
};

// property access
console.log(person.first);
console.log(person["last"]);
console.log(person["full name"]);
console.log("-----------------------------------------");

//====================================================================
// Problem: "full name" is a dependent property of "first" and "last".
//====================================================================
person.first = "Bob";

console.log(person.first);
console.log(person["last"]);
// should be dependent on another property
console.log(person["full name"]);
console.log("-----------------------------------------");

//============================================================================
// Computed properties - Call a function that will computer the property from
// the appropriate dependencies (sometimes called getters). Here the 'this'
// keyword is used in a "method" (a function attached to an object). 'this'
// returns a reference to the object itself when used in object methods.
//============================================================================
let person2 = {
    //properties
    first: "John",
    last: "Doe",
    // methods
    getFullName: function () {
        return this.first + " " + this.last;
    },
    // alternative function definition on an object literal.
    print() {
        console.log(this.first);
        console.log(this.last);
        console.log(this.getFullName());
        console.log("---------------------------------------------");
    },
};
person2.print();
person2.first = "Bob";
person2.print();


//============================================================================
// Note that using `this` in an object literal definition outside of methods
// won't work because the context of `this` is not executing in a function
// attached to an object, instead here `this` will refer to the outer scope
// since the object literal has not yet been created.
//============================================================================
let person3 = {
    //peroperties
    first: "John",
    last: "Doe",
    // failed computed property attempt
    fullName: this.first + " " + this.last,
    print: function () {
        console.log(this.first);
        console.log(this.last);
        console.log(this.fullName);
        console.log("-------------------------------------------------");
    },
};

//============================================================================
// The 'this keyword in an object method applies to the object on which the
// method resides and not necessarily the object where the function was defined
// For example:
//============================================================================
let person4 = {
    first: "Jane",
    last: "Doe",
};
person4.getFullName = person2.getFullName;
person4.print = person2.print;
person4.print();

//=============================================================================
// If there is no object that the function is attached to, `this` is undefined.
//=============================================================================
let getFullName = person4.getFullName;
console.log(getFullName());


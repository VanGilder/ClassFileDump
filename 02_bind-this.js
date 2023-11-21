
//====================================================================
// Using another object's method such that `this` references the other
// object rather than the current object.
//====================================================================

let alice = {
    //properties
    first: "Alice",
    last: "Alison",
    //methods
    getFullName: function () {
        return this.first + " " + this.last;
    },
};


// Helper function for use to print an object
function print () {
    console.log("------------------------------------------------");
    for (let property in this) {
        let value = this[property];
        let type = typeof value;
        let functionsNotToCall = ["print"];
        if (type === "function") {
            if (functionsNotToCall.includes(property))
                // value = value(); // unbound won't work because there is no parent object
                value = "FUNCTION";
            else
                value = this[property]();
        }
        console.log(`${property} (${type}): ${value}`);
    }
}


alice.print = print;
alice.print();


let bob = {
    first: "Bob",
    last: "Roberts",
    print, // equivalent to `print: print,`
};

bob.getFullName = alice.getFullName;
bob.getAliceFullName = alice.getFullName;
bob.print();

//==========================================================================================
// Join or "bind" a method to a specific object using a wrapper function.
//==========================================================================================
bob.getAliceFullNameWrapper = function () {
    return alice.getFullName();
};
bob.print();


//====================================================================================
// Built-in `bind` function to bind `this` to a specific object.
//====================================================================================
bob.getAliceFullNameBind = alice.getFullName.bind(alice);
bob.print();



//=================================================================================
// Can we build our own approximation of the bind function?
//=================================================================================
// Wrapper function - Attach function to object via temporary property, call
// method from object, then remove the temporary method.
// Clever, but not ideal

function mybind(obj, fn) {
    let prop = "-<{(TEMP_BIND_PROP)}>-";
    return function (...args) {
        obj[prop] = fn;
        let val = obj[prop](...args);
        delete obj[prop];
        return val;
    };
}

//17:35


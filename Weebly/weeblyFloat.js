// Steps : 
// (1) Take input string and convert it to an integer with only the digits.
// (2) Converts it to float based on the position of the decimal point.
// (3) Make it a negative number if input is negative.

function convertStringToFloat(inputFloatNum){
    var outputFloatNum = 0;
    var inputLength = inputFloatNum.length;
    
    if (inputLength === 0) writeln("No input given");
    else{
        for (var i = 0; i < inputLength; i++) {
            if (!isNaN(inputFloatNum[i]))
                outputFloatNum = outputFloatNum*10+parseInt(inputFloatNum[i]); 
        }
        outputFloatNum/= Math.pow(10,inputLength-1-inputFloatNum.indexOf('.'));
        if (inputFloatNum[0]=='-') outputFloatNum*= -1.0
    }
    return outputFloatNum;
}

var testCases = ["-14.26","-0.123","-.123","0.0","0.987","+1.014"];
for	(index = 0; index < testCases.length; index++) {
     writeln("The output for "+testCases[index]+ " is : "+convertStringToFloat(testCases[index]));
}


// Sample Output by using "http://math.chapman.edu/~jipsen/js/" to run the code is:
// The output for -14.26 is : -14.26
// The output for -0.123 is : -0.123
// The output for -.123 is : -0.123
// The output for 0.0 is : 0
// The output for 0.987 is : 0.987
// The output for +1.014 is : 1.014

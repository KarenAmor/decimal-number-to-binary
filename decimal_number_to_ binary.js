let number;
let binary = [];
process.stdout.write(`What number do you want to convert to binary?: `);

process.stdin.on('data', function(data){
    number = data.toString();
    do{
        if (number % 2 == 0){
            binary.unshift(0);
        }else{
            binary.unshift(1);
        }
        number = Math.trunc(number/2);
    }while(number >= 1);
    process.stdout.write(`The binary number is ${binary}!`)
    process.exit()
});

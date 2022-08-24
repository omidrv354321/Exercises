const content = ["rock,paper,scissor"];
const random = math.round(math.random() * 2);
const computer = content[random];
const userInput = prompt("rock, paper or scissors");
if(userInput){
    console.log(`you choos $(userInput)`);
}
else {
    console.log("you cheated");
}

console.log(`computer choosed ${computer}`)

if (computer == "rock") {
    if (userInput == "paper") alert("tie");
    else if ()


}
=3
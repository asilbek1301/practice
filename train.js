/* ANIMAL CHALLENGE: [2026년 4월 19일]
⭐️  Savol: Shunday function tuzing, unga argument sifatida tekstni pass qilganda, undagi harflar berilgan listda bor hayvonlarni return qilsin. 
MASALAN: 
findAnials('fdgwocalt') 
result: [ 'wolf', 'goat', 'dog', 'cat', 'cow' ] ni chiqaradi
*/

// ⭐️  Masalaning yechimi:
const animal_list = ["fox", "ant", "bird", "lion", "wolf", "deer", "bear", "frog", "hen", "mole", "duck", "goat", "dog", "cat", "bat", "cock", "cow"];

// DEFINE
function findAnimals(text) {
  //first we should erase same letters and leave only one
  let text1 = [...new Set(text)].join('');

  let new_animal_list = [];
  for (i1 = 0; i1 < animal_list.length; i1++) {
    let x = 0;
    for (i2 = 0; i2 < text1.length; i2++) {
      if (animal_list[i1].includes(text1[i2])) x++;
    }
    if (animal_list[i1].length == x) new_animal_list.push(animal_list[i1]);
  }
  return new_animal_list;
}

// CALL
const result = findAnimals('ffffffffffffffdgwocalxt');
console.log('result:', result);


//==================================================================


/* B-TASK (NodeJS): [2026년 4월 19일]
⭐️  Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN: countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

/* ⭐️  Masalaning yechimi:
// DEFINE
function countDigits(num) {
  let b = 0;
  for(i = 0; i < num.length; i++) {
    if(num[i] == Number(num[i])) b++
  }
  return b;
}

// CALL
result = countDigits("ad2a54y79wet0sfgb9")
console.log(result)
*/


//==================================================================


/* A-TASK (NodeJS): [2026년 4월 16일]
⭐️  Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak boladi. 
MASALAN: countLetter("e", "engineer") 3ni return qiladi.
*/

/* ⭐️  Masalaning yechimi:
// DEFINE
function countLetter(a, b) {
  let c = 0;
  for (let i = 0; i < b.length; i++) {
    if (a === b[i]) c++;
  }
  return c;
}

// CALL
const result = countLetter("e", "engineer");
console.log(result);
*/
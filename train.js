/* F-TASK (Nodejs): [2026년 4월 28일]
⭐️  Savol: Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak. 
MASALAN: findDoublers("hello") return true return qiladi
*/

// ⭐️  Masalaning yechimi:
// DEFINE
function findDoublers(string) {
  for(i = 0; i < string.length; i++) {
    let b = 0;
    for(x = 0; x < string.length; x++) {
      if(string[i] == string[x]) b++;
    }
    if(b > 1) return true
  }
  return false
}

// CALL
result = findDoublers("hello")
console.log(result)


//==================================================================


/* E-TASK (Nodejs): [2026년 4월 25일]
⭐️  Savol: Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin. 
MASALAN: getReverse("hello") return qilsin "olleh"
*/

/* ⭐️  Masalaning yechimi:
// DEFINE
function getReverse(string) {
  let newArray = []
  for(i = 0; i < string.length; i++) {
    newArray.unshift(string[i])
  }
  return newArray.join("")
}

// CALL
result = getReverse("hello")
console.log(result)
*/


//==================================================================


/* D-TASK (Nodejs): [2026년 4월 24일]
⭐️  Savol: Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin. 
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
*/

/* ⭐️  Masalaning yechimi:
// DEFINE
function getHighestIndex(array) {
  let highestIndex = 0

  for(i = 0; i < array.length; i++) {
    if(array[highestIndex] < array[i]) highestIndex = array.indexOf(array[i])
  }
  return highestIndex
}

// CALL
result = getHighestIndex([5, 21, 12, 21, 8])
console.log(result)
*/


//==================================================================


/* C-TASK (Nodejs): [2026년 4월 22일]
⭐️  Savol: Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin. 
MASALAN: checkContent("mitgroup", "gmtiprou") return qiladi true
*/

/* ⭐️  Masalaning yechimi:
// DEFINE
function checkContent(string1, string2) {
  if(string1.length != string2.length) return false
  else {
    sum = 0;
    for(i = 0; i < string1.length; i++) {
    if(string2.includes(string1[i])) sum++;
    }
    if(sum == string1.length) return true
    else {
    return false
    }
  }
}

// CALL
result = checkContent("mitgroup", "gmtiprou")
console.log(result)
*/


//==================================================================


/* ANIMAL CHALLENGE: [2026년 4월 19일]
⭐️  Savol: Shunday function tuzing, unga argument sifatida tekstni pass qilganda, undagi harflar berilgan listda bor hayvonlarni return qilsin. 
MASALAN: 
findAnials('fdgwocalt') 
result: [ 'wolf', 'goat', 'dog', 'cat', 'cow' ] ni chiqaradi
*/

/* ⭐️  Masalaning yechimi:
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
*/


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
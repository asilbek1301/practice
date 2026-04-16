/* A-TASK (NodeJS): [2026년 4월 16일]
⭐️  Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi so'zdan qatnashgan sonini return qilishi kerak boladi. 
MASALAN: countLetter("e", "engineer") 3ni return qiladi.
*/

// ⭐️  Masalaning yechimi:
function countLetter(a, b) {
  let c = 0;
  for (let i = 0; i < b.length; i++) {
    if (a === b[i]) c++;
  }
  return c;
}

const result = countLetter("e", "engineer");
console.log(result);
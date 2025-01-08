## All the description of the project is put inside this file
## Practising Git Commands

If I want ki mujhe ye folder github me daalna hai toh git initialization krna pdega.
S-1 Git init

Currently Readme.md is an untracked file, mai isko track krwana chahta hu
Now I want to commit my Readme.md file in my github repo. 
S-2 Git add Readme.md
Pehle 'U' tha ab 'A' hogya hai.

Ab ye saare files hum Staging environment me daalenge.
Staging environment - temporary environment, iss me saare files wgerah daalenge and then iss poore ko
Github repo. me push krenge
S-3 git commit -m "this is my first commit for this project"

Pushing all the files present in Staging environment to Github repo. 
S-4 git branch -M main  {Renaming the branch to main, main ki jageh master me bhi kr skta hu}
Iss step se pehle koi bhi branch nhi tha, ab ek main branch aa gya

Now I'll commit in this branch only and then push the files into github repo. 

S-5 Indication dedo ki mere Destination Repo. ka URL kya hai
git remote add origin https://github.com/Chirag2027/practisegit.git
Step 5 se ye pta chalega ki jo bhi mera file commit hoga woh origin me hi jayega

S-6 Final step hai
Pushing the Code in the Origin from main. 
main mera hogya local branch aur code local branch se origin me jayega
git push origin main

Jab bhi 1st Push ya Commit kre toh apne Github ka details daale,
if nhi daalenge toh chalega nhi 

developer_A branch is the exact replica of the main branch
Ab mai iss branch me kuch bhi code kr skta hu
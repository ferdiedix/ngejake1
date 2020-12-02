<?php

echo "Masukkan Balance => ";
$balance = trim(fgets(STDIN));
echo "Masukkan Base Bet => ";
$bet = trim(fgets(STDIN));
echo "Masukkan If Lose => ";
$if_lose = trim(fgets(STDIN));
$i = 1;
$balance -= $bet;
$balance = sprintf('%.8f', $balance);
while(true){
  $ls_bet += $bet;
  echo "[{$i}] {$bet} | {$balance} | -{$ls_bet}\n";
  $balance -= $bet;
  $balance = sprintf('%.8f', $balance);
  $bet *= $if_lose;
  $bet = sprintf('%.8f', $bet);
  $i++;
  if ($balance <= $bet){
    echo "Sisa Balance: {$balance}\n";
    exit();
  }
}

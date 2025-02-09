fn main() {

    let sub_end: u32= 1;
    let result= days_left(sub_end);

    println!("Your subscription will end in {result}.");

}


fn days_left(num: u32) -> String{

    let day_or_days = if num == 1 {format!("{num} day")} else {format!("{num} days")};
    day_or_days

}
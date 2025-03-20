use std::{env, fs};

fn main() {
    // ensure you have a file named version.txt with text 0.0.0 in it

    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
        panic!("Only one argument expected. Usage: ./bump <major/minor/patch/version>");
    }

    let bump_version: &str = &args[1];
    let f = fs::read_to_string("version.txt").expect("Unable to open file");
    let svp: Vec<&str> = f.trim().split(".").collect();

    let mut major = svp[0].parse().unwrap_or(0);
    let mut minor = svp[1].parse().unwrap_or(0);
    let mut patch = svp[2].parse().unwrap_or(0);

    match bump_version {
        "version" => version(),
        "major" => increment_major_version(&mut major),
        "minor" => increment_minor_version(&mut minor),
        "patch" => increment_patch_version(&mut patch),
        _ => panic!("Invalid argument. Usage: bump <major/minor/patch/version>"),
    };

    let version = format!("{major}.{minor}.{patch}");

    let _ = fs::write("version.txt", version);
}

fn version() {
    let current_version = fs::read_to_string("version.txt").expect("version.txt does not exist.");
    println!("{current_version}")
}

fn increment_major_version(major: &mut u16) {
    *major = *major + 1
}

fn increment_minor_version(minor: &mut u16) {
    *minor = *minor + 1
}

fn increment_patch_version(patch: &mut u16) {
    *patch = *patch + 1
}

/*
rustc bumpr.rs
echo "0.0.0" > version.txt
./bump version
0.0.0
./bump major
./bump version
1.0.0
./bump minor
./bump version
1.1.0
./bump patch
./bump version
1.1.1
* */

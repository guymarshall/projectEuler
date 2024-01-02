#![forbid(unsafe_code)]

use actix_web::{web, App, HttpResponse, HttpServer};
use problems::{
    even_fibonacci_numbers, find_10001st_prime, largest_palindrome_product, largest_prime_factor,
    largest_product_in_a_series, multiples_of_3_or_5, smallest_multiple,
    special_pythagorean_triplet, sum_square_difference, summation_of_primes,
};

mod problems;

async fn problem(info: web::Path<u32>) -> HttpResponse {
    match info.into_inner() {
        1 => HttpResponse::Ok().body(multiples_of_3_or_5()),
        2 => HttpResponse::Ok().body(even_fibonacci_numbers()),
        3 => HttpResponse::Ok().body(largest_prime_factor()),
        4 => HttpResponse::Ok().body(largest_palindrome_product()),
        5 => HttpResponse::Ok().body(smallest_multiple()),
        6 => HttpResponse::Ok().body(sum_square_difference()),
        7 => HttpResponse::Ok().body(find_10001st_prime()),
        8 => HttpResponse::Ok().body(largest_product_in_a_series()),
        9 => HttpResponse::Ok().body(special_pythagorean_triplet()),
        10 => HttpResponse::Ok().body(summation_of_primes()),
        _ => HttpResponse::NotFound().body("Page not found"),
    }
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| App::new().route("/{number}", web::get().to(problem)))
        .bind("127.0.0.1:8080")?
        .run()
        .await
}

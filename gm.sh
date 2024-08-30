#!/bin/bash

# Fungsi untuk menghasilkan email acak
generate_random_email() {
    local domain="gmail.com"
    local length=10
    local letters="abcdefghijklmnopqrstuvwxyz0123456789"
    local username=""
    
    for ((i=0; i<$length; i++)); do
        username="$username${letters:RANDOM%${#letters}:1}"
    done
    
    echo "$username@$domain"
}

# Fungsi untuk menghasilkan password acak
generate_random_password() {
    local length=12
    local chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#\$%^&*()-_+=<>?"
    local password=""
    
    for ((i=0; i<$length; i++)); do
        password="$password${chars:RANDOM%${#chars}:1}"
    done
    
    echo "$password"
}

# Menghasilkan 5 pasang email dan password acak
for i in {1..5}; do
    email=$(generate_random_email)
    password=$(generate_random_password)
    echo "Email: $email, Password: $password"
done

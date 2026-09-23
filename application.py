```python
from flask import Flask, render_template_string, jsonify
from datetime import datetime
import os

# Your GitHub repository
GITHUB_REPO_URL = "https://github.com/dahanayakas/web-app"

application = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>LUXORA | Modern Fashion</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }

        .hero-gradient {
            background: linear-gradient(135deg, #111827 0%, #374151 50%, #111827 100%);
        }

        .product-card {
            transition: transform 0.25s ease, box-shadow 0.25s ease;
        }

        .product-card:hover {
            transform: translateY(-6px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        }

        .product-image {
            transition: transform 0.4s ease;
        }

        .product-card:hover .product-image {
            transform: scale(1.05);
        }
    </style>

    <script>
        let cartCount = 0;

        function addToCart(name) {
            cartCount++;
            document.getElementById("cart-count").textContent = cartCount;

            alert(name + " added to your shopping bag!");
        }

        function toggleWishlist(button) {
            if (button.textContent === "♡") {
                button.textContent = "♥";
                button.classList.add("text-red-500");
            } else {
                button.textContent = "♡";
                button.classList.remove("text-red-500");
            }
        }

        function searchProducts() {
            const search = document.getElementById("search").value.toLowerCase();
            const products = document.querySelectorAll(".product-card");

            products.forEach(product => {
                const name = product.dataset.name.toLowerCase();

                if (name.includes(search)) {
                    product.style.display = "";
                } else {
                    product.style.display = "none";
                }
            });
        }
    </script>
</head>

<body class="bg-gray-50 text-gray-900">

<!-- NAVIGATION -->
<nav class="bg-white shadow-sm sticky top-0 z-50">

    <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">

        <div class="flex items-center space-x-10">

            <h1 class="text-3xl font-black tracking-widest">
                LUXORA
            </h1>

            <div class="hidden md:flex space-x-7 text-sm font-semibold">

                <a href="#new" class="hover:text-gray-500">
                    NEW ARRIVALS
                </a>

                <a href="#women" class="hover:text-gray-500">
                    WOMEN
                </a>

                <a href="#men" class="hover:text-gray-500">
                    MEN
                </a>

                <a href="#accessories" class="hover:text-gray-500">
                    ACCESSORIES
                </a>

            </div>

        </div>

        <div class="flex items-center space-x-5">

            <input
                id="search"
                onkeyup="searchProducts()"
                type="text"
                placeholder="Search..."
                class="hidden md:block border rounded-full px-4 py-2 text-sm w-48 focus:outline-none"
            >

            <button class="text-2xl">
                ♡
            </button>

            <button class="relative text-2xl">
                🛍️

                <span
                    id="cart-count"
                    class="absolute -top-2 -right-2 bg-black text-white text-xs rounded-full h-5 w-5 flex items-center justify-center"
                >
                    0
                </span>

            </button>

        </div>

    </div>

</nav>


<!-- HERO -->

<section class="hero-gradient text-white">

    <div class="max-w-7xl mx-auto px-6 py-24">

        <div class="max-w-2xl">

            <p class="uppercase tracking-[0.3em] text-sm mb-5 text-gray-300">
                LUXORA COLLECTION 2026
            </p>

            <h2 class="text-5xl md:text-7xl font-black leading-tight">
                STYLE THAT
                <span class="text-gray-300">
                    DEFINES YOU.
                </span>
            </h2>

            <p class="mt-6 text-gray-300 text-lg max-w-xl">
                Discover premium fashion designed for people
                who want to look confident, modern and unforgettable.
            </p>

            <div class="mt-8">

                <a
                    href="#new"
                    class="inline-block bg-white text-black px-8 py-4 font-bold rounded-full hover:bg-gray-200 transition"
                >
                    SHOP NEW COLLECTION
                </a>

            </div>

        </div>

    </div>

</section>


<!-- CATEGORIES -->

<section class="max-w-7xl mx-auto px-6 py-14">

    <div class="text-center mb-10">

        <p class="text-sm tracking-widest text-gray-500">
            EXPLORE
        </p>

        <h2 class="text-3xl font-bold mt-2">
            SHOP BY CATEGORY
        </h2>

    </div>

    <div class="grid md:grid-cols-3 gap-6">

        <div class="bg-gray-900 text-white p-10 rounded-xl">
            <p class="text-sm text-gray-400">
                COLLECTION
            </p>
            <h3 class="text-3xl font-bold mt-2">
                WOMEN
            </h3>
            <button class="mt-6 underline">
                SHOP NOW →
            </button>
        </div>

        <div class="bg-gray-200 p-10 rounded-xl">
            <p class="text-sm text-gray-500">
                COLLECTION
            </p>
            <h3 class="text-3xl font-bold mt-2">
                MEN
            </h3>
            <button class="mt-6 underline">
                SHOP NOW →
            </button>
        </div>

        <div class="bg-gray-100 p-10 rounded-xl border">
            <p class="text-sm text-gray-500">
                COLLECTION
            </p>
            <h3 class="text-3xl font-bold mt-2">
                ACCESSORIES
            </h3>
            <button class="mt-6 underline">
                SHOP NOW →
            </button>
        </div>

    </div>

</section>


<!-- PRODUCTS -->

<section id="new" class="max-w-7xl mx-auto px-6 py-12">

    <div class="flex justify-between items-end mb-8">

        <div>
            <p class="text-sm tracking-widest text-gray-500">
                LUXORA
            </p>

            <h2 class="text-4xl font-black mt-2">
                NEW ARRIVALS
            </h2>
        </div>

        <a href="#" class="text-sm font-bold underline">
            VIEW ALL
        </a>

    </div>


    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-7">


        <!-- PRODUCT 1 -->

        <div class="product-card bg-white rounded-xl overflow-hidden"
             data-name="Premium Black Jacket">

            <div class="bg-gray-200 h-72 flex items-center justify-center overflow-hidden">

                <div class="product-image text-8xl">
                    🧥
                </div>

            </div>

            <div class="p-5">

                <div class="flex justify-between">

                    <div>
                        <h3 class="font-bold">
                            Premium Black Jacket
                        </h3>

                        <p class="text-gray-500 text-sm mt-1">
                            Men's Collection
                        </p>
                    </div>

                    <button
                        onclick="toggleWishlist(this)"
                        class="text-2xl"
                    >
                        ♡
                    </button>

                </div>

                <div class="flex justify-between items-center mt-5">

                    <span class="font-bold text-lg">
                        $89.00
                    </span>

                    <button
                        onclick="addToCart('Premium Black Jacket')"
                        class="bg-black text-white px-4 py-2 rounded-full text-sm"
                    >
                        ADD
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 2 -->

        <div class="product-card bg-white rounded-xl overflow-hidden"
             data-name="Classic White Shirt">

            <div class="bg-gray-100 h-72 flex items-center justify-center overflow-hidden">

                <div class="product-image text-8xl">
                    👔
                </div>

            </div>

            <div class="p-5">

                <div class="flex justify-between">

                    <div>
                        <h3 class="font-bold">
                            Classic White Shirt
                        </h3>

                        <p class="text-gray-500 text-sm mt-1">
                            Men's Collection
                        </p>
                    </div>

                    <button
                        onclick="toggleWishlist(this)"
                        class="text-2xl"
                    >
                        ♡
                    </button>

                </div>

                <div class="flex justify-between items-center mt-5">

                    <span class="font-bold text-lg">
                        $49.00
                    </span>

                    <button
                        onclick="addToCart('Classic White Shirt')"
                        class="bg-black text-white px-4 py-2 rounded-full text-sm"
                    >
                        ADD
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 3 -->

        <div class="product-card bg-white rounded-xl overflow-hidden"
             data-name="Luxury Summer Dress">

            <div class="bg-gray-200 h-72 flex items-center justify-center overflow-hidden">

                <div class="product-image text-8xl">
                    👗
                </div>

            </div>

            <div class="p-5">

                <div class="flex justify-between">

                    <div>
                        <h3 class="font-bold">
                            Luxury Summer Dress
                        </h3>

                        <p class="text-gray-500 text-sm mt-1">
                            Women's Collection
                        </p>
                    </div>

                    <button
                        onclick="toggleWishlist(this)"
                        class="text-2xl"
                    >
                        ♡
                    </button>

                </div>

                <div class="flex justify-between items-center mt-5">

                    <span class="font-bold text-lg">
                        $79.00
                    </span>

                    <button
                        onclick="addToCart('Luxury Summer Dress')"
                        class="bg-black text-white px-4 py-2 rounded-full text-sm"
                    >
                        ADD
                    </button>

                </div>

            </div>

        </div>


        <!-- PRODUCT 4 -->

        <div class="product-card bg-white rounded-xl overflow-hidden"
             data-name="Urban Street Sneakers">

            <div class="bg-gray-100 h-72 flex items-center justify-center overflow-hidden">

                <div class="product-image text-8xl">
                    👟
                </div>

            </div>

            <div class="p-5">

                <div class="flex justify-between">

                    <div>
                        <h3 class="font-bold">
                            Urban Street Sneakers
                        </h3>

                        <p class="text-gray-500 text-sm mt-1">
                            Footwear
                        </p>
                    </div>

                    <button
                        onclick="toggleWishlist(this)"
                        class="text-2xl"
                    >
                        ♡
                    </button>

                </div>

                <div class="flex justify-between items-center mt-5">

                    <span class="font-bold text-lg">
                        $99.00
                    </span>

                    <button
                        onclick="addToCart('Urban Street Sneakers')"
                        class="bg-black text-white px-4 py-2 rounded-full text-sm"
                    >
                        ADD
                    </button>

                </div>

            </div>

        </div>

    </div>

</section>


<!-- PROMOTION -->

<section class="bg-black text-white mt-16">

    <div class="max-w-7xl mx-auto px-6 py-20 text-center">

        <p class="text-gray-400 tracking-widest text-sm">
            LUXORA MEMBERS
        </p>

        <h2 class="text-4xl md:text-5xl font-black mt-4">
            GET 15% OFF YOUR FIRST ORDER
        </h2>

        <p class="text-gray-400 mt-5">
            Join our fashion community and receive exclusive
            collections, offers and early access.
        </p>

        <button class="mt-8 bg-white text-black px-8 py-4 rounded-full font-bold">
            JOIN LUXORA
        </button>

    </div>

</section>


<!-- AWS STATUS -->

<footer class="bg-gray-950 text-gray-400">

    <div class="max-w-7xl mx-auto px-6 py-12">

        <div class="grid md:grid-cols-3 gap-10">

            <div>

                <h2 class="text-white text-2xl font-black tracking-widest">
                    LUXORA
                </h2>

                <p class="mt-4 text-sm">
                    Modern fashion. Premium quality.
                    Designed for your lifestyle.
                </p>

            </div>


            <div>

                <h3 class="text-white font-bold">
                    CUSTOMER SERVICE
                </h3>

                <p class="mt-4 text-sm">
                    Contact Us
                </p>

                <p class="mt-2 text-sm">
                    Shipping & Returns
                </p>

                <p class="mt-2 text-sm">
                    Size Guide
                </p>

            </div>


            <div>

                <h3 class="text-white font-bold">
                    CLOUD PLATFORM
                </h3>

                <p class="mt-4 text-sm">
                    AWS Region:
                    {{ aws_region }}
                </p>

                <p class="mt-2 text-sm">
                    Environment:
                    {{ env_name }}
                </p>

                <p class="mt-2 text-green-400">
                    ● ONLINE
                </p>

            </div>

        </div>


        <div class="border-t border-gray-800 mt-10 pt-6 flex flex-col md:flex-row justify-between text-xs">

            <p>
                © 2026 LUXORA. All rights reserved.
            </p>

            <div class="space-x-5 mt-3 md:mt-0">

                <a href="{{ github_url }}"
                   target="_blank"
                   class="hover:text-white">
                    GitHub
                </a>

                <a href="/health"
                   class="hover:text-white">
                    System Health
                </a>

            </div>

        </div>

    </div>

</footer>

</body>
</html>
"""


@application.route('/')
def home():

    now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    env_name = os.environ.get(
        'AWS_EB_ENVIRONMENT_NAME',
        'LOCAL_DEBUG'
    )

    aws_region = os.environ.get(
        'AWS_REGION',
        'us-east-1'
    )

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        github_url=GITHUB_REPO_URL,
        env_name=env_name,
        aws_region=aws_region
    )


@application.route('/health')
def health_check():

    return jsonify({
        "status": "nominal",
        "service": "LUXORA Fashion Store",
        "version": "1.0",
        "timestamp_utc": datetime.utcnow().isoformat()
    }), 200


if __name__ == '__main__':

    application.run(
        host='0.0.0.0',
        port=5000
    )
```

from flask import Flask, jsonify, request
from flask_cors import CORS  # Add this import

app = Flask(__name__)
CORS(app)  # Enable CORS for the app

# In-memory data to simulate the database
users_data = {
    1: "John Doe",
    2: "Jane Doe",
    3: "Rachel Young",
    4: "Alice Smith",
    5: "Bob Johnson",
    6: "Charlie Brown",
    7: "Edward Davis",
    8: "Fiona Miller",
    9: "George Wilson",
}

posts_data = [
    {"id": 246, "userid": 1, "content": "Post about ant", "comments": 5},
    {"id": 161, "userid": 1, "content": "Post about elephant", "comments": 10},
    {"id": 150, "userid": 1, "content": "Post about ocean", "comments": 3},
    {"id": 370, "userid": 1, "content": "Post about monkey", "comments": 8},
    {"id": 344, "userid": 1, "content": "Post about ocean", "comments": 12},
    {"id": 952, "userid": 1, "content": "Post about zebra", "comments": 15},
    {"id": 647, "userid": 1, "content": "Post about igloo", "comments": 2},
    {"id": 421, "userid": 1, "content": "Post about house", "comments": 7},
    {"id": 890, "userid": 1, "content": "Post about bat", "comments": 6},
    {"id": 461, "userid": 1, "content": "Post about umbrella", "comments": 1}
]

# Registration API (updated with new access code)
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()

    # Updated access code
    if data["accessCode"] != "eNLdvc":
        return jsonify({"message": "Given access code is invalid"}), 400
    
    return jsonify({"message": "Registration successful"}), 200


# Top Users API: Top 5 users
@app.route('/api/top-users', methods=['GET'])
def top_users():
    top_5_users = {k: users_data[k] for k in list(users_data.keys())[:5]}
    return jsonify({"top_users": top_5_users})


# Trending Posts API: Posts with the most comments
@app.route('/api/trending-posts', methods=['GET'])
def trending_posts():
    sorted_posts = sorted(posts_data, key=lambda x: x['comments'], reverse=True)
    highest_comments = sorted_posts[0]['comments']
    trending_posts = [post for post in sorted_posts if post['comments'] == highest_comments]
    return jsonify({"trending_posts": trending_posts})


# Feed API: Display the latest posts (newest first)
@app.route('/api/feed', methods=['GET'])
def feed():
    latest_posts = sorted(posts_data, key=lambda x: x['id'], reverse=True)
    return jsonify({"feed": latest_posts})

if __name__ == '__main__':
    app.run(debug=True)

import json

# Updated points per project
PROJECT_POINTS = {
    "libft": 42, "gnl": 84, "ft_prinf": 84, "b2br": 126, "push_swap": 292,
    "pipex": 268, "minitalk": 268, "so_long": 242, "fdf": 242, "fract-ol": 242,
    "philosophers": 342, "minishell": 322, "netpractice": 292, "cub3d": 392, "miniRT": 392,
    "CPP M 00": 0, "CPP M 01": 0, "CPP M 02": 0, "CPP M 03": 0, "CPP M 04": 336,
    "CPP M 05": 0, "CPP M 06": 0, "CPP M 07": 0, "CPP M 08": 0, "CPP M 09": 422,
    "Inseption": 402, "webserv": 462, "ft_irc": 442, "ft_transcendence": 500,
    "Piscine Django": 3090, "Cloud-1": 3132, "darkley": 3132, "snow-crash": 3132
}

# Load the JSON file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Update points for each user and sum total house points
total_house_points = 0
for username, user_data in data["users"].items():
    total_user_points = sum(PROJECT_POINTS.get(proj, 0) for proj, completed in user_data["projects"].items() if completed)
    user_data["points"] = total_user_points
    total_house_points += total_user_points

# Update total house points
data["total_points"] = total_house_points

# Save back to JSON
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("✅ Points updated successfully!")

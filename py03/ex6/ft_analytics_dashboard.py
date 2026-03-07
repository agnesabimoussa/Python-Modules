if __name__ == "__main__":
    # sample data
    data = {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5,
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2,
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7,
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4,
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7,
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1,
            },
        },
        'sessions': [
            {
                'player': 'bob',
                'duration_minutes': 94,
                'score': 1831,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 32,
                'score': 1478,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 17,
                'score': 1570,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 98,
                'score': 1981,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 15,
                'score': 2361,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 29,
                'score': 2985,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 34,
                'score': 1285,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'alice',
                'duration_minutes': 53,
                'score': 1238,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 1555,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 92,
                'score': 2754,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 98,
                'score': 1102,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 39,
                'score': 2721,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 46,
                'score': 329,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 56,
                'score': 1196,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 117,
                'score': 1388,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'diana',
                'duration_minutes': 118,
                'score': 2733,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 22,
                'score': 1110,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'frank',
                'duration_minutes': 79,
                'score': 1854,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'charlie',
                'duration_minutes': 33,
                'score': 666,
                'mode': 'ranked',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 101,
                'score': 292,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 25,
                'score': 2887,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'diana',
                'duration_minutes': 53,
                'score': 2540,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'eve',
                'duration_minutes': 115,
                'score': 147,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'frank',
                'duration_minutes': 118,
                'score': 2299,
                'mode': 'competitive',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 42,
                'score': 1880,
                'mode': 'casual',
                'completed': False,
            },
            {
                'player': 'alice',
                'duration_minutes': 97,
                'score': 1178,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 18,
                'score': 2661,
                'mode': 'competitive',
                'completed': True,
            },
            {
                'player': 'bob',
                'duration_minutes': 52,
                'score': 761,
                'mode': 'ranked',
                'completed': True,
            },
            {
                'player': 'eve',
                'duration_minutes': 46,
                'score': 2101,
                'mode': 'casual',
                'completed': True,
            },
            {
                'player': 'charlie',
                'duration_minutes': 117,
                'score': 1359,
                'mode': 'casual',
                'completed': True,
            },
        ],
        'game_modes': [
            'casual',
            'competitive',
            'ranked',
        ],
        'achievements': [
            'first_blood',
            'level_master',
            'speed_runner',
            'treasure_seeker',
            'boss_hunter',
            'pixel_perfect',
            'combo_king',
            'explorer',
        ],
    }

    print("=== Game Analytics Dashboard ===\n")

    # === List Comprehension Examples ===
    print("=== List Comprehension Examples ===")
    # high scorers (> 2000)
    high_scorers = [name for name, p in data['players'].items() if p['total_score'] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    # doubled scores list (for a sample transformation)
    doubled_scores = [p['total_score'] * 2 for p in data['players'].values()]
    print(f"Scores doubled: {doubled_scores[:4]}")
    # active players (played >= 1 session)
    active_players = [name for name, p in data['players'].items() if p['sessions_played'] > 0]
    print(f"Active players: {active_players}")

    # === Dict Comprehension Examples ===
    print("=== Dict Comprehension Examples ===")
    # player -> total_score mapping
    player_scores = {name: p['total_score'] for name, p in data['players'].items()}
    print(f"Player scores: {player_scores}")
    # score categories (simple high/medium/low by thresholds)
    def score_category(score: int) -> str:
        if score >= 5000:
            return 'high'
        if score >= 2000:
            return 'medium'
        return 'low'
    categories = {name: score_category(score) for name, score in player_scores.items()}
    # count categories using dict comprehesions + sum allowed in ex6
    category_counts = {cat: sum(1 for c in categories.values() if c == cat) for cat in {'high', 'medium', 'low'}}
    print(f"Score categories: {category_counts}")
    # achievement counts mapping
    ach_counts = {name: p['achievements_count'] for name, p in data['players'].items()}
    print(f"Achievement counts: {ach_counts}")

    # === Set Comprehension Examples ===
    print("=== Set Comprehension Examples ===")
    unique_players = {s['player'] for s in data['sessions']}
    print(f"Unique players: {unique_players}")
    unique_achievements = {a for a in data['achievements']}
    print(f"Unique achievements: {unique_achievements}")
    active_modes = {s['mode'] for s in data['sessions'] if s['completed']}
    print(f"Active modes (completed sessions): {active_modes}")

    # === Combined Analysis ===
    print("=== Combined Analysis ===")
    total_players = len(data['players'])
    total_unique_ach = len(unique_achievements)
    avg_score = sum(player_scores.values()) / total_players if total_players else 0
    # top performer by total_score
    top_name = sorted(player_scores.items(), key=lambda kv: kv[1], reverse=True)[0][0]
    top_perf = f"{top_name} ({player_scores[top_name]} points, {ach_counts[top_name]} achievements)"
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_ach}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_perf}")

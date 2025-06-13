import json
import datetime
from typing import Dict, List, Tuple

class CryptoInvestmentBot:
    def __init__(self):
        self.name = "CryptoWise AI"
        self.conversation_state = "greeting"
        self.user_profile = {
            "risk_tolerance": None,  # low, medium, high
            "investment_amount": None,
            "time_horizon": None,  # short, medium, long
            "sustainability_preference": None  # low, medium, high
        }

        # Predefined cryptocurrency dataset with updated environmental scores and rising trends
        self.crypto_data = {
            "bitcoin": {
                "symbol": "BTC",
                "current_price": 68500,
                "price_change_24h": 3.5,
                "price_change_7d": 5.8,
                "price_change_30d": 12.2,
                "market_cap": 1350000000000,
                "volume_24h": 25200000000,
                "energy_efficiency_score": 3,
                "environmental_score": 2, # Low due to Proof-of-Work
                "sustainability_rating": "Low",
                "environmental_rating": "Poor",
                "project_viability": 9,
                "adoption_score": 10,
                "technology_score": 8,
                "team_score": 9
            },
            "ethereum": {
                "symbol": "ETH",
                "current_price": 3850,
                "price_change_24h": 4.2,
                "price_change_7d": 8.1,
                "price_change_30d": 15.7,
                "market_cap": 462000000000,
                "volume_24h": 12500000000,
                "energy_efficiency_score": 9, # Post-merge Proof-of-Stake
                "environmental_score": 9,
                "sustainability_rating": "High",
                "environmental_rating": "Excellent",
                "project_viability": 9,
                "adoption_score": 9,
                "technology_score": 10,
                "team_score": 9
            },
            "cardano": {
                "symbol": "ADA",
                "current_price": 0.82,
                "price_change_24h": 2.1,
                "price_change_7d": 6.3,
                "price_change_30d": 18.5,
                "market_cap": 29000000000,
                "volume_24h": 850000000,
                "energy_efficiency_score": 9,
                "environmental_score": 9,
                "sustainability_rating": "High",
                "environmental_rating": "Excellent",
                "project_viability": 8,
                "adoption_score": 7,
                "technology_score": 8,
                "team_score": 8
            },
            "polygon": {
                "symbol": "MATIC",
                "current_price": 1.15,
                "price_change_24h": 5.7,
                "price_change_7d": 12.4,
                "price_change_30d": 25.2,
                "market_cap": 11500000000,
                "volume_24h": 720000000,
                "energy_efficiency_score": 8,
                "environmental_score": 8,
                "sustainability_rating": "High",
                "environmental_rating": "Good",
                "project_viability": 8,
                "adoption_score": 8,
                "technology_score": 9,
                "team_score": 7
            },
            "solana": {
                "symbol": "SOL",
                "current_price": 172.50,
                "price_change_24h": 6.8,
                "price_change_7d": 14.2,
                "price_change_30d": 28.9,
                "market_cap": 79000000000,
                "volume_24h": 2800000000,
                "energy_efficiency_score": 8,
                "environmental_score": 8,
                "sustainability_rating": "High",
                "environmental_rating": "Good",
                "project_viability": 8,
                "adoption_score": 8,
                "technology_score": 9,
                "team_score": 7
            }
        }

        print(f"🤖 Hello! I'm {self.name}, your cryptocurrency investment advisor.")
        print("I analyze crypto data based on profitability and sustainability to help you make informed decisions.")
        print("\nLet's start by getting to know your investment preferences...")

    def analyze_profitability(self, crypto_name: str) -> Dict:
        """Analyze profitability based on price trends"""
        data = self.crypto_data[crypto_name]

        # Profitability scoring logic
        score = 0
        signals = []

        # Short-term trend (24h)
        if data["price_change_24h"] > 5:
            score += 3
            signals.append("Strong 24h growth")
        elif data["price_change_24h"] > 0:
            score += 1
            signals.append("Positive 24h trend")
        elif data["price_change_24h"] < -5:
            score -= 2
            signals.append("Weak 24h performance")

        # Medium-term trend (7d)
        if data["price_change_7d"] > 10:
            score += 3
            signals.append("Excellent weekly performance")
        elif data["price_change_7d"] > 0:
            score += 2
            signals.append("Positive weekly trend")
        elif data["price_change_7d"] < -10:
            score -= 3
            signals.append("Poor weekly performance")

        # Long-term trend (30d)
        if data["price_change_30d"] > 20:
            score += 4
            signals.append("Outstanding monthly growth")
        elif data["price_change_30d"] > 10:
            score += 3
            signals.append("Strong monthly performance")
        elif data["price_change_30d"] > 0:
            score += 1
            signals.append("Positive monthly trend")
        elif data["price_change_30d"] < -20:
            score -= 4
            signals.append("Concerning monthly decline")

        # Volume analysis
        market_cap = data["market_cap"]
        volume_24h = data["volume_24h"]
        volume_ratio = volume_24h / market_cap if market_cap > 0 else 0

        if volume_ratio > 0.1:
            score += 2
            signals.append("High trading activity")
        elif volume_ratio > 0.05:
            score += 1
            signals.append("Good trading volume")
        elif volume_ratio < 0.01:
            score -= 1
            signals.append("Low trading volume")

        # Determine profitability rating
        if score >= 8:
            rating = "Excellent"
        elif score >= 5:
            rating = "Good"
        elif score >= 2:
            rating = "Moderate"
        elif score >= -2:
            rating = "Poor"
        else:
            rating = "Very Poor"

        return {
            "score": score,
            "rating": rating,
            "signals": signals,
            "recommendation": self._get_profitability_recommendation(score)
        }

    def analyze_sustainability(self, crypto_name: str) -> Dict:
        """Analyze sustainability based on environmental factors and project viability"""
        data = self.crypto_data[crypto_name]

        score = 0
        factors = []

        # Environmental Score (40% weight)
        environmental_score = data["environmental_score"]
        if environmental_score >= 8:
            score += 4
            factors.append("Excellent environmental rating")
        elif environmental_score >= 6:
            score += 2
            factors.append("Good environmental rating")
        elif environmental_score >= 4:
            score += 1
            factors.append("Moderate environmental rating")
        else:
            score -= 2
            factors.append("Poor environmental rating")

        # Project viability (30% weight)
        viability_score = data["project_viability"]
        if viability_score >= 8:
            score += 3
            factors.append("Strong project fundamentals")
        elif viability_score >= 6:
            score += 2
            factors.append("Solid project foundation")
        elif viability_score >= 4:
            score += 1
            factors.append("Moderate project strength")
        else:
            score -= 1
            factors.append("Weak project fundamentals")

        # Technology and adoption (30% weight)
        tech_adoption_avg = (data["technology_score"] + data["adoption_score"]) / 2
        if tech_adoption_avg >= 8:
            score += 3
            factors.append("Advanced technology with strong adoption")
        elif tech_adoption_avg >= 6:
            score += 2
            factors.append("Good technology and adoption balance")
        elif tech_adoption_avg >= 4:
            score += 1
            factors.append("Developing technology and adoption")
        else:
            factors.append("Limited technology adoption")

        # Determine sustainability rating
        if score >= 8:
            rating = "Highly Sustainable"
        elif score >= 5:
            rating = "Sustainable"
        elif score >= 2:
            rating = "Moderately Sustainable"
        else:
            rating = "Low Sustainability"

        return {
            "score": score,
            "rating": rating,
            "factors": factors,
            "recommendation": self._get_sustainability_recommendation(score)
        }

    def _get_profitability_recommendation(self, score: int) -> str:
        """Get profitability-based recommendation"""
        if score >= 8:
            return "Strong buy signal - excellent profit potential"
        elif score >= 5:
            return "Buy signal - good profit potential"
        elif score >= 2:
            return "Hold or small position - moderate potential"
        elif score >= -2:
            return "Caution advised - limited profit potential"
        else:
            return "Avoid - high risk of losses"

    def _get_sustainability_recommendation(self, score: int) -> str:
        """Get sustainability-based recommendation"""
        if score >= 8:
            return "Excellent long-term investment choice"
        elif score >= 5:
            return "Good sustainable investment option"
        elif score >= 2:
            return "Acceptable for ESG-conscious investors"
        else:
            return "Not recommended for sustainability-focused portfolios"

    def get_personalized_recommendation(self, crypto_name: str) -> Dict:
        """Generate personalized recommendation based on user profile"""
        profitability = self.analyze_profitability(crypto_name)
        sustainability = self.analyze_sustainability(crypto_name)

        # Weight factors based on user preferences
        profit_weight = 0.7 if self.user_profile.get("sustainability_preference") == "low" else 0.5
        sustain_weight = 1 - profit_weight

        # Calculate weighted score
        weighted_score = (profitability["score"] * profit_weight + 
                          sustainability["score"] * sustain_weight)

        # Risk adjustment
        risk_tolerance = self.user_profile.get("risk_tolerance", "medium")
        if risk_tolerance == "low":
            # Penalize volatile options
            if self.crypto_data[crypto_name]["price_change_7d"] > 15 or self.crypto_data[crypto_name]["price_change_7d"] < -15:
                weighted_score -= 2
        elif risk_tolerance == "high":
            # Bonus for high-growth potential
            if self.crypto_data[crypto_name]["price_change_30d"] > 20:
                weighted_score += 1

        # Generate final recommendation
        if weighted_score >= 7:
            final_rec = "Highly Recommended"
        elif weighted_score >= 4:
            final_rec = "Recommended"
        elif weighted_score >= 1:
            final_rec = "Consider with Caution"
        else:
            final_rec = "Not Recommended"

        return {
            "crypto": crypto_name.title(),
            "symbol": self.crypto_data[crypto_name]["symbol"],
            "profitability": profitability,
            "sustainability": sustainability,
            "weighted_score": round(weighted_score, 2),
            "final_recommendation": final_rec,
            "investment_advice": self._generate_investment_advice(crypto_name, weighted_score)
        }

    def _generate_investment_advice(self, crypto_name: str, score: float) -> str:
        """Generate specific investment advice"""
        data = self.crypto_data[crypto_name]
        advice = []

        # Position sizing advice
        risk_tolerance = self.user_profile.get("risk_tolerance", "medium")
        if score >= 7 and risk_tolerance == "high":
            advice.append("Consider a 15-25% portfolio allocation")
        elif score >= 4:
            advice.append("Consider a 5-15% portfolio allocation")
        elif score >= 1:
            advice.append("Consider a small 2-5% portfolio allocation")
        else:
            advice.append("Avoid or minimal exposure (<2%)")

        # Timing advice
        if data["price_change_24h"] < -3:
            advice.append("Current dip may present buying opportunity")
        elif data["price_change_24h"] > 5:
            advice.append("Consider dollar-cost averaging due to recent gains")

        # Time horizon advice
        time_horizon = self.user_profile.get("time_horizon", "medium")
        if time_horizon == "long" and self.crypto_data[crypto_name]["project_viability"] >= 8:
            advice.append("Well-suited for long-term holding strategy")
        elif time_horizon == "short":
            advice.append("Monitor closely for short-term trading opportunities")

        return " | ".join(advice)

    def chat(self):
        """Main chat interface"""
        while True:
            if self.conversation_state == "greeting":
                self._handle_greeting()
            elif self.conversation_state == "profile_setup":
                self._handle_profile_setup()
            elif self.conversation_state == "main_menu":
                self._handle_main_menu()
            elif self.conversation_state == "analysis":
                self._handle_analysis()
            elif self.conversation_state == "exit":
                print("\n🤖 Thank you for using CryptoWise AI! Happy investing! 📈")
                break

    def _handle_greeting(self):
        """Handle initial greeting and move to profile setup"""
        self.conversation_state = "profile_setup"
        self._collect_user_profile()

    def _collect_user_profile(self):
        """Collect user investment profile"""
        print("\n" + "="*50)
        print("📋 INVESTMENT PROFILE SETUP")
        print("="*50)

        # Risk tolerance
        print("\n1. What's your risk tolerance?")
        print("   a) Low - I prefer stable, safer investments")
        print("   b) Medium - I can handle some volatility")
        print("   c) High - I'm comfortable with high-risk, high-reward")

        risk_choice = input("\nYour choice (a/b/c): ").lower().strip()
        risk_map = {"a": "low", "b": "medium", "c": "high"}
        self.user_profile["risk_tolerance"] = risk_map.get(risk_choice, "medium")

        # Investment amount
        print("\n2. What's your approximate investment amount?")
        print("   a) Under $1,000")
        print("   b) $1,000 - $10,000") 
        print("   c) Over $10,000")

        amount_choice = input("\nYour choice (a/b/c): ").lower().strip()
        amount_map = {"a": "small", "b": "medium", "c": "large"}
        self.user_profile["investment_amount"] = amount_map.get(amount_choice, "medium")

        # Time horizon
        print("\n3. What's your investment time horizon?")
        print("   a) Short-term (weeks to months)")
        print("   b) Medium-term (months to 1-2 years)")
        print("   c) Long-term (2+ years)")

        time_choice = input("\nYour choice (a/b/c): ").lower().strip()
        time_map = {"a": "short", "b": "medium", "c": "long"}
        self.user_profile["time_horizon"] = time_map.get(time_choice, "medium")

        # Sustainability preference
        print("\n4. How important is sustainability/environmental impact?")
        print("   a) Not important - I focus purely on profits")
        print("   b) Somewhat important - I consider it alongside profits")
        print("   c) Very important - It's a key factor in my decisions")

        sustain_choice = input("\nYour choice (a/b/c): ").lower().strip()
        sustain_map = {"a": "low", "b": "medium", "c": "high"}
        self.user_profile["sustainability_preference"] = sustain_map.get(sustain_choice, "medium")

        print(f"\n✅ Profile setup complete! Moving to main menu...")
        self.conversation_state = "main_menu"

    def _handle_main_menu(self):
        """Handle main menu interactions"""
        print("\n" + "="*50)
        print("🚀 CRYPTOWISE AI - MAIN MENU")
        print("="*50)
        print("What would you like to do?")
        print("1. Analyze a specific cryptocurrency")
        print("2. Get top recommendations for my profile")
        print("3. Compare multiple cryptocurrencies")
        print("4. View market overview")
        print("5. Update my investment profile")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            self._analyze_specific_crypto()
        elif choice == "2":
            self._get_top_recommendations()
        elif choice == "3":
            self._compare_cryptocurrencies()
        elif choice == "4":
            self._show_market_overview()
        elif choice == "5":
            self._collect_user_profile()
        elif choice == "6":
            self.conversation_state = "exit"
        else:
            print("❌ Invalid choice. Please try again.")

    def _analyze_specific_crypto(self):
        """Analyze a specific cryptocurrency"""
        print("\n📊 Available cryptocurrencies:")
        for i, crypto in enumerate(self.crypto_data.keys(), 1):
            symbol = self.crypto_data[crypto]["symbol"]
            price = self.crypto_data[crypto]["current_price"]
            print(f"{i}. {crypto.title()} ({symbol}) - ${price:,.2f}")

        try:
            choice = int(input(f"\nSelect cryptocurrency (1-{len(self.crypto_data)}): "))
            crypto_list = list(self.crypto_data.keys())

            if 1 <= choice <= len(crypto_list):
                selected_crypto = crypto_list[choice - 1]
                recommendation = self.get_personalized_recommendation(selected_crypto)
                self._display_detailed_analysis(recommendation)
            else:
                print("❌ Invalid selection.")
        except ValueError:
            print("❌ Please enter a valid number.")

    def _display_detailed_analysis(self, rec: Dict):
        """Display detailed analysis results"""
        print("\n" + "="*60)
        print(f"📈 DETAILED ANALYSIS: {rec['crypto']} ({rec['symbol']})")
        print("="*60)

        # Current data
        crypto_data = self.crypto_data[rec['crypto'].lower()]
        print(f"💰 Current Price: ${crypto_data['current_price']:,.2f}")
        print(f"📊 24h Change: {crypto_data['price_change_24h']:+.1f}%")
        print(f"📊 7d Change: {crypto_data['price_change_7d']:+.1f}%")
        print(f"📊 30d Change: {crypto_data['price_change_30d']:+.1f}%")
        print(f"🏛️ Market Cap: ${crypto_data['market_cap']:,.0f}")

        # Profitability Analysis
        print(f"\n🎯 PROFITABILITY ANALYSIS")
        print(f"Rating: {rec['profitability']['rating']} (Score: {rec['profitability']['score']}/10)")
        print(f"Signals: {', '.join(rec['profitability']['signals'])}")
        print(f"Recommendation: {rec['profitability']['recommendation']}")

        # Sustainability Analysis
        print(f"\n🌱 SUSTAINABILITY ANALYSIS")
        print(f"Rating: {rec['sustainability']['rating']} (Score: {rec['sustainability']['score']}/10)")
        print(f"Environmental Rating: {crypto_data['environmental_rating']}")
        print(f"Factors: {', '.join(rec['sustainability']['factors'])}")
        print(f"Recommendation: {rec['sustainability']['recommendation']}")

        # Final Recommendation
        print(f"\n⭐ FINAL RECOMMENDATION")
        print(f"Overall Score: {rec['weighted_score']}/10")
        print(f"Verdict: {rec['final_recommendation']}")
        print(f"Investment Advice: {rec['investment_advice']}")

        input("\nPress Enter to continue...")

    def _get_top_recommendations(self):
        """Get top recommendations based on user profile"""
        print("\n🏆 Analyzing all cryptocurrencies for your profile...")

        recommendations = []
        for crypto_name in self.crypto_data.keys():
            rec = self.get_personalized_recommendation(crypto_name)
            recommendations.append(rec)

        # Sort by weighted score
        recommendations.sort(key=lambda x: x['weighted_score'], reverse=True)

        print("\n" + "="*60)
        print("🎯 TOP RECOMMENDATIONS FOR YOUR PROFILE")
        print("="*60)

        for i, rec in enumerate(recommendations[:3], 1):
            crypto_data = self.crypto_data[rec['crypto'].lower()]
            print(f"\n{i}. {rec['crypto']} ({rec['symbol']})")
            print(f"   💰 Price: ${crypto_data['current_price']:,.2f}")
            print(f"   ⭐ Score: {rec['weighted_score']}/10")
            print(f"   📈 Recommendation: {rec['final_recommendation']}")
            print(f"   💡 Advice: {rec['investment_advice']}")

        input("\nPress Enter to continue...")

    def _compare_cryptocurrencies(self):
        """Compare multiple cryptocurrencies"""
        print("\n🔍 Select cryptocurrencies to compare:")

        crypto_list = list(self.crypto_data.keys())
        for i, crypto in enumerate(crypto_list, 1):
            symbol = self.crypto_data[crypto]["symbol"]
            price = self.crypto_data[crypto]["current_price"]
            print(f"{i}. {crypto.title()} ({symbol}) - ${price:,.2f}")

        selections = input(f"\nEnter numbers separated by commas (e.g., 1,2,3): ").strip()

        try:
            indices = [int(x.strip()) - 1 for x in selections.split(',')]
            selected_cryptos = [crypto_list[i] for i in indices if 0 <= i < len(crypto_list)]

            if len(selected_cryptos) < 2:
                print("❌ Please select at least 2 cryptocurrencies.")
                return

            print("\n" + "="*80)
            print("⚖️ CRYPTOCURRENCY COMPARISON")
            print("="*80)

            # Headers
            print(f"{'Crypto':<12} {'Price':<12} {'24h%':<8} {'30d%':<8} {'Profit':<12} {'Sustain':<12} {'Score':<8}")
            print("-" * 80)

            # Comparison data
            for crypto in selected_cryptos:
                rec = self.get_personalized_recommendation(crypto)
                data = self.crypto_data[crypto]

                print(f"{crypto.title():<12} "
                      f"${data['current_price']:<11,.2f} "
                      f"{data['price_change_24h']:+6.1f}% "
                      f"{data['price_change_30d']:+6.1f}% "
                      f"{rec['profitability']['rating']:<12} "
                      f"{rec['sustainability']['rating']:<12} "
                      f"{rec['weighted_score']:<8.1f}")

            input("\nPress Enter to continue...")

        except (ValueError, IndexError):
            print("❌ Invalid selection format.")

    def _show_market_overview(self):
        """Show market overview"""
        print("\n" + "="*60)
        print("🌐 CRYPTOCURRENCY MARKET OVERVIEW")
        print("="*60)

        total_market_cap = sum(data["market_cap"] for data in self.crypto_data.values())
        total_volume = sum(data["volume_24h"] for data in self.crypto_data.values())

        print(f"📊 Total Market Cap: ${total_market_cap:,.0f}")
        print(f"📈 24h Volume: ${total_volume:,.0f}")

        print(f"\n{'Cryptocurrency':<15} {'Price':<12} {'24h Change':<12} {'Market Cap':<15}")
        print("-" * 60)

        for crypto, data in self.crypto_data.items():
            change_color = "📈" if data["price_change_24h"] >= 0 else "📉"
            print(f"{crypto.title():<15} "
                  f"${data['current_price']:<11,.2f} "
                  f"{change_color}{data['price_change_24h']:+6.1f}% "
                  f"${data['market_cap']:>14,.0f}")

        # Market sentiment
        positive_changes = sum(1 for data in self.crypto_data.values() if data["price_change_24h"] > 0)
        total_cryptos = len(self.crypto_data)
        sentiment = "Bullish 🐂" if positive_changes > total_cryptos / 2 else "Bearish 🐻"

        print(f"\n🎭 Market Sentiment: {sentiment}")
        print(f"📊 Positive Performers: {positive_changes}/{total_cryptos}")

        input("\nPress Enter to continue...")

# Main execution
def main():
    """Main function to run the chatbot"""
    print("🚀 Initializing CryptoWise AI...")
    print("This chatbot will help you make informed cryptocurrency investment decisions!")
    print("Based on profitability analysis and sustainability factors.\n")

    bot = CryptoInvestmentBot()

    try:
        bot.chat()
    except KeyboardInterrupt:
        print("\n\n🤖 Thanks for using CryptoWise AI! Goodbye! 👋")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please restart the bot and try again.")

if __name__ == "__main__":
    main()
# Purpose-AI-TTA Quick Start Guide

Welcome to the Purpose-AI-TTA Adaptive AI War Room! This guide will get you up and running in 5 minutes.

## 🚀 Installation

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Configure Environment (Optional)

For full AI integration, create a `.env` file:

```bash
cp .env.example .env
```

Then edit `.env` and add your API keys:
- OpenAI API key (for Grok)
- Anthropic API key (for Claude)
- Kimi API key

**Note:** The system works without API keys, but AI features will use placeholder responses.

## 🎮 Try It Out

### Option 1: Run the Demo

See all features in action:

```bash
python demo.py
```

### Option 2: Run Tests

Verify everything is working:

```bash
python tests/test_basic.py
```

### Option 3: Start the War Room

Launch the interactive interface:

```bash
python main.py
```

## 📚 Quick Tutorial

Once in the war room, try these commands:

### 1. TTA Loop - Transform Chaos to Purpose

```
Command > tta

Enter your thoughts: I have too many ideas and feel scattered

```

The system will:
- Process your thoughts (Tanker)
- Add emotional context (Følelser)
- Generate actionable items (Handling)

### 2. View Capital Management

```
Command > capital
```

See the 369 splits:
- 30% Innovation
- 60% Stability
- 10% Give-back to Folket

### 3. Run Moonshot Simulation

```
Command > moonshot

Select scenario number: 1
```

Evaluate high-impact projects with:
- Risk assessment
- Success probability
- Best/worst case analysis

### 4. Manage AI Providers

```
Command > ai
```

Switch between or use consensus from:
- Grok
- Kimi
- Claude

### 5. Free Speech Mode

```
Command > fri-tale
```

Open dialogue with AI - your voice matters!

## 🎯 Common Use Cases

### For Startups

```python
# Strategic planning
python main.py
> tta  # Process business ideas
> moonshot  # Evaluate moonshot scenarios
> capital  # Allocate budget
```

### For Community Projects

```python
# Social impact planning
python main.py
> tta  # Define community needs
> capital  # Use give-back allocation (10%)
> moonshot  # Simulate impact scenarios
```

### For Personal Development

```python
# Life planning
python main.py
> fri-tale  # Free dialogue about goals
> tta  # Transform chaos into action
```

## 🔑 Key Concepts

### TTA Loop
**Tanker → Følelser → Handling**
- Thoughts → Feelings → Actions
- Transforms chaos into purpose

### 369 Capital System
Based on Tesla's sacred numbers:
- 3 (30%): Innovation & Growth
- 6 (60%): Stability & Operations
- 9 (10%): Give-back to Folket

### Hybrid AI
Multiple AI providers working together:
- Switch providers anytime
- Get consensus from all
- Best of multiple models

### Power to Folket
Give-back ethos:
- 10% for community
- Transparent allocation
- People-first approach

## 📊 Example Session

```
$ python main.py

Command > tta
Input: I want to start a community tech hub but don't know where to begin

Results:
✓ Identified 5 key thoughts
✓ Sentiment: Positive (0.7)
✓ Priority: High (4/5)
✓ Purpose Alignment: 85%

Actions:
1. Research existing community hubs
2. Identify local needs
3. Run moonshot simulation
4. Allocate capital from give-back pool

Command > moonshot
Scenario: Open Source Innovation Lab
Success Probability: 60%
Recommendation: RECOMMENDED

Command > capital
Give-back Pool: $100,000
Allocation: Community Tech Hub

Command > exit
Power to Folket! 👋
```

## 🆘 Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "API key error"
AI features need API keys in `.env`. The system works without them, but uses placeholders.

### "Import errors"
Make sure you're in the project directory:
```bash
cd Purpose-AI-TTA
python main.py
```

## 🎓 Next Steps

1. **Read the docs**: Check `DOCUMENTATION.md` for technical details
2. **Customize**: Edit `config.yaml` for your preferences
3. **Extend**: Add custom moonshot scenarios
4. **Contribute**: Share improvements with the community

## 💡 Pro Tips

- Use `tta` frequently to process thoughts
- Run `moonshot` before big decisions
- Monitor `capital` to track allocations
- Try `fri-tale` for open exploration
- Check `history` to see patterns

## 🌟 Philosophy

Remember: **Power to Folket**

This system is built for the people, by the people. Use it to:
- Transform chaos into purpose
- Make evidence-based decisions
- Support your community
- Achieve your moonshots

---

**Ready to start?**

```bash
python main.py
```

**Need help?**
- Check `README.md` for detailed features
- Read `DOCUMENTATION.md` for architecture
- Create an issue on GitHub

**Power to Folket!** 🚀

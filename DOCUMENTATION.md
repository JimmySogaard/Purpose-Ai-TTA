# Purpose-AI-TTA Technical Documentation

## System Architecture

### Overview
Purpose-AI-TTA is built as a modular Python application that processes chaotic input into purposeful action through a multi-stage pipeline.

## Core Modules

### 1. TTA Loop (`tta_loop.py`)

The heart of the system, implementing the three-stage processing pipeline:

#### Tanker (Thoughts)
```python
class Tanker:
    raw_input: str           # Original user input
    timestamp: datetime      # When thought was captured
    context: Dict           # Additional context
    analyzed_thoughts: List # Processed thoughts
```

**Purpose**: Capture and structure raw, chaotic input

#### Følelser (Feelings)
```python
class Folelser:
    thoughts: Tanker        # Reference to thoughts
    sentiment_score: float  # -1.0 to 1.0
    emotional_tags: List    # Emotion labels
    intuition_signal: str   # Intuitive insight
```

**Purpose**: Add emotional intelligence and intuition

#### Handling (Actions)
```python
class Handling:
    feelings: Folelser      # Reference to feelings
    action_items: List      # Concrete actions
    priority_level: int     # 1-5 priority
    purpose_alignment: float # 0.0 to 1.0
```

**Purpose**: Generate aligned, actionable outcomes

### 2. Hybrid AI System (`hybrid_ai.py`)

#### Provider Architecture
```
AIProvider (Abstract Base)
    ├── GrokProvider
    ├── KimiProvider
    └── ClaudeProvider
```

#### Features
- **Provider Switching**: Seamless switching between AI models
- **Consensus Mode**: Get responses from all providers
- **Extensible**: Easy to add new providers

#### Usage
```python
hybrid_ai = HybridAI()

# Single provider
response = await hybrid_ai.generate_response(prompt)

# Consensus from all
responses = await hybrid_ai.consensus_response(prompt)
```

### 3. Capital Management (`capital_manager.py`)

#### 369 Philosophy
Based on Nikola Tesla's fascination with 3, 6, 9:

- **3 (30%)**: Innovation - The creative force
- **6 (60%)**: Stability - The foundation
- **9 (10%)**: Give-back - The purpose

#### Transaction Tracking
All capital movements are logged with:
- Timestamp
- Category
- Amount
- Purpose
- Remaining balance

### 4. Moonshot Simulator (`moonshot_sim.py`)

#### Scenario Components
```python
class MoonshotScenario:
    name: str
    description: str
    risk_level: float        # 0.0 to 1.0
    potential_impact: float  # 0.0 to 1.0
    resources_required: Dict
    timeline_months: int
```

#### Simulation Types

**1. Single Scenario Simulation**
- Calculates success probability
- Estimates expected return
- Provides best/worst case analysis

**2. Monte Carlo Simulation**
- Runs 1000+ iterations
- Statistical confidence intervals
- Risk-adjusted recommendations

### 5. War Room Interface (`war_room.py`)

#### Command Structure
```
WarRoom
  ├── execute_tta_command()      # Run TTA cycle
  ├── fri_tale_mode()            # Free speech dialogue
  ├── show_capital_status()      # Display 369 splits
  ├── run_moonshot_menu()        # Simulation interface
  ├── manage_ai_providers()      # AI configuration
  └── show_history()             # Session history
```

#### UI Features
- Rich terminal interface
- Color-coded output
- Interactive prompts
- Real-time feedback

### 6. Security Module (`security.py`)

#### Encryption
- Uses Fernet (symmetric encryption)
- AES-128 in CBC mode
- Automatic key generation

#### Features
- API key masking
- Password hashing (PBKDF2)
- Secure data storage
- Environment-based configuration

## Data Flow

```
User Input (Chaos)
    ↓
Tanker (Thoughts Processing)
    ↓
[Optional: Hybrid AI Enhancement]
    ↓
Følelser (Emotional Processing)
    ↓
[Optional: Hybrid AI Enhancement]
    ↓
Handling (Action Generation)
    ↓
[Optional: Moonshot Simulation]
    ↓
[Optional: Capital Allocation]
    ↓
Purposeful Actions (Output)
```

## Configuration

### Environment Variables (.env)
```bash
# AI API Keys
OPENAI_API_KEY=your_key
ANTHROPIC_API_KEY=your_key
KIMI_API_KEY=your_key

# Security
ENCRYPTION_KEY=generated_key
SECURE_MODE=true

# Capital
CAPITAL_SPLITS=369
GIVEBACK_PERCENTAGE=10

# App
DEBUG=false
LOG_LEVEL=INFO
```

### YAML Configuration (config.yaml)
Structured configuration for:
- TTA Loop settings
- AI provider preferences
- Capital management rules
- Moonshot parameters
- Security settings
- Interface customization

## Extension Points

### Adding New AI Provider

```python
from purpose_ai.hybrid_ai import AIProvider

class NewProvider(AIProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def generate_response(self, prompt: str, context: Dict) -> str:
        # Implement API call
        return response
    
    def get_provider_name(self) -> str:
        return "NewProvider"

# Add to HybridAI initialization
```

### Custom Moonshot Scenario

```python
scenario = MoonshotScenario(
    name="Your Moonshot",
    description="Description",
    risk_level=0.5,
    potential_impact=0.8,
    resources_required={'capital': 100000},
    timeline_months=12
)

simulator.scenarios_library.append(scenario)
```

### Custom TTA Processing

Extend the TTA loop by overriding methods:

```python
class CustomTTALoop(TTALoop):
    def _analyze_thoughts(self, raw_input: str) -> List[str]:
        # Custom thought analysis
        return custom_analysis
```

## Performance Considerations

### Async Operations
- All AI calls are async
- Supports concurrent provider queries
- Non-blocking UI operations

### Caching Strategy
- Session history (in-memory)
- Simulation results (persistent)
- AI responses (optional)

### Scalability
- Modular architecture
- Stateless operations
- Easy horizontal scaling

## Testing Strategy

### Unit Tests
- Test each module independently
- Mock AI provider responses
- Verify data transformations

### Integration Tests
- Test full TTA cycle
- Verify capital calculations
- Check simulation accuracy

### Security Tests
- Encryption/decryption
- Key management
- API key protection

## Deployment

### Local Development
```bash
python main.py
```

### Docker (Future)
```dockerfile
FROM python:3.11-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

### Cloud Deployment
- Environment variables via secrets
- Encrypted configuration
- Secure API endpoints

## Monitoring and Logging

### Log Levels
- DEBUG: Detailed system information
- INFO: General operations
- WARNING: Potential issues
- ERROR: Critical failures

### Metrics to Track
- TTA cycle completion time
- AI provider response time
- Simulation accuracy
- Capital allocation patterns

## Future Enhancements

1. **Multi-language Support**: Danish interface
2. **Web Interface**: Browser-based war room
3. **Collaborative Mode**: Multi-user sessions
4. **Advanced Analytics**: Pattern recognition
5. **API Endpoint**: RESTful API access
6. **Mobile App**: iOS/Android clients
7. **Blockchain Integration**: Transparent give-back tracking

## Troubleshooting

### Common Issues

**AI Provider Timeout**
- Check API keys in .env
- Verify network connectivity
- Try switching providers

**Encryption Errors**
- Regenerate encryption key
- Check ENCRYPTION_KEY format
- Verify cryptography library

**Import Errors**
- Install requirements: `pip install -r requirements.txt`
- Check Python version (>=3.8)
- Verify virtual environment

## Best Practices

1. **Always use .env for secrets**: Never commit API keys
2. **Regular backups**: Simulation results and history
3. **Monitor give-back**: Track community contributions
4. **Update providers**: Keep AI libraries current
5. **Test moonshots**: Validate scenarios before decisions

## Contributing

See CONTRIBUTING.md for:
- Code style guidelines
- Testing requirements
- PR process
- Community standards

---

**Remember**: This system is built with "Power to Folket" as its core principle. Every feature should empower users and serve the community.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T02:52:24.559690+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8574`

## Conditions

- `news_risk_high`: News Risk is elevated.
- `macro_risk_high`: Macro Risk is elevated.
- `risk_on_high`: Risk-On score is elevated.
- `market_context_high`: Market Context is supportive.
- `polymarket_volume_spike`: Polymarket 24h volume z-score is elevated.
- `flow_alert_high`: Flow Alert score is elevated.
- `news_and_polymarket`: News Risk and Polymarket volume spike happen together.
- `risk_on_and_context`: Risk-On and Market Context are both supportive.
- `macro_and_flow`: Macro Risk and Flow Alert are elevated together.

## Top Patterns

- `market_context_high->unknown_4h` score `38.6064` n `90` status `ready` deltaP `-4.3224` edge `3.2999` maxDD `-2.3109`
- `news_risk_high->crypto_major_4h` score `10.7759` n `62` status `ready` deltaP `37.6672` edge `0.6672` maxDD `-0.6258`
- `news_risk_high->crypto_alt_4h` score `6.9025` n `62` status `ready` deltaP `22.1725` edge `0.5618` maxDD `-6.4195`
- `news_risk_high->equity_24h` score `6.0853` n `62` status `ready` deltaP `15.1747` edge `0.4159` maxDD `-0.1298`
- `news_risk_high->index_24h` score `4.7758` n `62` status `ready` deltaP `34.6021` edge `0.1673` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `4.2724` n `90` status `ready` deltaP `10.2191` edge `0.777` maxDD `-16.7906`
- `news_risk_high->index_4h` score `2.9457` n `62` status `ready` deltaP `32.3073` edge `0.0563` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.4408` n `62` status `ready` deltaP `10.0251` edge `0.1721` maxDD `-1.5096`
- `market_context_high->crypto_major_4h` score `2.2711` n `90` status `ready` deltaP `15.7317` edge `0.1808` maxDD `-4.047`
- `news_risk_high->equity_4h` score `2.1298` n `62` status `ready` deltaP `17.4715` edge `0.1208` maxDD `-2.7837`
- `news_risk_high->index_1h` score `1.9289` n `62` status `ready` deltaP `24.2757` edge `0.0139` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.5807` n `90` status `ready` deltaP `12.7374` edge `0.0897` maxDD `-1.0977`
- `news_risk_high->metal_4h` score `1.4622` n `62` status `ready` deltaP `21.0956` edge `0.0884` maxDD `-0.993`
- `news_risk_high->unknown_4h` score `1.386` n `62` status `ready` deltaP `-7.2974` edge `0.2887` maxDD `-5.6309`
- `market_context_high->metal_24h` score `1.2113` n `90` status `ready` deltaP `21.1188` edge `0.163` maxDD `-3.5466`
- `market_context_high->fx_4h` score `1.0901` n `90` status `ready` deltaP `21.9783` edge `0.019` maxDD `-0.3077`
- `news_risk_high->crypto_alt_1h` score `1.0687` n `62` status `ready` deltaP `2.7091` edge `0.1229` maxDD `-2.4854`
- `market_context_high->fx_1h` score `0.725` n `90` status `ready` deltaP `12.0958` edge `0.004` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.1214` n `90` status `ready` deltaP `9.9534` edge `0.0381` maxDD `-3.7778`
- `market_context_high->crypto_alt_24h` score `0.1061` n `90` status `ready` deltaP `7.1127` edge `0.56` maxDD `-34.5048`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

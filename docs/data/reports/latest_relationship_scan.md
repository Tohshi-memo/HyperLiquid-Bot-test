# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-01T11:07:28.510375+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6537`

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

- `market_context_high->unknown_24h` score `7032.0984` n `55` status `ready` deltaP `2.4306` edge `585.992` maxDD `0.0`
- `market_context_high->unknown_4h` score `372.2871` n `55` status `ready` deltaP `5.3464` edge `30.9926` maxDD `-0.0124`
- `market_context_high->unknown_1h` score `59.1724` n `55` status `ready` deltaP `3.1628` edge `4.921` maxDD `-0.2178`
- `news_risk_high->unknown_1h` score `45.2697` n `124` status `ready` deltaP `-6.0894` edge `3.8417` maxDD `-0.9571`
- `market_context_high->equity_24h` score `21.3498` n `55` status `ready` deltaP `44.3624` edge `1.507` maxDD `-1.5546`
- `news_risk_high->crypto_alt_24h` score `12.842` n `98` status `ready` deltaP `29.6379` edge `1.0082` maxDD `-6.8493`
- `market_context_high->index_24h` score `7.0188` n `55` status `ready` deltaP `57.4653` edge `0.2018` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5421` n `55` status `ready` deltaP `45.7892` edge `0.271` maxDD `-0.8203`
- `market_context_high->crypto_alt_4h` score `5.7361` n `55` status `ready` deltaP `22.8354` edge `0.3552` maxDD `-1.6876`
- `market_context_high->crypto_major_4h` score `5.3831` n `55` status `ready` deltaP `29.673` edge `0.2844` maxDD `-1.6901`
- `news_risk_high->crypto_alt_4h` score `4.7558` n `112` status `ready` deltaP `18.7283` edge `0.4101` maxDD `-7.4246`
- `market_context_high->commodity_4h` score `3.3635` n `55` status `ready` deltaP `31.5244` edge `0.0952` maxDD `-0.3387`
- `market_context_high->equity_4h` score `3.3222` n `55` status `ready` deltaP `5.4379` edge `0.3108` maxDD `-2.283`
- `market_context_high->crypto_major_24h` score `2.4463` n `55` status `ready` deltaP `10.8586` edge `0.3089` maxDD `-3.0799`
- `market_context_high->crypto_alt_24h` score `1.7719` n `55` status `ready` deltaP `-5.1673` edge `0.4134` maxDD `-8.8096`
- `market_context_high->metal_4h` score `1.5582` n `55` status `ready` deltaP `18.3508` edge `0.05` maxDD `-0.7323`
- `market_context_high->equity_1h` score `1.4027` n `55` status `ready` deltaP `1.8291` edge `0.1572` maxDD `-1.5336`
- `market_context_high->crypto_major_1h` score `1.334` n `55` status `ready` deltaP `7.7327` edge `0.1206` maxDD `-2.2118`
- `market_context_high->crypto_alt_1h` score `1.2792` n `55` status `ready` deltaP `3.4758` edge `0.1505` maxDD `-2.3659`
- `market_context_high->metal_1h` score `0.8852` n `55` status `ready` deltaP `11.0261` edge `0.0251` maxDD `-0.3209`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

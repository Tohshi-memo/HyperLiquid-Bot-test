# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T21:22:24.669091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9116`

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

- `market_context_high->unknown_24h` score `1380.8097` n `40` status `ready` deltaP `-22.5694` edge `115.2543` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `49.7287` n `94` status `ready` deltaP `-3.2985` edge `4.2241` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.7948` n `40` status `ready` deltaP `27.6736` edge `0.5913` maxDD `-1.0977`
- `market_context_high->index_24h` score `6.406` n `40` status `ready` deltaP `52.4306` edge `0.1843` maxDD `0.0`
- `market_context_high->unknown_1h` score `5.0289` n `106` status `ready` deltaP `-3.3301` edge `0.4749` maxDD `-1.0231`
- `market_context_high->fx_24h` score `3.0852` n `40` status `ready` deltaP `35.0347` edge `0.0365` maxDD `-0.0374`
- `market_context_high->crypto_major_24h` score `1.3996` n `40` status `ready` deltaP `-21.1111` edge `0.5722` maxDD `-17.8526`
- `market_context_high->fx_4h` score `0.794` n `94` status `ready` deltaP `13.0546` edge `0.0075` maxDD `-0.2692`
- `market_context_high->commodity_4h` score `0.588` n `94` status `ready` deltaP `12.74` edge `0.0174` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.3439` n `106` status `ready` deltaP `7.4738` edge `0.0072` maxDD `-0.6025`
- `market_context_high->crypto_alt_1h` score `0.1975` n `106` status `ready` deltaP `5.8864` edge `0.0895` maxDD `-4.9401`
- `market_context_high->metal_4h` score `0.1585` n `94` status `ready` deltaP `9.568` edge `0.0217` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `0.0477` n `94` status `ready` deltaP `1.0768` edge `0.2095` maxDD `-11.1784`
- `market_context_high->fx_1h` score `-0.0317` n `106` status `ready` deltaP `3.1014` edge `0.0009` maxDD `-0.271`
- `market_context_high->metal_1h` score `-0.0883` n `106` status `ready` deltaP `7.1885` edge `0.0036` maxDD `-0.7107`
- `market_context_high->crypto_alt_4h` score `-0.158` n `94` status `ready` deltaP `-1.3817` edge `0.2448` maxDD `-13.8008`
- `market_context_high->crypto_major_1h` score `-0.3025` n `106` status `ready` deltaP `-0.1497` edge `0.0511` maxDD `-3.7778`
- `market_context_high->index_4h` score `-0.511` n `94` status `ready` deltaP `-0.3113` edge `0.0066` maxDD `-0.9364`
- `market_context_high->index_1h` score `-0.7661` n `106` status `ready` deltaP `-4.7763` edge `-0.0013` maxDD `-0.5392`
- `market_context_high->equity_1h` score `-0.9499` n `106` status `ready` deltaP `-5.6434` edge `0.0028` maxDD `-2.2898`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-08T20:22:29.865015+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8908`

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

- `market_context_high->unknown_4h` score `40.2048` n `91` status `ready` deltaP `-2.0721` edge `3.4181` maxDD `-2.3109`
- `news_risk_high->crypto_alt_4h` score `14.673` n `49` status `ready` deltaP `44.5122` edge `0.926` maxDD `0.0`
- `news_risk_high->crypto_major_4h` score `14.138` n `49` status `ready` deltaP `45.9184` edge `0.8788` maxDD `-0.2073`
- `news_risk_high->equity_24h` score `9.3103` n `49` status `ready` deltaP `25.1123` edge `0.6184` maxDD `-0.1298`
- `market_context_high->crypto_major_24h` score `8.6958` n `90` status `ready` deltaP `21.7388` edge `1.2673` maxDD `-16.7906`
- `market_context_high->equity_24h` score `6.6419` n `90` status `ready` deltaP `24.3867` edge `0.4338` maxDD `-1.0977`
- `news_risk_high->index_24h` score `6.2911` n `49` status `ready` deltaP `45.234` edge `0.2227` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.9491` n `49` status `ready` deltaP `32.233` edge `0.3014` maxDD `-0.6421`
- `news_risk_high->index_4h` score `4.5793` n `49` status `ready` deltaP `45.6726` edge `0.0816` maxDD `-0.025`
- `news_risk_high->crypto_major_1h` score `3.1649` n `49` status `ready` deltaP `12.7612` edge `0.2142` maxDD `-1.5096`
- `market_context_high->crypto_alt_24h` score `2.7627` n `90` status `ready` deltaP `13.4412` edge `0.8584` maxDD `-34.5048`
- `news_risk_high->crypto_alt_1h` score `2.6754` n `49` status `ready` deltaP `6.6388` edge `0.2104` maxDD `-1.2034`
- `news_risk_high->commodity_24h` score `2.5486` n `49` status `ready` deltaP `31.1004` edge `0.0135` maxDD `-0.0096`
- `news_risk_high->index_1h` score `2.4278` n `49` status `ready` deltaP `29.986` edge `0.0164` maxDD `-0.1194`
- `market_context_high->crypto_major_4h` score `1.9903` n `91` status `ready` deltaP `19.2308` edge `0.26` maxDD `-6.9761`
- `market_context_high->metal_24h` score `1.4238` n `90` status `ready` deltaP `23.6453` edge `0.1734` maxDD `-3.5466`
- `news_risk_high->metal_4h` score `1.2496` n `49` status `ready` deltaP `19.3629` edge `0.0727` maxDD `-0.993`
- `market_context_high->fx_4h` score `0.6209` n `91` status `ready` deltaP `17.0581` edge `0.0127` maxDD `-0.3077`
- `market_context_high->fx_1h` score `0.4512` n `91` status `ready` deltaP `8.9426` edge `0.0022` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `0.3457` n `91` status `ready` deltaP `11.1914` edge `0.0586` maxDD `-3.7778`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

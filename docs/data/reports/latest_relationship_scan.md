# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T06:22:24.847356+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5976`

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

- `market_context_high->unknown_4h` score `42.6603` n `85` status `ready` deltaP `-12.9484` edge `3.6994` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.6476` n `76` status `ready` deltaP `38.6787` edge `0.589` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.8677` n `76` status `ready` deltaP `14.9854` edge `1.2236` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.2796` n `85` status `ready` deltaP `18.6298` edge `0.0108` maxDD `-0.2692`
- `market_context_high->crypto_major_4h` score `0.424` n `85` status `ready` deltaP `8.6047` edge `0.1641` maxDD `-9.3683`
- `market_context_high->fx_1h` score `0.0658` n `97` status `ready` deltaP `4.704` edge `0.0013` maxDD `-0.271`
- `market_context_high->commodity_4h` score `-0.0671` n `85` status `ready` deltaP `6.1693` edge `0.0036` maxDD `-1.6002`
- `market_context_high->crypto_major_1h` score `-0.0859` n `97` status `ready` deltaP `5.7859` edge `0.0393` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.1189` n `97` status `ready` deltaP `2.5094` edge `0.0068` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.1753` n `76` status `ready` deltaP `8.1872` edge `0.0963` maxDD `-1.868`
- `market_context_high->metal_1h` score `-0.663` n `97` status `ready` deltaP `-3.9246` edge `0.0007` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.665` n `76` status `ready` deltaP `2.5858` edge `0.046` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8903` n `97` status `ready` deltaP `-2.6282` edge `0.0193` maxDD `-4.9401`
- `market_context_high->crypto_alt_24h` score `-1.1698` n `76` status `ready` deltaP `1.4345` edge `0.4517` maxDD `-35.5652`
- `market_context_high->metal_4h` score `-1.3474` n `85` status `ready` deltaP `-12.7242` edge `0.0134` maxDD `-1.1053`
- `market_context_high->fx_24h` score `-1.4453` n `76` status `ready` deltaP `-0.9686` edge `-0.0012` maxDD `-2.2109`
- `market_context_high->index_4h` score `-1.476` n `85` status `ready` deltaP `-14.401` edge `0.0` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.7117` n `97` status `ready` deltaP `-8.0314` edge `-0.0029` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.7662` n `97` status `ready` deltaP `-7.9835` edge `-0.007` maxDD `-2.2898`
- `market_context_high->equity_4h` score `-2.9273` n `85` status `ready` deltaP `-12.2633` edge `-0.0062` maxDD `-6.1456`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

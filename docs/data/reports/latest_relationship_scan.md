# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T08:52:15.588456+00:00`
- Price records: `672`
- Market context records: `1930`
- Flow alert records: `7455`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7540`

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

- `market_context_high->crypto_alt_4h` score `7.3274` n `209` status `ready` deltaP `23.1124` edge `0.571` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `6.799` n `209` status `ready` deltaP `27.8081` edge `0.5058` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.5138` n `209` status `ready` deltaP `17.176` edge `0.3807` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.1242` n `209` status `ready` deltaP `13.5554` edge `0.1961` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `0.647` n `221` status `ready` deltaP `7.9253` edge `0.0997` maxDD `-3.2225`
- `market_context_high->unknown_24h` score `0.6412` n `196` status `ready` deltaP `13.9916` edge `0.4922` maxDD `-35.8966`
- `market_context_high->crypto_alt_1h` score `0.4913` n `221` status `ready` deltaP `7.187` edge `0.1044` maxDD `-4.9097`
- `market_context_high->metal_24h` score `0.327` n `196` status `ready` deltaP `12.2626` edge `0.1881` maxDD `-12.7414`
- `market_context_high->index_24h` score `0.1718` n `196` status `ready` deltaP `4.2233` edge `0.109` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.1555` n `209` status `ready` deltaP `8.0341` edge `0.0683` maxDD `-3.7119`
- `market_context_high->equity_1h` score `-0.1977` n `221` status `ready` deltaP `4.5161` edge `0.0328` maxDD `-2.6836`
- `market_context_high->fx_24h` score `-0.2453` n `196` status `ready` deltaP `10.1793` edge `0.0166` maxDD `-1.3925`
- `market_context_high->fx_1h` score `-0.65` n `221` status `ready` deltaP `-3.0909` edge `0.0005` maxDD `-0.3914`
- `market_context_high->index_1h` score `-0.6872` n `221` status `ready` deltaP `-0.1788` edge `0.0071` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.7028` n `221` status `ready` deltaP `4.302` edge `0.0148` maxDD `-6.3532`
- `market_context_high->fx_4h` score `-0.9304` n `209` status `ready` deltaP `-4.4185` edge `-0.001` maxDD `-1.1056`
- `market_context_high->metal_4h` score `-1.1173` n `209` status `ready` deltaP `9.0719` edge `0.1156` maxDD `-12.5349`
- `market_context_high->equity_24h` score `-1.2226` n `196` status `ready` deltaP `7.2846` edge `0.3394` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.328` n `221` status `ready` deltaP `1.308` edge `-0.0242` maxDD `-3.6151`
- `market_context_high->commodity_1h` score `-1.9546` n `221` status `ready` deltaP `1.5905` edge `-0.0054` maxDD `-15.7972`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

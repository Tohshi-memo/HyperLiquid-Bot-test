# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T18:37:29.547467+00:00`
- Price records: `672`
- Market context records: `6310`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11133`

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

- `news_risk_high->crypto_alt_24h` score `15.255` n `32` status `ready` deltaP `43.2292` edge `0.9978` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0025` n `32` status `ready` deltaP `50.5208` edge `0.1634` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.2233` n `32` status `ready` deltaP `16.6667` edge `0.5083` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.1997` n `32` status `ready` deltaP `43.8262` edge `0.0624` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.2448` n `32` status `ready` deltaP `29.1667` edge `0.0965` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4015` n `32` status `ready` deltaP `28.8922` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.4452` n `32` status `ready` deltaP `14.2777` edge `0.1368` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9166` n `32` status `ready` deltaP `11.6205` edge `0.0862` maxDD `-1.6923`
- `market_context_high->unknown_1h` score `0.6789` n `208` status `ready` deltaP `-3.9469` edge `0.1837` maxDD `-3.7317`
- `market_context_high->metal_4h` score `0.0466` n `196` status `ready` deltaP `9.361` edge `0.0378` maxDD `-2.7056`
- `market_context_high->metal_24h` score `-0.0808` n `163` status `ready` deltaP `21.7323` edge `0.1016` maxDD `-11.8809`
- `market_context_high->metal_1h` score `-0.442` n `208` status `ready` deltaP `2.9249` edge `0.0016` maxDD `-1.8877`
- `news_risk_high->index_24h` score `-0.4599` n `32` status `ready` deltaP `4.5139` edge `-0.0019` maxDD `-2.3058`
- `market_context_high->commodity_1h` score `-0.5827` n `208` status `ready` deltaP `-0.7485` edge `-0.0014` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.7222` n `208` status `ready` deltaP `-0.9155` edge `-0.0021` maxDD `-0.825`
- `news_risk_high->metal_1h` score `-0.7294` n `32` status `ready` deltaP `-2.8443` edge `-0.0248` maxDD `-1.6464`
- `market_context_high->equity_4h` score `-0.7448` n `196` status `ready` deltaP `4.6043` edge `0.0437` maxDD `-8.2573`
- `market_context_high->index_1h` score `-0.7855` n `208` status `ready` deltaP `-2.4585` edge `0.0026` maxDD `-0.9531`
- `market_context_high->index_4h` score `-0.9195` n `196` status `ready` deltaP `1.7609` edge `0.0168` maxDD `-1.381`
- `market_context_high->equity_1h` score `-0.9528` n `208` status `ready` deltaP `-1.6064` edge `0.0001` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

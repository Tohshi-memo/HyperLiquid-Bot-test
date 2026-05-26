# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-26T05:56:11.958965+00:00`
- Price records: `672`
- Market context records: `1918`
- Flow alert records: `7420`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6052`

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

- `market_context_high->crypto_alt_4h` score `7.7744` n `199` status `ready` deltaP `24.1857` edge `0.6011` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `7.2847` n `199` status `ready` deltaP `29.5441` edge `0.5347` maxDD `-4.9684`
- `market_context_high->unknown_4h` score `3.9951` n `199` status `ready` deltaP `17.958` edge `0.4156` maxDD `-9.8581`
- `market_context_high->equity_4h` score `2.6981` n `199` status `ready` deltaP `16.2589` edge `0.2259` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `0.952` n `192` status `ready` deltaP `13.5416` edge `0.5211` maxDD `-35.8966`
- `market_context_high->metal_24h` score `0.9143` n `192` status `ready` deltaP `13.8889` edge `0.2262` maxDD `-12.7414`
- `market_context_high->crypto_major_1h` score `0.8434` n `209` status `ready` deltaP `8.9398` edge `0.1093` maxDD `-3.2225`
- `market_context_high->crypto_alt_1h` score `0.6808` n `209` status `ready` deltaP `8.1003` edge `0.1141` maxDD `-4.9097`
- `market_context_high->index_24h` score `0.5913` n `192` status `ready` deltaP `6.0764` edge `0.1316` maxDD `-4.1604`
- `market_context_high->index_4h` score `0.5466` n `199` status `ready` deltaP `10.7029` edge `0.0831` maxDD `-3.7119`
- `market_context_high->fx_24h` score `-0.06` n `192` status `ready` deltaP `11.8056` edge `0.0212` maxDD `-1.3925`
- `market_context_high->equity_1h` score `-0.1386` n `209` status `ready` deltaP `4.8041` edge `0.0358` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.622` n `209` status `ready` deltaP `0.351` edge `0.009` maxDD `-1.7205`
- `market_context_high->metal_1h` score `-0.6333` n `209` status `ready` deltaP `5.0533` edge `0.0187` maxDD `-6.3532`
- `market_context_high->fx_1h` score `-0.6401` n `209` status `ready` deltaP `-2.9603` edge `0.0009` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.6616` n `199` status `ready` deltaP `11.9331` edge `0.1345` maxDD `-12.5349`
- `market_context_high->fx_4h` score `-0.7869` n `199` status `ready` deltaP `-1.9901` edge `0.0012` maxDD `-1.1056`
- `market_context_high->equity_24h` score `-1.0806` n `192` status `ready` deltaP `6.9445` edge `0.3535` maxDD `-33.1875`
- `market_context_high->unknown_1h` score `-1.191` n `209` status `ready` deltaP `1.2814` edge `-0.0126` maxDD `-3.6151`
- `market_context_high->crypto_major_24h` score `-1.9403` n `192` status `ready` deltaP `13.8889` edge `0.6043` maxDD `-62.3533`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

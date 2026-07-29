# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-29T06:52:28.314630+00:00`
- Price records: `672`
- Market context records: `8277`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5892`

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

- `news_risk_high->unknown_24h` score `6577.6876` n `50` status `ready` deltaP `39.4097` edge `547.8779` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.2465` n `54` status `ready` deltaP `26.2308` edge `0.4887` maxDD `-3.4427`
- `news_risk_high->equity_1h` score `3.0151` n `54` status `ready` deltaP `21.3795` edge `0.1396` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.7315` n `54` status `ready` deltaP `22.5722` edge `0.0962` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.0601` n `54` status `ready` deltaP `9.8691` edge `0.2677` maxDD `-2.8833`
- `news_risk_high->crypto_alt_1h` score `1.7788` n `54` status `ready` deltaP `13.9554` edge `0.0986` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.5012` n `54` status `ready` deltaP `16.9264` edge `0.2188` maxDD `-5.8012`
- `news_risk_high->crypto_major_1h` score `1.4783` n `54` status `ready` deltaP `9.8581` edge `0.0972` maxDD `-1.1783`
- `news_risk_high->metal_4h` score `1.027` n `54` status `ready` deltaP `9.2818` edge `0.0705` maxDD `-0.7433`
- `news_risk_high->index_1h` score `0.4244` n `54` status `ready` deltaP `6.4538` edge `0.0212` maxDD `-0.3089`
- `news_risk_high->fx_1h` score `0.193` n `54` status `ready` deltaP `7.4462` edge `0.0032` maxDD `-0.2475`
- `news_risk_high->metal_1h` score `-0.112` n `54` status `ready` deltaP `2.9552` edge `0.0113` maxDD `-0.5599`
- `news_risk_high->fx_4h` score `-0.4089` n `54` status `ready` deltaP `5.3748` edge `0.0075` maxDD `-0.6604`
- `news_risk_high->commodity_1h` score `-2.1587` n `54` status `ready` deltaP `-8.9599` edge `-0.0416` maxDD `-2.9516`
- `news_risk_high->fx_24h` score `-4.7392` n `50` status `ready` deltaP `-19.9514` edge `-0.0492` maxDD `-5.0181`
- `news_risk_high->metal_24h` score `-5.4429` n `50` status `ready` deltaP `-17.6597` edge `-0.0612` maxDD `-10.6379`
- `news_risk_high->commodity_4h` score `-8.8344` n `54` status `ready` deltaP `-31.2669` edge `-0.197` maxDD `-13.1269`
- `news_risk_high->index_24h` score `-12.1805` n `50` status `ready` deltaP `-25.0694` edge `-0.3235` maxDD `-27.2864`
- `news_risk_high->commodity_24h` score `-12.3426` n `50` status `ready` deltaP `-13.2708` edge `-0.3461` maxDD `-33.8515`
- `news_risk_high->crypto_major_24h` score `-34.6229` n `50` status `ready` deltaP `-16.9722` edge `-1.3196` maxDD `-103.8662`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T08:22:40.963894+00:00`
- Price records: `672`
- Market context records: `6900`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11702`

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

- `market_context_high->unknown_24h` score `0.5543` n `185` status `ready` deltaP `-3.9552` edge `0.4848` maxDD `-13.3224`
- `market_context_high->fx_1h` score `-0.2129` n `224` status `ready` deltaP `2.8363` edge `0.0023` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.4127` n `224` status `ready` deltaP `2.9593` edge `0.0223` maxDD `-3.7803`
- `market_context_high->crypto_major_1h` score `-0.4867` n `224` status `ready` deltaP `4.4456` edge `0.0202` maxDD `-4.2314`
- `market_context_high->commodity_1h` score `-0.6065` n `224` status `ready` deltaP `-0.7485` edge `-0.0043` maxDD `-2.1443`
- `market_context_high->index_1h` score `-0.7845` n `224` status `ready` deltaP `-1.0292` edge `-0.0026` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.7963` n `224` status `ready` deltaP `14.3075` edge `0.0089` maxDD `-2.1765`
- `market_context_high->metal_1h` score `-0.8495` n `224` status `ready` deltaP `-3.8441` edge `-0.0065` maxDD `-2.1427`
- `market_context_high->commodity_4h` score `-1.3349` n `224` status `ready` deltaP `-1.8838` edge `-0.0096` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.6265` n `224` status `ready` deltaP `-3.5607` edge `-0.0217` maxDD `-3.2083`
- `market_context_high->equity_1h` score `-1.7902` n `224` status `ready` deltaP `1.7857` edge `-0.0234` maxDD `-13.1084`
- `market_context_high->index_4h` score `-1.9519` n `224` status `ready` deltaP `4.399` edge `-0.0216` maxDD `-11.3047`
- `market_context_high->commodity_24h` score `-2.0512` n `185` status `ready` deltaP `1.1981` edge `0.0079` maxDD `-5.2791`
- `market_context_high->metal_4h` score `-2.2261` n `224` status `ready` deltaP `2.0144` edge `-0.0005` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-2.8375` n `224` status `ready` deltaP `1.6006` edge `-0.0161` maxDD `-20.6678`
- `market_context_high->crypto_major_4h` score `-2.9145` n `224` status `ready` deltaP `-0.5445` edge `-0.0373` maxDD `-16.9508`
- `market_context_high->unknown_4h` score `-3.0655` n `224` status `ready` deltaP `-8.5802` edge `0.0383` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.2638` n `185` status `ready` deltaP `-6.7029` edge `-0.007` maxDD `-5.6237`
- `market_context_high->equity_4h` score `-7.2486` n `224` status `ready` deltaP `1.7966` edge `-0.1468` maxDD `-56.5591`
- `market_context_high->metal_24h` score `-8.4067` n `185` status `ready` deltaP `-13.6681` edge `-0.1281` maxDD `-28.352`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

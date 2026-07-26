# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-26T22:25:13.006111+00:00`
- Price records: `672`
- Market context records: `8031`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11832`

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

- `market_context_high->equity_24h` score `16.3589` n `86` status `ready` deltaP `25.9643` edge `1.3137` maxDD `-5.8845`
- `market_context_high->metal_24h` score `7.9124` n `86` status `ready` deltaP `35.8752` edge `0.4202` maxDD `0.0`
- `market_context_high->equity_4h` score `6.4141` n `99` status `ready` deltaP `24.9584` edge `0.4574` maxDD `-5.1426`
- `market_context_high->commodity_24h` score `3.1822` n `86` status `ready` deltaP `24.8015` edge `0.2278` maxDD `-6.2367`
- `market_context_high->metal_4h` score `2.6084` n `99` status `ready` deltaP `23.491` edge `0.123` maxDD `-0.979`
- `market_context_high->index_4h` score `2.5476` n `99` status `ready` deltaP `26.5028` edge `0.0716` maxDD `-0.8791`
- `market_context_high->index_24h` score `1.9103` n `86` status `ready` deltaP `10.6525` edge `0.1552` maxDD `-1.3621`
- `market_context_high->equity_1h` score `1.6829` n `99` status `ready` deltaP `13.9343` edge `0.1291` maxDD `-4.2072`
- `market_context_high->fx_24h` score `1.353` n `86` status `ready` deltaP `25.1663` edge `0.0361` maxDD `-2.2901`
- `market_context_high->index_1h` score `0.8548` n `99` status `ready` deltaP `13.9721` edge `0.0211` maxDD `-0.7743`
- `market_context_high->metal_1h` score `0.7172` n `99` status `ready` deltaP `10.2311` edge `0.0294` maxDD `-0.6936`
- `market_context_high->crypto_major_4h` score `0.6108` n `99` status `ready` deltaP `9.1202` edge `0.1619` maxDD `-6.7444`
- `market_context_high->crypto_alt_4h` score `0.597` n `99` status `ready` deltaP `5.785` edge `0.1229` maxDD `-3.9374`
- `market_context_high->crypto_major_1h` score `0.5561` n `99` status `ready` deltaP `11.1671` edge `0.0379` maxDD `-1.6171`
- `market_context_high->crypto_alt_1h` score `-0.021` n `99` status `ready` deltaP `1.4033` edge `0.0312` maxDD `-1.4603`
- `market_context_high->fx_4h` score `-0.5306` n `99` status `ready` deltaP `4.162` edge `0.0028` maxDD `-0.9813`
- `market_context_high->fx_1h` score `-0.5409` n `99` status `ready` deltaP `-1.2521` edge `0.0` maxDD `-0.2715`
- `market_context_high->commodity_1h` score `-0.6288` n `99` status `ready` deltaP `-2.0398` edge `-0.0047` maxDD `-1.9855`
- `market_context_high->commodity_4h` score `-1.245` n `99` status `ready` deltaP `-0.2756` edge `-0.0076` maxDD `-5.3478`
- `market_context_high->unknown_1h` score `-1.8484` n `99` status `ready` deltaP `7.5017` edge `-0.1617` maxDD `-1.054`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

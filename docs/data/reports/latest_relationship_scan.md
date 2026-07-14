# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T23:22:24.193813+00:00`
- Price records: `672`
- Market context records: `6758`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `1.0636` n `176` status `ready` deltaP `0.5366` edge `0.508` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `-0.0403` n `176` status `ready` deltaP `7.3524` edge `0.0318` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `-0.085` n `176` status `ready` deltaP `7.9704` edge `0.1266` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `-0.1448` n `176` status `ready` deltaP `5.3484` edge `0.0287` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3804` n `176` status `ready` deltaP `-0.1157` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.5812` n `176` status `ready` deltaP `-0.5682` edge `0.0007` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.5977` n `176` status `ready` deltaP `-0.0034` edge `-0.0083` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.6887` n `176` status `ready` deltaP `-4.8415` edge `-0.0035` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.0944` n `176` status `ready` deltaP `3.7051` edge `-0.0132` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.2177` n `176` status `ready` deltaP `7.5388` edge `0.0` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2199` n `176` status `ready` deltaP `6.5964` edge `-0.0124` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.4267` n `176` status `ready` deltaP `-1.7738` edge `-0.0221` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7645` n `176` status `ready` deltaP `-6.876` edge `-0.0111` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.497` n `176` status `ready` deltaP `3.9634` edge `-0.0151` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.6139` n `176` status `ready` deltaP `2.9795` edge `-0.0148` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.6604` n `176` status `ready` deltaP `-6.3193` edge `-0.0129` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-3.5783` n `176` status `ready` deltaP `-15.4102` edge `0.0411` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.1774` n `176` status `ready` deltaP `3.0072` edge `-0.1287` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2614` n `176` status `ready` deltaP `-7.5284` edge `-0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.4233` n `176` status `ready` deltaP `-13.2892` edge `-0.1428` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-08T22:13:09.910418+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11607`

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

- `market_context_high->equity_24h` score `2.9916` n `103` status `ready` deltaP `4.5729` edge `0.5248` maxDD `-21.1456`
- `market_context_high->metal_24h` score `2.4386` n `103` status `ready` deltaP `12.2118` edge `0.1794` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.6664` n `111` status `ready` deltaP `16.2094` edge `0.0981` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `1.0278` n `118` status `ready` deltaP `12.2628` edge `0.0382` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.8806` n `103` status `ready` deltaP `22.2694` edge `0.0511` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.4354` n `103` status `ready` deltaP `9.1002` edge `0.1483` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4699` n `118` status `ready` deltaP `2.2937` edge `-0.0049` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.5566` n `118` status `ready` deltaP `-3.844` edge `-0.0068` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.5915` n `118` status `ready` deltaP `-2.9483` edge `-0.0066` maxDD `-0.9664`
- `market_context_high->index_4h` score `-0.6438` n `111` status `ready` deltaP `-1.4886` edge `-0.0121` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.6522` n `118` status `ready` deltaP `2.1314` edge `0.0143` maxDD `-4.6286`
- `market_context_high->fx_4h` score `-0.727` n `111` status `ready` deltaP `2.9169` edge `-0.0047` maxDD `-1.6928`
- `market_context_high->metal_4h` score `-1.115` n `111` status `ready` deltaP `-3.9551` edge `-0.0157` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-2.0248` n `118` status `ready` deltaP `-11.6715` edge `-0.028` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-2.2452` n `111` status `ready` deltaP `0.9792` edge `-0.0599` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-2.6946` n `118` status `ready` deltaP `-8.9262` edge `-0.0569` maxDD `-5.3178`
- `market_context_high->crypto_major_24h` score `-3.7399` n `103` status `ready` deltaP `6.2197` edge `-0.1037` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.2406` n `103` status `ready` deltaP `-12.4461` edge `-0.1261` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-4.7163` n `111` status `ready` deltaP `-13.3254` edge `-0.139` maxDD `-6.5487`
- `market_context_high->unknown_1h` score `-8.3842` n `118` status `ready` deltaP `-5.3359` edge `-0.6184` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

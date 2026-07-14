# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T07:52:27.754219+00:00`
- Price records: `672`
- Market context records: `6689`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `0.8842` n `193` status `ready` deltaP `-5.2217` edge `0.1986` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.7068` n `193` status `ready` deltaP `10.9232` edge `0.1729` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.4327` n `193` status `ready` deltaP `9.8616` edge `0.0563` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.2964` n `193` status `ready` deltaP `-1.8108` edge `0.4253` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.1803` n `193` status `ready` deltaP `6.5915` edge `0.0475` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2737` n `193` status `ready` deltaP `2.0904` edge `0.0012` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4509` n `193` status `ready` deltaP `1.307` edge `0.0049` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.5027` n `193` status `ready` deltaP `4.1621` edge `0.0105` maxDD `-3.8827`
- `market_context_high->commodity_1h` score `-0.549` n `193` status `ready` deltaP `0.9494` edge `-0.0084` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.5621` n `193` status `ready` deltaP `-3.1259` edge `0.0013` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.9023` n `193` status `ready` deltaP `10.4994` edge `0.0023` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.4059` n `193` status `ready` deltaP `6.2358` edge `-0.0009` maxDD `-3.3397`
- `market_context_high->crypto_major_4h` score `-1.4787` n `193` status `ready` deltaP `8.336` edge `0.0863` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.6259` n `193` status `ready` deltaP `-3.4311` edge `-0.0361` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7317` n `193` status `ready` deltaP `6.4459` edge `0.0752` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1259` n `193` status `ready` deltaP `-1.1713` edge `0.0213` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-2.5858` n `193` status `ready` deltaP `-15.5575` edge `0.1288` maxDD `-10.5788`
- `market_context_high->equity_4h` score `-3.3311` n `193` status `ready` deltaP `7.1172` edge `-0.0476` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.5406` n `193` status `ready` deltaP `-10.9285` edge `-0.0075` maxDD `-9.1756`
- `market_context_high->metal_24h` score `-7.027` n `193` status `ready` deltaP `-6.5829` edge `-0.0085` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

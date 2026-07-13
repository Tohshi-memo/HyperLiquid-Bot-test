# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T18:22:26.433278+00:00`
- Price records: `672`
- Market context records: `6629`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.2103` n `203` status `ready` deltaP `-5.9401` edge `0.3139` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `2.0995` n `184` status `ready` deltaP `-0.8651` edge `0.4762` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.3945` n `184` status `ready` deltaP `9.2843` edge `0.1578` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0362` n `203` status `ready` deltaP `8.6642` edge `0.0412` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2381` n `203` status `ready` deltaP `5.9017` edge `0.0339` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2547` n `203` status `ready` deltaP `2.6363` edge `0.0005` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.5015` n `203` status `ready` deltaP `0.3717` edge `0.005` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6513` n `203` status `ready` deltaP `-1.1393` edge `-0.0076` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.8263` n `203` status `ready` deltaP `10.6264` edge `0.0112` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8574` n `203` status `ready` deltaP `3.0523` edge `0.0109` maxDD `-3.8827`
- `market_context_high->unknown_4h` score `-0.9179` n `203` status `ready` deltaP `-16.3388` edge `0.273` maxDD `-10.5788`
- `market_context_high->metal_1h` score `-1.1005` n `203` status `ready` deltaP `-2.758` edge `0.0008` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.2613` n `203` status `ready` deltaP `9.6525` edge `0.1054` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.3432` n `203` status `ready` deltaP `-1.1595` edge `-0.015` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.5386` n `203` status `ready` deltaP `3.6225` edge `-0.0002` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.6666` n `203` status `ready` deltaP `6.4978` edge `0.0832` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-1.9866` n `203` status `ready` deltaP `0.6075` edge `0.0273` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4355` n `203` status `ready` deltaP `8.9834` edge `-0.0026` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.0237` n `184` status `ready` deltaP `-2.1664` edge `0.0329` maxDD `-19.668`
- `market_context_high->fx_24h` score `-5.9988` n `184` status `ready` deltaP `-9.2353` edge `-0.0042` maxDD `-10.064`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

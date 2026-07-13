# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T15:37:31.507948+00:00`
- Price records: `672`
- Market context records: `6616`
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

- `market_context_high->unknown_24h` score `3.2667` n `174` status `ready` deltaP `1.1435` edge `0.5378` maxDD `-12.5228`
- `market_context_high->unknown_1h` score `2.125` n `204` status `ready` deltaP `-6.1671` edge `0.3083` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.1739` n `174` status `ready` deltaP `7.4415` edge `0.1517` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.1975` n `204` status `ready` deltaP `7.1768` edge `0.0273` maxDD `-4.704`
- `market_context_high->fx_1h` score `-0.2645` n `204` status `ready` deltaP `2.448` edge `0.0005` maxDD `-0.7249`
- `market_context_high->commodity_1h` score `-0.574` n `204` status `ready` deltaP `-0.1614` edge `-0.0042` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5768` n `204` status `ready` deltaP `-0.7632` edge `0.0031` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6149` n `204` status `ready` deltaP `4.2767` edge `0.0175` maxDD `-3.7803`
- `market_context_high->index_4h` score `-0.8867` n `204` status `ready` deltaP `9.7501` edge `0.0093` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.112` n `204` status `ready` deltaP `1.8933` edge `-0.0014` maxDD `-3.978`
- `market_context_high->metal_1h` score `-1.2308` n `204` status `ready` deltaP `-3.8687` edge `-0.0012` maxDD `-1.7126`
- `market_context_high->commodity_4h` score `-1.234` n `204` status `ready` deltaP `-0.3348` edge `-0.0065` maxDD `-5.6246`
- `market_context_high->unknown_4h` score `-1.4488` n `204` status `ready` deltaP `-17.68` edge `0.2377` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6184` n `204` status `ready` deltaP `2.2088` edge `-0.001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6295` n `204` status `ready` deltaP `8.1809` edge `0.068` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0368` n `204` status `ready` deltaP `5.0334` edge `0.0455` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.115` n `204` status `ready` deltaP `-0.81` edge `0.0203` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0379` n `204` status `ready` deltaP `8.1361` edge `-0.0168` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.9323` n `174` status `ready` deltaP `-1.2747` edge `0.0487` maxDD `-13.8806`
- `market_context_high->fx_24h` score `-5.7345` n `174` status `ready` deltaP `-7.33` edge `-0.001` maxDD `-9.2406`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

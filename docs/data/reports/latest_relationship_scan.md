# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T09:37:34.901342+00:00`
- Price records: `672`
- Market context records: `6696`
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

- `market_context_high->unknown_24h` score `0.7306` n `186` status `ready` deltaP `-0.0168` edge `0.469` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.3135` n `186` status `ready` deltaP `9.106` edge `0.0514` maxDD `-4.2122`
- `market_context_high->commodity_24h` score `0.214` n `186` status `ready` deltaP `9.7727` edge `0.1395` maxDD `-5.2791`
- `market_context_high->crypto_alt_1h` score `0.1051` n `186` status `ready` deltaP `6.0573` edge `0.0448` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3841` n `186` status `ready` deltaP `0.1014` edge `0.0003` maxDD `-0.6845`
- `market_context_high->unknown_1h` score `-0.4994` n `186` status `ready` deltaP `-6.3019` edge `0.0905` maxDD `-3.2083`
- `market_context_high->index_1h` score `-0.525` n `186` status `ready` deltaP `0.1223` edge `0.0033` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.5445` n `186` status `ready` deltaP `-2.8926` edge `0.002` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6471` n `186` status `ready` deltaP `-0.4282` edge `-0.0118` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9662` n `186` status `ready` deltaP `3.192` edge `0.0009` maxDD `-3.8827`
- `market_context_high->index_4h` score `-0.9901` n `186` status `ready` deltaP `9.3807` edge `-0.0015` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3486` n `186` status `ready` deltaP `6.9237` edge `-0.0014` maxDD `-3.0791`
- `market_context_high->crypto_major_4h` score `-1.6025` n `186` status `ready` deltaP `7.3662` edge `0.0769` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.7832` n `186` status `ready` deltaP `-5.1666` edge `-0.0447` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.8504` n `186` status `ready` deltaP `5.1518` edge `0.0686` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.2659` n `186` status `ready` deltaP `-3.2029` edge `0.0169` maxDD `-5.2172`
- `market_context_high->unknown_4h` score `-4.1178` n `186` status `ready` deltaP `-17.5583` edge `0.0113` maxDD `-10.3252`
- `market_context_high->fx_24h` score `-4.8375` n `186` status `ready` deltaP `-9.739` edge `-0.0035` maxDD `-7.7757`
- `market_context_high->equity_4h` score `-5.4897` n `186` status `ready` deltaP `5.8255` edge `-0.0694` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-7.0804` n `186` status `ready` deltaP `-6.8884` edge `-0.0133` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

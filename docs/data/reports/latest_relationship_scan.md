# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T15:07:27.863585+00:00`
- Price records: `672`
- Market context records: `6614`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_24h` score `3.1548` n `174` status `ready` deltaP `1.1435` edge `0.5372` maxDD `-12.8872`
- `market_context_high->unknown_1h` score `2.0981` n `205` status `ready` deltaP `-6.0537` edge `0.3053` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.1859` n `174` status `ready` deltaP `7.4415` edge `0.1527` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2658` n `205` status `ready` deltaP `2.4069` edge `0.0006` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3024` n `205` status `ready` deltaP `7.1893` edge `0.0269` maxDD `-5.755`
- `market_context_high->crypto_alt_1h` score `-0.5282` n `205` status `ready` deltaP `4.3012` edge `0.0167` maxDD `-4.7141`
- `market_context_high->commodity_1h` score `-0.5513` n `205` status `ready` deltaP `0.2154` edge `-0.0038` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.569` n `205` status `ready` deltaP `-0.6594` edge `0.0034` maxDD `-0.7564`
- `market_context_high->index_4h` score `-0.8737` n `205` status `ready` deltaP `9.939` edge `0.0097` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1116` n `205` status `ready` deltaP `1.9344` edge `-0.0002` maxDD `-4.0932`
- `market_context_high->commodity_4h` score `-1.2151` n `205` status `ready` deltaP `-0.1219` edge `-0.0055` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.2612` n `205` status `ready` deltaP `-3.7798` edge `-0.0013` maxDD `-1.9545`
- `market_context_high->unknown_4h` score `-1.5418` n `205` status `ready` deltaP `-17.9878` edge `0.232` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6199` n `205` status `ready` deltaP `2.1647` edge `-0.0009` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6811` n `205` status `ready` deltaP `7.7439` edge `0.0643` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0732` n `205` status `ready` deltaP `4.6037` edge `0.0437` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1306` n `205` status `ready` deltaP `-1.0061` edge `0.0196` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0377` n `205` status `ready` deltaP `8.0488` edge `-0.0162` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.8641` n `174` status `ready` deltaP `-1.2747` edge `0.0489` maxDD `-13.5305`
- `market_context_high->fx_24h` score `-5.7922` n `174` status `ready` deltaP `-7.33` edge `-0.0011` maxDD `-9.2843`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T10:37:28.716239+00:00`
- Price records: `672`
- Market context records: `6594`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9808`

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

- `market_context_high->unknown_24h` score `3.9324` n `162` status `ready` deltaP `5.1493` edge `0.6234` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `2.0388` n `210` status `ready` deltaP `-5.1297` edge `0.2942` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.688` n `162` status `ready` deltaP `10.1932` edge `0.1762` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2927` n `210` status `ready` deltaP `1.9062` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4532` n `210` status `ready` deltaP `6.5982` edge `0.0245` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.537` n `210` status `ready` deltaP `0.3393` edge `-0.0028` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5545` n `210` status `ready` deltaP `-0.3807` edge `0.0034` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6513` n `210` status `ready` deltaP `4.3941` edge `0.0185` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9175` n `210` status `ready` deltaP `9.142` edge `0.0094` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.2064` n `210` status `ready` deltaP `1.7822` edge `-0.0014` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2341` n `210` status `ready` deltaP `-0.5168` edge `-0.0053` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.353` n `210` status `ready` deltaP `-4.3256` edge `-0.0032` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6539` n `210` status `ready` deltaP `1.6013` edge `-0.0015` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7495` n `210` status `ready` deltaP `-17.5232` edge `0.2116` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.9074` n `210` status `ready` deltaP `6.3618` edge `0.0445` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1948` n `210` status `ready` deltaP `-1.8061` edge `0.0167` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2078` n `210` status `ready` deltaP `3.4088` edge `0.0344` maxDD `-19.2145`
- `market_context_high->fx_24h` score `-3.7843` n `162` status `ready` deltaP `-4.66` edge `-0.0006` maxDD `-9.2795`
- `market_context_high->metal_24h` score `-4.0753` n `162` status `ready` deltaP `1.3849` edge `0.0651` maxDD `-9.4488`
- `market_context_high->equity_4h` score `-4.8049` n `210` status `ready` deltaP `7.2009` edge `-0.0215` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

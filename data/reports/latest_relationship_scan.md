# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T09:37:27.297017+00:00`
- Price records: `672`
- Market context records: `6590`
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

- `market_context_high->unknown_24h` score `4.3912` n `158` status `ready` deltaP `6.4143` edge `0.6532` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.9957` n `210` status `ready` deltaP `-5.5788` edge `0.2936` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.8929` n `158` status `ready` deltaP `11.2995` edge `0.1859` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3183` n `210` status `ready` deltaP `1.4571` edge `0.0002` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4929` n `210` status `ready` deltaP `6.1491` edge `0.0224` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5012` n `210` status `ready` deltaP `0.7884` edge `-0.0012` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5802` n `210` status `ready` deltaP `-0.8298` edge `0.0031` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6677` n `210` status `ready` deltaP `4.2444` edge `0.0174` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.9136` n `210` status `ready` deltaP `9.142` edge `0.0099` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.222` n `210` status `ready` deltaP `1.6325` edge `-0.0017` maxDD `-4.2147`
- `market_context_high->commodity_4h` score `-1.2404` n `210` status `ready` deltaP `-0.5168` edge `-0.0061` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.4141` n `210` status `ready` deltaP `-4.9244` edge `-0.0043` maxDD `-2.1239`
- `market_context_high->fx_4h` score `-1.6752` n `210` status `ready` deltaP `1.2964` edge `-0.0022` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.7337` n `210` status `ready` deltaP `-17.3708` edge `0.2119` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.8917` n `210` status `ready` deltaP `6.5143` edge `0.0455` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.1878` n `210` status `ready` deltaP `-1.8061` edge `0.0176` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.2016` n `210` status `ready` deltaP `3.4088` edge `0.0352` maxDD `-19.2145`
- `market_context_high->metal_24h` score `-3.6287` n `158` status `ready` deltaP `2.3382` edge `0.0695` maxDD `-8.6648`
- `market_context_high->fx_24h` score `-3.7534` n `158` status `ready` deltaP `-4.0522` edge `-0.0007` maxDD `-9.2795`
- `market_context_high->equity_4h` score `-4.7651` n `210` status `ready` deltaP `7.3534` edge `-0.0192` maxDD `-27.1529`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

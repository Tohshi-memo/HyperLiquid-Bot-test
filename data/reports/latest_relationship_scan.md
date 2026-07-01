# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T10:37:33.154701+00:00`
- Price records: `672`
- Market context records: `5343`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->unknown_24h` score `16.5802` n `158` status `ready` deltaP `21.1916` edge `1.2494` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `5.933` n `158` status `ready` deltaP `22.431` edge `0.7898` maxDD `-28.9274`
- `market_context_high->equity_24h` score `4.6994` n `158` status `ready` deltaP `18.0599` edge `0.8341` maxDD `-40.0306`
- `market_context_high->crypto_major_4h` score `2.9779` n `194` status `ready` deltaP `13.3361` edge `0.3885` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8417` n `194` status `ready` deltaP `11.579` edge `0.3237` maxDD `-9.46`
- `market_context_high->equity_4h` score `1.998` n `194` status `ready` deltaP `10.8546` edge `0.258` maxDD `-7.4425`
- `market_context_high->index_24h` score `0.8004` n `158` status `ready` deltaP `25.0813` edge `0.0989` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.4943` n `194` status `ready` deltaP `8.0129` edge `0.0843` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.2285` n `158` status `ready` deltaP `10.3309` edge `0.0397` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.067` n `194` status `ready` deltaP `6.5174` edge `0.0125` maxDD `-1.0296`
- `market_context_high->crypto_alt_1h` score `0.0158` n `194` status `ready` deltaP `1.9461` edge `0.0845` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.0121` n `194` status `ready` deltaP `4.1916` edge `0.0956` maxDD `-6.9639`
- `market_context_high->fx_1h` score `-0.3555` n `194` status `ready` deltaP `0.5649` edge `-0.0004` maxDD `-0.5823`
- `market_context_high->index_4h` score `-0.3667` n `194` status `ready` deltaP `6.3741` edge `0.0264` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.4059` n `194` status `ready` deltaP `1.3473` edge `0.0065` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.6573` n `194` status `ready` deltaP `2.2881` edge `0.0034` maxDD `-1.567`
- `market_context_high->unknown_4h` score `-1.2603` n `194` status `ready` deltaP `7.908` edge `-0.0395` maxDD `-6.126`
- `market_context_high->commodity_1h` score `-1.4215` n `194` status `ready` deltaP `-3.1761` edge `-0.0055` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-2.4916` n `194` status `ready` deltaP `-6.4622` edge `-0.0239` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.7831` n `158` status `ready` deltaP `11.2342` edge `0.3098` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

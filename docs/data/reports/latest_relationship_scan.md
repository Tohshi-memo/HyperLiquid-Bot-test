# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T13:22:26.136212+00:00`
- Price records: `672`
- Market context records: `6712`
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

- `market_context_high->unknown_24h` score `1.4875` n `176` status `ready` deltaP `2.7935` edge `0.5473` maxDD `-12.3511`
- `market_context_high->crypto_major_1h` score `0.1038` n `176` status `ready` deltaP `8.8494` edge `0.0403` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `0.0243` n `176` status `ready` deltaP `6.0969` edge `0.0378` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.3384` n `176` status `ready` deltaP `0.6328` edge `0.0009` maxDD `-0.5468`
- `market_context_high->commodity_24h` score `-0.505` n `176` status `ready` deltaP `7.9704` edge `0.0916` maxDD `-5.2791`
- `market_context_high->index_1h` score `-0.5375` n `176` status `ready` deltaP `0.0306` edge `0.0023` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.6607` n `176` status `ready` deltaP `-4.5421` edge `-0.0019` maxDD `-1.2017`
- `market_context_high->commodity_1h` score `-0.6764` n `176` status `ready` deltaP `-0.9016` edge `-0.0124` maxDD `-2.1314`
- `market_context_high->equity_1h` score `-0.9492` n `176` status `ready` deltaP `4.0045` edge `-0.0031` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.0174` n `176` status `ready` deltaP `9.0355` edge `-0.0027` maxDD `-5.7046`
- `market_context_high->unknown_1h` score `-1.1283` n `176` status `ready` deltaP `-8.5227` edge `0.0529` maxDD `-3.2083`
- `market_context_high->fx_4h` score `-1.1964` n `176` status `ready` deltaP `7.8437` edge `0.0007` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.7332` n `176` status `ready` deltaP `-4.5177` edge `-0.0431` maxDD `-5.5853`
- `market_context_high->crypto_major_4h` score `-1.8311` n `176` status `ready` deltaP `6.5549` edge `0.053` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0039` n `176` status `ready` deltaP `4.9612` edge `0.0502` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.4393` n `176` status `ready` deltaP `-4.9474` edge `0.0063` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.5336` n `176` status `ready` deltaP `7.1231` edge `-0.0736` maxDD `-27.1529`
- `market_context_high->unknown_4h` score `-3.9422` n `176` status `ready` deltaP `-17.5444` edge `0.025` maxDD `-10.2579`
- `market_context_high->fx_24h` score `-4.258` n `176` status `ready` deltaP `-7.8756` edge `0.0013` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-7.0544` n `176` status `ready` deltaP `-6.3447` edge `-0.0136` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

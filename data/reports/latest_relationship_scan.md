# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T13:52:29.219465+00:00`
- Price records: `672`
- Market context records: `6609`
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

- `market_context_high->unknown_24h` score `3.4767` n `170` status `ready` deltaP `2.3875` edge `0.565` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.1124` n `206` status `ready` deltaP `-5.6799` edge `0.304` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2437` n `170` status `ready` deltaP `7.4741` edge `0.1573` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2775` n `206` status `ready` deltaP `2.2135` edge `0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.413` n `206` status `ready` deltaP `7.0548` edge `0.0266` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5341` n `206` status `ready` deltaP `0.4404` edge `-0.0031` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.563` n `206` status `ready` deltaP `-0.5581` edge `0.0035` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6641` n `206` status `ready` deltaP `4.3282` edge `0.0173` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8822` n `206` status `ready` deltaP `9.8212` edge `0.0094` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1732` n `206` status `ready` deltaP `1.8284` edge `0.0004` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.2106` n `206` status `ready` deltaP `-0.0637` edge `-0.0053` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.341` n `206` status `ready` deltaP `-4.2876` edge `-0.003` maxDD `-2.0797`
- `market_context_high->unknown_4h` score `-1.539` n `206` status `ready` deltaP `-17.532` edge `0.2292` maxDD `-10.5788`
- `market_context_high->fx_4h` score `-1.6231` n `206` status `ready` deltaP `2.1179` edge `-0.001` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.6926` n `206` status `ready` deltaP `7.4621` edge `0.0647` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0764` n `206` status `ready` deltaP `4.4814` edge `0.0441` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1493` n `206` status `ready` deltaP `-1.2003` edge `0.0185` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0974` n `206` status `ready` deltaP `7.502` edge `-0.0202` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.4073` n `170` status `ready` deltaP `-0.4498` edge `0.0562` maxDD `-11.5366`
- `market_context_high->fx_24h` score `-5.7326` n `170` status `ready` deltaP `-6.5051` edge `-0.0004` maxDD `-9.0496`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

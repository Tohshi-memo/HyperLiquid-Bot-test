# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T22:52:20.536892+00:00`
- Price records: `672`
- Market context records: `2605`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.9574` n `141` status `ready` deltaP `18.1258` edge `0.5751` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.3963` n `146` status `ready` deltaP `25.3488` edge `0.5486` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6431` n `146` status `ready` deltaP `15.3734` edge `0.3821` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4372` n `146` status `ready` deltaP `11.73` edge `0.1603` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `0.914` n `141` status `ready` deltaP `2.2791` edge `0.6988` maxDD `-39.0265`
- `market_context_high->unknown_4h` score `0.8309` n `146` status `ready` deltaP `7.5321` edge `0.124` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.7856` n `146` status `ready` deltaP `9.0128` edge `0.1248` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.7482` n `141` status `ready` deltaP `8.5993` edge `0.1031` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2132` n `146` status `ready` deltaP `8.8227` edge `0.0431` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0808` n `146` status `ready` deltaP `4.5402` edge `0.0124` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.4188` n `146` status `ready` deltaP `1.9502` edge `0.0184` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4578` n `146` status `ready` deltaP `5.0529` edge `0.016` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5458` n `146` status `ready` deltaP `2.0097` edge `0.0159` maxDD `-2.9823`
- `market_context_high->fx_1h` score `-0.6138` n `146` status `ready` deltaP `-0.2358` edge `0.0039` maxDD `-0.278`
- `market_context_high->metal_4h` score `-0.6266` n `146` status `ready` deltaP `4.6546` edge `0.0555` maxDD `-4.7664`
- `market_context_high->equity_1h` score `-0.7534` n `146` status `ready` deltaP `0.2215` edge `0.0196` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8876` n `146` status `ready` deltaP `-0.0731` edge `0.0123` maxDD `-0.8621`
- `market_context_high->fx_24h` score `-0.9014` n `141` status `ready` deltaP `3.7715` edge `-0.0009` maxDD `-1.6157`
- `market_context_high->equity_24h` score `-1.0428` n `141` status `ready` deltaP `11.1333` edge `-0.0941` maxDD `-2.3615`
- `market_context_high->commodity_4h` score `-1.1386` n `146` status `ready` deltaP `2.7292` edge `0.0301` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T19:22:30.475752+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11777`

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

- `market_context_high->unknown_24h` score `71.5857` n `109` status `ready` deltaP `3.8203` edge `5.9443` maxDD `-0.0104`
- `market_context_high->commodity_4h` score `1.1867` n `119` status `ready` deltaP `13.3978` edge `0.0942` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.8235` n `109` status `ready` deltaP `2.8439` edge `0.1665` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5816` n `109` status `ready` deltaP `22.3102` edge `0.0464` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4894` n `119` status `ready` deltaP `7.9626` edge `0.0293` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0059` n `119` status `ready` deltaP `5.9713` edge `-0.0043` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.3837` n `119` status `ready` deltaP `5.6857` edge `-0.0011` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.548` n `119` status `ready` deltaP `-2.1466` edge `-0.0065` maxDD `-1.6224`
- `market_context_high->index_1h` score `-1.0569` n `119` status `ready` deltaP `-2.8917` edge `-0.0154` maxDD `-1.6054`
- `market_context_high->crypto_alt_4h` score `-1.2526` n `119` status `ready` deltaP `1.6205` edge `-0.0324` maxDD `-5.7857`
- `market_context_high->crypto_alt_1h` score `-1.2639` n `119` status `ready` deltaP `-3.4753` edge `-0.0111` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-1.341` n `119` status `ready` deltaP `1.0532` edge `0.0047` maxDD `-3.211`
- `market_context_high->equity_1h` score `-1.4042` n `119` status `ready` deltaP `3.1272` edge `-0.0444` maxDD `-10.5179`
- `market_context_high->index_24h` score `-1.5222` n `109` status `ready` deltaP `-6.0107` edge `0.0644` maxDD `-7.8922`
- `market_context_high->index_4h` score `-1.7587` n `119` status `ready` deltaP `-8.8692` edge `-0.0409` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-2.7177` n `119` status `ready` deltaP `-7.4616` edge `-0.0394` maxDD `-7.6533`
- `market_context_high->crypto_alt_24h` score `-2.7775` n `109` status `ready` deltaP `-4.7175` edge `-0.0557` maxDD `-4.5445`
- `market_context_high->commodity_24h` score `-6.0633` n `109` status `ready` deltaP `10.989` edge `0.0259` maxDD `-52.7876`
- `market_context_high->equity_4h` score `-6.2812` n `119` status `ready` deltaP `-1.0207` edge `-0.2696` maxDD `-34.9766`
- `market_context_high->crypto_major_4h` score `-7.3446` n `119` status `ready` deltaP `-6.7578` edge `-0.1458` maxDD `-27.3622`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

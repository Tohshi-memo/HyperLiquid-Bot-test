# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T18:52:38.837968+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9856`

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

- `market_context_high->unknown_24h` score `24.5368` n `64` status `ready` deltaP `20.6597` edge `1.9113` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4786` n `89` status `ready` deltaP `1.5449` edge `0.5458` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `1.558` n `64` status `ready` deltaP `13.1944` edge `0.1613` maxDD `-3.5544`
- `market_context_high->commodity_4h` score `1.3438` n `89` status `ready` deltaP `16.2921` edge `0.088` maxDD `-2.7703`
- `market_context_high->commodity_1h` score `0.185` n `90` status `ready` deltaP `5.0432` edge `0.0234` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1746` n `90` status `ready` deltaP `7.9042` edge `-0.0033` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1533` n `89` status `ready` deltaP `14.677` edge `0.0078` maxDD `-1.8797`
- `market_context_high->fx_24h` score `0.0029` n `64` status `ready` deltaP `10.9375` edge `0.0479` maxDD `-4.3126`
- `market_context_high->metal_24h` score `-0.3186` n `64` status `ready` deltaP `-9.7222` edge `0.1408` maxDD `-2.6802`
- `market_context_high->index_1h` score `-0.5479` n `90` status `ready` deltaP `0.2928` edge `-0.0188` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5511` n `90` status `ready` deltaP `-1.7565` edge `-0.0095` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.7281` n `90` status `ready` deltaP `-2.3087` edge `-0.0069` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7714` n `89` status `ready` deltaP `2.2901` edge `0.0093` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8658` n `89` status `ready` deltaP `4.3334` edge `-0.0009` maxDD `-5.7857`
- `market_context_high->commodity_24h` score `-0.9332` n `64` status `ready` deltaP `16.8403` edge `0.0904` maxDD `-19.7844`
- `market_context_high->equity_1h` score `-1.7266` n `90` status `ready` deltaP `4.3513` edge `-0.0968` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0125` n `89` status `ready` deltaP `-11.6505` edge `-0.0549` maxDD `-4.7021`
- `market_context_high->index_24h` score `-3.0037` n `64` status `ready` deltaP `-14.2361` edge `-0.0707` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.4727` n `90` status `ready` deltaP `-12.159` edge `-0.071` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.49` n `90` status `ready` deltaP `2.0492` edge `-0.2598` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T19:37:43.938106+00:00`
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

- `market_context_high->unknown_24h` score `23.1244` n `67` status `ready` deltaP `20.2089` edge `1.7966` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3155` n `90` status `ready` deltaP `1.2906` edge `0.5339` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.3515` n `90` status `ready` deltaP `16.0129` edge `0.0905` maxDD `-2.7703`
- `market_context_high->crypto_alt_24h` score `0.8936` n `67` status `ready` deltaP `10.186` edge `0.1426` maxDD `-3.8833`
- `market_context_high->fx_24h` score `0.2743` n `67` status `ready` deltaP `13.1452` edge `0.0558` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.173` n `90` status `ready` deltaP `4.8935` edge `0.0234` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1566` n `90` status `ready` deltaP `14.6816` edge `0.0082` maxDD `-1.8797`
- `market_context_high->fx_1h` score `0.1362` n `90` status `ready` deltaP `7.4551` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->metal_24h` score `0.0188` n `67` status `ready` deltaP `-7.5534` edge `0.1696` maxDD `-2.6802`
- `market_context_high->metal_1h` score `-0.5418` n `90` status `ready` deltaP `-1.6068` edge `-0.0093` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5744` n `90` status `ready` deltaP `-0.1563` edge `-0.0192` maxDD `-1.6054`
- `market_context_high->crypto_alt_1h` score `-0.7258` n `90` status `ready` deltaP `-2.3087` edge `-0.0066` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7772` n `90` status `ready` deltaP `2.2696` edge `0.0087` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8264` n `90` status `ready` deltaP `4.4004` edge `0.0037` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.7227` n `90` status `ready` deltaP `4.3513` edge `-0.0963` maxDD `-10.619`
- `market_context_high->commodity_24h` score `-1.8434` n `67` status `ready` deltaP `14.4926` edge `0.0474` maxDD `-23.4276`
- `market_context_high->index_4h` score `-1.9987` n `90` status `ready` deltaP `-11.521` edge `-0.054` maxDD `-4.7021`
- `market_context_high->index_24h` score `-2.6862` n `67` status `ready` deltaP `-12.3445` edge `-0.0426` maxDD `-7.8922`
- `market_context_high->crypto_major_1h` score `-3.432` n `90` status `ready` deltaP `-11.8596` edge `-0.0696` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4336` n `90` status `ready` deltaP `2.3486` edge `-0.2571` maxDD `-1.2421`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

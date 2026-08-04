# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T23:37:30.090063+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11823`

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

- `market_context_high->unknown_24h` score `17.0548` n `83` status `ready` deltaP `17.7188` edge `1.3074` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4697` n `90` status `ready` deltaP `1.7479` edge `0.5437` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6296` n `90` status `ready` deltaP `17.6897` edge `0.1025` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.2041` n `83` status `ready` deltaP `1.3659` edge `0.2621` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9528` n `83` status `ready` deltaP `24.0189` edge `0.0826` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2965` n `90` status `ready` deltaP `5.7917` edge `0.0277` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1003` n `90` status `ready` deltaP `7.006` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0696` n `90` status `ready` deltaP `13.1572` edge `0.0072` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3932` n `83` status `ready` deltaP `7.095` edge `0.0466` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.5309` n `90` status `ready` deltaP `-1.4571` edge `-0.0089` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5651` n `90` status `ready` deltaP `-0.1563` edge `-0.018` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6737` n `90` status `ready` deltaP `3.794` edge `0.0118` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7258` n `90` status `ready` deltaP `-2.3087` edge `-0.0066` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-1.0038` n `90` status `ready` deltaP `3.0284` edge `-0.0099` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6595` n `90` status `ready` deltaP `4.3513` edge `-0.0882` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.7747` n `83` status `ready` deltaP `-5.9153` edge `0.0314` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0333` n `90` status `ready` deltaP `-11.8259` edge `-0.0564` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3613` n `90` status `ready` deltaP `-11.1111` edge `-0.0687` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4084` n `90` status `ready` deltaP `2.0492` edge `-0.253` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-6.0541` n `83` status `ready` deltaP `5.474` edge `-0.1212` maxDD `-42.9833`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

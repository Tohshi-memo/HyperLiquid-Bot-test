# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T23:22:33.024337+00:00`
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

- `market_context_high->unknown_24h` score `17.3699` n `82` status `ready` deltaP `17.8777` edge `1.3326` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.4157` n `90` status `ready` deltaP `1.7479` edge `0.5392` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.6272` n `90` status `ready` deltaP `17.6897` edge `0.1023` maxDD `-2.7703`
- `market_context_high->metal_24h` score `1.1453` n `82` status `ready` deltaP `0.9104` edge `0.2576` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.9144` n `82` status `ready` deltaP `23.4459` edge `0.0815` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.2989` n `90` status `ready` deltaP `5.7917` edge `0.0279` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.1003` n `90` status `ready` deltaP `7.006` edge `-0.0035` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.0775` n `90` status `ready` deltaP `13.3096` edge `0.0072` maxDD `-1.8797`
- `market_context_high->crypto_alt_24h` score `-0.3836` n `82` status `ready` deltaP `6.8132` edge `0.0497` maxDD `-4.5445`
- `market_context_high->metal_1h` score `-0.541` n `90` status `ready` deltaP `-1.6068` edge `-0.0092` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.5682` n `90` status `ready` deltaP `-0.1563` edge `-0.0184` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.6832` n `90` status `ready` deltaP `3.6416` edge `0.0116` maxDD `-3.211`
- `market_context_high->crypto_alt_1h` score `-0.7421` n `90` status `ready` deltaP `-2.4584` edge `-0.0077` maxDD `-3.0178`
- `market_context_high->crypto_alt_4h` score `-0.9984` n `90` status `ready` deltaP `3.0284` edge `-0.0092` maxDD `-5.7857`
- `market_context_high->equity_1h` score `-1.6806` n `90` status `ready` deltaP `4.3513` edge `-0.0909` maxDD `-10.619`
- `market_context_high->index_24h` score `-1.8143` n `82` status `ready` deltaP `-6.2119` edge `0.0283` maxDD `-7.8922`
- `market_context_high->index_4h` score `-2.0302` n `90` status `ready` deltaP `-11.8259` edge `-0.056` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.3913` n `90` status `ready` deltaP `-11.2608` edge `-0.0702` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4144` n `90` status `ready` deltaP `2.0492` edge `-0.2535` maxDD `-1.2421`
- `market_context_high->commodity_24h` score `-5.8135` n `82` status `ready` deltaP `5.9028` edge `-0.1126` maxDD `-41.7658`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

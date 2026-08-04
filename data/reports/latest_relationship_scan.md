# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T16:52:29.510445+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9839`

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

- `market_context_high->unknown_24h` score `28.9969` n `56` status `ready` deltaP `21.8254` edge `2.2752` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.2767` n `89` status `ready` deltaP `0.3254` edge `0.5371` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `3.8` n `56` status `ready` deltaP `22.7926` edge `0.2332` maxDD `-2.1455`
- `market_context_high->commodity_24h` score `1.6845` n `56` status `ready` deltaP `24.6032` edge `0.226` maxDD `-10.5916`
- `market_context_high->commodity_4h` score `1.1827` n `89` status `ready` deltaP `15.0726` edge `0.0827` maxDD `-2.7703`
- `market_context_high->fx_1h` score `0.2129` n `90` status `ready` deltaP `8.3533` edge `-0.0031` maxDD `-0.7878`
- `market_context_high->fx_4h` score `0.1897` n `89` status `ready` deltaP `15.2868` edge `0.0084` maxDD `-1.8797`
- `market_context_high->commodity_1h` score `0.1802` n `90` status `ready` deltaP `5.0432` edge `0.023` maxDD `-1.3282`
- `market_context_high->index_1h` score `-0.4997` n `90` status `ready` deltaP `1.0413` edge `-0.0176` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5472` n `90` status `ready` deltaP `-1.7565` edge `-0.009` maxDD `-1.6224`
- `market_context_high->crypto_alt_1h` score `-0.672` n `90` status `ready` deltaP `-1.7099` edge `-0.0037` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.691` n `89` status `ready` deltaP `3.3571` edge `0.0125` maxDD `-3.211`
- `market_context_high->fx_24h` score `-0.8104` n `56` status `ready` deltaP `3.621` edge `0.0289` maxDD `-4.3126`
- `market_context_high->crypto_alt_4h` score `-0.8225` n `89` status `ready` deltaP `4.7907` edge `0.0016` maxDD `-5.7857`
- `market_context_high->metal_24h` score `-1.5136` n `56` status `ready` deltaP `-15.9474` edge `0.0291` maxDD `-2.6802`
- `market_context_high->equity_1h` score `-1.6791` n `90` status `ready` deltaP `4.8004` edge `-0.0937` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9473` n `89` status `ready` deltaP `-11.0407` edge `-0.0506` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4104` n `90` status `ready` deltaP `-11.8596` edge `-0.0678` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.4972` n `90` status `ready` deltaP `2.0492` edge `-0.2604` maxDD `-1.2421`
- `market_context_high->index_24h` score `-3.9714` n `56` status `ready` deltaP `-19.9901` edge `-0.1564` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-04T17:22:40.113434+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9855`

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

- `market_context_high->unknown_24h` score `27.7944` n `58` status `ready` deltaP `21.5398` edge `2.1769` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `5.3395` n `89` status `ready` deltaP `0.6303` edge `0.5403` maxDD `-3.6303`
- `market_context_high->crypto_alt_24h` score `3.2178` n `58` status `ready` deltaP `20.1448` edge `0.2134` maxDD `-2.364`
- `market_context_high->commodity_4h` score `1.2239` n `89` status `ready` deltaP `15.3775` edge `0.0841` maxDD `-2.7703`
- `market_context_high->commodity_24h` score `1.0048` n `58` status `ready` deltaP `22.4258` edge `0.1894` maxDD `-12.8071`
- `market_context_high->fx_1h` score `0.1877` n `90` status `ready` deltaP `8.0539` edge `-0.0032` maxDD `-0.7878`
- `market_context_high->commodity_1h` score `0.1862` n `90` status `ready` deltaP `5.0432` edge `0.0235` maxDD `-1.3282`
- `market_context_high->fx_4h` score `0.1722` n `89` status `ready` deltaP `14.9819` edge `0.0082` maxDD `-1.8797`
- `market_context_high->index_1h` score `-0.5199` n `90` status `ready` deltaP `0.7419` edge `-0.0182` maxDD `-1.6054`
- `market_context_high->metal_1h` score `-0.5683` n `90` status `ready` deltaP `-2.0559` edge `-0.0097` maxDD `-1.6224`
- `market_context_high->fx_24h` score `-0.5933` n `58` status `ready` deltaP `5.6753` edge `0.0333` maxDD `-4.3126`
- `market_context_high->crypto_alt_1h` score `-0.704` n `90` status `ready` deltaP `-2.0093` edge `-0.0058` maxDD `-3.0178`
- `market_context_high->metal_4h` score `-0.7178` n `89` status `ready` deltaP `3.0522` edge `0.0111` maxDD `-3.211`
- `market_context_high->crypto_alt_4h` score `-0.8501` n `89` status `ready` deltaP `4.4858` edge `0.0001` maxDD `-5.7857`
- `market_context_high->metal_24h` score `-1.175` n `58` status `ready` deltaP `-14.3858` edge `0.0621` maxDD `-2.6802`
- `market_context_high->equity_1h` score `-1.7118` n `90` status `ready` deltaP `4.501` edge `-0.0959` maxDD `-10.619`
- `market_context_high->index_4h` score `-1.9756` n `89` status `ready` deltaP `-11.3456` edge `-0.0522` maxDD `-4.7021`
- `market_context_high->crypto_major_1h` score `-3.4667` n `90` status `ready` deltaP `-12.159` edge `-0.0705` maxDD `-7.6533`
- `market_context_high->unknown_1h` score `-3.478` n `90` status `ready` deltaP `2.1989` edge `-0.2598` maxDD `-1.2421`
- `market_context_high->index_24h` score `-3.7029` n `58` status `ready` deltaP `-18.3668` edge `-0.1328` maxDD `-7.8922`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

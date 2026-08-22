# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T13:43:13.139061+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14754`

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

- `market_context_high->unknown_1h` score `0.8253` n `147` status `ready` deltaP `6.2691` edge `0.0497` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5618` n `141` status `ready` deltaP `18.59` edge `-0.0332` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1197` n `141` status `ready` deltaP `8.355` edge `0.0099` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0112` n `147` status `ready` deltaP `7.0746` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0395` n `147` status `ready` deltaP `3.9044` edge `0.0048` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2427` n `141` status `ready` deltaP `7.1225` edge `-0.017` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.311` n `147` status `ready` deltaP `1.0337` edge `-0.0049` maxDD `-0.6822`
- `market_context_high->equity_1h` score `-0.3762` n `147` status `ready` deltaP `3.9992` edge `0.0321` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.4704` n `141` status `ready` deltaP `4.7623` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7882` n `141` status `ready` deltaP `-2.6736` edge `0.0018` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0253` n `147` status `ready` deltaP `-7.7284` edge `-0.0025` maxDD `-1.1941`
- `market_context_high->fx_24h` score `-1.6888` n `127` status `ready` deltaP `1.4176` edge `0.0108` maxDD `-2.2121`
- `market_context_high->equity_4h` score `-1.7549` n `141` status `ready` deltaP `-1.8855` edge `0.0681` maxDD `-16.1079`
- `market_context_high->commodity_24h` score `-2.1655` n `127` status `ready` deltaP `-6.2295` edge `0.0444` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.257` n `141` status `ready` deltaP `4.1602` edge `-0.069` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.5059` n `147` status `ready` deltaP `-2.7373` edge `-0.0411` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.559` n `147` status `ready` deltaP `-5.3352` edge `-0.1151` maxDD `-7.6729`
- `market_context_high->index_24h` score `-4.5407` n `127` status `ready` deltaP `-8.9744` edge `-0.0432` maxDD `-20.9951`
- `market_context_high->metal_24h` score `-5.5097` n `127` status `ready` deltaP `-25.257` edge `-0.2072` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.6358` n `141` status `ready` deltaP `-1.2087` edge `-0.3286` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

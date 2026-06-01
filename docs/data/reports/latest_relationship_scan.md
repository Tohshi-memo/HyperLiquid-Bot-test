# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T01:37:21.328615+00:00`
- Price records: `672`
- Market context records: `2516`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.0051` n `119` status `ready` deltaP `19.548` edge `0.3196` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7707` n `152` status `ready` deltaP `21.7586` edge `0.5204` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8986` n `152` status `ready` deltaP `17.9075` edge `0.3865` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2333` n `119` status `ready` deltaP `11.6363` edge `0.598` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0775` n `152` status `ready` deltaP `11.8501` edge `0.1991` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0176` n `162` status `ready` deltaP `8.435` edge `0.1473` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6357` n `162` status `ready` deltaP `7.9489` edge `0.1194` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `-0.0163` n `119` status `ready` deltaP `0.8782` edge `0.6878` maxDD `-43.6595`
- `market_context_high->index_24h` score `-0.0198` n `119` status `ready` deltaP `3.1994` edge `0.0751` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1156` n `152` status `ready` deltaP `6.948` edge `0.0282` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1622` n `119` status `ready` deltaP `17.8324` edge `0.0203` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3859` n `162` status `ready` deltaP `3.9089` edge `0.0123` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4471` n `162` status `ready` deltaP `0.8021` edge `0.0068` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4484` n `162` status `ready` deltaP `1.1791` edge `0.0106` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4494` n `162` status `ready` deltaP `1.6837` edge `0.0048` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.536` n `162` status `ready` deltaP `1.8888` edge `0.0147` maxDD `-3.0902`
- `market_context_high->fx_24h` score `-0.8078` n `119` status `ready` deltaP `3.9478` edge `0.0052` maxDD `-2.4729`
- `market_context_high->equity_1h` score `-0.8221` n `162` status `ready` deltaP `-0.0979` edge `0.016` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.9205` n `152` status `ready` deltaP `-0.2006` edge `0.0106` maxDD `-0.8774`
- `market_context_high->commodity_4h` score `-1.0225` n `152` status `ready` deltaP `3.5221` edge `0.0397` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

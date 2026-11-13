# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T11:22:37.867062+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `384.7063` n `74` status `ready` deltaP `5.9779` edge `32.0331` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.7174` n `53` status `ready` deltaP `31.9314` edge `2.5842` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.695` n `74` status `ready` deltaP `27.5713` edge `2.0742` maxDD `-7.3408`
- `market_context_high->crypto_alt_24h` score `17.4708` n `74` status `ready` deltaP `50.0938` edge `1.4313` maxDD `-20.0822`
- `news_risk_high->crypto_major_24h` score `14.1652` n `53` status `ready` deltaP `42.3906` edge `1.73` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5044` n `53` status `ready` deltaP `35.1731` edge `0.7539` maxDD `-7.0416`
- `market_context_high->metal_24h` score `6.6113` n `74` status `ready` deltaP `41.5353` edge `0.3433` maxDD `-2.541`
- `news_risk_high->commodity_24h` score `5.9613` n `53` status `ready` deltaP `38.0208` edge `0.2433` maxDD `0.0`
- `market_context_high->index_24h` score `4.8192` n `74` status `ready` deltaP `25.9572` edge `0.2377` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.612` n `53` status `ready` deltaP `44.1096` edge `0.1279` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1351` n `53` status `ready` deltaP `24.0959` edge `0.2143` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.2854` n `53` status `ready` deltaP `17.5658` edge `0.2197` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.2199` n `53` status `ready` deltaP `19.6762` edge `0.2859` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1229` n `53` status `ready` deltaP `28.6931` edge `0.0943` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.1048` n `53` status `ready` deltaP `19.9816` edge `0.7154` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1187` n `53` status `ready` deltaP `24.9915` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.949` n `53` status `ready` deltaP `20.1363` edge `0.0718` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8594` n `53` status `ready` deltaP `26.346` edge `0.2266` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1472` n `53` status `ready` deltaP `15.8287` edge `0.0202` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6244` n `53` status `ready` deltaP `17.1449` edge `0.0637` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T22:07:26.633314+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `311.0864` n `84` status `ready` deltaP `6.4732` edge `25.8948` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.8166` n `94` status `ready` deltaP `8.1053` edge `6.3088` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.4297` n `53` status `ready` deltaP `24.4661` edge `2.36` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.4123` n `84` status `ready` deltaP `22.1974` edge `1.707` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.7173` n `53` status `ready` deltaP `37.1823` edge `1.4509` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1665` n `53` status `ready` deltaP `32.4292` edge `0.6607` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.6655` n `84` status `ready` deltaP `42.2619` edge `1.2388` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3223` n `53` status `ready` deltaP `43.2292` edge `0.322` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3131` n `84` status `ready` deltaP `38.8641` edge `0.3083` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.619` n `53` status `ready` deltaP `43.9571` edge `0.1295` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.2065` n `84` status `ready` deltaP `24.1568` edge `0.199` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.7982` n `53` status `ready` deltaP `22.3598` edge `0.1978` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0263` n `53` status `ready` deltaP `17.1167` edge `0.2011` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9271` n `53` status `ready` deltaP `26.7114` edge `0.0912` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6823` n `53` status `ready` deltaP `19.6762` edge `0.2411` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2205` n `53` status `ready` deltaP `26.1891` edge `0.0359` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6243` n `53` status `ready` deltaP `17.6973` edge `0.061` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.3485` n `53` status `ready` deltaP `24.5168` edge `0.1733` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.2279` n `53` status `ready` deltaP `12.3427` edge `0.5257` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1543` n `53` status `ready` deltaP `16.2778` edge `0.0178` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

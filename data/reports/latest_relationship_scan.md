# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T12:37:27.588311+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9354`

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

- `market_context_high->unknown_24h` score `573.2255` n `66` status `ready` deltaP `4.5139` edge `47.7387` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.7153` n `53` status `ready` deltaP `38.355` edge `3.0412` maxDD `-3.6503`
- `market_context_high->equity_24h` score `34.9616` n `66` status `ready` deltaP `33.3807` edge `2.8451` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `22.8266` n `66` status `ready` deltaP `57.7652` edge `1.6248` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.2742` n `53` status `ready` deltaP `42.0434` edge `2.0027` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2` n `53` status `ready` deltaP `35.7829` edge `0.8078` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9984` n `53` status `ready` deltaP `48.0903` edge `0.2626` maxDD `0.0`
- `market_context_high->index_24h` score `6.9283` n `66` status `ready` deltaP `39.6464` edge `0.3222` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.5703` n `53` status `ready` deltaP `35.9014` edge `0.2552` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.1962` n `66` status `ready` deltaP `51.5152` edge `0.4119` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8564` n `53` status `ready` deltaP `45.634` edge `0.1381` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0096` n `53` status `ready` deltaP `20.7433` edge `0.3446` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5756` n `53` status `ready` deltaP `18.7634` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2223` n `53` status `ready` deltaP `29.4553` edge `0.0975` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.2065` n `53` status `ready` deltaP `22.5754` edge `0.077` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.1703` n `53` status `ready` deltaP `25.2909` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `2.1668` n `53` status `ready` deltaP `26.4985` edge `0.265` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.9961` n `53` status `ready` deltaP `14.4261` edge `0.6103` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.225` n `53` status `ready` deltaP `16.5772` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.725` n `53` status `ready` deltaP `17.4443` edge `0.0746` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

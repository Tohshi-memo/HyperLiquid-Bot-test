# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T21:52:28.931312+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11772`

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

- `market_context_high->unknown_24h` score `312.6668` n `84` status `ready` deltaP `6.4732` edge `26.0265` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `75.813` n `94` status `ready` deltaP `8.1053` edge `6.3085` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `29.3079` n `53` status `ready` deltaP `24.2925` edge `2.351` maxDD `-3.6503`
- `market_context_high->equity_24h` score `21.2905` n `84` status `ready` deltaP `22.0238` edge `1.698` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.6854` n `53` status `ready` deltaP `37.1823` edge `1.4468` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.1315` n `53` status `ready` deltaP `32.2768` edge `0.6588` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `8.6128` n `84` status `ready` deltaP `42.0883` edge `1.2332` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.3379` n `53` status `ready` deltaP `43.2292` edge `0.3233` maxDD `0.0`
- `market_context_high->metal_24h` score `6.2836` n `84` status `ready` deltaP `38.6905` edge `0.307` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6056` n `53` status `ready` deltaP `43.8047` edge `0.1294` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.1818` n `84` status `ready` deltaP `23.9831` edge `0.1981` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.7735` n `53` status `ready` deltaP `22.1861` edge `0.1969` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.0275` n `53` status `ready` deltaP `17.1167` edge `0.2012` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9307` n `53` status `ready` deltaP `26.7114` edge `0.0915` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.6823` n `53` status `ready` deltaP `19.6762` edge `0.2411` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.2337` n `53` status `ready` deltaP `26.3388` edge `0.036` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6097` n `53` status `ready` deltaP `17.5449` edge `0.0608` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.3547` n `53` status `ready` deltaP `24.5168` edge `0.1741` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.1752` n `53` status `ready` deltaP `12.1691` edge `0.5201` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1555` n `53` status `ready` deltaP `16.2778` edge `0.0179` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

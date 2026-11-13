# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T02:07:28.112968+00:00`
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

- `market_context_high->unknown_24h` score `296.2009` n `84` status `ready` deltaP `6.2996` edge `24.6555` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `62.2814` n `94` status `ready` deltaP `7.8004` edge `5.1829` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.6572` n `53` status `ready` deltaP `26.5494` edge `2.4484` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.6398` n `84` status `ready` deltaP `24.2807` edge `1.7954` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.2078` n `53` status `ready` deltaP `38.9184` edge `1.5022` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.4609` n `53` status `ready` deltaP `32.7341` edge `0.6832` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.3388` n `84` status `ready` deltaP `45.0397` edge `1.3066` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.0547` n `53` status `ready` deltaP `43.2292` edge `0.2997` maxDD `0.0`
- `market_context_high->metal_24h` score `6.65` n `84` status `ready` deltaP `40.6002` edge `0.3248` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.4688` n `53` status `ready` deltaP `42.8901` edge `0.1241` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3514` n `84` status `ready` deltaP `24.6776` edge `0.2076` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9431` n `53` status `ready` deltaP `22.8806` edge `0.2064` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0995` n `53` status `ready` deltaP `28.2358` edge `0.0954` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.018` n `53` status `ready` deltaP `16.8173` edge `0.2024` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6243` n `53` status `ready` deltaP `19.3713` edge `0.2383` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.0995` n `53` status `ready` deltaP `24.9915` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.9012` n `53` status `ready` deltaP `15.1205` edge `0.5935` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6907` n `53` status `ready` deltaP `18.0022` edge `0.0645` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4212` n `53` status `ready` deltaP `24.6692` edge `0.1816` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.098` n `53` status `ready` deltaP `15.5293` edge `0.0181` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T16:07:42.647784+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_24h` score `574.7447` n `66` status `ready` deltaP `4.5139` edge `47.8653` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.5565` n `53` status `ready` deltaP `40.7856` edge `3.0951` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.8028` n `66` status `ready` deltaP `35.8113` edge `2.899` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.8838` n `66` status `ready` deltaP `57.7652` edge `1.7129` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.2196` n `53` status `ready` deltaP `42.3906` edge `2.1216` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.3316` n `53` status `ready` deltaP `36.3926` edge `0.8147` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2805` n `53` status `ready` deltaP `50.5208` edge `0.2699` maxDD `0.0`
- `market_context_high->index_24h` score `7.1188` n `66` status `ready` deltaP `41.3825` edge `0.3265` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.7608` n `53` status `ready` deltaP `37.6375` edge `0.2595` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2578` n `66` status `ready` deltaP `51.5152` edge `0.4198` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8586` n `53` status `ready` deltaP `45.4815` edge `0.1393` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.3526` n `53` status `ready` deltaP `20.5908` edge `0.3742` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6739` n `53` status `ready` deltaP `19.5119` edge `0.2391` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.4024` n `53` status `ready` deltaP `31.437` edge `0.0993` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.6833` n `53` status `ready` deltaP `14.4261` edge `0.6984` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.4416` n `53` status `ready` deltaP `26.8033` edge `0.2982` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.3916` n `53` status `ready` deltaP `24.7095` edge `0.0782` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2541` n `53` status `ready` deltaP `26.1891` edge `0.0387` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3867` n `53` status `ready` deltaP `18.5233` edge `0.0222` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8716` n `53` status `ready` deltaP `18.1928` edge `0.0884` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

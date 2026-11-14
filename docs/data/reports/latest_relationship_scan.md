# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T16:22:30.708381+00:00`
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

- `market_context_high->unknown_24h` score `574.8683` n `66` status `ready` deltaP `4.5139` edge `47.8756` maxDD `0.0`
- `news_risk_high->equity_24h` score `39.5836` n `53` status `ready` deltaP `40.9592` edge `3.0962` maxDD `-3.6503`
- `market_context_high->equity_24h` score `35.8299` n `66` status `ready` deltaP `35.9849` edge `2.9001` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `23.9894` n `66` status `ready` deltaP `57.7652` edge `1.7217` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `17.3043` n `53` status `ready` deltaP `42.5642` edge `2.1313` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.363` n `53` status `ready` deltaP `36.5451` edge `0.8163` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2992` n `53` status `ready` deltaP `50.6944` edge `0.2703` maxDD `0.0`
- `market_context_high->index_24h` score `7.1188` n `66` status `ready` deltaP `41.3825` edge `0.3265` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.7608` n `53` status `ready` deltaP `37.6375` edge `0.2595` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.2617` n `66` status `ready` deltaP `51.5152` edge `0.4203` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8622` n `53` status `ready` deltaP `45.4815` edge `0.1396` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.4224` n `53` status `ready` deltaP `20.7433` edge `0.379` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6919` n `53` status `ready` deltaP `19.6616` edge `0.2396` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.417` n `53` status `ready` deltaP `31.5894` edge `0.0995` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.7519` n `53` status `ready` deltaP `14.4261` edge `0.7072` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `2.4901` n `53` status `ready` deltaP `26.9558` edge `0.3034` maxDD `-10.1088`
- `news_risk_high->index_4h` score `2.4062` n `53` status `ready` deltaP `24.8619` edge `0.0784` maxDD `-0.8235`
- `news_risk_high->metal_1h` score `2.2565` n `53` status `ready` deltaP `26.1891` edge `0.0389` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.3879` n `53` status `ready` deltaP `18.5233` edge `0.0223` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.8911` n `53` status `ready` deltaP `18.3425` edge `0.0899` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

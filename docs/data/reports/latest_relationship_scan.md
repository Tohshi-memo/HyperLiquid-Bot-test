# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T12:07:27.005670+00:00`
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

- `market_context_high->unknown_24h` score `573.0791` n `66` status `ready` deltaP `4.5139` edge `47.7265` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.5555` n `53` status `ready` deltaP `38.0078` edge `3.0302` maxDD `-3.6503`
- `market_context_high->equity_24h` score `34.8018` n `66` status `ready` deltaP `33.0335` edge `2.8341` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `22.7282` n `66` status `ready` deltaP `57.7652` edge `1.6166` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `16.1821` n `53` status `ready` deltaP `42.0434` edge `1.9909` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.217` n `53` status `ready` deltaP `35.9353` edge `0.8082` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9562` n `53` status `ready` deltaP `47.7431` edge `0.2614` maxDD `0.0`
- `market_context_high->index_24h` score `6.8885` n `66` status `ready` deltaP `39.2992` edge `0.3212` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.5306` n `53` status `ready` deltaP `35.5542` edge `0.2542` maxDD `-0.4279`
- `market_context_high->metal_24h` score `5.1861` n `66` status `ready` deltaP `51.5152` edge `0.4106` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8819` n `53` status `ready` deltaP `45.9388` edge `0.1382` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.0434` n `53` status `ready` deltaP `20.8957` edge `0.3464` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5637` n `53` status `ready` deltaP `18.6137` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.2199` n `53` status `ready` deltaP `29.4553` edge `0.0973` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.1809` n `53` status `ready` deltaP `22.2705` edge `0.0769` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1715` n `53` status `ready` deltaP `26.4985` edge `0.2656` maxDD `-10.1088`
- `news_risk_high->metal_1h` score `2.1703` n `53` status `ready` deltaP `25.2909` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `1.9322` n `53` status `ready` deltaP `14.4261` edge `0.6021` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.225` n `53` status `ready` deltaP `16.5772` edge `0.0217` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7359` n `53` status `ready` deltaP `17.594` edge `0.075` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

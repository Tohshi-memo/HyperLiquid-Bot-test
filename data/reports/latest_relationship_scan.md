# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T05:37:27.415017+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10410`

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

- `market_context_high->unknown_24h` score `433.1753` n `75` status `ready` deltaP `2.1944` edge `36.0974` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.8801` n `53` status `ready` deltaP `35.23` edge `2.9091` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.6464` n `75` status `ready` deltaP `29.7708` edge `2.3429` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.6386` n `75` status `ready` deltaP `47.5834` edge `1.3208` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.392` n `53` status `ready` deltaP `42.0434` edge `1.8896` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2692` n `53` status `ready` deltaP `36.3926` edge `0.8095` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.4487` n `53` status `ready` deltaP `43.2292` edge `0.2492` maxDD `0.0`
- `market_context_high->index_24h` score `5.7565` n `75` status `ready` deltaP `33.5486` edge `0.2652` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.0755` n `53` status `ready` deltaP `31.5611` edge `0.2429` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `5.0745` n `53` status `ready` deltaP `48.2254` edge `0.139` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.2861` n `75` status `ready` deltaP `41.3334` edge `0.3631` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.1336` n `53` status `ready` deltaP `21.9628` edge `0.3468` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6116` n `53` status `ready` deltaP `19.0628` edge `0.2369` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0361` n `53` status `ready` deltaP `27.4736` edge `0.0952` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3188` n `53` status `ready` deltaP `27.0873` edge `0.0381` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1675` n `53` status `ready` deltaP `22.118` edge `0.0768` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1019` n `53` status `ready` deltaP `26.346` edge `0.2577` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6092` n `53` status `ready` deltaP `14.4261` edge `0.5607` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2382` n `53` status `ready` deltaP `16.7269` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7328` n `53` status `ready` deltaP `17.7437` edge `0.0736` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T08:37:27.266080+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11174`

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

- `market_context_high->unknown_24h` score `287.1732` n `79` status `ready` deltaP `6.149` edge `23.9042` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `79.4918` n `89` status `ready` deltaP `6.2551` edge `6.6274` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.3119` n `53` status `ready` deltaP `31.0633` edge `2.5562` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.247` n `79` status `ready` deltaP `27.8151` edge `1.9891` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.6887` n `53` status `ready` deltaP `41.5226` edge `1.6747` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.424` n `53` status `ready` deltaP `35.1731` edge `0.7472` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.2704` n `79` status `ready` deltaP `47.7453` edge `1.408` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.2975` n `79` status `ready` deltaP `44.1346` edge `0.3552` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.1771` n `53` status `ready` deltaP `38.8889` edge `0.2555` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.567` n `53` status `ready` deltaP `43.6523` edge `0.1272` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.5636` n `79` status `ready` deltaP `25.2901` edge `0.2212` maxDD `-0.0934`
- `news_risk_high->index_24h` score `4.1255` n `53` status `ready` deltaP `24.0959` edge `0.2135` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4356` n `53` status `ready` deltaP `20.4384` edge `0.2988` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.2602` n `53` status `ready` deltaP `17.8652` edge `0.2156` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0865` n `53` status `ready` deltaP `28.3882` edge `0.0933` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0111` n `53` status `ready` deltaP `19.6344` edge `0.7057` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1319` n `53` status `ready` deltaP `25.1412` edge `0.0355` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9406` n `53` status `ready` deltaP `20.1363` edge `0.0711` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9391` n `53` status `ready` deltaP `26.4985` edge `0.2358` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1891` n `53` status `ready` deltaP `16.4275` edge `0.0197` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

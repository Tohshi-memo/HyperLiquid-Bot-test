# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T11:07:25.906919+00:00`
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

- `market_context_high->unknown_24h` score `526.0055` n `70` status `ready` deltaP `4.5139` edge `43.8037` maxDD `0.0`
- `news_risk_high->equity_24h` score `38.2311` n `53` status `ready` deltaP `37.3133` edge `3.0078` maxDD `-3.6503`
- `market_context_high->equity_24h` score `32.475` n `70` status `ready` deltaP `33.3779` edge `2.6379` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `20.565` n `70` status `ready` deltaP `52.9167` edge `1.4943` maxDD `-8.3327`
- `news_risk_high->crypto_major_24h` score `16.0175` n `53` status `ready` deltaP `42.0434` edge `1.9698` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2474` n `53` status `ready` deltaP `36.2402` edge `0.8087` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.8803` n `53` status `ready` deltaP `47.0486` edge `0.2597` maxDD `0.0`
- `market_context_high->index_24h` score `6.594` n `70` status `ready` deltaP `39.0377` edge `0.2984` maxDD `-0.0653`
- `news_risk_high->index_24h` score `5.4498` n `53` status `ready` deltaP `34.8598` edge `0.2521` maxDD `-0.4279`
- `news_risk_high->metal_4h` score `4.9209` n `53` status `ready` deltaP `46.3962` edge `0.1384` maxDD `-1.0104`
- `market_context_high->metal_24h` score `4.792` n `70` status `ready` deltaP `46.6667` edge `0.3924` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.093` n `53` status `ready` deltaP `21.2006` edge `0.3485` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.5517` n `53` status `ready` deltaP `18.464` edge `0.2359` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1785` n `53` status `ready` deltaP `28.998` edge `0.0969` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1835` n `53` status `ready` deltaP `25.4406` edge `0.0378` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1553` n `53` status `ready` deltaP `21.9656` edge `0.0768` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.1486` n `53` status `ready` deltaP `26.1936` edge `0.2647` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.823` n `53` status `ready` deltaP `14.4261` edge `0.5881` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2382` n `53` status `ready` deltaP `16.7269` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.7289` n `53` status `ready` deltaP `17.4443` edge `0.0751` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

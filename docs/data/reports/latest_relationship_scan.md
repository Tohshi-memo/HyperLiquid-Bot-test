# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T14:37:30.294362+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11962`

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

- `market_context_high->unknown_24h` score `288.1315` n `84` status `ready` deltaP `6.4425` edge `23.9821` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `101.8954` n `88` status `ready` deltaP `7.525` edge `8.4859` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.2291` n `53` status `ready` deltaP `21.0486` edge `2.1994` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.2117` n `84` status `ready` deltaP `18.7799` edge `1.5464` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.0208` n `53` status `ready` deltaP `36.8969` edge `1.3635` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.2424` n `53` status `ready` deltaP `33.9536` edge `0.7402` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3876` n `53` status `ready` deltaP `42.5606` edge `0.3319` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8808` n `84` status `ready` deltaP `38.2106` edge `1.037` maxDD `-25.4331`
- `market_context_high->metal_24h` score `5.9879` n `84` status `ready` deltaP `38.8491` edge `0.2813` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6604` n `53` status `ready` deltaP `44.4145` edge `0.1299` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.8713` n `84` status `ready` deltaP `20.926` edge `0.1926` maxDD `-0.0934`
- `news_risk_high->equity_1h` score `3.6538` n `53` status `ready` deltaP `18.0149` edge `0.2474` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.4629` n `53` status `ready` deltaP `19.129` edge `0.1914` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.424` n `53` status `ready` deltaP `21.6579` edge `0.2897` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.0471` n `53` status `ready` deltaP `26.7114` edge `0.1012` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.2661` n `53` status `ready` deltaP `26.4885` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0004` n `53` status `ready` deltaP `19.9839` edge `0.0771` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.74` n `53` status `ready` deltaP `25.4314` edge `0.2174` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3532` n `53` status `ready` deltaP `17.7748` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.8174` n `53` status `ready` deltaP `19.091` edge `0.0827` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T13:52:26.717597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10554`

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

- `market_context_high->unknown_24h` score `372.059` n `75` status `ready` deltaP `5.1458` edge `30.9847` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `32.5869` n `53` status `ready` deltaP `31.4106` edge `2.5768` maxDD `-3.6503`
- `market_context_high->equity_24h` score `24.3532` n `75` status `ready` deltaP `25.9514` edge `2.0106` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `18.4184` n `75` status `ready` deltaP `51.5764` edge `1.4425` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.2255` n `53` status `ready` deltaP `42.217` edge `1.7389` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.1643` n `53` status `ready` deltaP `33.8012` edge `0.7347` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `5.6918` n `53` status `ready` deltaP `36.6319` edge `0.2301` maxDD `0.0`
- `market_context_high->index_24h` score `4.7111` n `75` status `ready` deltaP `25.0417` edge `0.2348` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `4.567` n `53` status `ready` deltaP `43.6523` edge `0.1272` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.0302` n `53` status `ready` deltaP `23.0542` edge `0.2125` maxDD `-0.4279`
- `market_context_high->metal_24h` score `3.7931` n `75` status `ready` deltaP `37.6875` edge `0.3242` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.2902` n `53` status `ready` deltaP `17.5658` edge `0.2201` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `2.9945` n `53` status `ready` deltaP `27.7784` edge `0.0897` maxDD `-0.3611`
- `news_risk_high->crypto_major_4h` score `2.9005` n `53` status `ready` deltaP `18.6091` edge `0.2664` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `2.7661` n `53` status `ready` deltaP `18.4191` edge `0.6824` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0864` n `53` status `ready` deltaP `24.6921` edge `0.0347` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9076` n `53` status `ready` deltaP `19.679` edge `0.0714` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.7818` n `53` status `ready` deltaP `25.8887` edge `0.2197` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1615` n `53` status `ready` deltaP `15.9784` edge `0.0204` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.5559` n `53` status `ready` deltaP `16.5461` edge `0.0589` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

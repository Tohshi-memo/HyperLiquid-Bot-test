# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T12:52:27.317606+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11734`

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

- `market_context_high->unknown_24h` score `270.4309` n `87` status `ready` deltaP `6.5246` edge `22.5065` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `107.7358` n `87` status `ready` deltaP `7.4205` edge `8.9733` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.4151` n `53` status `ready` deltaP `21.0486` edge `2.2149` maxDD `-3.6503`
- `market_context_high->equity_24h` score `14.9396` n `87` status `ready` deltaP `15.8653` edge `1.3324` maxDD `-11.7897`
- `news_risk_high->crypto_major_24h` score `11.2158` n `53` status `ready` deltaP `36.8969` edge `1.3885` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.8232` n `53` status `ready` deltaP `33.9536` edge `0.7886` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.2856` n `53` status `ready` deltaP `42.2145` edge `0.3257` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `5.4131` n `87` status `ready` deltaP `35.7475` edge `0.9249` maxDD `-30.2052`
- `market_context_high->metal_24h` score `5.3028` n `87` status `ready` deltaP `35.9345` edge `0.2526` maxDD `-1.021`
- `news_risk_high->metal_4h` score `4.6144` n `53` status `ready` deltaP `44.1096` edge `0.1281` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `3.7528` n `53` status `ready` deltaP `21.6579` edge `0.3171` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.6298` n `53` status `ready` deltaP `18.0149` edge `0.2454` maxDD `-3.7082`
- `news_risk_high->index_24h` score `3.5253` n `53` status `ready` deltaP `19.129` edge `0.1966` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0241` n `53` status `ready` deltaP `26.5589` edge `0.1003` maxDD `-0.3611`
- `market_context_high->index_24h` score `3.0126` n `87` status `ready` deltaP `17.8061` edge `0.1665` maxDD `-1.7328`
- `news_risk_high->metal_1h` score `2.2026` n `53` status `ready` deltaP `26.0394` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0724` n `53` status `ready` deltaP `19.9839` edge `0.0831` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0193` n `53` status `ready` deltaP `25.4314` edge `0.2532` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3293` n `53` status `ready` deltaP `17.4754` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7987` n `53` status `ready` deltaP `18.9413` edge `0.0813` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

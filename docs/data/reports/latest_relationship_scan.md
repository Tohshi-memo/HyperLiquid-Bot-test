# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-12T13:37:28.725297+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11946`

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

- `market_context_high->unknown_24h` score `287.2855` n `84` status `ready` deltaP `6.4425` edge `23.9116` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `109.1957` n `85` status `ready` deltaP `7.2041` edge `9.0964` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `27.3143` n `53` status `ready` deltaP `21.0486` edge `2.2065` maxDD `-3.6503`
- `market_context_high->equity_24h` score `19.2969` n `84` status `ready` deltaP `18.7799` edge `1.5535` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.1128` n `53` status `ready` deltaP `36.8969` edge `1.3753` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5112` n `53` status `ready` deltaP `33.9536` edge `0.7626` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `7.3366` n `53` status `ready` deltaP `42.3875` edge `0.3288` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `6.8153` n `84` status `ready` deltaP `38.2106` edge `1.0286` maxDD `-25.4331`
- `market_context_high->metal_24h` score `5.9279` n `84` status `ready` deltaP `38.8491` edge `0.2763` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.5974` n `53` status `ready` deltaP `43.9571` edge `0.1277` maxDD `-1.0104`
- `market_context_high->index_24h` score `3.9061` n `84` status `ready` deltaP `20.926` edge `0.1955` maxDD `-0.0934`
- `news_risk_high->equity_1h` score `3.6238` n `53` status `ready` deltaP `18.0149` edge `0.2449` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.5728` n `53` status `ready` deltaP `21.6579` edge `0.3021` maxDD `-9.2335`
- `news_risk_high->index_24h` score `3.4977` n `53` status `ready` deltaP `19.129` edge `0.1943` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.0495` n `53` status `ready` deltaP `26.7114` edge `0.1014` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1942` n `53` status `ready` deltaP `25.8897` edge `0.0357` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.0388` n `53` status `ready` deltaP `19.9839` edge `0.0803` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8773` n `53` status `ready` deltaP `25.4314` edge `0.235` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.3293` n `53` status `ready` deltaP `17.4754` edge `0.0244` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7886` n `53` status `ready` deltaP `18.9413` edge `0.08` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

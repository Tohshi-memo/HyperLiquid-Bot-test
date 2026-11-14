# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T05:22:28.084078+00:00`
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

- `market_context_high->unknown_24h` score `431.1617` n `75` status `ready` deltaP `2.1944` edge `35.9296` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `36.8321` n `53` status `ready` deltaP `35.23` edge `2.9051` maxDD `-3.6503`
- `market_context_high->equity_24h` score `28.5984` n `75` status `ready` deltaP `29.7708` edge `2.3389` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.6734` n `75` status `ready` deltaP `47.5834` edge `1.3237` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `15.374` n `53` status `ready` deltaP `42.0434` edge `1.8873` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.2656` n `53` status `ready` deltaP `36.3926` edge `0.8092` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.43` n `53` status `ready` deltaP `43.0556` edge `0.2488` maxDD `0.0`
- `market_context_high->index_24h` score `5.7378` n `75` status `ready` deltaP `33.375` edge `0.2648` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0733` n `53` status `ready` deltaP `48.2254` edge `0.1389` maxDD `-1.0104`
- `news_risk_high->index_24h` score `5.0568` n `53` status `ready` deltaP `31.3875` edge `0.2425` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.2791` n `75` status `ready` deltaP `41.3334` edge `0.3622` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `4.0782` n `53` status `ready` deltaP `21.8103` edge `0.3432` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.626` n `53` status `ready` deltaP `19.2125` edge `0.2371` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0215` n `53` status `ready` deltaP `27.3211` edge `0.095` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.3188` n `53` status `ready` deltaP `27.0873` edge `0.0381` maxDD `-0.3692`
- `news_risk_high->index_4h` score `2.1541` n `53` status `ready` deltaP `21.9656` edge `0.0767` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `2.0887` n `53` status `ready` deltaP `26.346` edge `0.256` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.6319` n `53` status `ready` deltaP `14.4261` edge `0.5636` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.2502` n `53` status `ready` deltaP `16.8766` edge `0.0218` maxDD `-0.4103`
- `news_risk_high->crypto_major_1h` score `0.7286` n `53` status `ready` deltaP `17.8934` edge `0.0793` maxDD `-7.0808`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

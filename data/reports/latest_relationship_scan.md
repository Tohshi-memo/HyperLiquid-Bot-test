# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T09:52:25.414334+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11334`

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

- `market_context_high->unknown_24h` score `329.986` n `76` status `ready` deltaP `6.049` edge `27.4726` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `85.173` n `84` status `ready` deltaP `5.7201` edge `7.1044` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.6094` n `53` status `ready` deltaP `31.9314` edge `2.5752` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.3365` n `76` status `ready` deltaP `25.4021` edge `2.0259` maxDD `-3.0428`
- `news_risk_high->crypto_major_24h` score `13.9663` n `53` status `ready` deltaP `42.3906` edge `1.7045` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5768` n `53` status `ready` deltaP `35.478` edge `0.7579` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.3799` n `76` status `ready` deltaP `48.209` edge `1.4057` maxDD `-25.0401`
- `market_context_high->metal_24h` score `7.2347` n `76` status `ready` deltaP `44.0058` edge `0.3571` maxDD `-0.8067`
- `news_risk_high->commodity_24h` score `6.0472` n `53` status `ready` deltaP `38.1944` edge `0.2493` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.618` n `53` status `ready` deltaP `44.1096` edge `0.1284` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.4216` n `76` status `ready` deltaP `22.7796` edge `0.2261` maxDD `-0.0934`
- `news_risk_high->index_24h` score `4.1816` n `53` status `ready` deltaP `24.6167` edge `0.2147` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.39` n `53` status `ready` deltaP `20.4384` edge `0.295` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3681` n `53` status `ready` deltaP `18.1646` edge `0.2226` maxDD `-3.7082`
- `news_risk_high->crypto_alt_24h` score `3.0915` n `53` status `ready` deltaP `19.9816` edge `0.7137` maxDD `-29.0448`
- `news_risk_high->commodity_4h` score `3.0549` n `53` status `ready` deltaP `28.0833` edge `0.0927` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1211` n `53` status `ready` deltaP `24.9915` edge `0.0356` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9782` n `53` status `ready` deltaP `20.4412` edge `0.0722` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8829` n `53` status `ready` deltaP `26.4985` edge `0.2286` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2238` n `53` status `ready` deltaP `16.7269` edge `0.0206` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

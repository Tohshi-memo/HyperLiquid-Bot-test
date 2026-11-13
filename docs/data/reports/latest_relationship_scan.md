# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T10:07:30.687951+00:00`
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

- `market_context_high->unknown_24h` score `343.054` n `76` status `ready` deltaP `6.049` edge `28.5616` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `89.743` n `83` status `ready` deltaP `5.6053` edge `7.486` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.6322` n `53` status `ready` deltaP `31.9314` edge `2.5771` maxDD `-3.6503`
- `market_context_high->equity_24h` score `25.0376` n `76` status `ready` deltaP `25.4021` edge `2.0133` maxDD `-4.361`
- `news_risk_high->crypto_major_24h` score `14.0021` n `53` status `ready` deltaP `42.3906` edge `1.7091` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5684` n `53` status `ready` deltaP `35.478` edge `0.7572` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.4103` n `76` status `ready` deltaP `48.209` edge `1.3991` maxDD `-24.5337`
- `market_context_high->metal_24h` score `7.1338` n `76` status `ready` deltaP `44.0058` edge `0.3535` maxDD `-1.1913`
- `news_risk_high->commodity_24h` score `6.0364` n `53` status `ready` deltaP `38.1944` edge `0.2484` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.6168` n `53` status `ready` deltaP `44.1096` edge `0.1283` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.4204` n `76` status `ready` deltaP `22.7796` edge `0.226` maxDD `-0.0934`
- `news_risk_high->index_24h` score `4.1828` n `53` status `ready` deltaP `24.6167` edge `0.2148` maxDD `-0.4279`
- `news_risk_high->equity_1h` score `3.3478` n `53` status `ready` deltaP `18.0149` edge `0.2219` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.3478` n `53` status `ready` deltaP `20.2859` edge `0.2925` maxDD `-9.2335`
- `news_risk_high->crypto_alt_24h` score `3.0993` n `53` status `ready` deltaP `19.9816` edge `0.7147` maxDD `-29.0448`
- `news_risk_high->commodity_4h` score `3.0743` n `53` status `ready` deltaP `28.2358` edge `0.0933` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.1068` n `53` status `ready` deltaP `24.8418` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9782` n `53` status `ready` deltaP `20.4412` edge `0.0722` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8696` n `53` status `ready` deltaP `26.4985` edge `0.2269` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2118` n `53` status `ready` deltaP `16.5772` edge `0.0206` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

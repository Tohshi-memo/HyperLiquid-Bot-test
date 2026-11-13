# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T09:22:28.052212+00:00`
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

- `market_context_high->unknown_24h` score `303.9496` n `76` status `ready` deltaP `6.049` edge `25.3029` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `79.7283` n `86` status `ready` deltaP `5.9416` edge `6.6492` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `32.4988` n `53` status `ready` deltaP `31.5842` edge `2.5683` maxDD `-3.6503`
- `market_context_high->equity_24h` score `26.2279` n `76` status `ready` deltaP `27.6864` edge `2.0717` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.8601` n `53` status `ready` deltaP `42.0434` edge `1.6932` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `10.5612` n `53` status `ready` deltaP `35.478` edge `0.7566` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `10.4264` n `76` status `ready` deltaP `48.209` edge `1.4249` maxDD `-25.4331`
- `market_context_high->metal_24h` score `7.4072` n `76` status `ready` deltaP `44.0058` edge `0.3652` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.0898` n `53` status `ready` deltaP `38.3681` edge `0.2517` maxDD `0.0`
- `market_context_high->index_24h` score `4.6319` n `76` status `ready` deltaP `25.064` edge `0.2284` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.6168` n `53` status `ready` deltaP `44.1096` edge `0.1283` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1502` n `53` status `ready` deltaP `24.2695` edge `0.2144` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.426` n `53` status `ready` deltaP `20.4384` edge `0.298` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.3621` n `53` status `ready` deltaP `18.1646` edge `0.2221` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.0695` n `53` status `ready` deltaP `28.2358` edge `0.0929` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `3.0689` n `53` status `ready` deltaP `19.9816` edge `0.7108` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.1511` n `53` status `ready` deltaP `25.2909` edge `0.0361` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.977` n `53` status `ready` deltaP `20.4412` edge `0.0721` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.9071` n `53` status `ready` deltaP `26.4985` edge `0.2317` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.2226` n `53` status `ready` deltaP `16.7269` edge `0.0205` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

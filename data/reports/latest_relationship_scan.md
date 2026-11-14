# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-14T00:56:02.577213+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10302`

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

- `market_context_high->unknown_24h` score `393.6845` n `75` status `ready` deltaP `2.1944` edge `32.8065` maxDD `-0.4606`
- `news_risk_high->equity_24h` score `35.5695` n `53` status `ready` deltaP `34.8828` edge `2.8022` maxDD `-3.6503`
- `market_context_high->equity_24h` score `27.3358` n `75` status `ready` deltaP `29.4236` edge `2.236` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `16.9098` n `75` status `ready` deltaP `47.5834` edge `1.3434` maxDD `-16.4511`
- `news_risk_high->crypto_major_24h` score `14.9279` n `53` status `ready` deltaP `42.0434` edge `1.8301` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `11.1036` n `53` status `ready` deltaP `35.478` edge `0.8018` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.131` n `53` status `ready` deltaP `40.2778` edge `0.2424` maxDD `0.0`
- `market_context_high->index_24h` score `5.3582` n `75` status `ready` deltaP `30.25` edge `0.254` maxDD `-0.0653`
- `news_risk_high->metal_4h` score `5.0649` n `53` status `ready` deltaP `48.2254` edge `0.1382` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.6772` n `53` status `ready` deltaP `28.2625` edge `0.2317` maxDD `-0.4279`
- `market_context_high->metal_24h` score `4.1434` n `75` status `ready` deltaP `41.3334` edge `0.3448` maxDD `-3.7989`
- `news_risk_high->equity_1h` score `3.5577` n `53` status `ready` deltaP `18.6137` edge `0.2354` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `3.5538` n `53` status `ready` deltaP `20.8957` edge `0.3056` maxDD `-9.2335`
- `news_risk_high->commodity_4h` score `3.1321` n `53` status `ready` deltaP `28.3882` edge `0.0971` maxDD `-0.3611`
- `news_risk_high->metal_1h` score `2.302` n `53` status `ready` deltaP `26.9376` edge `0.0377` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.9532` n `53` status `ready` deltaP `19.679` edge `0.0752` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.8642` n `53` status `ready` deltaP `25.5838` edge `0.2323` maxDD `-10.1088`
- `news_risk_high->crypto_alt_24h` score `1.7855` n `53` status `ready` deltaP `14.4261` edge `0.5833` maxDD `-29.0448`
- `news_risk_high->index_1h` score `1.1484` n `53` status `ready` deltaP `15.679` edge `0.0213` maxDD `-0.4103`
- `news_risk_high->crypto_alt_1h` score `0.6486` n `53` status `ready` deltaP `17.1449` edge `0.0668` maxDD `-6.1688`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

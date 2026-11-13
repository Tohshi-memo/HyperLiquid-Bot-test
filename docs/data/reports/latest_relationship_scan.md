# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T07:22:25.187617+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11824`

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

- `market_context_high->unknown_24h` score `262.6705` n `84` status `ready` deltaP `6.2996` edge `21.8613` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `64.3452` n `94` status `ready` deltaP `6.7333` edge `5.362` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `31.9797` n `53` status `ready` deltaP `30.1953` edge `2.5343` maxDD `-3.6503`
- `market_context_high->equity_24h` score `23.9623` n `84` status `ready` deltaP `27.9266` edge `1.8813` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `13.3729` n `53` status `ready` deltaP `40.6545` edge `1.64` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `10.3053` n `84` status `ready` deltaP `48.6855` edge `1.4062` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `10.1722` n `53` status `ready` deltaP `34.4109` edge `0.7313` maxDD `-7.0416`
- `market_context_high->metal_24h` score `7.22` n `84` status `ready` deltaP `44.246` edge `0.348` maxDD `-0.3044`
- `news_risk_high->commodity_24h` score `6.3294` n `53` status `ready` deltaP `39.7569` edge `0.2624` maxDD `0.0`
- `market_context_high->index_24h` score `4.5146` n `84` status `ready` deltaP `25.8929` edge `0.2131` maxDD `-0.0934`
- `news_risk_high->metal_4h` score `4.4652` n `53` status `ready` deltaP `42.8901` edge `0.1238` maxDD `-1.0104`
- `news_risk_high->index_24h` score `4.1063` n `53` status `ready` deltaP `24.0959` edge `0.2119` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `3.4128` n `53` status `ready` deltaP `20.4384` edge `0.2969` maxDD `-9.2335`
- `news_risk_high->equity_1h` score `3.1775` n `53` status `ready` deltaP `17.4161` edge `0.2117` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.1339` n `53` status `ready` deltaP `28.8455` edge `0.0942` maxDD `-0.3611`
- `news_risk_high->crypto_alt_24h` score `2.8677` n `53` status `ready` deltaP `18.7663` edge `0.6931` maxDD `-29.0448`
- `news_risk_high->metal_1h` score `2.0636` n `53` status `ready` deltaP `24.5424` edge `0.0338` maxDD `-0.3692`
- `news_risk_high->crypto_alt_4h` score `1.9742` n `53` status `ready` deltaP `26.4985` edge `0.2403` maxDD `-10.1088`
- `news_risk_high->index_4h` score `1.8556` n `53` status `ready` deltaP `19.3741` edge `0.0691` maxDD `-0.8235`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

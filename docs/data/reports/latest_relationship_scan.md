# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T00:07:30.161636+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `303.8569` n `84` status `ready` deltaP `6.2996` edge `25.2935` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `72.3546` n `94` status `ready` deltaP `8.1053` edge `6.0203` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.1342` n `53` status `ready` deltaP `25.6814` edge `2.4106` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.1168` n `84` status `ready` deltaP `23.4127` edge `1.7576` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `11.9637` n `53` status `ready` deltaP `38.0503` edge `1.4767` maxDD `-12.7247`
- `news_risk_high->equity_4h` score `9.3985` n `53` status `ready` deltaP `32.7341` edge `0.678` maxDD `-7.0416`
- `market_context_high->crypto_alt_24h` score `9.0217` n `84` status `ready` deltaP `43.6508` edge `1.2752` maxDD `-25.4331`
- `news_risk_high->commodity_24h` score `7.1795` n `53` status `ready` deltaP `43.2292` edge `0.3101` maxDD `0.0`
- `market_context_high->metal_24h` score `6.5068` n `84` status `ready` deltaP `39.9057` edge `0.3175` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.6312` n `53` status `ready` deltaP `44.1096` edge `0.1295` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.313` n `84` status `ready` deltaP `24.6776` edge `0.2044` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9047` n `53` status `ready` deltaP `22.8806` edge `0.2032` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `2.9503` n `53` status `ready` deltaP `27.0162` edge `0.0911` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `2.8524` n `53` status `ready` deltaP `16.3682` edge `0.1916` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6943` n `53` status `ready` deltaP `19.6762` edge `0.2421` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.1547` n `53` status `ready` deltaP `25.4406` edge `0.0354` maxDD `-0.3692`
- `news_risk_high->index_4h` score `1.6799` n `53` status `ready` deltaP `18.0022` edge `0.0636` maxDD `-0.8235`
- `news_risk_high->crypto_alt_24h` score `1.5841` n `53` status `ready` deltaP `13.7316` edge `0.5621` maxDD `-29.0448`
- `news_risk_high->crypto_alt_4h` score `1.3672` n `53` status `ready` deltaP `24.5168` edge `0.1757` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.098` n `53` status `ready` deltaP `15.679` edge `0.0171` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

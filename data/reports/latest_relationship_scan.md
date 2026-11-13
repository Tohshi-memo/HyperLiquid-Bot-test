# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-13T03:07:36.277714+00:00`
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

- `market_context_high->unknown_24h` score `292.6333` n `84` status `ready` deltaP `6.2996` edge `24.3582` maxDD `-0.4606`
- `market_context_high->unknown_4h` score `56.2884` n `94` status `ready` deltaP `7.6479` edge `4.6845` maxDD `-0.9162`
- `news_risk_high->equity_24h` score `30.9204` n `53` status `ready` deltaP `27.2439` edge `2.4657` maxDD `-3.6503`
- `market_context_high->equity_24h` score `22.903` n `84` status `ready` deltaP `24.9752` edge `1.8127` maxDD `-1.983`
- `news_risk_high->crypto_major_24h` score `12.365` n `53` status `ready` deltaP `39.092` edge `1.5212` maxDD `-12.7247`
- `market_context_high->crypto_alt_24h` score `9.5138` n `84` status `ready` deltaP `45.7342` edge `1.3244` maxDD `-25.4331`
- `news_risk_high->equity_4h` score `9.4393` n `53` status `ready` deltaP `32.7341` edge `0.6814` maxDD `-7.0416`
- `news_risk_high->commodity_24h` score `6.9399` n `53` status `ready` deltaP `42.7083` edge `0.2936` maxDD `0.0`
- `market_context_high->metal_24h` score `6.7463` n `84` status `ready` deltaP `41.2946` edge `0.3282` maxDD `-0.3044`
- `news_risk_high->metal_4h` score `4.3853` n `53` status `ready` deltaP `42.2803` edge `0.1212` maxDD `-1.0104`
- `market_context_high->index_24h` score `4.3658` n `84` status `ready` deltaP `24.6776` edge `0.2088` maxDD `-0.0934`
- `news_risk_high->index_24h` score `3.9575` n `53` status `ready` deltaP `22.8806` edge `0.2076` maxDD `-0.4279`
- `news_risk_high->commodity_4h` score `3.1651` n `53` status `ready` deltaP `28.8455` edge `0.0968` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.1451` n `53` status `ready` deltaP `17.2664` edge `0.21` maxDD `-3.7082`
- `news_risk_high->crypto_major_4h` score `2.6327` n `53` status `ready` deltaP `19.3713` edge `0.239` maxDD `-9.2335`
- `news_risk_high->metal_1h` score `2.0864` n `53` status `ready` deltaP `24.8418` edge `0.0337` maxDD `-0.3692`
- `news_risk_high->crypto_alt_24h` score `2.0762` n `53` status `ready` deltaP `15.815` edge `0.6113` maxDD `-29.0448`
- `news_risk_high->index_4h` score `1.6615` n `53` status `ready` deltaP `17.6973` edge `0.0641` maxDD `-0.8235`
- `news_risk_high->crypto_alt_4h` score `1.4721` n `53` status `ready` deltaP `24.9741` edge `0.1861` maxDD `-10.1088`
- `news_risk_high->index_1h` score `1.1459` n `53` status `ready` deltaP `15.9784` edge `0.0191` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

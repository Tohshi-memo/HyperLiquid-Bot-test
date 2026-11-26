# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-26T12:52:27.146835+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `3467`

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

- `news_risk_high->unknown_1h` score `3231.2076` n `31` status `ready` deltaP `1.7819` edge `269.273` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3215.8927` n `31` status `ready` deltaP `3.4815` edge `267.9735` maxDD `-0.1191`
- `market_context_high->unknown_1h` score `100.9158` n `31` status `ready` deltaP `1.7819` edge `8.4072` maxDD `-0.4209`
- `news_risk_high->crypto_major_24h` score `35.3228` n `31` status `ready` deltaP `43.75` edge `2.6519` maxDD `0.0`
- `news_risk_high->equity_24h` score `34.879` n `31` status `ready` deltaP `42.8819` edge `2.6207` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `29.4448` n `31` status `ready` deltaP `43.0556` edge `2.1667` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `10.7459` n `31` status `ready` deltaP `26.9128` edge `0.8031` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `10.566` n `31` status `ready` deltaP `39.0539` edge `0.6682` maxDD `-2.178`
- `news_risk_high->metal_24h` score `8.4602` n `31` status `ready` deltaP `29.4299` edge `0.5363` maxDD `-0.1986`
- `news_risk_high->crypto_major_4h` score `6.9657` n `31` status `ready` deltaP `19.6744` edge `0.9036` maxDD `-7.6714`
- `news_risk_high->index_24h` score `5.8361` n `31` status `ready` deltaP `44.2708` edge `0.1912` maxDD `0.0`
- `news_risk_high->fx_24h` score `4.9693` n `31` status `ready` deltaP `41.8851` edge `0.1477` maxDD `-0.0262`
- `news_risk_high->equity_1h` score `3.7542` n `31` status `ready` deltaP `20.4365` edge `0.1953` maxDD `-0.1621`
- `news_risk_high->index_4h` score `3.4836` n `31` status `ready` deltaP `37.682` edge `0.0651` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7357` n `31` status `ready` deltaP `32.2919` edge `0.0212` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.5133` n `31` status `ready` deltaP `10.1603` edge `0.3006` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.2806` n `31` status `ready` deltaP `13.1543` edge `0.2404` maxDD `-1.5232`
- `market_context_high->fx_4h` score `1.9582` n `31` status `ready` deltaP `25.1328` edge `0.0241` maxDD `-0.2774`
- `news_risk_high->metal_1h` score `1.4682` n `31` status `ready` deltaP `28.8342` edge `0.0239` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `1.0022` n `31` status `ready` deltaP `15.5586` edge `0.0805` maxDD `-0.7918`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

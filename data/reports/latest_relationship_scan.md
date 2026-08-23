# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T01:56:49.613707+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14882`

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

- `news_risk_high->unknown_1h` score `3.3149` n `41` status `ready` deltaP `27.9685` edge `0.1016` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.7504` n `135` status `ready` deltaP `6.6135` edge `0.1245` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.4428` n `41` status `ready` deltaP `19.5779` edge `0.0067` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.2876` n `135` status `ready` deltaP `20.7058` edge `-0.0094` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `1.2563` n `41` status `ready` deltaP `24.456` edge `0.0262` maxDD `-0.9204`
- `news_risk_high->crypto_major_1h` score `0.4495` n `41` status `ready` deltaP `12.6479` edge `0.0409` maxDD `-5.0209`
- `news_risk_high->commodity_1h` score `0.2561` n `41` status `ready` deltaP `11.0194` edge `-0.0098` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `0.139` n `41` status `ready` deltaP `7.0396` edge `-0.0068` maxDD `-0.1184`
- `market_context_high->fx_4h` score `0.13` n `135` status `ready` deltaP `8.7161` edge `0.0088` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1428` n `135` status `ready` deltaP `1.9628` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->index_1h` score `-0.2042` n `41` status `ready` deltaP `1.0698` edge `0.002` maxDD `-0.1583`
- `market_context_high->equity_1h` score `-0.3618` n `135` status `ready` deltaP `4.185` edge `0.0327` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6525` n `135` status `ready` deltaP `-1.1266` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6671` n `135` status `ready` deltaP `1.1755` edge `0.0102` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8965` n `119` status `ready` deltaP `0.1211` edge `0.0064` maxDD `-2.105`
- `market_context_high->commodity_1h` score `-1.0495` n `135` status `ready` deltaP `-7.21` edge `-0.0017` maxDD `-1.1164`
- `market_context_high->commodity_4h` score `-1.0547` n `135` status `ready` deltaP `-7.2279` edge `-0.002` maxDD `-2.4692`
- `market_context_high->crypto_alt_4h` score `-1.2345` n `135` status `ready` deltaP `8.0465` edge `-0.0097` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

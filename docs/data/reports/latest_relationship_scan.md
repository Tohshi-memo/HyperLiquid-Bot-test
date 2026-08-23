# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T01:22:27.512486+00:00`
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

- `news_risk_high->unknown_1h` score `2.5752` n `39` status `ready` deltaP `29.8826` edge `0.0272` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.8069` n `135` status `ready` deltaP `6.4638` edge `0.1302` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.7286` n `39` status `ready` deltaP `23.0309` edge `0.0075` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.3864` n `135` status `ready` deltaP `21.0106` edge `-0.0032` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `1.197` n `39` status `ready` deltaP `23.3303` edge `0.0261` maxDD `-0.9204`
- `news_risk_high->crypto_major_1h` score `0.8346` n `39` status `ready` deltaP `13.5614` edge `0.0669` maxDD `-5.0209`
- `news_risk_high->commodity_1h` score `0.4166` n `39` status `ready` deltaP `13.9721` edge `-0.0089` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1308` n `135` status `ready` deltaP `8.7161` edge `0.0089` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `0.0307` n `39` status `ready` deltaP `5.063` edge `-0.0075` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0548` n `135` status `ready` deltaP `6.2963` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1583` n `135` status `ready` deltaP `1.6634` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->index_1h` score `-0.3296` n `39` status `ready` deltaP `-1.2821` edge `0.0016` maxDD `-0.1583`
- `market_context_high->equity_1h` score `-0.3626` n `135` status `ready` deltaP `4.185` edge `0.0326` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4571` n `135` status `ready` deltaP `6.0603` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6405` n `135` status `ready` deltaP `-0.9769` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6671` n `135` status `ready` deltaP `1.1755` edge `0.0102` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8746` n `119` status `ready` deltaP `0.4683` edge `0.0069` maxDD `-2.105`
- `market_context_high->commodity_4h` score `-1.0547` n `135` status `ready` deltaP `-7.2279` edge `-0.002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0667` n `135` status `ready` deltaP `-7.5094` edge `-0.0019` maxDD `-1.1164`
- `news_risk_high->crypto_alt_1h` score `-1.0889` n `39` status `ready` deltaP `3.7733` edge `-0.0475` maxDD `-6.7137`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

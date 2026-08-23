# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T01:37:26.254909+00:00`
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

- `news_risk_high->unknown_1h` score `2.3162` n `40` status `ready` deltaP `27.7246` edge `0.02` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.8188` n `135` status `ready` deltaP `6.6135` edge `0.1302` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.5807` n `40` status `ready` deltaP `21.2575` edge `0.007` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.3586` n `135` status `ready` deltaP `20.8582` edge `-0.0045` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `1.2286` n `40` status `ready` deltaP `23.9072` edge `0.0263` maxDD `-0.9204`
- `news_risk_high->crypto_major_1h` score `0.8454` n `40` status `ready` deltaP `14.2665` edge `0.0631` maxDD `-5.0209`
- `news_risk_high->commodity_1h` score `0.3331` n `40` status `ready` deltaP `12.4551` edge `-0.0095` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1308` n `135` status `ready` deltaP `8.7161` edge `0.0089` maxDD `-0.3527`
- `news_risk_high->metal_1h` score `0.0827` n `40` status `ready` deltaP `6.003` edge `-0.0071` maxDD `-0.1184`
- `market_context_high->index_1h` score `-0.0626` n `135` status `ready` deltaP `6.1466` edge `0.0041` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1505` n `135` status `ready` deltaP `1.8131` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->index_1h` score `-0.27` n `40` status `ready` deltaP `-0.1497` edge `0.0017` maxDD `-0.1583`
- `market_context_high->equity_1h` score `-0.3626` n `135` status `ready` deltaP `4.185` edge `0.0326` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4571` n `135` status `ready` deltaP `6.0603` edge `-0.0169` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6525` n `135` status `ready` deltaP `-1.1266` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.6671` n `135` status `ready` deltaP `1.1755` edge `0.0102` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8859` n `119` status `ready` deltaP `0.2947` edge `0.0066` maxDD `-2.105`
- `market_context_high->commodity_4h` score `-1.0547` n `135` status `ready` deltaP `-7.2279` edge `-0.002` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0581` n `135` status `ready` deltaP `-7.3597` edge `-0.0018` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.2091` n `135` status `ready` deltaP `8.1989` edge `-0.0086` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

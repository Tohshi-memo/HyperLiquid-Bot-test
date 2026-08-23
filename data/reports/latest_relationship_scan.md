# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T00:22:29.533914+00:00`
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

- `news_risk_high->unknown_1h` score `2.3416` n `35` status `ready` deltaP `29.3029` edge `0.0116` maxDD `-0.2787`
- `market_context_high->unknown_1h` score `1.8596` n `135` status `ready` deltaP `6.7632` edge `0.1326` maxDD `-0.4843`
- `news_risk_high->fx_1h` score `1.775` n `35` status `ready` deltaP `23.5501` edge `0.0079` maxDD `-0.0257`
- `market_context_high->unknown_4h` score `1.4528` n `135` status `ready` deltaP `21.3155` edge `0.0003` maxDD `-0.3736`
- `news_risk_high->equity_1h` score `0.9974` n `35` status `ready` deltaP `20.9923` edge `0.0161` maxDD `-0.9204`
- `news_risk_high->commodity_1h` score `0.7082` n `35` status `ready` deltaP `18.2849` edge `-0.0086` maxDD `-0.4666`
- `market_context_high->fx_4h` score `0.1323` n `135` status `ready` deltaP `8.7161` edge `0.0091` maxDD `-0.3527`
- `market_context_high->index_1h` score `-0.0462` n `135` status `ready` deltaP `6.446` edge `0.0042` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1428` n `135` status `ready` deltaP `1.9628` edge `0.0045` maxDD `-0.2043`
- `news_risk_high->metal_1h` score `-0.2268` n `35` status `ready` deltaP `0.3807` edge `-0.0093` maxDD `-0.1184`
- `news_risk_high->crypto_major_1h` score `-0.3334` n `35` status `ready` deltaP `10.6373` edge `-0.0259` maxDD `-5.0209`
- `market_context_high->equity_1h` score `-0.3416` n `135` status `ready` deltaP `4.4844` edge `0.0333` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.4559` n `135` status `ready` deltaP `6.0603` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.6153` n `135` status `ready` deltaP `-0.6775` edge `-0.0049` maxDD `-0.6822`
- `news_risk_high->index_1h` score `-0.6336` n `35` status `ready` deltaP `-6.9932` edge `0.0007` maxDD `-0.1583`
- `market_context_high->index_4h` score `-0.6663` n `135` status `ready` deltaP `1.1755` edge `0.0103` maxDD `-2.618`
- `market_context_high->fx_24h` score `-0.8299` n `119` status `ready` deltaP `1.1628` edge `0.008` maxDD `-2.105`
- `market_context_high->commodity_4h` score `-1.0642` n `135` status `ready` deltaP `-7.3803` edge `-0.0022` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-1.0931` n `135` status `ready` deltaP `-7.9585` edge `-0.0023` maxDD `-1.1164`
- `market_context_high->crypto_alt_4h` score `-1.1389` n `135` status `ready` deltaP `8.6563` edge `-0.0058` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-23T05:07:26.118826+00:00`
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

- `news_risk_high->unknown_4h` score `16.0879` n `42` status `ready` deltaP `28.6585` edge `1.1496` maxDD `0.0`
- `news_risk_high->equity_4h` score `5.6588` n `42` status `ready` deltaP `40.5705` edge `0.2166` maxDD `-0.2402`
- `news_risk_high->unknown_1h` score `3.8162` n `51` status `ready` deltaP `20.6763` edge `0.2106` maxDD `-0.7674`
- `news_risk_high->fx_4h` score `3.2365` n `42` status `ready` deltaP `38.4364` edge `0.0269` maxDD `-0.0746`
- `news_risk_high->metal_4h` score `1.672` n `42` status `ready` deltaP `23.0256` edge `-0.0013` maxDD `-0.0296`
- `news_risk_high->index_4h` score `1.3554` n `42` status `ready` deltaP `18.9533` edge `0.0252` maxDD `-0.0884`
- `market_context_high->unknown_1h` score `1.2761` n `135` status `ready` deltaP `4.9901` edge `0.1002` maxDD `-0.837`
- `news_risk_high->fx_1h` score `1.2086` n `51` status `ready` deltaP `16.696` edge `0.0064` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8173` n `51` status `ready` deltaP `17.8936` edge `0.022` maxDD `-0.9204`
- `market_context_high->unknown_4h` score `0.8038` n `132` status `ready` deltaP `21.0827` edge `-0.0564` maxDD `-0.3736`
- `news_risk_high->index_1h` score `0.199` n `51` status `ready` deltaP `8.6738` edge `0.003` maxDD `-0.1583`
- `market_context_high->fx_4h` score `0.1769` n `132` status `ready` deltaP `8.4581` edge `0.0086` maxDD `-0.3527`
- `news_risk_high->commodity_1h` score `0.1608` n `51` status `ready` deltaP `8.2394` edge `-0.0107` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1084` n `51` status `ready` deltaP `2.3424` edge `-0.0072` maxDD `-0.1184`
- `market_context_high->fx_1h` score `-0.1206` n `135` status `ready` deltaP `2.4041` edge `0.0044` maxDD `-0.2043`
- `market_context_high->index_1h` score `-0.1411` n `135` status `ready` deltaP `4.6651` edge `0.0039` maxDD `-0.9144`
- `market_context_high->equity_1h` score `-0.3937` n `135` status `ready` deltaP `3.6017` edge `0.0325` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.4568` n `135` status `ready` deltaP `-1.7099` edge `-0.0053` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.484` n `132` status `ready` deltaP `5.7096` edge `-0.0168` maxDD `-1.5942`
- `market_context_high->crypto_alt_4h` score `-0.7121` n `132` status `ready` deltaP `8.8461` edge `0.0285` maxDD `-7.0785`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

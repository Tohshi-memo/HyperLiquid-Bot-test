# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T18:37:25.801133+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14866`

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

- `market_context_high->unknown_1h` score `1.5383` n `149` status `ready` deltaP `6.7074` edge `0.1062` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.9807` n `149` status `ready` deltaP `18.7418` edge `0.0007` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.1081` n `149` status `ready` deltaP `8.2071` edge `0.0094` maxDD `-0.3539`
- `market_context_high->index_1h` score `-0.0282` n `149` status `ready` deltaP `6.7476` edge `0.0045` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.1036` n `149` status `ready` deltaP `2.7157` edge `0.0045` maxDD `-0.2043`
- `market_context_high->metal_4h` score `-0.2935` n `149` status `ready` deltaP `8.1498` edge `-0.0172` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.3283` n `149` status `ready` deltaP `4.8738` edge `0.0324` maxDD `-5.2257`
- `market_context_high->metal_1h` score `-0.3639` n `149` status `ready` deltaP `0.0312` edge `-0.005` maxDD `-0.6822`
- `market_context_high->index_4h` score `-0.5293` n `149` status `ready` deltaP `3.6299` edge `0.0115` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.8517` n `149` status `ready` deltaP `-3.6237` edge `0.0` maxDD `-2.4692`
- `market_context_high->fx_24h` score `-1.1093` n `133` status `ready` deltaP `1.1343` edge `0.0112` maxDD `-2.2121`
- `market_context_high->commodity_1h` score `-1.1383` n `149` status `ready` deltaP `-8.6213` edge `-0.0027` maxDD `-1.1941`
- `market_context_high->equity_4h` score `-1.6768` n `149` status `ready` deltaP `-0.5177` edge `0.0701` maxDD `-16.1967`
- `market_context_high->commodity_24h` score `-2.1508` n `133` status `ready` deltaP `-4.7266` edge `0.0356` maxDD `-4.666`
- `market_context_high->crypto_alt_4h` score `-2.4975` n `149` status `ready` deltaP `2.9986` edge `-0.0813` maxDD `-7.0785`
- `market_context_high->crypto_alt_1h` score `-2.5592` n `149` status `ready` deltaP `-2.8332` edge `-0.0449` maxDD `-7.9582`
- `market_context_high->crypto_major_1h` score `-3.6544` n `149` status `ready` deltaP `-5.6574` edge `-0.1191` maxDD `-7.8171`
- `market_context_high->index_24h` score `-4.376` n `133` status `ready` deltaP `-6.7356` edge `-0.0354` maxDD `-21.1244`
- `market_context_high->metal_24h` score `-5.4181` n `133` status `ready` deltaP `-23.8096` edge `-0.2051` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.664` n `149` status `ready` deltaP `-0.5412` edge `-0.3354` maxDD `-5.6395`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

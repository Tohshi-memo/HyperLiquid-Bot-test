# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T21:21:09.208170+00:00`
- Price records: `672`
- Market context records: `4555`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10045`

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

- `market_context_high->unknown_1h` score `61.6712` n `160` status `ready` deltaP `6.4671` edge `5.1462` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.848` n `160` status `ready` deltaP `7.7134` edge `0.3082` maxDD `-4.7829`
- `market_context_high->fx_4h` score `-0.499` n `160` status `ready` deltaP `6.2805` edge `0.0024` maxDD `-1.9927`
- `market_context_high->fx_1h` score `-0.6761` n `160` status `ready` deltaP `0.3181` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_1h` score `-0.6821` n `160` status `ready` deltaP `-2.0172` edge `0.0247` maxDD `-5.5624`
- `market_context_high->commodity_1h` score `-0.6939` n `160` status `ready` deltaP `0.4154` edge `0.019` maxDD `-2.0345`
- `market_context_high->equity_4h` score `-0.6958` n `160` status `ready` deltaP `2.0122` edge `0.0743` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.7346` n `160` status `ready` deltaP `3.7043` edge `-0.0066` maxDD `-5.9823`
- `market_context_high->commodity_4h` score `-1.1862` n `160` status `ready` deltaP `3.5671` edge `0.0349` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.4735` n `160` status `ready` deltaP `-1.744` edge `-0.0103` maxDD `-2.7358`
- `market_context_high->metal_1h` score `-2.8923` n `160` status `ready` deltaP `-3.6527` edge `-0.0813` maxDD `-17.8795`
- `market_context_high->unknown_24h` score `-2.9786` n `158` status `ready` deltaP `1.9075` edge `-0.1686` maxDD `-4.7201`
- `market_context_high->crypto_alt_1h` score `-5.4743` n `160` status `ready` deltaP `-2.8443` edge `-0.1085` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.606` n `158` status `ready` deltaP `-14.8713` edge `-0.0168` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.7602` n `158` status `ready` deltaP `-10.0805` edge `-0.1338` maxDD `-29.3321`
- `market_context_high->commodity_24h` score `-6.2539` n `158` status `ready` deltaP `7.4872` edge `0.0446` maxDD `-36.587`
- `market_context_high->crypto_major_1h` score `-6.542` n `160` status `ready` deltaP `-5.0973` edge `-0.1359` maxDD `-27.356`
- `market_context_high->crypto_alt_4h` score `-8.7193` n `160` status `ready` deltaP `-1.3567` edge `-0.2431` maxDD `-63.9243`
- `market_context_high->metal_4h` score `-10.2317` n `160` status `ready` deltaP `-8.6433` edge `-0.3324` maxDD `-67.4051`
- `market_context_high->crypto_major_4h` score `-11.4531` n `160` status `ready` deltaP `0.2896` edge `-0.3759` maxDD `-82.2164`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

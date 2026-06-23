# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T20:52:32.447685+00:00`
- Price records: `672`
- Market context records: `4553`
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

- `market_context_high->unknown_1h` score `60.3938` n `162` status `ready` deltaP `5.964` edge `5.0431` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `2.3218` n `162` status `ready` deltaP `7.2004` edge `0.291` maxDD `-6.6414`
- `market_context_high->fx_4h` score `-0.4669` n `162` status `ready` deltaP `6.8824` edge `0.0025` maxDD `-1.9927`
- `market_context_high->equity_1h` score `-0.677` n `162` status `ready` deltaP `-1.8906` edge `0.0245` maxDD `-5.5624`
- `market_context_high->fx_1h` score `-0.685` n `162` status `ready` deltaP `0.207` edge `-0.003` maxDD `-1.1038`
- `market_context_high->equity_4h` score `-0.6961` n `162` status `ready` deltaP `2.232` edge `0.0728` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.7758` n `162` status `ready` deltaP `2.9867` edge `-0.0071` maxDD `-5.9823`
- `market_context_high->commodity_1h` score `-0.7818` n `162` status `ready` deltaP `-0.1479` edge `0.0163` maxDD `-2.1037`
- `market_context_high->commodity_4h` score `-1.2172` n `162` status `ready` deltaP `3.301` edge `0.0327` maxDD `-9.1941`
- `market_context_high->index_1h` score `-1.5014` n `162` status `ready` deltaP `-2.0773` edge `-0.0104` maxDD `-2.7358`
- `market_context_high->unknown_24h` score `-2.917` n `160` status `ready` deltaP `2.1528` edge `-0.1651` maxDD `-4.7201`
- `market_context_high->metal_1h` score `-4.4654` n `162` status `ready` deltaP `-3.9089` edge `-0.0809` maxDD `-17.8795`
- `market_context_high->crypto_alt_1h` score `-5.5009` n `162` status `ready` deltaP `-3.1622` edge `-0.1086` maxDD `-22.2982`
- `market_context_high->fx_24h` score `-5.554` n `160` status `ready` deltaP `-14.3403` edge `-0.016` maxDD `-6.0982`
- `market_context_high->index_24h` score `-5.74` n `160` status `ready` deltaP `-9.8264` edge `-0.1329` maxDD `-29.3321`
- `market_context_high->crypto_major_1h` score `-6.5395` n `162` status `ready` deltaP `-5.2007` edge `-0.135` maxDD `-27.356`
- `market_context_high->commodity_24h` score `-6.6493` n `160` status `ready` deltaP `6.9097` edge `0.038` maxDD `-38.3871`
- `market_context_high->crypto_alt_4h` score `-8.7079` n `162` status `ready` deltaP `-1.6768` edge `-0.2395` maxDD `-63.9243`
- `market_context_high->crypto_major_4h` score `-11.426` n `162` status `ready` deltaP `-0.0151` edge `-0.3704` maxDD `-82.2164`
- `market_context_high->equity_24h` score `-13.4364` n `160` status `ready` deltaP `-1.2847` edge `-0.2461` maxDD `-102.1031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

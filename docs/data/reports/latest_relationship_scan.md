# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T11:37:30.672623+00:00`
- Price records: `672`
- Market context records: `4823`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7588`

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

- `market_context_high->unknown_1h` score `13.3207` n `111` status `ready` deltaP `12.1676` edge `1.0707` maxDD `-1.674`
- `market_context_high->unknown_4h` score `8.0096` n `111` status `ready` deltaP `17.4014` edge `0.6725` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `2.9916` n `104` status `ready` deltaP `15.2778` edge `0.2163` maxDD `-2.8416`
- `market_context_high->equity_4h` score `0.829` n `111` status `ready` deltaP `12.6195` edge `0.1603` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.8048` n `111` status `ready` deltaP `10.2354` edge `0.0455` maxDD `-0.7334`
- `market_context_high->commodity_4h` score `0.4367` n `111` status `ready` deltaP `15.5845` edge `0.0693` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.2037` n `111` status `ready` deltaP `6.2942` edge `0.0248` maxDD `-1.3161`
- `market_context_high->equity_1h` score `-0.0404` n `111` status `ready` deltaP `3.6023` edge `0.0324` maxDD `-2.928`
- `market_context_high->fx_4h` score `-0.4552` n `111` status `ready` deltaP `2.8758` edge `0.0001` maxDD `-1.5439`
- `market_context_high->index_1h` score `-0.5504` n `111` status `ready` deltaP `0.0041` edge `0.0055` maxDD `-0.7537`
- `market_context_high->fx_1h` score `-1.0815` n `111` status `ready` deltaP `-3.1613` edge `-0.0041` maxDD `-0.8626`
- `market_context_high->crypto_alt_1h` score `-1.9812` n `111` status `ready` deltaP `4.6502` edge `-0.0079` maxDD `-12.7225`
- `market_context_high->metal_1h` score `-2.1668` n `111` status `ready` deltaP `-0.3116` edge `-0.0654` maxDD `-13.4916`
- `market_context_high->crypto_major_1h` score `-2.1746` n `111` status `ready` deltaP `2.6905` edge `-0.0392` maxDD `-17.9354`
- `market_context_high->fx_24h` score `-2.3822` n `104` status `ready` deltaP `-11.4984` edge `-0.0195` maxDD `-2.8555`
- `market_context_high->commodity_24h` score `-2.3916` n `104` status `ready` deltaP `17.9354` edge `0.0847` maxDD `-27.5371`
- `market_context_high->crypto_alt_4h` score `-3.7377` n `111` status `ready` deltaP `8.5723` edge `0.0088` maxDD `-38.2779`
- `market_context_high->index_24h` score `-4.0237` n `104` status `ready` deltaP `-3.5123` edge `-0.1016` maxDD `-23.2678`
- `market_context_high->crypto_major_4h` score `-7.2719` n `111` status `ready` deltaP `5.4398` edge `-0.1454` maxDD `-60.5192`
- `market_context_high->metal_4h` score `-8.6079` n `111` status `ready` deltaP `6.2706` edge `-0.3349` maxDD `-60.1721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

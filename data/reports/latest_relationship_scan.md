# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T00:07:31.521738+00:00`
- Price records: `672`
- Market context records: `4774`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `8.1601` n `122` status `ready` deltaP `12.5798` edge `0.6379` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3763` n `122` status `ready` deltaP `17.1956` edge `0.6211` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.85` n `107` status `ready` deltaP `11.52` edge `0.1697` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1545` n `122` status `ready` deltaP `12.2726` edge `0.0552` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1273` n `122` status `ready` deltaP `5.5315` edge `0.0325` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.3941` n `122` status `ready` deltaP `3.736` edge `0.0022` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5566` n `122` status `ready` deltaP `5.013` edge `0.0021` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.6643` n `122` status `ready` deltaP `5.6428` edge `0.0458` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8597` n `122` status `ready` deltaP `-0.5841` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.052` n `122` status `ready` deltaP `-0.0785` edge `-0.0104` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.5381` n `122` status `ready` deltaP `-2.8443` edge `-0.0088` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0124` n `107` status `ready` deltaP `21.312` edge `0.1108` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3296` n `122` status `ready` deltaP `-1.5461` edge `-0.0708` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2365` n `107` status `ready` deltaP `-14.0317` edge `-0.0212` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3726` n `122` status `ready` deltaP `-0.1497` edge `-0.0561` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.7561` n `122` status `ready` deltaP `-0.6626` edge `-0.0829` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.2188` n `122` status `ready` deltaP `3.0688` edge `-0.0471` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6678` n `107` status `ready` deltaP `-5.1029` edge `-0.1049` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5488` n `122` status `ready` deltaP `1.8293` edge `-0.1851` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6705` n `122` status `ready` deltaP `3.791` edge `-0.3128` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

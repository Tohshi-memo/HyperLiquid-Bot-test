# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-20T04:52:37.134145+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2790`

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

- `market_context_high->unknown_1h` score `11994.7352` n `108` status `ready` deltaP `0.987` edge `999.5745` maxDD `-0.9181`
- `market_context_high->unknown_4h` score `7455.1461` n `108` status `ready` deltaP `-0.0903` edge `621.2912` maxDD `-0.6072`
- `market_context_high->crypto_major_24h` score `16.0654` n `99` status `ready` deltaP `32.9388` edge `1.4246` maxDD `-20.7657`
- `market_context_high->crypto_alt_24h` score `6.4382` n `99` status `ready` deltaP `18.5449` edge `1.1623` maxDD `-33.1747`
- `market_context_high->crypto_major_4h` score `1.3296` n `108` status `ready` deltaP `4.0932` edge `0.3654` maxDD `-16.2179`
- `market_context_high->crypto_alt_4h` score `1.0749` n `108` status `ready` deltaP `5.6176` edge `0.2597` maxDD `-12.9396`
- `market_context_high->metal_4h` score `0.8247` n `108` status `ready` deltaP `20.0034` edge `0.0698` maxDD `-6.4211`
- `market_context_high->metal_1h` score `-0.0427` n `108` status `ready` deltaP `6.1377` edge `0.022` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.2475` n `108` status `ready` deltaP `3.5651` edge `0.0057` maxDD `-1.2295`
- `market_context_high->crypto_major_1h` score `-0.3202` n `108` status `ready` deltaP `4.5465` edge `0.0683` maxDD `-6.5061`
- `market_context_high->crypto_alt_1h` score `-0.7441` n `108` status `ready` deltaP `-1.935` edge `0.0397` maxDD `-5.4428`
- `market_context_high->equity_1h` score `-1.1194` n `108` status `ready` deltaP `6.6423` edge `0.0403` maxDD `-10.8962`
- `market_context_high->fx_1h` score `-1.6349` n `108` status `ready` deltaP `-11.6988` edge `-0.0023` maxDD `-0.4757`
- `market_context_high->index_4h` score `-1.8344` n `108` status `ready` deltaP `-2.2245` edge `-0.0037` maxDD `-4.7471`
- `market_context_high->fx_4h` score `-2.3936` n `108` status `ready` deltaP `-15.1027` edge `-0.0046` maxDD `-1.794`
- `market_context_high->commodity_1h` score `-2.4223` n `108` status `ready` deltaP `-9.8193` edge `-0.0282` maxDD `-3.9892`
- `market_context_high->metal_24h` score `-3.7245` n `99` status `ready` deltaP `15.404` edge `0.1121` maxDD `-32.0132`
- `market_context_high->fx_24h` score `-6.5562` n `99` status `ready` deltaP `-17.077` edge `-0.0052` maxDD `-5.5179`
- `market_context_high->commodity_4h` score `-8.0956` n `108` status `ready` deltaP `-28.9577` edge `-0.1123` maxDD `-15.5426`
- `market_context_high->equity_4h` score `-9.3571` n `108` status `ready` deltaP `-6.8992` edge `-0.0516` maxDD `-44.2396`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

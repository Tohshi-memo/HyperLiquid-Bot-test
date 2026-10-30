# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-30T05:37:31.602161+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `6612`

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

- `market_context_high->unknown_24h` score `1711.9574` n `134` status `ready` deltaP `-2.7908` edge `142.7247` maxDD `-1.1049`
- `market_context_high->unknown_4h` score `35.2957` n `134` status `ready` deltaP `4.3798` edge `2.9254` maxDD `-0.3966`
- `market_context_high->index_24h` score `2.9958` n `134` status `ready` deltaP `33.3541` edge `0.0456` maxDD `-0.1315`
- `market_context_high->equity_24h` score `1.048` n `134` status `ready` deltaP `16.3117` edge `0.2543` maxDD `-14.0571`
- `market_context_high->metal_1h` score `0.3182` n `134` status `ready` deltaP `10.0054` edge `0.012` maxDD `-0.3659`
- `market_context_high->metal_4h` score `0.2034` n `134` status `ready` deltaP `14.3066` edge `0.0203` maxDD `-1.8344`
- `market_context_high->commodity_4h` score `0.1405` n `134` status `ready` deltaP `12.7184` edge `0.0488` maxDD `-1.0837`
- `market_context_high->equity_1h` score `-0.0368` n `134` status `ready` deltaP `3.4342` edge `0.0616` maxDD `-2.3383`
- `market_context_high->fx_1h` score `-0.0855` n `134` status `ready` deltaP `3.8788` edge `-0.001` maxDD `-0.1986`
- `market_context_high->crypto_major_1h` score `-0.0923` n `134` status `ready` deltaP `6.5667` edge `0.0513` maxDD `-5.2213`
- `market_context_high->commodity_1h` score `-0.2816` n `134` status `ready` deltaP `2.0936` edge `0.014` maxDD `-0.4475`
- `market_context_high->equity_4h` score `-0.3494` n `134` status `ready` deltaP `1.4766` edge `0.1038` maxDD `-6.008`
- `market_context_high->fx_4h` score `-0.5694` n `134` status `ready` deltaP `-1.3878` edge `-0.0039` maxDD `-0.4545`
- `market_context_high->crypto_alt_1h` score `-0.7901` n `134` status `ready` deltaP `3.5973` edge `0.0612` maxDD `-8.251`
- `market_context_high->index_1h` score `-0.8762` n `134` status `ready` deltaP `-2.5449` edge `-0.0002` maxDD `-1.1344`
- `market_context_high->metal_24h` score `-1.4073` n `134` status `ready` deltaP `3.9257` edge `0.0581` maxDD `-10.5088`
- `market_context_high->crypto_major_4h` score `-1.59` n `134` status `ready` deltaP `8.6185` edge `0.0682` maxDD `-19.0267`
- `market_context_high->fx_24h` score `-1.6802` n `134` status `ready` deltaP `-1.236` edge `0.0013` maxDD `-0.9792`
- `market_context_high->index_4h` score `-1.9674` n `134` status `ready` deltaP `-2.9282` edge `-0.0124` maxDD `-3.5621`
- `market_context_high->commodity_24h` score `-3.8537` n `134` status `ready` deltaP `7.328` edge `0.0161` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

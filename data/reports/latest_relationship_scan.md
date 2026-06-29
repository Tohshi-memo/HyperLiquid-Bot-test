# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T03:07:26.851655+00:00`
- Price records: `672`
- Market context records: `5104`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10340`

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

- `market_context_high->unknown_24h` score `18.8605` n `79` status `ready` deltaP `27.8942` edge `1.42` maxDD `-1.4072`
- `market_context_high->unknown_4h` score `8.2758` n `111` status `ready` deltaP `22.7656` edge `0.6401` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `6.5708` n `123` status `ready` deltaP `4.3218` edge `0.5829` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `3.0419` n `111` status `ready` deltaP `14.49` edge `0.4533` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `2.3646` n `111` status `ready` deltaP `12.8406` edge `0.4468` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.6644` n `111` status `ready` deltaP `8.7248` edge `0.161` maxDD `-6.3852`
- `market_context_high->crypto_alt_1h` score `0.6183` n `123` status `ready` deltaP `7.7443` edge `0.1238` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5107` n `123` status `ready` deltaP `8.5986` edge `0.1327` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.4529` n `123` status `ready` deltaP `8.6218` edge `0.0599` maxDD `-2.745`
- `market_context_high->metal_1h` score `0.3584` n `123` status `ready` deltaP `9.6904` edge `0.031` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.0551` n `123` status `ready` deltaP `4.7709` edge `0.0115` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.2032` n `111` status `ready` deltaP `5.3285` edge `0.0296` maxDD `-2.294`
- `market_context_high->metal_4h` score `-0.4154` n `111` status `ready` deltaP `3.4154` edge `0.065` maxDD `-4.6157`
- `market_context_high->fx_1h` score `-0.8209` n `123` status `ready` deltaP `-5.9917` edge `-0.0012` maxDD `-0.7944`
- `market_context_high->commodity_1h` score `-0.9198` n `123` status `ready` deltaP `-0.0864` edge `-0.0003` maxDD `-2.062`
- `market_context_high->fx_24h` score `-1.6384` n `79` status `ready` deltaP `-4.0106` edge `-0.0086` maxDD `-1.7626`
- `market_context_high->commodity_24h` score `-1.6768` n `79` status `ready` deltaP `7.7004` edge `0.0299` maxDD `-15.0303`
- `market_context_high->fx_4h` score `-1.8004` n `111` status `ready` deltaP `-5.8559` edge `-0.0037` maxDD `-1.9169`
- `market_context_high->commodity_4h` score `-2.1925` n `111` status `ready` deltaP `1.6273` edge `-0.0226` maxDD `-7.3435`
- `market_context_high->metal_24h` score `-4.5597` n `79` status `ready` deltaP `-6.5995` edge `0.0049` maxDD `-32.9721`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

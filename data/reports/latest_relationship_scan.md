# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T02:07:22.016110+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `4435.3606` n `54` status `ready` deltaP `22.9745` edge `369.5023` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `14.3331` n `40` status `ready` deltaP `51.4583` edge `0.8911` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.235` n `40` status `ready` deltaP `51.3194` edge `0.6069` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `3.8371` n `54` status `ready` deltaP `10.2191` edge `0.328` maxDD `-3.4427`
- `news_risk_high->index_4h` score `1.5772` n `54` status `ready` deltaP `15.1648` edge `0.0684` maxDD `-0.3783`
- `market_context_high->commodity_4h` score `0.7458` n `43` status `ready` deltaP `9.8908` edge `0.1143` maxDD `-2.7703`
- `news_risk_high->equity_1h` score `0.4956` n `54` status `ready` deltaP `8.3223` edge `0.0681` maxDD `-2.916`
- `market_context_high->fx_4h` score `0.417` n `43` status `ready` deltaP `17.6652` edge `0.0153` maxDD `-1.3685`
- `news_risk_high->metal_4h` score `0.3984` n `54` status `ready` deltaP `9.2818` edge `0.0243` maxDD `-0.8085`
- `market_context_high->commodity_1h` score `0.3845` n `47` status `ready` deltaP `7.864` edge `0.0343` maxDD `-1.3282`
- `market_context_high->crypto_alt_4h` score `0.336` n `43` status `ready` deltaP `5.736` edge `0.0954` maxDD `-4.9116`
- `market_context_high->fx_1h` score `0.0001` n `47` status `ready` deltaP `7.1155` edge `-0.0085` maxDD `-0.7804`
- `news_risk_high->index_1h` score `-0.0159` n `54` status `ready` deltaP `3.3101` edge `0.0082` maxDD `-0.5845`
- `news_risk_high->fx_4h` score `-0.2147` n `54` status `ready` deltaP `6.7694` edge `0.0231` maxDD `-0.6604`
- `news_risk_high->metal_1h` score `-0.2944` n `54` status `ready` deltaP `0.6543` edge `0.0031` maxDD `-0.5599`
- `news_risk_high->crypto_alt_1h` score `-0.3256` n `54` status `ready` deltaP `4.7516` edge `0.0094` maxDD `-3.1233`
- `news_risk_high->crypto_major_1h` score `-0.3447` n `54` status `ready` deltaP `3.1992` edge `0.0065` maxDD `-3.762`
- `news_risk_high->fx_1h` score `-0.3544` n `54` status `ready` deltaP `-0.0555` edge `0.0031` maxDD `-0.2475`
- `market_context_high->fx_24h` score `-0.7223` n `40` status `ready` deltaP `0.6597` edge `0.0334` maxDD `-2.506`
- `news_risk_high->commodity_1h` score `-1.0159` n `54` status `ready` deltaP `0.693` edge `-0.0215` maxDD `-2.0891`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

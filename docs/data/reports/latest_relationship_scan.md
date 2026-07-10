# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-10T23:07:24.624174+00:00`
- Price records: `672`
- Market context records: `6331`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11134`

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

- `news_risk_high->crypto_alt_24h` score `15.4662` n `32` status `ready` deltaP `43.2292` edge `1.0154` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.0728` n `32` status `ready` deltaP `50.6944` edge `0.1681` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.4363` n `32` status `ready` deltaP `16.6667` edge `0.5356` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `4.2045` n `32` status `ready` deltaP `43.8262` edge `0.0628` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.4145` n `32` status `ready` deltaP `30.2083` edge `0.1037` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `2.4374` n `32` status `ready` deltaP `29.3413` edge `0.0214` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `1.5403` n `32` status `ready` deltaP `15.0262` edge `0.144` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.9603` n `32` status `ready` deltaP `11.9199` edge `0.0898` maxDD `-1.6923`
- `market_context_high->metal_4h` score `0.1589` n `196` status `ready` deltaP `10.4343` edge `0.04` maxDD `-2.7056`
- `market_context_high->index_4h` score `-0.1162` n `196` status `ready` deltaP `6.054` edge `0.021` maxDD `-0.7669`
- `market_context_high->unknown_1h` score `-0.1227` n `208` status `ready` deltaP `-8.5819` edge `0.1478` maxDD `-3.7317`
- `market_context_high->metal_1h` score `-0.3684` n `208` status `ready` deltaP `4.2492` edge `0.0022` maxDD `-1.8877`
- `market_context_high->metal_24h` score `-0.3847` n `145` status `ready` deltaP `17.7933` edge `0.0889` maxDD `-11.8809`
- `market_context_high->fx_1h` score `-0.5328` n `208` status `ready` deltaP `-1.9087` edge `-0.0022` maxDD `-0.9376`
- `market_context_high->index_1h` score `-0.5429` n `208` status `ready` deltaP `-3.1207` edge `0.0025` maxDD `-0.7709`
- `market_context_high->commodity_1h` score `-0.5694` n `208` status `ready` deltaP `-0.7485` edge `0.0003` maxDD `-2.1314`
- `news_risk_high->index_24h` score `-0.627` n `32` status `ready` deltaP `1.7361` edge `-0.0048` maxDD `-2.3058`
- `news_risk_high->unknown_1h` score `-0.7036` n `32` status `ready` deltaP `6.0816` edge `-0.0647` maxDD `-0.7581`
- `market_context_high->equity_4h` score `-0.7618` n `196` status `ready` deltaP `4.2466` edge `0.0439` maxDD `-8.2573`
- `news_risk_high->metal_1h` score `-0.7636` n `32` status `ready` deltaP `-3.4431` edge `-0.0252` maxDD `-1.6464`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

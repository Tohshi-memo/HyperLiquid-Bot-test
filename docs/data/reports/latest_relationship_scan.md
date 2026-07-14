# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-14T07:22:30.618200+00:00`
- Price records: `672`
- Market context records: `6687`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11784`

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

- `market_context_high->unknown_1h` score `1.9625` n `195` status `ready` deltaP `-4.9578` edge `0.2867` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.8291` n `195` status `ready` deltaP `11.2367` edge `0.181` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.3485` n `195` status `ready` deltaP `9.2292` edge `0.0535` maxDD `-4.2122`
- `market_context_high->unknown_24h` score `0.172` n `195` status `ready` deltaP `-2.2997` edge `0.4126` maxDD `-12.3511`
- `market_context_high->crypto_alt_1h` score `0.1038` n `195` status `ready` deltaP `5.9804` edge `0.0452` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2636` n `195` status `ready` deltaP `2.2693` edge `0.0013` maxDD `-0.6845`
- `market_context_high->index_1h` score `-0.4652` n `195` status `ready` deltaP `1.0909` edge `0.0045` maxDD `-0.7136`
- `market_context_high->equity_1h` score `-0.5342` n `195` status `ready` deltaP `3.8876` edge `0.0083` maxDD `-3.8827`
- `market_context_high->commodity_1h` score `-0.5614` n `195` status `ready` deltaP `0.6802` edge `-0.0082` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.5908` n `195` status `ready` deltaP `-3.5882` edge `0.0007` maxDD `-1.2017`
- `market_context_high->index_4h` score `-0.872` n `195` status `ready` deltaP `10.8873` edge `0.0036` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.4164` n `195` status `ready` deltaP `6.0623` edge `-0.0008` maxDD `-3.3635`
- `market_context_high->crypto_major_4h` score `-1.4478` n `195` status `ready` deltaP `8.7664` edge `0.0874` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.5841` n `195` status `ready` deltaP `-2.9581` edge `-0.0339` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.7137` n `195` status `ready` deltaP `6.5213` edge `0.077` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-1.9943` n `195` status `ready` deltaP `-14.8241` edge `0.1732` maxDD `-10.5788`
- `market_context_high->metal_4h` score `-2.1317` n `195` status `ready` deltaP `-1.2969` edge `0.0214` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.2527` n `195` status `ready` deltaP `7.5742` edge `-0.0406` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-5.7251` n `195` status `ready` deltaP `-11.2526` edge `-0.0085` maxDD `-9.4862`
- `market_context_high->metal_24h` score `-7.0089` n `195` status `ready` deltaP `-6.3836` edge `-0.0075` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

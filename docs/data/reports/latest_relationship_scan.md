# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T21:07:28.041899+00:00`
- Price records: `672`
- Market context records: `6642`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11766`

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

- `market_context_high->unknown_1h` score `2.4034` n `203` status `ready` deltaP `-4.8922` edge `0.323` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `0.8108` n `191` status `ready` deltaP `-1.4865` edge `0.4385` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.6457` n `191` status `ready` deltaP `10.4594` edge `0.1709` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0994` n `203` status `ready` deltaP `8.6642` edge `0.0493` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1277` n `203` status `ready` deltaP `5.9017` edge `0.0431` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4766` n `203` status `ready` deltaP `0.8208` edge `0.0052` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6817` n `203` status `ready` deltaP `-1.5884` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.6947` n `203` status `ready` deltaP `-15.4241` edge `0.2855` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.794` n `203` status `ready` deltaP `10.9313` edge `0.0133` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.873` n `203` status `ready` deltaP `3.0523` edge `0.0096` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0247` n `203` status `ready` deltaP `10.872` edge `0.1276` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.0933` n `203` status `ready` deltaP `-2.758` edge `0.0014` maxDD `-1.5966`
- `market_context_high->crypto_alt_4h` score `-1.4044` n `203` status `ready` deltaP `7.5648` edge `0.1097` maxDD `-19.2145`
- `market_context_high->commodity_4h` score `-1.4213` n `203` status `ready` deltaP `-1.3119` edge `-0.024` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.4808` n `203` status `ready` deltaP `4.6895` edge `0.0001` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8874` n `203` status `ready` deltaP `1.827` edge `0.0319` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3467` n `203` status `ready` deltaP `8.9834` edge `0.0048` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.7186` n `191` status `ready` deltaP `-2.8425` edge `0.0258` maxDD `-23.5333`
- `market_context_high->fx_24h` score `-6.2151` n `191` status `ready` deltaP `-10.4503` edge `-0.0076` maxDD `-10.5858`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

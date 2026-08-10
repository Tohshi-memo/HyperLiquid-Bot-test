# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T23:37:26.519460+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11712`

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

- `market_context_high->fx_24h` score `1.0929` n `145` status `ready` deltaP `20.4064` edge `0.0358` maxDD `-1.4613`
- `market_context_high->commodity_4h` score `0.7706` n `175` status `ready` deltaP `10.7961` edge `0.0637` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.5455` n `180` status `ready` deltaP `7.688` edge `0.0285` maxDD `-0.7439`
- `market_context_high->fx_1h` score `-0.0277` n `180` status `ready` deltaP `6.151` edge `0.0006` maxDD `-0.613`
- `market_context_high->fx_4h` score `-0.0494` n `175` status `ready` deltaP `7.2543` edge `0.0075` maxDD `-0.4647`
- `market_context_high->index_24h` score `-1.1909` n `145` status `ready` deltaP `-4.4607` edge `0.0466` maxDD `-6.2304`
- `market_context_high->index_4h` score `-1.1914` n `175` status `ready` deltaP `-6.764` edge `-0.0172` maxDD `-1.5693`
- `market_context_high->index_1h` score `-1.2241` n `180` status `ready` deltaP `-7.0758` edge `-0.0057` maxDD `-0.9309`
- `market_context_high->metal_1h` score `-1.2564` n `180` status `ready` deltaP `-4.8137` edge `-0.009` maxDD `-2.0884`
- `market_context_high->metal_24h` score `-1.3518` n `145` status `ready` deltaP `2.5482` edge `0.0028` maxDD `-2.9283`
- `market_context_high->equity_1h` score `-1.3977` n `180` status `ready` deltaP `-6.0545` edge `-0.0225` maxDD `-6.6398`
- `market_context_high->crypto_alt_1h` score `-2.9545` n `180` status `ready` deltaP `-11.9494` edge `-0.0468` maxDD `-6.5795`
- `market_context_high->metal_4h` score `-3.1209` n `175` status `ready` deltaP `-6.9582` edge `-0.0373` maxDD `-6.1111`
- `market_context_high->crypto_major_1h` score `-3.8192` n `180` status `ready` deltaP `-10.642` edge `-0.0569` maxDD `-11.9002`
- `market_context_high->equity_4h` score `-4.4032` n `175` status `ready` deltaP `-15.9451` edge `-0.1473` maxDD `-15.8728`
- `market_context_high->crypto_major_24h` score `-4.9123` n `145` status `ready` deltaP `-7.046` edge `-0.1352` maxDD `-26.8083`
- `market_context_high->equity_24h` score `-5.1484` n `145` status `ready` deltaP `-4.3053` edge `-0.0084` maxDD `-38.5028`
- `market_context_high->commodity_24h` score `-5.2111` n `145` status `ready` deltaP `2.0965` edge `-0.034` maxDD `-38.8455`
- `market_context_high->crypto_alt_4h` score `-7.2271` n `175` status `ready` deltaP `-15.9835` edge `-0.1609` maxDD `-20.1177`
- `market_context_high->crypto_alt_24h` score `-8.1197` n `145` status `ready` deltaP `-12.8226` edge `-0.2172` maxDD `-22.583`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

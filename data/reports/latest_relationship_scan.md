# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T18:52:27.748245+00:00`
- Price records: `672`
- Market context records: `6631`
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

- `market_context_high->unknown_1h` score `2.2643` n `203` status `ready` deltaP `-5.7904` edge `0.3174` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.8474` n `186` status `ready` deltaP `-1.0566` edge `0.4648` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.4617` n `186` status `ready` deltaP `9.6291` edge `0.1611` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.0736` n `203` status `ready` deltaP `8.8139` edge `0.045` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1781` n `203` status `ready` deltaP `6.0514` edge `0.0379` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.2461` n `203` status `ready` deltaP `2.786` edge `0.0006` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4929` n `203` status `ready` deltaP `0.5214` edge `0.0051` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6537` n `203` status `ready` deltaP `-1.1393` edge `-0.0079` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.8179` n `203` status `ready` deltaP `-16.0339` edge `0.2793` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.8224` n `203` status `ready` deltaP `10.6264` edge `0.0117` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8418` n `203` status `ready` deltaP `3.202` edge `0.0112` maxDD `-3.8827`
- `market_context_high->metal_1h` score `-1.1137` n `203` status `ready` deltaP `-2.9077` edge `0.0007` maxDD `-1.5966`
- `market_context_high->crypto_major_4h` score `-1.183` n `203` status `ready` deltaP `9.9574` edge `0.1134` maxDD `-16.8495`
- `market_context_high->commodity_4h` score `-1.3596` n `203` status `ready` deltaP `-1.1595` edge `-0.0171` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.522` n `203` status `ready` deltaP `3.9274` edge `-0.0001` maxDD `-3.3635`
- `market_context_high->crypto_alt_4h` score `-1.5844` n `203` status `ready` deltaP `6.8026` edge `0.0917` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-1.9638` n `203` status `ready` deltaP `0.9124` edge `0.0282` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.4115` n `203` status `ready` deltaP `8.9834` edge `-0.0006` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.2238` n `186` status `ready` deltaP `-2.344` edge `0.0301` maxDD `-20.7356`
- `market_context_high->fx_24h` score `-6.0544` n `186` status `ready` deltaP `-9.5918` edge `-0.0047` maxDD `-10.2041`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

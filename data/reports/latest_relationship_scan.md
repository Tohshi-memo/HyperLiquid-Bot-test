# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-16T23:22:24.337777+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11831`

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

- `market_context_high->unknown_24h` score `102.3009` n `81` status `ready` deltaP `-30.7871` edge `13.5891` maxDD `-7.8016`
- `market_context_high->commodity_24h` score `5.5501` n `81` status `ready` deltaP `37.2107` edge `0.2333` maxDD `-0.1757`
- `market_context_high->commodity_4h` score `1.0723` n `110` status `ready` deltaP `12.4002` edge `0.0538` maxDD `-0.7687`
- `market_context_high->commodity_1h` score `-0.2107` n `114` status `ready` deltaP `1.6914` edge `0.0123` maxDD `-0.624`
- `market_context_high->metal_4h` score `-0.2576` n `110` status `ready` deltaP `14.8337` edge `0.0088` maxDD `-4.5909`
- `market_context_high->fx_1h` score `-0.3502` n `114` status `ready` deltaP `0.8562` edge `0.0016` maxDD `-0.2527`
- `market_context_high->fx_4h` score `-0.5005` n `110` status `ready` deltaP `2.694` edge `0.0008` maxDD `-0.504`
- `market_context_high->metal_1h` score `-0.5297` n `114` status `ready` deltaP `1.1346` edge `-0.0039` maxDD `-1.7257`
- `market_context_high->crypto_major_4h` score `-0.5923` n `110` status `ready` deltaP `3.484` edge `0.0045` maxDD `-3.9599`
- `market_context_high->index_1h` score `-0.6157` n `114` status `ready` deltaP `-3.8055` edge `-0.0014` maxDD `-0.5064`
- `market_context_high->index_24h` score `-0.6424` n `81` status `ready` deltaP `7.9089` edge `-0.0458` maxDD `-0.8365`
- `market_context_high->crypto_major_24h` score `-1.1514` n `81` status `ready` deltaP `-3.6266` edge `0.1354` maxDD `-15.0399`
- `market_context_high->index_4h` score `-1.1638` n `110` status `ready` deltaP `-9.4678` edge `-0.0052` maxDD `-0.8045`
- `market_context_high->crypto_alt_1h` score `-1.7941` n `114` status `ready` deltaP `-4.6854` edge `-0.0161` maxDD `-4.5069`
- `market_context_high->crypto_major_1h` score `-1.8992` n `114` status `ready` deltaP `-5.2632` edge `-0.0248` maxDD `-3.8701`
- `market_context_high->fx_24h` score `-2.3241` n `81` status `ready` deltaP `-18.9622` edge `-0.0108` maxDD `-1.8596`
- `market_context_high->metal_24h` score `-2.3791` n `81` status `ready` deltaP `-14.1783` edge `0.0407` maxDD `-7.0954`
- `market_context_high->equity_1h` score `-2.4488` n `114` status `ready` deltaP `-9.8382` edge `-0.0432` maxDD `-4.289`
- `market_context_high->equity_24h` score `-5.156` n `81` status `ready` deltaP `2.1991` edge `-0.3083` maxDD `-23.3906`
- `market_context_high->crypto_alt_4h` score `-5.3155` n `110` status `ready` deltaP `-6.5105` edge `-0.0314` maxDD `-16.786`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

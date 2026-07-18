# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-18T16:52:31.522990+00:00`
- Price records: `672`
- Market context records: `7160`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11762`

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

- `market_context_high->fx_4h` score `0.191` n `157` status `ready` deltaP `11.6369` edge `0.0125` maxDD `-0.9333`
- `market_context_high->fx_1h` score `-0.3563` n `167` status `ready` deltaP `2.3952` edge `0.0015` maxDD `-0.4393`
- `market_context_high->unknown_1h` score `-0.6032` n `167` status `ready` deltaP `-1.7964` edge `0.0259` maxDD `-1.4688`
- `market_context_high->crypto_alt_1h` score `-0.6176` n `167` status `ready` deltaP `-0.1497` edge `0.0257` maxDD `-5.9775`
- `market_context_high->crypto_major_1h` score `-0.6637` n `167` status `ready` deltaP `3.1437` edge `0.035` maxDD `-7.6171`
- `market_context_high->commodity_1h` score `-0.6659` n `167` status `ready` deltaP `-1.0479` edge `-0.0163` maxDD `-1.9668`
- `market_context_high->index_1h` score `-0.7534` n `167` status `ready` deltaP `1.1976` edge `-0.0043` maxDD `-2.3175`
- `market_context_high->metal_1h` score `-1.8983` n `167` status `ready` deltaP `-7.1857` edge `-0.005` maxDD `-2.0897`
- `market_context_high->unknown_4h` score `-2.0242` n `157` status `ready` deltaP `-6.1917` edge `0.0128` maxDD `-6.1498`
- `market_context_high->commodity_4h` score `-2.1159` n `157` status `ready` deltaP `-5.1587` edge `-0.0384` maxDD `-2.9494`
- `market_context_high->metal_4h` score `-2.9358` n `157` status `ready` deltaP `-10.3999` edge `-0.0122` maxDD `-5.2551`
- `market_context_high->equity_1h` score `-3.6162` n `167` status `ready` deltaP `-1.3473` edge `-0.0397` maxDD `-15.5469`
- `market_context_high->index_4h` score `-3.9457` n `157` status `ready` deltaP `-2.4303` edge `-0.0427` maxDD `-12.2591`
- `market_context_high->commodity_24h` score `-4.4928` n `133` status `ready` deltaP `-13.4581` edge `-0.1538` maxDD `-4.4704`
- `market_context_high->fx_24h` score `-4.8632` n `133` status `ready` deltaP `-14.6629` edge `-0.0248` maxDD `-3.9503`
- `market_context_high->crypto_major_4h` score `-4.8922` n `157` status `ready` deltaP `2.6487` edge `0.01` maxDD `-25.1605`
- `market_context_high->crypto_alt_4h` score `-5.5136` n `157` status `ready` deltaP `-3.1216` edge `-0.029` maxDD `-24.7723`
- `market_context_high->unknown_24h` score `-10.092` n `133` status `ready` deltaP `-32.7029` edge `-0.1083` maxDD `-23.5076`
- `market_context_high->metal_24h` score `-14.7562` n `133` status `ready` deltaP `-32.1232` edge `-0.1974` maxDD `-40.7836`
- `market_context_high->equity_4h` score `-14.8047` n `157` status `ready` deltaP `-4.2975` edge `-0.2145` maxDD `-66.5792`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

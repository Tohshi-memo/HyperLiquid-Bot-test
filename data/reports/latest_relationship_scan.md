# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T18:22:25.188694+00:00`
- Price records: `672`
- Market context records: `5799`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9058`

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

- `market_context_high->equity_24h` score `0.5201` n `248` status `ready` deltaP `15.3954` edge `0.4486` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0579` n `300` status `ready` deltaP `6.2155` edge `0.1176` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.2512` n `300` status `ready` deltaP `2.2994` edge `0.001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.6271` n `300` status `ready` deltaP `3.2156` edge `0.027` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.6316` n `300` status `ready` deltaP `0.3393` edge `0.0036` maxDD `-0.9472`
- `market_context_high->metal_1h` score `-0.6459` n `300` status `ready` deltaP `2.2036` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7734` n `300` status `ready` deltaP `-2.02` edge `-0.0052` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9284` n `300` status `ready` deltaP `3.1697` edge `0.0336` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1241` n `300` status `ready` deltaP `1.4212` edge `0.0303` maxDD `-6.6758`
- `market_context_high->fx_24h` score `-1.1869` n `248` status `ready` deltaP `12.6568` edge `0.0365` maxDD `-4.8432`
- `market_context_high->index_4h` score `-1.2121` n `300` status `ready` deltaP `0.4838` edge `0.0101` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4603` n `300` status `ready` deltaP `0.628` edge `0.0035` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.2916` n `300` status `ready` deltaP `-3.0915` edge `-0.0245` maxDD `-12.5616`
- `market_context_high->metal_4h` score `-2.4616` n `300` status `ready` deltaP `-5.1829` edge `-0.0472` maxDD `-11.3737`
- `market_context_high->index_24h` score `-2.7979` n `248` status `ready` deltaP `3.7131` edge `0.031` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9298` n `300` status `ready` deltaP `7.6931` edge `0.1418` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.5334` n `300` status `ready` deltaP `5.4553` edge `0.0867` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.6071` n `248` status `ready` deltaP `-6.8324` edge `-0.2483` maxDD `-24.9241`
- `market_context_high->crypto_major_24h` score `-8.9145` n `248` status `ready` deltaP `-0.1568` edge `-0.1835` maxDD `-30.0`
- `market_context_high->commodity_24h` score `-10.3966` n `248` status `ready` deltaP `-14.0681` edge `-0.0791` maxDD `-38.1463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

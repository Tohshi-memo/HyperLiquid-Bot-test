# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T00:52:30.421628+00:00`
- Price records: `672`
- Market context records: `5829`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10076`

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

- `market_context_high->equity_4h` score `0.4978` n `274` status `ready` deltaP `7.1802` edge `0.1394` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2626` n `274` status `ready` deltaP `2.1712` edge `0.0004` maxDD `-0.5499`
- `market_context_high->equity_24h` score `-0.4423` n `246` status `ready` deltaP `15.2905` edge `0.3691` maxDD `-31.6316`
- `market_context_high->commodity_1h` score `-0.5293` n `274` status `ready` deltaP `-0.8053` edge `-0.0016` maxDD `-2.2045`
- `market_context_high->equity_1h` score `-0.5575` n `274` status `ready` deltaP `3.2301` edge `0.0327` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5711` n `274` status `ready` deltaP `2.7143` edge `0.0014` maxDD `-2.0339`
- `market_context_high->index_1h` score `-0.6071` n `274` status `ready` deltaP `0.4404` edge `0.004` maxDD `-0.7819`
- `market_context_high->crypto_major_1h` score `-0.9249` n `274` status `ready` deltaP `2.9296` edge `0.0355` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.0782` n `274` status `ready` deltaP `1.4697` edge `0.0338` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1588` n `274` status `ready` deltaP `0.8646` edge `0.0144` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5379` n `246` status `ready` deltaP `9.0193` edge `0.0245` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.5893` n `274` status `ready` deltaP `-1.3118` edge `-0.0001` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2116` n `274` status `ready` deltaP `-5.035` edge `-0.0454` maxDD `-9.0328`
- `market_context_high->commodity_4h` score `-2.7103` n `274` status `ready` deltaP `-1.4332` edge `-0.0165` maxDD `-8.6511`
- `market_context_high->index_24h` score `-2.8482` n `246` status `ready` deltaP `3.3918` edge `0.0267` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.0678` n `274` status `ready` deltaP `6.704` edge `0.1369` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8371` n `274` status `ready` deltaP `4.029` edge `0.0709` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.7491` n `246` status `ready` deltaP `-12.1232` edge `-0.0603` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-6.5282` n `246` status `ready` deltaP `-1.3085` edge `-0.2205` maxDD `-14.517`
- `market_context_high->crypto_alt_24h` score `-12.6471` n `246` status `ready` deltaP `-10.6411` edge `-0.5198` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

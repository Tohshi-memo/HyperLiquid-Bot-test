# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T07:37:32.628867+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7926`

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

- `market_context_high->unknown_4h` score `45.1639` n `102` status `ready` deltaP `1.1687` edge `3.7894` maxDD `-1.016`
- `market_context_high->unknown_1h` score `12.6875` n `114` status `ready` deltaP `4.4831` edge `1.0763` maxDD `-1.5781`
- `market_context_high->crypto_alt_24h` score `8.6257` n `38` status `ready` deltaP `25.4203` edge `0.6202` maxDD `-4.669`
- `market_context_high->crypto_major_24h` score `2.1426` n `38` status `ready` deltaP `14.428` edge `0.1883` maxDD `-5.8084`
- `market_context_high->commodity_24h` score `0.741` n `38` status `ready` deltaP `14.4006` edge `0.0899` maxDD `-3.6055`
- `market_context_high->fx_1h` score `-0.0409` n `114` status `ready` deltaP `3.9999` edge `0.003` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0845` n `102` status `ready` deltaP `6.0767` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2906` n `38` status `ready` deltaP `6.6338` edge `0.006` maxDD `-0.9988`
- `market_context_high->commodity_1h` score `-0.5649` n `114` status `ready` deltaP `-0.8115` edge `0.0084` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6071` n `114` status `ready` deltaP `4.9191` edge `-0.0042` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6448` n `114` status `ready` deltaP `-1.8411` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.8543` n `102` status `ready` deltaP `-3.0039` edge `0.0334` maxDD `-1.165`
- `market_context_high->crypto_major_1h` score `-1.4294` n `114` status `ready` deltaP `1.1136` edge `-0.0326` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-1.8297` n `102` status `ready` deltaP `5.8554` edge `-0.0205` maxDD `-5.3474`
- `market_context_high->index_4h` score `-1.997` n `102` status `ready` deltaP `-4.6629` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.563` n `38` status `ready` deltaP `-4.4682` edge `-0.0292` maxDD `-6.3676`
- `market_context_high->crypto_alt_1h` score `-3.1658` n `114` status `ready` deltaP `-2.4189` edge `-0.0603` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7851` n `114` status `ready` deltaP `-0.1944` edge `-0.0868` maxDD `-12.1865`
- `market_context_high->crypto_major_4h` score `-5.9116` n `102` status `ready` deltaP `-9.6306` edge `-0.194` maxDD `-33.3092`
- `market_context_high->index_24h` score `-6.2313` n `38` status `ready` deltaP `-29.6144` edge `-0.1917` maxDD `-5.078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

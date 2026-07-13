# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T20:07:29.554407+00:00`
- Price records: `672`
- Market context records: `6637`
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

- `market_context_high->unknown_1h` score `2.3423` n `203` status `ready` deltaP `-5.491` edge `0.3219` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `1.4865` n `189` status `ready` deltaP `-1.3228` edge `0.449` maxDD `-12.3047`
- `market_context_high->commodity_24h` score `0.5703` n `189` status `ready` deltaP `10.1326` edge `0.1668` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `0.108` n `203` status `ready` deltaP `8.8139` edge `0.0494` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.1205` n `203` status `ready` deltaP `6.0514` edge `0.0427` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.222` n `203` status `ready` deltaP `3.2351` edge `0.0007` maxDD `-0.7249`
- `market_context_high->index_1h` score `-0.4758` n `203` status `ready` deltaP `0.8208` edge `0.0053` maxDD `-0.7417`
- `market_context_high->commodity_1h` score `-0.6817` n `203` status `ready` deltaP `-1.5884` edge `-0.0085` maxDD `-2.1314`
- `market_context_high->unknown_4h` score `-0.7237` n `203` status `ready` deltaP `-15.5766` edge `0.2841` maxDD `-10.5788`
- `market_context_high->index_4h` score `-0.8051` n `203` status `ready` deltaP `10.7788` edge `0.0129` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-0.8167` n `203` status `ready` deltaP `3.3517` edge `0.0123` maxDD `-3.8827`
- `market_context_high->crypto_major_4h` score `-1.0601` n `203` status `ready` deltaP `10.5671` edge `0.1251` maxDD `-16.8495`
- `market_context_high->metal_1h` score `-1.1125` n `203` status `ready` deltaP `-2.9077` edge `0.0008` maxDD `-1.5966`
- `market_context_high->commodity_4h` score `-1.4034` n `203` status `ready` deltaP `-1.3119` edge `-0.0217` maxDD `-5.6246`
- `market_context_high->crypto_alt_4h` score `-1.4474` n `203` status `ready` deltaP `7.4124` edge `0.1052` maxDD `-19.2145`
- `market_context_high->fx_4h` score `-1.4895` n `203` status `ready` deltaP `4.5371` edge `0.0` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.9023` n `203` status `ready` deltaP `1.6746` edge `0.031` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-4.3407` n `203` status `ready` deltaP `8.9834` edge `0.0053` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-5.5315` n `189` status `ready` deltaP `-2.6831` edge `0.0269` maxDD `-22.4543`
- `market_context_high->fx_24h` score `-6.1558` n `189` status `ready` deltaP `-10.1124` edge `-0.0063` maxDD `-10.475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

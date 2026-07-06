# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-06T01:52:29.018426+00:00`
- Price records: `672`
- Market context records: `5833`
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

- `market_context_high->equity_4h` score `0.5881` n `270` status `ready` deltaP `7.5429` edge `0.1445` maxDD `-6.9958`
- `market_context_high->fx_1h` score `-0.2856` n `270` status `ready` deltaP `1.7731` edge `0.0001` maxDD `-0.5499`
- `market_context_high->equity_1h` score `-0.4369` n `270` status `ready` deltaP `4.1384` edge `0.0367` maxDD `-5.0555`
- `market_context_high->commodity_1h` score `-0.5194` n `270` status `ready` deltaP `-0.7097` edge `-0.0016` maxDD `-2.1545`
- `market_context_high->equity_24h` score `-0.5229` n `242` status `ready` deltaP `15.4227` edge `0.3615` maxDD `-31.6316`
- `market_context_high->index_1h` score `-0.5591` n `270` status `ready` deltaP `1.2298` edge `0.0049` maxDD `-0.7819`
- `market_context_high->metal_1h` score `-0.6151` n `270` status `ready` deltaP `2.2699` edge `0.0007` maxDD `-2.0339`
- `market_context_high->crypto_major_1h` score `-0.9648` n `270` status `ready` deltaP `2.6403` edge `0.0341` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1163` n `270` status `ready` deltaP `1.1588` edge `0.0327` maxDD `-6.6758`
- `market_context_high->index_4h` score `-1.1719` n `270` status `ready` deltaP `0.6132` edge `0.0144` maxDD `-3.165`
- `market_context_high->fx_24h` score `-1.5986` n `242` status `ready` deltaP `8.1525` edge `0.0225` maxDD `-5.5435`
- `market_context_high->fx_4h` score `-1.6232` n `270` status `ready` deltaP `-1.8293` edge `-0.001` maxDD `-2.2593`
- `market_context_high->metal_4h` score `-2.2018` n `270` status `ready` deltaP `-5.0949` edge `-0.0452` maxDD `-8.9164`
- `market_context_high->commodity_4h` score `-2.5623` n `270` status `ready` deltaP `-0.8763` edge `-0.0145` maxDD `-8.1216`
- `market_context_high->index_24h` score `-2.8882` n `242` status `ready` deltaP `2.9069` edge `0.0248` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-3.1027` n `270` status `ready` deltaP `6.3866` edge `0.1361` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.8674` n `270` status `ready` deltaP `3.8155` edge `0.0698` maxDD `-28.7346`
- `market_context_high->commodity_24h` score `-5.6968` n `242` status `ready` deltaP `-11.4311` edge `-0.0582` maxDD `-30.3426`
- `market_context_high->metal_24h` score `-5.7379` n `242` status `ready` deltaP `-0.7934` edge `-0.2127` maxDD `-11.4803`
- `market_context_high->crypto_alt_24h` score `-12.7383` n `242` status `ready` deltaP `-11.4339` edge `-0.5262` maxDD `-61.7883`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T20:22:25.348864+00:00`
- Price records: `672`
- Market context records: `5700`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8856`

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

- `market_context_high->crypto_major_4h` score `2.244` n `259` status `ready` deltaP `12.9944` edge `0.2375` maxDD `-6.6368`
- `market_context_high->equity_24h` score `1.1385` n `209` status `ready` deltaP `16.3286` edge `0.545` maxDD `-31.6316`
- `market_context_high->crypto_alt_4h` score `1.0561` n `259` status `ready` deltaP `10.3217` edge `0.1801` maxDD `-7.5392`
- `market_context_high->equity_4h` score `0.2325` n `259` status `ready` deltaP `6.7556` edge `0.1382` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `-0.1793` n `271` status `ready` deltaP `4.233` edge `0.0441` maxDD `-3.9811`
- `market_context_high->fx_1h` score `-0.2708` n `271` status `ready` deltaP `1.8798` edge `0.0008` maxDD `-0.5103`
- `market_context_high->crypto_alt_1h` score `-0.2757` n `271` status `ready` deltaP `2.5759` edge `0.0417` maxDD `-3.8812`
- `market_context_high->metal_1h` score `-0.4437` n `271` status `ready` deltaP `1.6395` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.5439` n `271` status `ready` deltaP `3.9403` edge `0.0291` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.5995` n `271` status `ready` deltaP `0.8214` edge `0.0045` maxDD `-0.9472`
- `market_context_high->fx_24h` score `-0.962` n `209` status `ready` deltaP `12.9336` edge `0.0455` maxDD `-3.4049`
- `market_context_high->commodity_1h` score `-1.1011` n `271` status `ready` deltaP `-0.9816` edge `-0.0045` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.1894` n `259` status `ready` deltaP `3.668` edge `0.0065` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.3257` n `259` status `ready` deltaP `-1.2201` edge `0.0069` maxDD `-3.165`
- `market_context_high->metal_4h` score `-2.7342` n `259` status `ready` deltaP `-9.1758` edge `-0.0518` maxDD `-11.6719`
- `market_context_high->index_24h` score `-2.8819` n `209` status `ready` deltaP `2.551` edge `0.0264` maxDD `-18.0307`
- `market_context_high->crypto_major_24h` score `-3.8301` n `209` status `ready` deltaP `6.6023` edge `0.0825` maxDD `-29.6555`
- `market_context_high->commodity_4h` score `-3.9713` n `259` status `ready` deltaP `-4.4078` edge `-0.034` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.0427` n `209` status `ready` deltaP `-8.8816` edge `-0.2443` maxDD `-32.5421`
- `market_context_high->commodity_24h` score `-12.2479` n `209` status `ready` deltaP `-12.0398` edge `-0.0795` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

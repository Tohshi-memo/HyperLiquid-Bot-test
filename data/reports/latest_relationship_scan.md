# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T17:37:27.634374+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5412`

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

- `market_context_high->unknown_4h` score `30.2097` n `113` status `ready` deltaP `-0.7487` edge `2.556` maxDD `-1.016`
- `market_context_high->fx_4h` score `-0.0439` n `113` status `ready` deltaP `7.1539` edge `0.0085` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0653` n `113` status `ready` deltaP `3.5597` edge `0.0028` maxDD `-0.1258`
- `market_context_high->crypto_major_24h` score `-0.3715` n `68` status `ready` deltaP `-1.0519` edge `0.0786` maxDD `-4.5369`
- `market_context_high->commodity_1h` score `-0.4655` n `113` status `ready` deltaP `0.2663` edge `0.0095` maxDD `-1.0053`
- `market_context_high->commodity_24h` score `-0.5785` n `68` status `ready` deltaP `2.6757` edge `0.0239` maxDD `-3.6055`
- `market_context_high->metal_1h` score `-0.6539` n `113` status `ready` deltaP `4.4844` edge `-0.0052` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.7102` n `113` status `ready` deltaP `-2.9344` edge `-0.0063` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.7937` n `113` status `ready` deltaP `-1.6283` edge `0.032` maxDD `-1.165`
- `market_context_high->fx_24h` score `-1.1297` n `68` status `ready` deltaP `7.5878` edge `0.0125` maxDD `-1.2451`
- `market_context_high->crypto_major_1h` score `-1.3667` n `113` status `ready` deltaP `2.6482` edge `-0.0348` maxDD `-9.3126`
- `market_context_high->index_24h` score `-1.7249` n `68` status `ready` deltaP `2.0527` edge `-0.1066` maxDD `-4.925`
- `market_context_high->metal_4h` score `-1.8988` n `113` status `ready` deltaP `4.7661` edge `-0.019` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.206` n `113` status `ready` deltaP `-8.6822` edge `-0.0375` maxDD `-4.3282`
- `market_context_high->metal_24h` score `-2.8275` n `68` status `ready` deltaP `-2.594` edge `0.0487` maxDD `-7.3625`
- `market_context_high->crypto_alt_1h` score `-3.2518` n `113` status `ready` deltaP `-2.3091` edge `-0.0682` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.9746` n `113` status `ready` deltaP `-1.4374` edge `-0.0943` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.5789` n `68` status `ready` deltaP `0.0` edge `-0.1978` maxDD `-42.3182`
- `market_context_high->crypto_major_4h` score `-10.0756` n `113` status `ready` deltaP `-13.3526` edge `-0.2508` maxDD `-32.9851`
- `market_context_high->equity_24h` score `-10.4788` n `68` status `ready` deltaP `-12.2957` edge `-0.7331` maxDD `-36.6024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

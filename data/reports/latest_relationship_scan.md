# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T04:37:30.869782+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7090`

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

- `market_context_high->unknown_4h` score `27.127` n `113` status `ready` deltaP `-2.578` edge `2.3113` maxDD `-1.016`
- `market_context_high->metal_24h` score `0.3336` n `105` status `ready` deltaP `24.871` edge `0.144` maxDD `-7.3625`
- `market_context_high->fx_24h` score `0.1345` n `105` status `ready` deltaP `21.7163` edge `0.0297` maxDD `-1.2451`
- `market_context_high->fx_4h` score `-0.0377` n `113` status `ready` deltaP `7.3063` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.0636` n `123` status `ready` deltaP `3.8934` edge `0.0017` maxDD `-0.1986`
- `market_context_high->commodity_1h` score `-0.3773` n `123` status `ready` deltaP `-1.155` edge `0.0094` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.3926` n `123` status `ready` deltaP `4.5981` edge `-0.0018` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.5305` n `113` status `ready` deltaP `1.5729` edge `0.0444` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6537` n `123` status `ready` deltaP `-2.0118` edge `-0.0052` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7873` n `105` status `ready` deltaP `9.5536` edge `-0.0364` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.4793` n `123` status `ready` deltaP `1.8183` edge `-0.0437` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.1033` n `113` status `ready` deltaP `2.4795` edge `-0.0208` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1537` n `113` status `ready` deltaP `-7.7676` edge `-0.0369` maxDD `-4.3282`
- `market_context_high->equity_1h` score `-2.4966` n `123` status `ready` deltaP `-0.8787` edge `-0.0856` maxDD `-12.2891`
- `market_context_high->crypto_major_24h` score `-3.9453` n `105` status `ready` deltaP `-1.1706` edge `-0.1168` maxDD `-23.4959`
- `market_context_high->crypto_alt_1h` score `-4.1165` n `123` status `ready` deltaP `-2.9977` edge `-0.0746` maxDD `-13.2099`
- `market_context_high->commodity_24h` score `-5.5195` n `105` status `ready` deltaP `-16.498` edge `-0.1303` maxDD `-19.387`
- `market_context_high->equity_24h` score `-7.4132` n `105` status `ready` deltaP `-4.0277` edge `-0.3952` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1612` n `113` status `ready` deltaP `-12.7428` edge `-0.262` maxDD `-32.9851`
- `market_context_high->crypto_alt_24h` score `-12.2372` n `105` status `ready` deltaP `-12.247` edge `-0.4642` maxDD `-70.8424`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

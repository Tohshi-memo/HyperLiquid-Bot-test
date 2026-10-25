# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T22:37:26.927717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.6757` n `113` status `ready` deltaP `-0.7487` edge `2.5115` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.6419` n `81` status `ready` deltaP `6.5007` edge `0.1127` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0832` n `113` status `ready` deltaP `3.2603` edge `0.0025` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.0986` n `113` status `ready` deltaP `6.5441` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.3292` n `81` status `ready` deltaP `14.3133` edge `0.0196` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4607` n `113` status `ready` deltaP `0.1166` edge `0.0109` maxDD `-1.0053`
- `market_context_high->index_1h` score `-0.6775` n `113` status `ready` deltaP `-2.3356` edge `-0.0061` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.7078` n `113` status `ready` deltaP `3.8856` edge `-0.0057` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7694` n `113` status `ready` deltaP `-1.4759` edge `0.0341` maxDD `-1.165`
- `market_context_high->metal_24h` score `-0.8107` n `81` status `ready` deltaP `9.9151` edge `0.097` maxDD `-7.3625`
- `market_context_high->index_24h` score `-1.0568` n `81` status `ready` deltaP `8.6613` edge `-0.065` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3317` n `113` status `ready` deltaP `3.247` edge `-0.0343` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0254` n `113` status `ready` deltaP `3.3941` edge `-0.0204` maxDD `-5.3474`
- `market_context_high->commodity_24h` score `-2.1231` n `81` status `ready` deltaP `-6.0571` edge `-0.0278` maxDD `-6.3209`
- `market_context_high->index_4h` score `-2.1783` n `113` status `ready` deltaP `-8.2249` edge `-0.037` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1895` n `113` status `ready` deltaP `-1.5606` edge `-0.068` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8955` n `113` status `ready` deltaP `-0.6889` edge `-0.0927` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-6.8883` n `81` status `ready` deltaP `-3.0864` edge `-0.2169` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-8.1377` n `81` status `ready` deltaP `-2.8549` edge `-0.4959` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.1252` n `113` status `ready` deltaP `-13.6574` edge `-0.2529` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

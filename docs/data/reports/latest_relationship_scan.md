# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T01:07:27.891106+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5070`

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

- `market_context_high->unknown_4h` score `29.9625` n `113` status `ready` deltaP `-0.7487` edge `2.5354` maxDD `-1.016`
- `market_context_high->fx_24h` score `-0.0866` n `91` status `ready` deltaP `18.1395` edge `0.0252` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0996` n `113` status `ready` deltaP `2.9609` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1144` n `113` status `ready` deltaP `6.3917` edge `0.0077` maxDD `-0.4545`
- `market_context_high->crypto_major_24h` score `-0.2045` n `91` status `ready` deltaP `4.3651` edge `0.0564` maxDD `-4.5369`
- `market_context_high->metal_24h` score `-0.2542` n `91` status `ready` deltaP `17.1054` edge `0.1204` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.4163` n `113` status `ready` deltaP `0.5657` edge `0.0116` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6143` n `113` status `ready` deltaP `4.9335` edge `-0.0049` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6254` n `113` status `ready` deltaP `-1.4374` edge `-0.0054` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6701` n `113` status `ready` deltaP `-0.2564` edge `0.0387` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.8237` n `91` status `ready` deltaP `10.6094` edge `-0.0481` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2577` n `113` status `ready` deltaP `3.9955` edge `-0.0298` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0022` n `113` status `ready` deltaP `3.699` edge `-0.0205` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1514` n `113` status `ready` deltaP `-7.7676` edge `-0.0366` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.1152` n `113` status `ready` deltaP `-1.1115` edge `-0.0648` maxDD `-11.3243`
- `market_context_high->commodity_24h` score `-3.4883` n `91` status `ready` deltaP `-11.0768` edge `-0.0713` maxDD `-10.8322`
- `market_context_high->equity_1h` score `-3.8068` n `113` status `ready` deltaP `-0.2398` edge `-0.0883` maxDD `-12.1865`
- `market_context_high->equity_24h` score `-7.3005` n `91` status `ready` deltaP `0.7212` edge `-0.4124` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-8.3404` n `91` status `ready` deltaP `-6.6793` edge `-0.3033` maxDD `-48.3827`
- `market_context_high->crypto_major_4h` score `-9.968` n `113` status `ready` deltaP `-12.7428` edge `-0.2459` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

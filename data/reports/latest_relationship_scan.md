# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T02:22:28.412412+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5104`

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

- `market_context_high->unknown_4h` score `27.7357` n `113` status `ready` deltaP `-1.3585` edge `2.3539` maxDD `-1.016`
- `market_context_high->fx_24h` score `0.009` n `96` status `ready` deltaP `19.6181` edge `0.0276` maxDD `-1.2451`
- `market_context_high->metal_24h` score `-0.0411` n `96` status `ready` deltaP `20.1389` edge `0.1275` maxDD `-7.3625`
- `market_context_high->fx_4h` score `-0.101` n `113` status `ready` deltaP `6.5441` edge `0.0078` maxDD `-0.4545`
- `market_context_high->fx_1h` score `-0.1094` n `114` status `ready` deltaP `2.8023` edge `0.0022` maxDD `-0.1258`
- `market_context_high->commodity_1h` score `-0.4135` n `114` status `ready` deltaP `0.5568` edge `0.0119` maxDD `-1.0053`
- `market_context_high->commodity_4h` score `-0.6268` n `113` status `ready` deltaP `0.201` edge `0.0412` maxDD `-1.165`
- `market_context_high->metal_1h` score `-0.6558` n `114` status `ready` deltaP `4.491` edge `-0.0054` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6619` n `114` status `ready` deltaP `-2.1405` edge `-0.0054` maxDD `-1.2155`
- `market_context_high->index_24h` score `-0.7421` n `96` status `ready` deltaP `11.4583` edge `-0.0433` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.2951` n `114` status `ready` deltaP `3.6795` edge `-0.0325` maxDD `-9.3126`
- `market_context_high->crypto_major_24h` score `-1.8604` n `96` status `ready` deltaP `2.0834` edge `0.0009` maxDD `-9.5861`
- `market_context_high->metal_4h` score `-2.0108` n `113` status `ready` deltaP `3.5466` edge `-0.0202` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.2196` n `114` status `ready` deltaP `-1.2003` edge `-0.0671` maxDD `-11.4556`
- `market_context_high->equity_1h` score `-3.8343` n `114` status `ready` deltaP `-0.6435` edge `-0.0879` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-4.2051` n `96` status `ready` deltaP `-13.1944` edge `-0.0925` maxDD `-13.6922`
- `market_context_high->equity_24h` score `-7.3395` n `96` status `ready` deltaP `-1.2152` edge `-0.4045` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-9.579` n `96` status `ready` deltaP `-8.8542` edge `-0.3591` maxDD `-55.4624`
- `market_context_high->crypto_major_4h` score `-10.0436` n `113` status `ready` deltaP `-12.7428` edge `-0.2522` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

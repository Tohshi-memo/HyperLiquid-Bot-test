# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-26T01:52:26.865503+00:00`
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

- `market_context_high->unknown_4h` score `29.8601` n `113` status `ready` deltaP `-1.0536` edge `2.5289` maxDD `-1.016`
- `market_context_high->fx_24h` score `-0.0256` n `94` status `ready` deltaP `19.0566` edge `0.0269` maxDD `-1.2451`
- `market_context_high->fx_1h` score `-0.0918` n `113` status `ready` deltaP `3.1106` edge `0.0024` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1144` n `113` status `ready` deltaP `6.3917` edge `0.0077` maxDD `-0.4545`
- `market_context_high->metal_24h` score `-0.1233` n `94` status `ready` deltaP `18.9642` edge `0.1248` maxDD `-7.3625`
- `market_context_high->commodity_1h` score `-0.402` n `113` status `ready` deltaP `0.7154` edge `0.0118` maxDD `-1.0053`
- `market_context_high->metal_1h` score `-0.6012` n `113` status `ready` deltaP `5.0832` edge `-0.0048` maxDD `-1.6682`
- `market_context_high->index_1h` score `-0.6324` n `113` status `ready` deltaP `-1.5871` edge `-0.0053` maxDD `-1.2155`
- `market_context_high->commodity_4h` score `-0.6465` n `113` status `ready` deltaP `-0.1039` edge `0.0407` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.7456` n `94` status `ready` deltaP `11.6615` edge `-0.0451` maxDD `-4.925`
- `market_context_high->crypto_major_24h` score `-1.1173` n `94` status `ready` deltaP `2.8885` edge `0.0248` maxDD `-7.3067`
- `market_context_high->crypto_major_1h` score `-1.2413` n `113` status `ready` deltaP `4.1452` edge `-0.0287` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0132` n `113` status `ready` deltaP `3.5466` edge `-0.0204` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1522` n `113` status `ready` deltaP `-7.7676` edge `-0.0367` maxDD `-4.3282`
- `market_context_high->crypto_alt_1h` score `-3.0876` n `113` status `ready` deltaP `-0.9618` edge `-0.0635` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.7732` n `113` status `ready` deltaP `-0.0901` edge `-0.0865` maxDD `-12.1865`
- `market_context_high->commodity_24h` score `-3.921` n `94` status `ready` deltaP `-12.3744` edge `-0.0844` maxDD `-12.5305`
- `market_context_high->equity_24h` score `-7.3253` n `94` status `ready` deltaP `-0.4765` edge `-0.4076` maxDD `-36.6024`
- `market_context_high->crypto_alt_24h` score `-9.0866` n `94` status `ready` deltaP `-8.012` edge `-0.3371` maxDD `-52.6215`
- `market_context_high->crypto_major_4h` score `-10.0148` n `113` status `ready` deltaP `-12.7428` edge `-0.2498` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

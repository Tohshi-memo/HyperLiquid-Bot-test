# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T09:52:32.239242+00:00`
- Price records: `672`
- Market context records: `5236`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `23.2198` n `127` status `ready` deltaP `32.0935` edge `1.74` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.2028` n `127` status `ready` deltaP `33.645` edge `1.2421` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `6.8842` n `127` status `ready` deltaP `22.2618` edge `0.7723` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.1255` n `155` status `ready` deltaP `13.8464` edge `0.4114` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.001` n `155` status `ready` deltaP `14.6794` edge `0.4648` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2094` n `155` status `ready` deltaP `17.1351` edge `0.1721` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8082` n `155` status `ready` deltaP `8.0896` edge `0.1609` maxDD `-2.7986`
- `market_context_high->equity_24h` score `1.1935` n `127` status `ready` deltaP `17.6906` edge `0.5444` maxDD `-40.0306`
- `market_context_high->fx_24h` score `0.5839` n `127` status `ready` deltaP `13.3941` edge `0.0489` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4616` n `155` status `ready` deltaP `4.6533` edge `0.1036` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4252` n `155` status `ready` deltaP `6.7027` edge `0.1153` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1253` n `155` status `ready` deltaP `6.3306` edge `0.1321` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.1486` n `127` status `ready` deltaP `17.3009` edge `0.0291` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.1624` n `155` status `ready` deltaP `5.5196` edge `0.0462` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1667` n `155` status `ready` deltaP `3.9617` edge `0.0114` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2062` n `155` status `ready` deltaP `3.6875` edge `0.0086` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.311` n `155` status `ready` deltaP `0.9108` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6647` n `155` status `ready` deltaP `-0.3226` edge `-0.0022` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7481` n `155` status `ready` deltaP `0.7474` edge `0.0025` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8959` n `155` status `ready` deltaP `3.1619` edge `0.016` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T13:52:31.940953+00:00`
- Price records: `672`
- Market context records: `5253`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7584`

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

- `market_context_high->unknown_24h` score `25.2863` n `142` status `ready` deltaP `29.9956` edge `1.9262` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.0246` n `142` status `ready` deltaP `29.7877` edge `1.0863` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.2419` n `157` status `ready` deltaP `14.4458` edge `0.4171` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9352` n `157` status `ready` deltaP `14.6526` edge `0.4595` maxDD `-14.0065`
- `market_context_high->equity_24h` score `2.7694` n `142` status `ready` deltaP `19.1046` edge `0.6663` maxDD `-40.0306`
- `market_context_high->crypto_alt_24h` score `2.2474` n `142` status `ready` deltaP `17.2462` edge `0.5842` maxDD `-31.6181`
- `market_context_high->unknown_4h` score `1.9798` n `157` status `ready` deltaP `16.6499` edge `0.1562` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.524` n `157` status `ready` deltaP `7.9997` edge `0.1542` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5209` n `142` status `ready` deltaP `12.7861` edge `0.0477` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5004` n `164` status `ready` deltaP `4.8233` edge `0.1057` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3713` n `164` status `ready` deltaP `6.1487` edge `0.1145` maxDD `-6.9639`
- `market_context_high->unknown_1h` score `0.2449` n `164` status `ready` deltaP `8.0035` edge `0.0312` maxDD `-2.7986`
- `market_context_high->index_24h` score `0.1` n `142` status `ready` deltaP `20.4616` edge `0.0399` maxDD `-7.413`
- `market_context_high->equity_1h` score `0.0226` n `164` status `ready` deltaP `6.4517` edge `0.0554` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.1143` n `164` status `ready` deltaP `4.6115` edge `0.0101` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.1266` n `164` status `ready` deltaP `4.3742` edge `0.0138` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3335` n `164` status `ready` deltaP `0.4929` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.7735` n `157` status `ready` deltaP `4.3469` edge `0.0183` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.797` n `157` status `ready` deltaP `0.0621` edge `0.0008` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.2665` n `164` status `ready` deltaP `-2.4171` edge `-0.0065` maxDD `-2.634`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

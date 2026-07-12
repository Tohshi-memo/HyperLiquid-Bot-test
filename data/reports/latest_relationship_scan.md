# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T17:37:28.507081+00:00`
- Price records: `672`
- Market context records: `6522`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7864`

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

- `news_risk_high->crypto_alt_24h` score `13.2607` n `32` status `ready` deltaP `36.211` edge `0.8784` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5248` n `32` status `ready` deltaP `53.8995` edge `0.1844` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.4301` n `141` status `ready` deltaP `11.0955` edge `0.7919` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8871` n `32` status `ready` deltaP `20.911` edge `0.5651` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6865` n `38` status `ready` deltaP `39.0164` edge `0.0517` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.5187` n `184` status `ready` deltaP `-5.8058` edge `0.3387` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.1768` n `32` status `ready` deltaP `23.1965` edge `0.0473` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7772` n `38` status `ready` deltaP `22.3133` edge `0.0174` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6564` n `141` status `ready` deltaP `14.708` edge `0.2268` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.6463` n `173` status `ready` deltaP `13.8446` edge `0.0292` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5847` n `38` status `ready` deltaP `5.2001` edge `0.094` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.3858` n `173` status `ready` deltaP `10.5033` edge `0.1175` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0929` n `38` status `ready` deltaP `1.7334` edge `0.0513` maxDD `-2.0756`
- `market_context_high->unknown_4h` score `-0.2906` n `173` status `ready` deltaP `-20.1519` edge `0.3507` maxDD `-10.5788`
- `news_risk_high->index_24h` score `-0.3065` n `32` status `ready` deltaP `6.6833` edge `0.0033` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3625` n `173` status `ready` deltaP `9.8107` edge `0.058` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4318` n `184` status `ready` deltaP `-0.4556` edge `-0.0016` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.4739` n `173` status `ready` deltaP `12.1801` edge `0.0871` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.4899` n `184` status `ready` deltaP `1.1097` edge `-0.0019` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5049` n `184` status `ready` deltaP `7.088` edge `0.0146` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

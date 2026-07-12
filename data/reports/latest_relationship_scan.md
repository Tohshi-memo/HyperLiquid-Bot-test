# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T16:07:27.398018+00:00`
- Price records: `672`
- Market context records: `6515`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5884`

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

- `news_risk_high->crypto_alt_24h` score `13.2631` n `32` status `ready` deltaP `36.211` edge `0.8786` maxDD `-0.5131`
- `market_context_high->unknown_24h` score `6.536` n `139` status `ready` deltaP `10.5445` edge `0.8044` maxDD `-15.0689`
- `news_risk_high->fx_24h` score `6.5104` n `32` status `ready` deltaP `53.8995` edge `0.1832` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `4.9658` n `32` status `ready` deltaP `20.911` edge `0.5752` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7377` n `38` status `ready` deltaP `39.6261` edge `0.0519` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.7604` n `180` status `ready` deltaP `-5.1098` edge `0.3542` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.3428` n `32` status `ready` deltaP `24.2364` edge `0.0542` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8047` n `38` status `ready` deltaP `22.6127` edge `0.0177` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6267` n `139` status `ready` deltaP `14.6815` edge `0.2245` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5786` n `168` status `ready` deltaP `13.1025` edge `0.0285` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5644` n `38` status `ready` deltaP `5.0504` edge `0.0924` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2969` n `168` status `ready` deltaP `9.4367` edge `0.1172` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.1161` n `168` status `ready` deltaP `-19.6283` edge `0.3811` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0765` n `38` status `ready` deltaP `1.5837` edge `0.0502` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.3116` n `168` status `ready` deltaP `10.6997` edge `0.0586` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.3414` n `32` status `ready` deltaP `6.1633` edge `0.0023` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.4205` n `180` status `ready` deltaP `-0.2528` edge `-0.0015` maxDD `-0.7249`
- `market_context_high->crypto_alt_1h` score `-0.5205` n `180` status `ready` deltaP `6.7299` edge `0.0197` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5309` n `180` status `ready` deltaP `0.5323` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.542` n `180` status `ready` deltaP `6.6001` edge `0.0131` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

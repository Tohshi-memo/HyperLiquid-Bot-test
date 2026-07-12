# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T15:07:25.589606+00:00`
- Price records: `672`
- Market context records: `6510`
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

- `news_risk_high->crypto_alt_24h` score `13.2691` n `32` status `ready` deltaP `36.211` edge `0.8791` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.5044` n `32` status `ready` deltaP `53.8995` edge `0.1827` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.3938` n `143` status `ready` deltaP `11.6312` edge `0.7853` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.9783` n `32` status `ready` deltaP `20.911` edge `0.5768` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.7803` n `38` status `ready` deltaP `40.0835` edge `0.0524` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.6966` n `180` status `ready` deltaP `-5.9215` edge `0.3543` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.4475` n `32` status `ready` deltaP `24.9296` edge `0.0583` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.8059` n `38` status `ready` deltaP `22.6127` edge `0.0178` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.4175` n `143` status `ready` deltaP `13.2819` edge `0.2164` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.5774` n `168` status `ready` deltaP `13.1025` edge `0.0284` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5636` n `38` status `ready` deltaP `5.0504` edge `0.0923` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.2885` n `168` status `ready` deltaP `9.4367` edge `0.1165` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2632` n `168` status `ready` deltaP `-18.3` edge `0.3845` maxDD `-10.5788`
- `news_risk_high->crypto_alt_1h` score `0.0711` n `38` status `ready` deltaP `1.5837` edge `0.0495` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.3551` n `32` status `ready` deltaP `5.99` edge `0.0017` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.3631` n `168` status `ready` deltaP `9.8141` edge `0.0579` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4304` n `180` status `ready` deltaP `-0.2528` edge `-0.0018` maxDD `-0.8019`
- `market_context_high->crypto_alt_1h` score `-0.5064` n `180` status `ready` deltaP `6.7299` edge `0.0215` maxDD `-5.8368`
- `market_context_high->commodity_1h` score `-0.5098` n `180` status `ready` deltaP `0.9381` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->crypto_major_1h` score `-0.5412` n `180` status `ready` deltaP `6.6001` edge `0.0132` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

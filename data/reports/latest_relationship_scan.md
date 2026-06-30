# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T13:37:29.674073+00:00`
- Price records: `672`
- Market context records: `5252`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7578`

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

- `market_context_high->unknown_24h` score `25.2002` n `141` status `ready` deltaP `30.1492` edge `1.918` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.2082` n `141` status `ready` deltaP `30.2822` edge `1.0983` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.3722` n `156` status `ready` deltaP `14.8296` edge `0.4254` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0626` n `156` status `ready` deltaP `15.0446` edge `0.4675` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `2.7228` n `141` status `ready` deltaP `17.6307` edge `0.5978` maxDD `-30.0752`
- `market_context_high->equity_24h` score `2.6906` n `141` status `ready` deltaP `19.0197` edge `0.6603` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.0539` n `156` status `ready` deltaP `16.6471` edge `0.1624` maxDD `-5.5109`
- `market_context_high->equity_4h` score `0.5373` n `156` status `ready` deltaP `7.9112` edge `0.1559` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5276` n `141` status `ready` deltaP `12.8398` edge `0.0479` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4647` n `163` status `ready` deltaP `4.6774` edge `0.1037` maxDD `-5.0257`
- `market_context_high->unknown_1h` score `0.3787` n `163` status `ready` deltaP `7.9213` edge `0.0429` maxDD `-2.7986`
- `market_context_high->crypto_major_1h` score `0.3386` n `163` status `ready` deltaP `5.9953` edge `0.1128` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.0807` n `141` status `ready` deltaP `20.2718` edge `0.0387` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0047` n `163` status `ready` deltaP `6.3508` edge `0.0538` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1373` n `163` status `ready` deltaP `4.2283` edge `0.0134` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1416` n `163` status `ready` deltaP `4.3459` edge `0.0096` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3409` n `163` status `ready` deltaP `0.3508` edge `-0.0008` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.7902` n `156` status `ready` deltaP `4.2136` edge `0.0178` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.8013` n `156` status `ready` deltaP `-0.0508` edge `0.001` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-1.2353` n `163` status `ready` deltaP `-2.1178` edge `-0.0063` maxDD `-2.6019`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

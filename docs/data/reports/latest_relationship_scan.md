# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T19:07:24.010227+00:00`
- Price records: `672`
- Market context records: `6530`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7866`

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

- `news_risk_high->crypto_alt_24h` score `13.433` n `32` status `ready` deltaP `36.3843` edge `0.8916` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.588` n `32` status `ready` deltaP `54.4194` edge `0.1862` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.2671` n `144` status `ready` deltaP `11.8934` edge `0.773` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.8875` n `32` status `ready` deltaP `21.0843` edge `0.564` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.6987` n `38` status `ready` deltaP `39.1688` edge `0.0517` maxDD `-0.0345`
- `market_context_high->unknown_1h` score `2.2831` n `190` status `ready` deltaP `-5.6303` edge `0.3179` maxDD `-3.2083`
- `news_risk_high->commodity_24h` score `2.0656` n `32` status `ready` deltaP `22.6766` edge `0.0415` maxDD `-0.3101`
- `news_risk_high->fx_1h` score `1.7784` n `38` status `ready` deltaP `22.3133` edge `0.0175` maxDD `-0.1113`
- `market_context_high->commodity_24h` score `1.6466` n `144` status `ready` deltaP `14.6905` edge `0.2261` maxDD `-5.2791`
- `market_context_high->index_4h` score `0.7124` n `179` status `ready` deltaP `14.6997` edge `0.029` maxDD `-0.4108`
- `news_risk_high->crypto_major_1h` score `0.5823` n `38` status `ready` deltaP `5.2001` edge `0.0937` maxDD `-2.6299`
- `market_context_high->crypto_alt_4h` score `0.4181` n `179` status `ready` deltaP `10.8921` edge `0.1176` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `0.0921` n `38` status `ready` deltaP `1.7334` edge `0.0512` maxDD `-2.0756`
- `news_risk_high->index_24h` score `-0.2392` n `32` status `ready` deltaP `7.7231` edge `0.005` maxDD `-2.3058`
- `market_context_high->crypto_major_4h` score `-0.3749` n `179` status `ready` deltaP `13.229` edge `0.0928` maxDD `-12.6576`
- `market_context_high->equity_4h` score `-0.3978` n `179` status `ready` deltaP `9.1165` edge `0.0581` maxDD `-8.2573`
- `market_context_high->commodity_1h` score `-0.4461` n `190` status `ready` deltaP `1.8925` edge `-0.0015` maxDD `-2.1314`
- `market_context_high->fx_1h` score `-0.4536` n `190` status `ready` deltaP `-0.8446` edge `-0.0018` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.5562` n `190` status `ready` deltaP `6.2528` edge `0.0136` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.6121` n `190` status `ready` deltaP `5.4176` edge `0.0167` maxDD `-5.8368`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

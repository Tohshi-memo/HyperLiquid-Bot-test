# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T10:22:34.975147+00:00`
- Price records: `672`
- Market context records: `8506`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5882`

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

- `news_risk_high->unknown_24h` score `6275.0865` n `52` status `ready` deltaP `44.7383` edge `522.6677` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0608` n `64` status `ready` deltaP `22.1799` edge `0.4169` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0667` n `64` status `ready` deltaP `17.1113` edge `0.0772` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7721` n `64` status `ready` deltaP `16.2519` edge `0.087` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9423` n `64` status `ready` deltaP `5.8308` edge `0.1595` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8835` n `64` status `ready` deltaP `14.4817` edge `0.1559` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6074` n `64` status `ready` deltaP `9.7586` edge `0.0655` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.3883` n `64` status `ready` deltaP `7.2137` edge `0.0529` maxDD `-2.0972`
- `market_context_high->equity_1h` score `0.2133` n `34` status `ready` deltaP `1.6379` edge `0.036` maxDD `-0.9985`
- `news_risk_high->fx_1h` score `0.1259` n `64` status `ready` deltaP `6.0348` edge `0.004` maxDD `-0.2475`
- `market_context_high->index_1h` score `0.0981` n `34` status `ready` deltaP `5.3804` edge `-0.0036` maxDD `-0.2417`
- `news_risk_high->fx_4h` score `0.0656` n `64` status `ready` deltaP `11.9284` edge `0.0217` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.048` n `64` status `ready` deltaP `4.3694` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0674` n `64` status `ready` deltaP `1.1052` edge `0.0316` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1024` n `64` status `ready` deltaP `3.5554` edge `0.0081` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.3553` n `34` status `ready` deltaP `0.2466` edge `-0.0104` maxDD `-0.6101`
- `market_context_high->crypto_major_1h` score `-0.4261` n `34` status `ready` deltaP `2.3424` edge `-0.0205` maxDD `-1.9791`
- `market_context_high->commodity_1h` score `-0.4779` n `34` status `ready` deltaP `1.9461` edge `-0.0117` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.8659` n `34` status `ready` deltaP `-9.8186` edge `0.0046` maxDD `-2.012`
- `market_context_high->fx_1h` score `-1.6366` n `34` status `ready` deltaP `-13.3586` edge `-0.0008` maxDD `-0.3888`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

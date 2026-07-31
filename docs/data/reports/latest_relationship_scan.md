# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T10:11:59.961662+00:00`
- Price records: `672`
- Market context records: `8505`
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

- `news_risk_high->unknown_24h` score `6274.8129` n `52` status `ready` deltaP `44.7383` edge `522.6449` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `6.0752` n `64` status `ready` deltaP `22.1799` edge `0.4181` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0667` n `64` status `ready` deltaP `17.1113` edge `0.0772` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7709` n `64` status `ready` deltaP `16.2519` edge `0.0869` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.9454` n `64` status `ready` deltaP `5.8308` edge `0.1599` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8944` n `64` status `ready` deltaP `14.4817` edge `0.1573` maxDD `-5.8012`
- `news_risk_high->crypto_alt_1h` score `0.6207` n `64` status `ready` deltaP `9.9083` edge `0.0662` maxDD `-1.8813`
- `market_context_high->equity_1h` score `0.4527` n `33` status `ready` deltaP `3.4205` edge `0.0399` maxDD `-0.9985`
- `news_risk_high->crypto_major_1h` score `0.3976` n `64` status `ready` deltaP `7.3634` edge `0.0531` maxDD `-2.0972`
- `market_context_high->index_1h` score `0.1947` n `33` status `ready` deltaP `7.163` edge `-0.0031` maxDD `-0.2417`
- `news_risk_high->fx_1h` score `0.1352` n `64` status `ready` deltaP `6.1845` edge `0.0042` maxDD `-0.2475`
- `news_risk_high->fx_4h` score `0.079` n `64` status `ready` deltaP `12.0808` edge `0.0218` maxDD `-0.6604`
- `news_risk_high->index_1h` score `0.048` n `64` status `ready` deltaP `4.3694` edge `0.0087` maxDD `-0.5338`
- `news_risk_high->metal_4h` score `-0.0689` n `64` status `ready` deltaP `1.1052` edge `0.0314` maxDD `-0.8085`
- `news_risk_high->metal_1h` score `-0.1036` n `64` status `ready` deltaP `3.5554` edge `0.008` maxDD `-0.5599`
- `market_context_high->metal_1h` score `-0.4341` n `33` status `ready` deltaP `-1.1794` edge `-0.011` maxDD `-0.6101`
- `market_context_high->crypto_major_1h` score `-0.5221` n `33` status `ready` deltaP `1.0661` edge `-0.0243` maxDD `-1.9791`
- `market_context_high->commodity_1h` score `-0.5965` n `33` status `ready` deltaP `0.4309` edge `-0.0168` maxDD `-2.0038`
- `market_context_high->crypto_alt_1h` score `-0.9991` n `33` status `ready` deltaP `-11.5406` edge `-0.001` maxDD `-2.012`
- `news_risk_high->commodity_1h` score `-1.7143` n `64` status `ready` deltaP `-4.3039` edge `-0.0356` maxDD `-2.9516`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

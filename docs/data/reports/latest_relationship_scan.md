# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T16:22:24.931003+00:00`
- Price records: `672`
- Market context records: `2260`
- Flow alert records: `8401`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9257`

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

- `news_risk_high->crypto_alt_24h` score `22.4339` n `43` status `ready` deltaP `52.9877` edge `1.5751` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `15.8076` n `43` status `ready` deltaP `42.6397` edge `1.077` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `14.9883` n `43` status `ready` deltaP `33.6119` edge `1.0564` maxDD `-2.1831`
- `news_risk_high->crypto_major_24h` score `12.163` n `43` status `ready` deltaP `23.5868` edge `0.9144` maxDD `-3.3119`
- `market_context_high->unknown_24h` score `9.4274` n `115` status `ready` deltaP `29.846` edge `0.6278` maxDD `-1.626`
- `news_risk_high->unknown_24h` score `8.9909` n `43` status `ready` deltaP `33.8905` edge `0.5459` maxDD `-1.4744`
- `market_context_high->crypto_alt_4h` score `8.3102` n `143` status `ready` deltaP `27.4529` edge `0.7774` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `7.9864` n `143` status `ready` deltaP `32.8853` edge `0.6273` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `6.1843` n `115` status `ready` deltaP `17.2977` edge `1.0668` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.3599` n `143` status `ready` deltaP `21.6336` edge `0.3634` maxDD `-1.8773`
- `news_risk_high->commodity_4h` score `3.7554` n `43` status `ready` deltaP `32.1575` edge `0.3342` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.7403` n `43` status `ready` deltaP `12.0559` edge `0.2732` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.6447` n `43` status `ready` deltaP `37.2295` edge `0.074` maxDD `-0.1442`
- `market_context_high->index_24h` score `3.3506` n `115` status `ready` deltaP `13.8557` edge `0.2386` maxDD `-1.4737`
- `market_context_high->index_4h` score `3.2131` n `143` status `ready` deltaP `26.841` edge `0.1491` maxDD `-1.8228`
- `news_risk_high->commodity_24h` score `3.1262` n `43` status `ready` deltaP `2.5517` edge `0.3252` maxDD `-3.202`
- `market_context_high->equity_24h` score `2.6272` n `115` status `ready` deltaP `21.1549` edge `0.2306` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.4135` n `155` status `ready` deltaP `14.4698` edge `0.2234` maxDD `-6.1656`
- `market_context_high->equity_4h` score `2.3151` n `143` status `ready` deltaP `19.0762` edge `0.2062` maxDD `-5.9024`
- `news_risk_high->fx_4h` score `2.0613` n `43` status `ready` deltaP `26.3648` edge `0.0144` maxDD `-0.1382`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

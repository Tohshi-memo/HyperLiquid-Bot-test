# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T05:22:28.046288+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `384.821` n `83` status `ready` deltaP `-20.7483` edge `32.2962` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `15.6246` n `83` status `ready` deltaP `36.7888` edge `1.1947` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.3276` n `83` status `ready` deltaP `28.855` edge `1.2011` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `10.6105` n `83` status `ready` deltaP `38.0878` edge `0.8077` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `8.1169` n `52` status `ready` deltaP `44.7917` edge `0.3778` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.1169` n `52` status `ready` deltaP `44.7917` edge `0.3778` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.8178` n `149` status `ready` deltaP `38.0803` edge `0.3668` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.287` n `83` status `ready` deltaP `43.5178` edge `0.2514` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.4766` n `83` status `ready` deltaP `31.9905` edge `0.2052` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5994` n `52` status `ready` deltaP `33.6672` edge `-0.0036` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5994` n `52` status `ready` deltaP `33.6672` edge `-0.0036` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4645` n `149` status `ready` deltaP `30.8923` edge `0.021` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1337` n `52` status `ready` deltaP `27.3569` edge `0.0304` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1337` n `52` status `ready` deltaP `27.3569` edge `0.0304` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0334` n `149` status `ready` deltaP `23.8592` edge `0.0522` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.9024` n `149` status `ready` deltaP `14.2648` edge `0.0178` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.4022` n `83` status `ready` deltaP `12.3457` edge `0.0321` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2791` n `52` status `ready` deltaP `7.3469` edge `0.0095` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.135` n `52` status `ready` deltaP `6.1147` edge `0.0071` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

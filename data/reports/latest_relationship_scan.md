# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T23:07:26.548076+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `risk_on_high->crypto_alt_4h` score `8.0321` n `47` status `ready` deltaP `28.571` edge `0.5012` maxDD `-0.4529`
- `risk_on_and_context->crypto_alt_4h` score `8.0321` n `47` status `ready` deltaP `28.571` edge `0.5012` maxDD `-0.4529`
- `news_risk_high->crypto_alt_24h` score `6.6426` n `44` status `ready` deltaP `21.1332` edge `1.0483` maxDD `-22.3391`
- `risk_on_high->crypto_major_4h` score `6.4824` n `47` status `ready` deltaP `34.1852` edge `0.3399` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `6.4824` n `47` status `ready` deltaP `34.1852` edge `0.3399` maxDD `-1.208`
- `news_risk_high->unknown_4h` score `6.0065` n `53` status `ready` deltaP `-0.0834` edge `0.5601` maxDD `-1.7205`
- `market_context_high->metal_24h` score `4.6826` n `104` status `ready` deltaP `34.415` edge `0.2627` maxDD `-3.1535`
- `news_risk_high->unknown_1h` score `3.1869` n `53` status `ready` deltaP `-4.3243` edge `0.3301` maxDD `-0.8558`
- `risk_on_high->metal_4h` score `3.1123` n `47` status `ready` deltaP `34.928` edge `0.0351` maxDD `-0.0208`
- `risk_on_and_context->metal_4h` score `3.1123` n `47` status `ready` deltaP `34.928` edge `0.0351` maxDD `-0.0208`
- `risk_on_high->equity_4h` score `2.2504` n `47` status `ready` deltaP `17.9197` edge `0.093` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.2504` n `47` status `ready` deltaP `17.9197` edge `0.093` maxDD `-0.3281`
- `market_context_high->unknown_4h` score `1.8102` n `149` status `ready` deltaP `18.1893` edge `0.0766` maxDD `-1.0945`
- `market_context_high->unknown_1h` score `1.4745` n `161` status `ready` deltaP `8.6371` edge `0.1134` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.3613` n `47` status `ready` deltaP `20.1998` edge `0.0097` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.3613` n `47` status `ready` deltaP `20.1998` edge `0.0097` maxDD `-0.1405`
- `news_risk_high->fx_4h` score `1.178` n `53` status `ready` deltaP `28.6901` edge `0.0147` maxDD `-0.3953`
- `risk_on_high->metal_1h` score `1.1541` n `59` status `ready` deltaP `16.4975` edge `0.0076` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1541` n `59` status `ready` deltaP `16.4975` edge `0.0076` maxDD `-0.0463`
- `risk_on_high->unknown_1h` score `0.8899` n `59` status `ready` deltaP `1.7838` edge `0.1062` maxDD `-1.5148`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

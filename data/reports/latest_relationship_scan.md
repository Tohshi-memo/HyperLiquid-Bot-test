# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T16:52:31.822775+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8290`

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

- `market_context_high->commodity_24h` score `2.2024` n `76` status `ready` deltaP `19.7368` edge `0.1371` maxDD `-1.8119`
- `risk_on_high->equity_1h` score `0.4984` n `43` status `ready` deltaP `13.8978` edge `0.0067` maxDD `-1.9591`
- `risk_on_and_context->equity_1h` score `0.4984` n `43` status `ready` deltaP `13.8978` edge `0.0067` maxDD `-1.9591`
- `risk_on_high->index_1h` score `0.4423` n `43` status `ready` deltaP `10.1553` edge `-0.0005` maxDD `-0.4273`
- `risk_on_and_context->index_1h` score `0.4423` n `43` status `ready` deltaP `10.1553` edge `-0.0005` maxDD `-0.4273`
- `risk_on_high->commodity_24h` score `0.3516` n `43` status `ready` deltaP `15.1163` edge `0.0083` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `0.3516` n `43` status `ready` deltaP `15.1163` edge `0.0083` maxDD `-1.7154`
- `risk_on_high->fx_4h` score `-0.1787` n `43` status `ready` deltaP `0.8579` edge `0.0058` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `-0.1787` n `43` status `ready` deltaP `0.8579` edge `0.0058` maxDD `-0.1126`
- `risk_on_high->fx_1h` score `-0.2403` n `43` status `ready` deltaP `0.7137` edge `-0.0009` maxDD `-0.1065`
- `risk_on_and_context->fx_1h` score `-0.2403` n `43` status `ready` deltaP `0.7137` edge `-0.0009` maxDD `-0.1065`
- `market_context_high->crypto_major_1h` score `-0.3209` n `92` status `ready` deltaP `1.0544` edge `0.0535` maxDD `-4.8007`
- `market_context_high->crypto_major_4h` score `-0.3667` n `80` status `ready` deltaP `1.128` edge `0.3027` maxDD `-16.5789`
- `market_context_high->metal_1h` score `-0.4775` n `92` status `ready` deltaP `-3.6774` edge `0.0008` maxDD `-0.6669`
- `market_context_high->crypto_major_24h` score `-0.5074` n `76` status `ready` deltaP `-2.7687` edge `0.5631` maxDD `-35.1086`
- `market_context_high->fx_4h` score `-0.6208` n `80` status `ready` deltaP `-2.8049` edge `0.003` maxDD `-0.7783`
- `market_context_high->index_1h` score `-0.6649` n `92` status `ready` deltaP `2.1674` edge `-0.0031` maxDD `-1.0073`
- `risk_on_high->index_4h` score `-0.6936` n `43` status `ready` deltaP `4.0201` edge `0.0021` maxDD `-0.9359`
- `risk_on_and_context->index_4h` score `-0.6936` n `43` status `ready` deltaP `4.0201` edge `0.0021` maxDD `-0.9359`
- `market_context_high->metal_4h` score `-0.7431` n `80` status `ready` deltaP `-1.9512` edge `0.0446` maxDD `-1.1488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

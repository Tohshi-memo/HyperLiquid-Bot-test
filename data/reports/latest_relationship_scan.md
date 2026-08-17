# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-17T05:22:26.963243+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11865`

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

- `risk_on_high->unknown_1h` score `4.4227` n `33` status `ready` deltaP `5.6297` edge `0.3705` maxDD `-0.8243`
- `risk_on_and_context->unknown_1h` score `4.4227` n `33` status `ready` deltaP `5.6297` edge `0.3705` maxDD `-0.8243`
- `market_context_high->commodity_24h` score `3.0428` n `74` status `ready` deltaP `29.8658` edge `0.1204` maxDD `-1.2753`
- `market_context_high->crypto_major_24h` score `1.8982` n `74` status `ready` deltaP `4.3262` edge `0.267` maxDD `-5.6792`
- `market_context_high->index_24h` score `1.4661` n `74` status `ready` deltaP `21.7014` edge `-0.0225` maxDD `0.0`
- `risk_on_high->crypto_major_1h` score `1.4032` n `33` status `ready` deltaP `15.4691` edge `0.0444` maxDD `-1.1144`
- `risk_on_and_context->crypto_major_1h` score `1.4032` n `33` status `ready` deltaP `15.4691` edge `0.0444` maxDD `-1.1144`
- `market_context_high->equity_24h` score `1.4023` n `74` status `ready` deltaP `15.8502` edge `0.0321` maxDD `-0.6726`
- `risk_on_high->equity_1h` score `0.8148` n `33` status `ready` deltaP `12.8471` edge `0.0366` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `0.8148` n `33` status `ready` deltaP `12.8471` edge `0.0366` maxDD `-1.6811`
- `market_context_high->commodity_4h` score `0.7231` n `105` status `ready` deltaP `12.8557` edge `0.0557` maxDD `-0.8962`
- `risk_on_high->index_1h` score `0.4703` n `33` status `ready` deltaP `12.8108` edge `0.0124` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.4703` n `33` status `ready` deltaP `12.8108` edge `0.0124` maxDD `-0.3343`
- `risk_on_high->commodity_1h` score `0.0573` n `33` status `ready` deltaP `2.4497` edge `0.0163` maxDD `-0.356`
- `risk_on_and_context->commodity_1h` score `0.0573` n `33` status `ready` deltaP `2.4497` edge `0.0163` maxDD `-0.356`
- `risk_on_high->fx_1h` score `-0.105` n `33` status `ready` deltaP `1.2158` edge `0.0012` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `-0.105` n `33` status `ready` deltaP `1.2158` edge `0.0012` maxDD `-0.1547`
- `market_context_high->metal_4h` score `-0.2278` n `105` status `ready` deltaP `15.9799` edge `0.0152` maxDD `-4.5909`
- `risk_on_high->crypto_alt_1h` score `-0.3071` n `33` status `ready` deltaP `0.4673` edge `0.031` maxDD `-1.7766`
- `risk_on_and_context->crypto_alt_1h` score `-0.3071` n `33` status `ready` deltaP `0.4673` edge `0.031` maxDD `-1.7766`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

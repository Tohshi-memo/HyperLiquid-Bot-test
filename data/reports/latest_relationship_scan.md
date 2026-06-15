# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-15T22:52:32.112944+00:00`
- Price records: `672`
- Market context records: `4034`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10624`

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

- `risk_on_high->unknown_4h` score `145.7667` n `40` status `ready` deltaP `-6.9817` edge `12.3754` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.7667` n `40` status `ready` deltaP `-6.9817` edge `12.3754` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.9301` n `134` status `ready` deltaP `-6.719` edge `4.3585` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `24.5141` n `151` status `ready` deltaP `1.7435` edge `2.5735` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `5.122` n `40` status `ready` deltaP `36.3951` edge `0.1842` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.122` n `40` status `ready` deltaP `36.3951` edge `0.1842` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.2221` n `40` status `ready` deltaP `35.9146` edge `0.0338` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.2221` n `40` status `ready` deltaP `35.9146` edge `0.0338` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.8491` n `134` status `ready` deltaP `23.3438` edge `0.103` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.8363` n `151` status `ready` deltaP `17.2225` edge `0.1663` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.6518` n `134` status `ready` deltaP `11.5277` edge `0.1595` maxDD `-4.8962`
- `market_context_high->equity_1h` score `1.1807` n `156` status `ready` deltaP `8.4984` edge `0.0977` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.9221` n `40` status `ready` deltaP `18.689` edge `0.0188` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9221` n `40` status `ready` deltaP `18.689` edge `0.0188` maxDD `-2.6576`
- `risk_on_high->commodity_24h` score `0.6286` n `40` status `ready` deltaP `2.9896` edge `0.2606` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.6286` n `40` status `ready` deltaP `2.9896` edge `0.2606` maxDD `-12.9187`
- `market_context_high->crypto_major_1h` score `0.5418` n `156` status `ready` deltaP `7.6693` edge `0.055` maxDD `-2.8785`
- `market_context_high->metal_1h` score `0.4163` n `156` status `ready` deltaP `9.98` edge `0.0494` maxDD `-3.0049`
- `risk_on_high->index_24h` score `0.4068` n `40` status `ready` deltaP `24.0901` edge `-0.1267` maxDD `0.0`
- `risk_on_and_context->index_24h` score `0.4068` n `40` status `ready` deltaP `24.0901` edge `-0.1267` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

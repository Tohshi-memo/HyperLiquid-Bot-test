# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T00:52:32.592828+00:00`
- Price records: `672`
- Market context records: `4043`
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

- `risk_on_high->unknown_4h` score `145.6023` n `40` status `ready` deltaP `-7.8963` edge `12.3678` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `145.6023` n `40` status `ready` deltaP `-7.8963` edge `12.3678` maxDD `-10.864`
- `market_context_high->unknown_24h` score `46.4755` n `134` status `ready` deltaP `-7.9322` edge `4.3287` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.8883` n `156` status `ready` deltaP `1.9114` edge `2.4369` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.4207` n `40` status `ready` deltaP `35.0087` edge `0.135` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.4207` n `40` status `ready` deltaP `35.0087` edge `0.135` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.3806` n `40` status `ready` deltaP `36.9817` edge `0.0399` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.3806` n `40` status `ready` deltaP `36.9817` edge `0.0399` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.4669` n `134` status `ready` deltaP `21.9573` edge `0.0804` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.6608` n `156` status `ready` deltaP `15.7638` edge `0.1614` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.2729` n `134` status `ready` deltaP `10.6612` edge `0.1337` maxDD `-4.8962`
- `market_context_high->equity_1h` score `0.9043` n `163` status `ready` deltaP `6.6034` edge `0.0873` maxDD `-2.144`
- `risk_on_high->crypto_major_4h` score `0.8981` n `40` status `ready` deltaP `18.689` edge `0.0168` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.8981` n `40` status `ready` deltaP `18.689` edge `0.0168` maxDD `-2.6576`
- `risk_on_high->equity_1h` score `0.386` n `40` status `ready` deltaP `10.9132` edge `-0.0015` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.386` n `40` status `ready` deltaP `10.9132` edge `-0.0015` maxDD `-0.7937`
- `risk_on_high->commodity_24h` score `0.3268` n `40` status `ready` deltaP `1.6031` edge `0.2447` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.3268` n `40` status `ready` deltaP `1.6031` edge `0.2447` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.2748` n `163` status `ready` deltaP `9.1657` edge `0.0427` maxDD `-3.4858`
- `market_context_high->crypto_major_1h` score `0.261` n `163` status `ready` deltaP `7.4281` edge `0.0444` maxDD `-3.7739`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

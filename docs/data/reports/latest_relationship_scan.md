# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T22:56:24.828632+00:00`
- Price records: `672`
- Market context records: `3936`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11443`

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

- `risk_on_high->unknown_4h` score `81.438` n `46` status `ready` deltaP `-1.7895` edge `10.6581` maxDD `-12.7655`
- `risk_on_and_context->unknown_4h` score `81.438` n `46` status `ready` deltaP `-1.7895` edge `10.6581` maxDD `-12.7655`
- `market_context_high->unknown_4h` score `15.0573` n `182` status `ready` deltaP `-3.9634` edge `1.8221` maxDD `-35.6052`
- `risk_on_high->equity_24h` score `10.0931` n `40` status `ready` deltaP `42.0139` edge `0.561` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `10.0931` n `40` status `ready` deltaP `42.0139` edge `0.561` maxDD `0.0`
- `risk_on_high->equity_4h` score `4.9213` n `46` status `ready` deltaP `38.1827` edge `0.1603` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `4.9213` n `46` status `ready` deltaP `38.1827` edge `0.1603` maxDD `-0.0458`
- `market_context_high->equity_24h` score `3.7632` n `165` status `ready` deltaP `20.8018` edge `0.4779` maxDD `-14.5715`
- `risk_on_high->index_24h` score `3.6268` n `40` status `ready` deltaP `30.0347` edge `0.102` maxDD `0.0`
- `risk_on_and_context->index_24h` score `3.6268` n `40` status `ready` deltaP `30.0347` edge `0.102` maxDD `0.0`
- `market_context_high->index_24h` score `3.57` n `165` status `ready` deltaP `25.7923` edge `0.2395` maxDD `-7.1159`
- `market_context_high->unknown_24h` score `3.4504` n `165` status `ready` deltaP `-12.9608` edge `2.0897` maxDD `-121.2608`
- `risk_on_high->crypto_major_4h` score `3.4317` n `46` status `ready` deltaP `26.2394` edge `0.1776` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `3.4317` n `46` status `ready` deltaP `26.2394` edge `0.1776` maxDD `-2.6576`
- `market_context_high->metal_24h` score `2.6206` n `165` status `ready` deltaP `15.4325` edge `0.267` maxDD `-9.1203`
- `market_context_high->crypto_major_4h` score `1.7675` n `182` status `ready` deltaP `17.7348` edge `0.2055` maxDD `-9.4488`
- `risk_on_high->commodity_24h` score `1.692` n `40` status `ready` deltaP `4.1667` edge `0.3046` maxDD `-11.9767`
- `risk_on_and_context->commodity_24h` score `1.692` n `40` status `ready` deltaP `4.1667` edge `0.3046` maxDD `-11.9767`
- `risk_on_high->equity_1h` score `1.2873` n `46` status `ready` deltaP `10.9542` edge `0.0736` maxDD `-0.8151`
- `risk_on_and_context->equity_1h` score `1.2873` n `46` status `ready` deltaP `10.9542` edge `0.0736` maxDD `-0.8151`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

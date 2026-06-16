# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-16T01:22:35.389655+00:00`
- Price records: `672`
- Market context records: `4045`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10528`

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

- `risk_on_high->unknown_4h` score `144.9097` n `40` status `ready` deltaP `-8.0488` edge `12.3111` maxDD `-10.864`
- `risk_on_and_context->unknown_4h` score `144.9097` n `40` status `ready` deltaP `-8.0488` edge `12.3111` maxDD `-10.864`
- `market_context_high->unknown_24h` score `45.5113` n `135` status `ready` deltaP `-8.03` edge `4.249` maxDD `-24.2289`
- `market_context_high->unknown_4h` score `22.1957` n `156` status `ready` deltaP `1.7589` edge `2.3802` maxDD `-35.7161`
- `risk_on_high->equity_24h` score `4.2826` n `40` status `ready` deltaP `34.662` edge `0.1258` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `4.2826` n `40` status `ready` deltaP `34.662` edge `0.1258` maxDD `0.0`
- `risk_on_high->equity_4h` score `3.4734` n `40` status `ready` deltaP `37.2866` edge `0.0456` maxDD `-0.0446`
- `risk_on_and_context->equity_4h` score `3.4734` n `40` status `ready` deltaP `37.2866` edge `0.0456` maxDD `-0.0446`
- `market_context_high->index_24h` score `2.3953` n `135` status `ready` deltaP `21.6163` edge `0.0767` maxDD `-1.3629`
- `market_context_high->equity_4h` score `1.7536` n `156` status `ready` deltaP `16.0687` edge `0.1671` maxDD `-6.9137`
- `market_context_high->metal_24h` score `1.0713` n `135` status `ready` deltaP `10.0918` edge `0.1207` maxDD `-4.8962`
- `risk_on_high->crypto_major_4h` score `0.9873` n `40` status `ready` deltaP `18.9939` edge `0.0222` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `0.9873` n `40` status `ready` deltaP `18.9939` edge `0.0222` maxDD `-2.6576`
- `market_context_high->equity_1h` score `0.8285` n `165` status `ready` deltaP `6.1368` edge `0.0841` maxDD `-2.144`
- `risk_on_high->equity_1h` score `0.4364` n `40` status `ready` deltaP `11.2126` edge `0.0007` maxDD `-0.7937`
- `risk_on_and_context->equity_1h` score `0.4364` n `40` status `ready` deltaP `11.2126` edge `0.0007` maxDD `-0.7937`
- `market_context_high->crypto_major_1h` score `0.2607` n `165` status `ready` deltaP `7.4551` edge `0.0442` maxDD `-3.7739`
- `risk_on_high->commodity_24h` score `0.2583` n `40` status `ready` deltaP `1.2565` edge `0.2413` maxDD `-12.9187`
- `risk_on_and_context->commodity_24h` score `0.2583` n `40` status `ready` deltaP `1.2565` edge `0.2413` maxDD `-12.9187`
- `market_context_high->metal_1h` score `0.2141` n `165` status `ready` deltaP `8.7661` edge `0.0418` maxDD `-3.8232`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T09:52:32.275342+00:00`
- Price records: `672`
- Market context records: `7552`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14475`

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

- `risk_on_high->crypto_major_4h` score `8.0413` n `35` status `ready` deltaP `42.1908` edge `0.4081` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `8.0413` n `35` status `ready` deltaP `42.1908` edge `0.4081` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.2752` n `35` status `ready` deltaP `31.5244` edge `0.2538` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.2752` n `35` status `ready` deltaP `31.5244` edge `0.2538` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.8848` n `35` status `ready` deltaP `17.3171` edge `0.3346` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8848` n `35` status `ready` deltaP `17.3171` edge `0.3346` maxDD `-0.4384`
- `risk_on_high->crypto_major_24h` score `4.7268` n `35` status `ready` deltaP `12.748` edge `0.4022` maxDD `-5.4627`
- `risk_on_and_context->crypto_major_24h` score `4.7268` n `35` status `ready` deltaP `12.748` edge `0.4022` maxDD `-5.4627`
- `risk_on_high->crypto_major_1h` score `1.6313` n `35` status `ready` deltaP `24.136` edge `0.0727` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6313` n `35` status `ready` deltaP `24.136` edge `0.0727` maxDD `-0.957`
- `risk_on_high->crypto_alt_24h` score `1.3477` n `35` status `ready` deltaP `13.0457` edge `0.1689` maxDD `-4.6471`
- `risk_on_and_context->crypto_alt_24h` score `1.3477` n `35` status `ready` deltaP `13.0457` edge `0.1689` maxDD `-4.6471`
- `risk_on_high->fx_24h` score `0.9558` n `34` status `ready` deltaP `22.0434` edge `0.0212` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.9558` n `34` status `ready` deltaP `22.0434` edge `0.0212` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.5124` n `35` status `ready` deltaP `8.1896` edge `0.0488` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5124` n `35` status `ready` deltaP `8.1896` edge `0.0488` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.3192` n `35` status `ready` deltaP `4.4402` edge `0.0251` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.3192` n `35` status `ready` deltaP `4.4402` edge `0.0251` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.2204` n `35` status `ready` deltaP `2.0274` edge `0.0518` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.2204` n `35` status `ready` deltaP `2.0274` edge `0.0518` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

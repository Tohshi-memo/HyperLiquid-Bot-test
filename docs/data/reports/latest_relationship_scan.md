# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T18:22:25.793528+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10225`

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

- `risk_on_high->unknown_24h` score `204.9398` n `105` status `ready` deltaP `22.7431` edge `16.9267` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `204.9398` n `105` status `ready` deltaP `22.7431` edge `16.9267` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `15.647` n `105` status `ready` deltaP `29.3056` edge `1.2982` maxDD `-11.1723`
- `risk_on_and_context->crypto_major_24h` score `15.647` n `105` status `ready` deltaP `29.3056` edge `1.2982` maxDD `-11.1723`
- `risk_on_high->crypto_alt_24h` score `12.6154` n `105` status `ready` deltaP `30.992` edge `0.8508` maxDD `-0.1572`
- `risk_on_and_context->crypto_alt_24h` score `12.6154` n `105` status `ready` deltaP `30.992` edge `0.8508` maxDD `-0.1572`
- `market_context_high->crypto_alt_24h` score `7.3553` n `217` status `ready` deltaP `24.1103` edge `0.5097` maxDD `-2.5998`
- `risk_on_high->crypto_alt_4h` score `5.745` n `117` status `ready` deltaP `30.4826` edge `0.3127` maxDD `-1.9733`
- `risk_on_and_context->crypto_alt_4h` score `5.745` n `117` status `ready` deltaP `30.4826` edge `0.3127` maxDD `-1.9733`
- `risk_on_high->crypto_major_4h` score `5.0633` n `117` status `ready` deltaP `26.8957` edge `0.3285` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `5.0633` n `117` status `ready` deltaP `26.8957` edge `0.3285` maxDD `-3.8693`
- `market_context_high->equity_24h` score `4.0755` n `217` status `ready` deltaP `15.7986` edge `0.2343` maxDD `0.0`
- `risk_on_high->equity_24h` score `3.3015` n `105` status `ready` deltaP `15.7986` edge `0.1698` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `3.3015` n `105` status `ready` deltaP `15.7986` edge `0.1698` maxDD `0.0`
- `risk_on_high->index_24h` score `1.9685` n `105` status `ready` deltaP `17.4554` edge `0.0519` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `1.9685` n `105` status `ready` deltaP `17.4554` edge `0.0519` maxDD `-0.0051`
- `market_context_high->index_24h` score `1.22` n `217` status `ready` deltaP `12.0176` edge `0.0609` maxDD `-0.1483`
- `risk_on_high->crypto_alt_1h` score `1.0112` n `117` status `ready` deltaP `4.6958` edge `0.0882` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `1.0112` n `117` status `ready` deltaP `4.6958` edge `0.0882` maxDD `-1.1521`
- `risk_on_high->metal_24h` score `0.5192` n `105` status `ready` deltaP `16.0565` edge `0.0751` maxDD `-0.9131`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

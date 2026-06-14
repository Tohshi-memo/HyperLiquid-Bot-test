# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T19:37:26.036606+00:00`
- Price records: `672`
- Market context records: `3922`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11427`

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

- `risk_on_high->unknown_4h` score `62.4617` n `58` status `ready` deltaP `4.9622` edge `8.189` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `62.4617` n `58` status `ready` deltaP `4.9622` edge `8.189` maxDD `-13.467`
- `risk_on_high->equity_24h` score `15.6515` n `39` status `ready` deltaP `42.0139` edge `1.0242` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `15.6515` n `39` status `ready` deltaP `42.0139` edge `1.0242` maxDD `0.0`
- `market_context_high->unknown_4h` score `13.1347` n `194` status `ready` deltaP `-1.5966` edge `1.6461` maxDD `-35.6052`
- `risk_on_high->crypto_major_4h` score `8.1448` n `58` status `ready` deltaP `29.1579` edge `0.5509` maxDD `-2.6576`
- `risk_on_and_context->crypto_major_4h` score `8.1448` n `58` status `ready` deltaP `29.1579` edge `0.5509` maxDD `-2.6576`
- `risk_on_high->equity_4h` score `6.5777` n `58` status `ready` deltaP `38.4724` edge `0.2964` maxDD `-0.0458`
- `risk_on_and_context->equity_4h` score `6.5777` n `58` status `ready` deltaP `38.4724` edge `0.2964` maxDD `-0.0458`
- `risk_on_high->index_24h` score `6.2536` n `39` status `ready` deltaP `30.0347` edge `0.3209` maxDD `0.0`
- `risk_on_and_context->index_24h` score `6.2536` n `39` status `ready` deltaP `30.0347` edge `0.3209` maxDD `0.0`
- `market_context_high->equity_24h` score `4.8768` n `165` status `ready` deltaP `20.8018` edge `0.5707` maxDD `-14.5715`
- `market_context_high->index_24h` score `4.0824` n `165` status `ready` deltaP `25.7923` edge `0.2822` maxDD `-7.1159`
- `risk_on_high->crypto_major_24h` score `3.6546` n `39` status `ready` deltaP `-14.3964` edge `0.8219` maxDD `-13.2573`
- `risk_on_and_context->crypto_major_24h` score `3.6546` n `39` status `ready` deltaP `-14.3964` edge `0.8219` maxDD `-13.2573`
- `market_context_high->crypto_major_4h` score `3.2715` n `194` status `ready` deltaP `19.4352` edge `0.3195` maxDD `-9.4488`
- `risk_on_high->crypto_major_1h` score `2.8781` n `58` status `ready` deltaP `13.4937` edge `0.2041` maxDD `-2.3372`
- `risk_on_and_context->crypto_major_1h` score `2.8781` n `58` status `ready` deltaP `13.4937` edge `0.2041` maxDD `-2.3372`
- `market_context_high->metal_24h` score `2.5417` n `165` status `ready` deltaP `17.1622` edge `0.2489` maxDD `-9.1203`
- `market_context_high->equity_4h` score `1.8975` n `194` status `ready` deltaP `17.1784` edge `0.214` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

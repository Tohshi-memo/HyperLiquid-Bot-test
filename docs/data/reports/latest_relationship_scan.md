# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T05:52:24.866327+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11550`

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

- `risk_on_high->unknown_4h` score `8.867` n `60` status `ready` deltaP `22.5101` edge `0.6317` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.867` n `60` status `ready` deltaP `22.5101` edge `0.6317` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.0841` n `162` status `ready` deltaP `19.4237` edge `0.3412` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6369` n `98` status `ready` deltaP `33.064` edge `0.2679` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.1697` n `60` status `ready` deltaP `23.0082` edge `0.2224` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.1697` n `60` status `ready` deltaP `23.0082` edge `0.2224` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.6696` n `60` status `ready` deltaP `9.6707` edge `0.2616` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.6696` n `60` status `ready` deltaP `9.6707` edge `0.2616` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.2381` n `60` status `ready` deltaP `29.6545` edge `0.0908` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.2381` n `60` status `ready` deltaP `29.6545` edge `0.0908` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.5589` n `60` status `ready` deltaP `31.1789` edge `0.0139` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.5589` n `60` status `ready` deltaP `31.1789` edge `0.0139` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.5285` n `162` status `ready` deltaP `11.8929` edge `0.1723` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `1.9539` n `60` status `ready` deltaP `12.4187` edge `0.216` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `1.9539` n `60` status `ready` deltaP `12.4187` edge `0.216` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.8399` n `60` status `ready` deltaP `23.1301` edge `0.0289` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.8399` n `60` status `ready` deltaP `23.1301` edge `0.0289` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.6449` n `60` status `ready` deltaP `21.8563` edge `0.0084` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.6449` n `60` status `ready` deltaP `21.8563` edge `0.0084` maxDD `-0.0291`
- `news_risk_high->unknown_1h` score `0.8119` n `33` status `ready` deltaP `-14.8748` edge `0.1998` maxDD `-0.9715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

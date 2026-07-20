# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-20T18:37:31.512102+00:00`
- Price records: `672`
- Market context records: `7380`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14631`

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

- `risk_on_high->crypto_major_4h` score `6.1948` n `32` status `ready` deltaP `35.5945` edge `0.2982` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1948` n `32` status `ready` deltaP `35.5945` edge `0.2982` maxDD `-0.8742`
- `risk_on_high->unknown_4h` score `4.9571` n `32` status `ready` deltaP `15.7012` edge `0.3514` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9571` n `32` status `ready` deltaP `15.7012` edge `0.3514` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.8668` n `32` status `ready` deltaP `28.4299` edge `0.2404` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.8668` n `32` status `ready` deltaP `28.4299` edge `0.2404` maxDD `-0.9492`
- `risk_on_high->crypto_major_1h` score `1.0648` n `32` status `ready` deltaP `18.881` edge `0.0351` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.0648` n `32` status `ready` deltaP `18.881` edge `0.0351` maxDD `-0.957`
- `risk_on_high->commodity_1h` score `0.37` n `32` status `ready` deltaP `5.0488` edge `0.0251` maxDD `-0.2339`
- `risk_on_and_context->commodity_1h` score `0.37` n `32` status `ready` deltaP `5.0488` edge `0.0251` maxDD `-0.2339`
- `risk_on_high->equity_1h` score `0.0914` n `32` status `ready` deltaP `3.3033` edge `0.0274` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.0914` n `32` status `ready` deltaP `3.3033` edge `0.0274` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `-0.0402` n `32` status `ready` deltaP `-0.5988` edge `0.0359` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `-0.0402` n `32` status `ready` deltaP `-0.5988` edge `0.0359` maxDD `-0.9651`
- `market_context_high->fx_1h` score `-0.1621` n `129` status `ready` deltaP `4.2392` edge `-0.0001` maxDD `-0.5821`
- `risk_on_high->metal_4h` score `-0.281` n `32` status `ready` deltaP `-1.5244` edge `0.0691` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `-0.281` n `32` status `ready` deltaP `-1.5244` edge `0.0691` maxDD `-0.5882`
- `market_context_high->commodity_1h` score `-0.6355` n `129` status `ready` deltaP `-2.364` edge `-0.0085` maxDD `-1.5775`
- `market_context_high->commodity_4h` score `-0.7096` n `129` status `ready` deltaP `-0.1707` edge `0.007` maxDD `-2.4139`
- `market_context_high->unknown_4h` score `-0.8207` n `129` status `ready` deltaP `3.6372` edge `0.1064` maxDD `-6.2031`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

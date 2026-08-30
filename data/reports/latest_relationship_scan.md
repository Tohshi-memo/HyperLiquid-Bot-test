# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T04:07:23.014571+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11504`

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

- `risk_on_high->unknown_4h` score `8.2621` n `66` status `ready` deltaP `22.9583` edge `0.5783` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.2621` n `66` status `ready` deltaP `22.9583` edge `0.5783` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `4.8392` n `168` status `ready` deltaP `19.0622` edge `0.3232` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6639` n `104` status `ready` deltaP `34.2414` edge `0.2623` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `3.6491` n `66` status `ready` deltaP `20.5839` edge `0.2028` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `3.6491` n `66` status `ready` deltaP `20.5839` edge `0.2028` maxDD `-1.208`
- `risk_on_high->crypto_alt_4h` score `2.6434` n `66` status `ready` deltaP `15.4472` edge `0.2842` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.6434` n `66` status `ready` deltaP `15.4472` edge `0.2842` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `2.6068` n `66` status `ready` deltaP `24.2054` edge `0.0808` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.6068` n `66` status `ready` deltaP `24.2054` edge `0.0808` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0149` n `66` status `ready` deltaP `3.3071` edge `0.1898` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0149` n `66` status `ready` deltaP `3.3071` edge `0.1898` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.9271` n `168` status `ready` deltaP `9.3136` edge `0.1466` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.6677` n `66` status `ready` deltaP `23.9099` edge `0.0105` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.6677` n `66` status `ready` deltaP `23.9099` edge `0.0105` maxDD `-0.1405`
- `risk_on_high->metal_4h` score `1.582` n `66` status `ready` deltaP `20.2513` edge `0.0266` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.582` n `66` status `ready` deltaP `20.2513` edge `0.0266` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1789` n `66` status `ready` deltaP `16.8527` edge `0.0073` maxDD `-0.0463`
- `news_risk_high->unknown_1h` score `0.8791` n `33` status `ready` deltaP `-14.8748` edge `0.2026` maxDD `-0.7475`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T04:22:26.180337+00:00`
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

- `risk_on_high->unknown_4h` score `8.2887` n `66` status `ready` deltaP `23.1107` edge `0.5795` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `8.2887` n `66` status `ready` deltaP `23.1107` edge `0.5795` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `4.8658` n `168` status `ready` deltaP `19.2146` edge `0.3244` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.6639` n `104` status `ready` deltaP `34.2414` edge `0.2623` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `3.6383` n `66` status `ready` deltaP `20.5839` edge `0.2019` maxDD `-1.208`
- `risk_on_and_context->crypto_major_4h` score `3.6383` n `66` status `ready` deltaP `20.5839` edge `0.2019` maxDD `-1.208`
- `risk_on_high->crypto_alt_4h` score `2.6426` n `66` status `ready` deltaP `15.4472` edge `0.2841` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.6426` n `66` status `ready` deltaP `15.4472` edge `0.2841` maxDD `-1.5298`
- `risk_on_high->equity_4h` score `2.5898` n `66` status `ready` deltaP `24.053` edge `0.0804` maxDD `-0.3281`
- `risk_on_and_context->equity_4h` score `2.5898` n `66` status `ready` deltaP `24.053` edge `0.0804` maxDD `-0.3281`
- `risk_on_high->unknown_1h` score `2.0161` n `66` status `ready` deltaP `3.3071` edge `0.1899` maxDD `-1.5148`
- `risk_on_and_context->unknown_1h` score `2.0161` n `66` status `ready` deltaP `3.3071` edge `0.1899` maxDD `-1.5148`
- `market_context_high->unknown_1h` score `1.9283` n `168` status `ready` deltaP `9.3136` edge `0.1467` maxDD `-1.5148`
- `risk_on_high->index_4h` score `1.6677` n `66` status `ready` deltaP `23.9099` edge `0.0105` maxDD `-0.1405`
- `risk_on_and_context->index_4h` score `1.6677` n `66` status `ready` deltaP `23.9099` edge `0.0105` maxDD `-0.1405`
- `risk_on_high->metal_4h` score `1.582` n `66` status `ready` deltaP `20.2513` edge `0.0266` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.582` n `66` status `ready` deltaP `20.2513` edge `0.0266` maxDD `-0.0488`
- `news_risk_high->unknown_1h` score `1.2483` n `32` status `ready` deltaP `-13.4543` edge `0.2239` maxDD `-0.7475`
- `risk_on_high->metal_1h` score `1.1669` n `66` status `ready` deltaP `16.703` edge `0.0073` maxDD `-0.0463`
- `risk_on_and_context->metal_1h` score `1.1669` n `66` status `ready` deltaP `16.703` edge `0.0073` maxDD `-0.0463`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

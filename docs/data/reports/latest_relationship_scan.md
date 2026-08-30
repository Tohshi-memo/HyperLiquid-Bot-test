# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-30T10:22:24.787595+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11460`

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

- `risk_on_high->unknown_4h` score `9.465` n `59` status `ready` deltaP `24.2093` edge `0.6702` maxDD `-1.0945`
- `risk_on_and_context->unknown_4h` score `9.465` n `59` status `ready` deltaP `24.2093` edge `0.6702` maxDD `-1.0945`
- `market_context_high->unknown_4h` score `5.7099` n `152` status `ready` deltaP `20.1059` edge `0.3888` maxDD `-1.0945`
- `market_context_high->metal_24h` score `4.5409` n `98` status `ready` deltaP `33.064` edge `0.2599` maxDD `-3.1535`
- `risk_on_high->crypto_major_4h` score `4.5216` n `59` status `ready` deltaP `24.1371` edge `0.2442` maxDD `-0.5985`
- `risk_on_and_context->crypto_major_4h` score `4.5216` n `59` status `ready` deltaP `24.1371` edge `0.2442` maxDD `-0.5985`
- `risk_on_high->unknown_1h` score `3.9131` n `59` status `ready` deltaP `10.6592` edge `0.2753` maxDD `-0.2885`
- `risk_on_and_context->unknown_1h` score `3.9131` n `59` status `ready` deltaP `10.6592` edge `0.2753` maxDD `-0.2885`
- `risk_on_high->equity_4h` score `3.3809` n `59` status `ready` deltaP `30.4956` edge `0.0971` maxDD `-0.1594`
- `risk_on_and_context->equity_4h` score `3.3809` n `59` status `ready` deltaP `30.4956` edge `0.0971` maxDD `-0.1594`
- `risk_on_high->index_4h` score `2.7518` n `59` status `ready` deltaP `33.41` edge `0.0151` maxDD `-0.0147`
- `risk_on_and_context->index_4h` score `2.7518` n `59` status `ready` deltaP `33.41` edge `0.0151` maxDD `-0.0147`
- `market_context_high->unknown_1h` score `2.7372` n `152` status `ready` deltaP `11.5624` edge `0.1919` maxDD `-0.9372`
- `risk_on_high->crypto_alt_4h` score `2.1444` n `59` status `ready` deltaP `12.407` edge `0.2405` maxDD `-1.5298`
- `risk_on_and_context->crypto_alt_4h` score `2.1444` n `59` status `ready` deltaP `12.407` edge `0.2405` maxDD `-1.5298`
- `risk_on_high->metal_4h` score `1.7832` n `59` status `ready` deltaP `22.362` edge `0.0293` maxDD `-0.0488`
- `risk_on_and_context->metal_4h` score `1.7832` n `59` status `ready` deltaP `22.362` edge `0.0293` maxDD `-0.0488`
- `risk_on_high->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_and_context->metal_1h` score `1.7131` n `59` status `ready` deltaP `22.6784` edge `0.0086` maxDD `-0.0291`
- `risk_on_high->equity_1h` score `1.3225` n `59` status `ready` deltaP `17.1928` edge `0.019` maxDD `-0.2062`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

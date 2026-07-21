# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T08:22:28.698366+00:00`
- Price records: `672`
- Market context records: `7439`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14665`

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

- `risk_on_high->crypto_major_4h` score `6.063` n `32` status `ready` deltaP `35.2217` edge `0.2897` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.063` n `32` status `ready` deltaP `35.2217` edge `0.2897` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.8415` n `32` status `ready` deltaP `16.7732` edge `0.4771` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.8415` n `32` status `ready` deltaP `16.7732` edge `0.4771` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.8484` n `32` status `ready` deltaP `15.0019` edge `0.347` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.8484` n `32` status `ready` deltaP `15.0019` edge `0.347` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.5154` n `32` status `ready` deltaP `26.5268` edge `0.2238` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.5154` n `32` status `ready` deltaP `26.5268` edge `0.2238` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.5429` n `32` status `ready` deltaP `17.0927` edge `0.3049` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.5429` n `32` status `ready` deltaP `17.0927` edge `0.3049` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.3108` n `36` status `ready` deltaP `21.1078` edge `0.0518` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3108` n `36` status `ready` deltaP `21.1078` edge `0.0518` maxDD `-0.957`
- `risk_on_high->equity_24h` score `1.0701` n `31` status `ready` deltaP `13.0996` edge `0.2732` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `1.0701` n `31` status `ready` deltaP `13.0996` edge `0.2732` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.681` n `36` status `ready` deltaP `7.8828` edge `0.0323` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.681` n `36` status `ready` deltaP `7.8828` edge `0.0323` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.4957` n `36` status `ready` deltaP `8.4085` edge `0.0452` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.4957` n `36` status `ready` deltaP `8.4085` edge `0.0452` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.2101` n `31` status `ready` deltaP `11.9775` edge `-0.0073` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.2101` n `31` status `ready` deltaP `11.9775` edge `-0.0073` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-06T21:22:24.836818+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10449`

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

- `risk_on_high->unknown_24h` score `291.8234` n `105` status `ready` deltaP `27.2569` edge `24.1369` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `291.8234` n `105` status `ready` deltaP `27.2569` edge `24.1369` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `19.9137` n `105` status `ready` deltaP `33.7897` edge `1.4859` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.9137` n `105` status `ready` deltaP `33.7897` edge `1.4859` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.5122` n `105` status `ready` deltaP `28.6508` edge `0.9442` maxDD `-0.4016`
- `risk_on_and_context->crypto_alt_24h` score `13.5122` n `105` status `ready` deltaP `28.6508` edge `0.9442` maxDD `-0.4016`
- `market_context_high->crypto_alt_24h` score `8.3938` n `196` status `ready` deltaP `22.9025` edge `0.6043` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.7972` n `196` status `ready` deltaP `23.0903` edge `0.4125` maxDD `0.0`
- `risk_on_high->equity_24h` score `5.9932` n `105` status `ready` deltaP `23.0903` edge `0.3455` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.9932` n `105` status `ready` deltaP `23.0903` edge `0.3455` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `4.9428` n `119` status `ready` deltaP `28.4946` edge `0.3079` maxDD `-5.8774`
- `risk_on_and_context->crypto_alt_4h` score `4.9428` n `119` status `ready` deltaP `28.4946` edge `0.3079` maxDD `-5.8774`
- `market_context_high->unknown_1h` score `3.5011` n `250` status `ready` deltaP `-4.109` edge `0.3916` maxDD `-2.4626`
- `risk_on_high->crypto_major_4h` score `3.2895` n `119` status `ready` deltaP `22.6673` edge `0.2481` maxDD `-7.007`
- `risk_on_and_context->crypto_major_4h` score `3.2895` n `119` status `ready` deltaP `22.6673` edge `0.2481` maxDD `-7.007`
- `risk_on_high->index_24h` score `2.5045` n `105` status `ready` deltaP `21.627` edge `0.0808` maxDD `-0.3018`
- `risk_on_and_context->index_24h` score `2.5045` n `105` status `ready` deltaP `21.627` edge `0.0808` maxDD `-0.3018`
- `market_context_high->index_24h` score `2.4045` n `196` status `ready` deltaP `21.2869` edge `0.0943` maxDD `-0.5338`
- `risk_on_high->crypto_alt_1h` score `0.7674` n `128` status `ready` deltaP `4.5004` edge `0.0814` maxDD `-2.1293`
- `risk_on_and_context->crypto_alt_1h` score `0.7674` n `128` status `ready` deltaP `4.5004` edge `0.0814` maxDD `-2.1293`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

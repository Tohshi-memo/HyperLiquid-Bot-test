# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T06:52:32.848191+00:00`
- Price records: `672`
- Market context records: `7432`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14659`

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

- `risk_on_high->crypto_major_4h` score `6.1523` n `32` status `ready` deltaP `35.6783` edge `0.2941` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.1523` n `32` status `ready` deltaP `35.6783` edge `0.2941` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.7767` n `32` status `ready` deltaP `16.7732` edge `0.4717` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.7767` n `32` status `ready` deltaP `16.7732` edge `0.4717` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.9285` n `32` status `ready` deltaP `15.7629` edge `0.3486` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9285` n `32` status `ready` deltaP `15.7629` edge `0.3486` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6604` n `32` status `ready` deltaP `27.4401` edge `0.2298` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6604` n `32` status `ready` deltaP `27.4401` edge `0.2298` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.6334` n `32` status `ready` deltaP `17.0927` edge `0.3165` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.6334` n `32` status `ready` deltaP `17.0927` edge `0.3165` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.26` n `34` status `ready` deltaP `20.3857` edge `0.0501` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.26` n `34` status `ready` deltaP `20.3857` edge `0.0501` maxDD `-0.957`
- `risk_on_high->equity_24h` score `1.0677` n `31` status `ready` deltaP `13.0996` edge `0.273` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `1.0677` n `31` status `ready` deltaP `13.0996` edge `0.273` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.3853` n `34` status `ready` deltaP `5.1316` edge `0.026` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.3853` n `34` status `ready` deltaP `5.1316` edge `0.026` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.3411` n `34` status `ready` deltaP `6.0944` edge `0.0408` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.3411` n `34` status `ready` deltaP `6.0944` edge `0.0408` maxDD `-1.3497`
- `risk_on_high->crypto_alt_1h` score `0.158` n `34` status `ready` deltaP `2.043` edge `0.0437` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.158` n `34` status `ready` deltaP `2.043` edge `0.0437` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

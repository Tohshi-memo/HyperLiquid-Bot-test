# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T10:22:32.836509+00:00`
- Price records: `672`
- Market context records: `3883`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13645`

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

- `risk_on_high->unknown_4h` score `47.4164` n `72` status `ready` deltaP `5.8943` edge `6.2539` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.4164` n `72` status `ready` deltaP `5.8943` edge `6.2539` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.3762` n `32` status `ready` deltaP `34.0278` edge `2.6421` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.3762` n `32` status `ready` deltaP `34.0278` edge `2.6421` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.8847` n `32` status `ready` deltaP `42.0139` edge `1.9603` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.8847` n `32` status `ready` deltaP `42.0139` edge `1.9603` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.2029` n `32` status `ready` deltaP `30.9028` edge `1.7427` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.2029` n `32` status `ready` deltaP `30.9028` edge `1.7427` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.1484` n `32` status `ready` deltaP `30.0347` edge `0.7288` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.1484` n `32` status `ready` deltaP `30.0347` edge `0.7288` maxDD `0.0`
- `market_context_high->unknown_4h` score `7.0802` n `205` status `ready` deltaP `-1.7073` edge `1.46` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4027` n `148` status `ready` deltaP `18.3653` edge `0.7141` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.4606` n `72` status `ready` deltaP `19.7662` edge `0.4355` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.4606` n `72` status `ready` deltaP `19.7662` edge `0.4355` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.133` n `148` status `ready` deltaP `25.305` edge `0.373` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.3139` n `148` status `ready` deltaP `21.5137` edge `0.2759` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.429` n `72` status `ready` deltaP `24.3394` edge `0.1536` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.429` n `72` status `ready` deltaP `24.3394` edge `0.1536` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `2.3557` n `148` status `ready` deltaP `5.396` edge `0.6067` maxDD `-31.0425`
- `market_context_high->crypto_major_4h` score `2.1682` n `205` status `ready` deltaP `14.2988` edge `0.2618` maxDD `-9.4488`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

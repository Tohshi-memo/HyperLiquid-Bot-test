# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T09:37:27.204402+00:00`
- Price records: `672`
- Market context records: `3673`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `12897`

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

- `risk_on_high->crypto_major_24h` score `33.7145` n `32` status `ready` deltaP `37.8472` edge `2.5615` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `33.7145` n `32` status `ready` deltaP `37.8472` edge `2.5615` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `28.1947` n `32` status `ready` deltaP `40.1042` edge `2.0822` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `28.1947` n `32` status `ready` deltaP `40.1042` edge `2.0822` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `25.5227` n `32` status `ready` deltaP `36.9792` edge `1.8955` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `25.5227` n `32` status `ready` deltaP `36.9792` edge `1.8955` maxDD `-0.8779`
- `risk_on_high->index_24h` score `15.6312` n `32` status `ready` deltaP `39.9306` edge `1.0364` maxDD `0.0`
- `risk_on_and_context->index_24h` score `15.6312` n `32` status `ready` deltaP `39.9306` edge `1.0364` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.551` n `32` status `ready` deltaP `20.7317` edge `0.9366` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.551` n `32` status `ready` deltaP `20.7317` edge `0.9366` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `6.9229` n `32` status `ready` deltaP `25.5208` edge `0.4329` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `6.9229` n `32` status `ready` deltaP `25.5208` edge `0.4329` maxDD `-0.7574`
- `market_context_high->index_24h` score `5.2352` n `157` status `ready` deltaP `25.2809` edge `0.4393` maxDD `-11.3924`
- `market_context_high->equity_24h` score `3.9068` n `157` status `ready` deltaP `17.1743` edge `0.7775` maxDD `-35.3144`
- `risk_on_high->crypto_alt_4h` score `2.684` n `32` status `ready` deltaP `0.8384` edge `0.4025` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.684` n `32` status `ready` deltaP `0.8384` edge `0.4025` maxDD `-11.7537`
- `risk_on_high->equity_4h` score `2.6784` n `32` status `ready` deltaP `10.5945` edge `0.3862` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6784` n `32` status `ready` deltaP `10.5945` edge `0.3862` maxDD `-5.7426`
- `risk_on_high->crypto_major_1h` score `1.2753` n `32` status `ready` deltaP `3.125` edge `0.2496` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `1.2753` n `32` status `ready` deltaP `3.125` edge `0.2496` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

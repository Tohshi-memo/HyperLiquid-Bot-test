# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T05:52:32.664576+00:00`
- Price records: `672`
- Market context records: `3864`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13683`

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

- `risk_on_high->unknown_4h` score `48.7746` n `72` status `ready` deltaP `8.0284` edge `6.4138` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `48.7746` n `72` status `ready` deltaP `8.0284` edge `6.4138` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `34.183` n `32` status `ready` deltaP `34.0278` edge `2.626` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.183` n `32` status `ready` deltaP `34.0278` edge `2.626` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.9423` n `32` status `ready` deltaP `42.0139` edge `1.9651` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.9423` n `32` status `ready` deltaP `42.0139` edge `1.9651` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.4776` n `32` status `ready` deltaP `31.7708` edge `1.7598` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.4776` n `32` status `ready` deltaP `31.7708` edge `1.7598` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.2761` n `32` status `ready` deltaP `31.0764` edge `0.7325` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.2761` n `32` status `ready` deltaP `31.0764` edge `0.7325` maxDD `0.0`
- `market_context_high->unknown_4h` score `8.1019` n `206` status `ready` deltaP `0.1805` edge `1.5784` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.747` n `132` status `ready` deltaP `15.4987` edge `0.7619` maxDD `-14.5715`
- `market_context_high->index_24h` score `5.8797` n `132` status `ready` deltaP `25.7734` edge `0.4321` maxDD `-7.1159`
- `market_context_high->unknown_24h` score `5.8177` n `132` status `ready` deltaP `-20.7387` edge `3.7323` maxDD `-200.1879`
- `risk_on_high->crypto_major_4h` score `5.462` n `72` status `ready` deltaP `19.004` edge `0.4407` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.462` n `72` status `ready` deltaP `19.004` edge `0.4407` maxDD `-5.9781`
- `market_context_high->metal_24h` score `3.5801` n `132` status `ready` deltaP `20.9122` edge `0.3021` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.6787` n `72` status `ready` deltaP `26.3211` edge `0.1612` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.6787` n `72` status `ready` deltaP `26.3211` edge `0.1612` maxDD `-5.7426`
- `market_context_high->crypto_major_24h` score `1.9554` n `132` status `ready` deltaP `1.5467` edge `0.599` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

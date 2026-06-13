# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-13T19:52:25.638392+00:00`
- Price records: `672`
- Market context records: `3821`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13781`

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

- `risk_on_high->crypto_major_24h` score `32.2774` n `32` status `ready` deltaP `34.0278` edge `2.4672` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `32.2774` n `32` status `ready` deltaP `34.0278` edge `2.4672` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `26.1779` n `32` status `ready` deltaP `42.0139` edge `1.9014` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `26.1779` n `32` status `ready` deltaP `42.0139` edge `1.9014` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `23.5671` n `32` status `ready` deltaP `31.9444` edge `1.7661` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `23.5671` n `32` status `ready` deltaP `31.9444` edge `1.7661` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3656` n `32` status `ready` deltaP `31.25` edge `0.7388` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3656` n `32` status `ready` deltaP `31.25` edge `0.7388` maxDD `0.0`
- `market_context_high->equity_24h` score `6.6682` n `147` status `ready` deltaP `18.2044` edge `0.7373` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.619` n `39` status `ready` deltaP `3.0566` edge `0.5601` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.619` n `39` status `ready` deltaP `3.0566` edge `0.5601` maxDD `-5.9781`
- `market_context_high->index_24h` score `5.4557` n `147` status `ready` deltaP `26.4881` edge `0.392` maxDD `-7.1159`
- `market_context_high->crypto_major_24h` score `4.7672` n `147` status `ready` deltaP `5.18` edge `0.8091` maxDD `-31.0425`
- `market_context_high->metal_24h` score `4.2589` n `147` status `ready` deltaP `25.9318` edge `0.3252` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.1784` n `39` status `ready` deltaP `14.1729` edge `0.2005` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.1784` n `39` status `ready` deltaP `14.1729` edge `0.2005` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.0661` n `191` status `ready` deltaP `10.5206` edge `0.2921` maxDD `-10.5381`
- `risk_on_high->metal_24h` score `1.4104` n `32` status `ready` deltaP `14.4097` edge `0.0476` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `1.4104` n `32` status `ready` deltaP `14.4097` edge `0.0476` maxDD `-0.7574`
- `market_context_high->equity_4h` score `1.1159` n `191` status `ready` deltaP `11.4879` edge `0.1868` maxDD `-8.2982`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T06:07:30.192333+00:00`
- Price records: `672`
- Market context records: `3659`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `13157`

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

- `risk_on_high->crypto_major_24h` score `35.0226` n `32` status `ready` deltaP `40.2778` edge `2.6543` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.0226` n `32` status `ready` deltaP `40.2778` edge `2.6543` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `30.7597` n `32` status `ready` deltaP `42.3611` edge `2.2809` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `30.7597` n `32` status `ready` deltaP `42.3611` edge `2.2809` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.9807` n `32` status `ready` deltaP `39.4097` edge `2.0008` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.9807` n `32` status `ready` deltaP `39.4097` edge `2.0008` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.4109` n `32` status `ready` deltaP `42.3611` edge `1.1685` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.4109` n `32` status `ready` deltaP `42.3611` edge `1.1685` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.1779` n `32` status `ready` deltaP `19.8171` edge `0.9116` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.1779` n `32` status `ready` deltaP `19.8171` edge `0.9116` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `9.0757` n `32` status `ready` deltaP `27.9514` edge `0.5961` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `9.0757` n `32` status `ready` deltaP `27.9514` edge `0.5961` maxDD `-0.7574`
- `market_context_high->index_24h` score `7.0149` n `157` status `ready` deltaP `27.7114` edge `0.5714` maxDD `-11.3924`
- `market_context_high->equity_24h` score `6.4717` n `157` status `ready` deltaP `19.4312` edge `0.9762` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.4738` n `32` status `ready` deltaP `9.375` edge `0.3681` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.4738` n `32` status `ready` deltaP `9.375` edge `0.3681` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.4192` n `32` status `ready` deltaP `0.2287` edge `0.3845` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.4192` n `32` status `ready` deltaP `0.2287` edge `0.3845` maxDD `-11.7537`
- `market_context_high->metal_24h` score `2.1183` n `157` status `ready` deltaP `22.2587` edge `0.5184` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.2285` n `32` status `ready` deltaP `3.125` edge `0.2436` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

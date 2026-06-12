# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-12T06:52:26.744300+00:00`
- Price records: `672`
- Market context records: `3662`
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

- `risk_on_high->crypto_major_24h` score `34.7985` n `32` status `ready` deltaP `39.7569` edge `2.6391` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `34.7985` n `32` status `ready` deltaP `39.7569` edge `2.6391` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `30.1732` n `32` status `ready` deltaP `41.8403` edge `2.2355` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `30.1732` n `32` status `ready` deltaP `41.8403` edge `2.2355` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `26.6858` n `32` status `ready` deltaP `38.8889` edge `1.9797` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `26.6858` n `32` status `ready` deltaP `38.8889` edge `1.9797` maxDD `-0.8779`
- `risk_on_high->index_24h` score `17.0248` n `32` status `ready` deltaP `41.8403` edge `1.1398` maxDD `0.0`
- `risk_on_and_context->index_24h` score `17.0248` n `32` status `ready` deltaP `41.8403` edge `1.1398` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `11.344` n `32` status `ready` deltaP `20.2744` edge `0.9224` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `11.344` n `32` status `ready` deltaP `20.2744` edge `0.9224` maxDD `-5.9781`
- `risk_on_high->metal_24h` score `8.6344` n `32` status `ready` deltaP `27.4306` edge `0.5628` maxDD `-0.7574`
- `risk_on_and_context->metal_24h` score `8.6344` n `32` status `ready` deltaP `27.4306` edge `0.5628` maxDD `-0.7574`
- `market_context_high->index_24h` score `6.6288` n `157` status `ready` deltaP `27.1906` edge `0.5427` maxDD `-11.3924`
- `market_context_high->equity_24h` score `5.8853` n `157` status `ready` deltaP `18.9104` edge `0.9308` maxDD `-35.3144`
- `risk_on_high->equity_4h` score `2.5506` n `32` status `ready` deltaP `9.8323` edge `0.3749` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5506` n `32` status `ready` deltaP `9.8323` edge `0.3749` maxDD `-5.7426`
- `risk_on_high->crypto_alt_4h` score `2.5504` n `32` status `ready` deltaP `0.5335` edge `0.3934` maxDD `-11.7537`
- `risk_on_and_context->crypto_alt_4h` score `2.5504` n `32` status `ready` deltaP `0.5335` edge `0.3934` maxDD `-11.7537`
- `market_context_high->metal_24h` score `1.8315` n `157` status `ready` deltaP `21.7379` edge `0.4851` maxDD `-21.6171`
- `risk_on_high->crypto_major_1h` score `1.2682` n `32` status `ready` deltaP `3.4244` edge `0.2467` maxDD `-5.8885`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

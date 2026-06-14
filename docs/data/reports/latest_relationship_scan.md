# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-14T14:07:25.823741+00:00`
- Price records: `672`
- Market context records: `3899`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11144`

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

- `risk_on_high->unknown_4h` score `47.2005` n `72` status `ready` deltaP `5.1321` edge `6.2313` maxDD `-13.467`
- `risk_on_and_context->unknown_4h` score `47.2005` n `72` status `ready` deltaP `5.1321` edge `6.2313` maxDD `-13.467`
- `risk_on_high->crypto_major_24h` score `35.2203` n `32` status `ready` deltaP `35.0694` edge `2.7055` maxDD `-0.0083`
- `risk_on_and_context->crypto_major_24h` score `35.2203` n `32` status `ready` deltaP `35.0694` edge `2.7055` maxDD `-0.0083`
- `risk_on_high->equity_24h` score `27.2267` n `32` status `ready` deltaP `42.0139` edge `1.9888` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `27.2267` n `32` status `ready` deltaP `42.0139` edge `1.9888` maxDD `0.0`
- `risk_on_high->crypto_alt_24h` score `24.0836` n `32` status `ready` deltaP `32.9861` edge `1.8022` maxDD `-0.8779`
- `risk_on_and_context->crypto_alt_24h` score `24.0836` n `32` status `ready` deltaP `32.9861` edge `1.8022` maxDD `-0.8779`
- `risk_on_high->index_24h` score `11.3656` n `32` status `ready` deltaP `30.0347` edge `0.7469` maxDD `0.0`
- `risk_on_and_context->index_24h` score `11.3656` n `32` status `ready` deltaP `30.0347` edge `0.7469` maxDD `0.0`
- `market_context_high->unknown_4h` score `6.5467` n `209` status `ready` deltaP `-1.5266` edge `1.3904` maxDD `-35.6052`
- `market_context_high->equity_24h` score `6.4976` n `159` status `ready` deltaP `20.0013` edge `0.7111` maxDD `-14.5715`
- `risk_on_high->crypto_major_4h` score `5.5976` n `72` status `ready` deltaP `19.9187` edge `0.4459` maxDD `-5.9781`
- `risk_on_and_context->crypto_major_4h` score `5.5976` n `72` status `ready` deltaP `19.9187` edge `0.4459` maxDD `-5.9781`
- `market_context_high->index_24h` score `4.882` n `159` status `ready` deltaP `25.6322` edge `0.3499` maxDD `-7.1159`
- `market_context_high->metal_24h` score `3.351` n `159` status `ready` deltaP `22.4286` edge `0.2729` maxDD `-9.1203`
- `risk_on_high->equity_4h` score `2.5627` n `72` status `ready` deltaP `24.7967` edge `0.1617` maxDD `-5.7426`
- `risk_on_and_context->equity_4h` score `2.5627` n `72` status `ready` deltaP `24.7967` edge `0.1617` maxDD `-5.7426`
- `market_context_high->crypto_major_4h` score `2.4948` n `209` status `ready` deltaP `16.071` edge `0.2772` maxDD `-9.4488`
- `market_context_high->crypto_major_24h` score `2.1173` n `159` status `ready` deltaP `4.8611` edge `0.5904` maxDD `-31.0425`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

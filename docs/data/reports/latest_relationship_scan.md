# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T14:37:26.191829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `40`

- Symbol pattern count: `7480`

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

- `market_context_high->crypto_major_24h` score `30.8327` n `44` status `ready` deltaP `50.2999` edge `2.2534` maxDD `-1.2138`
- `market_context_high->crypto_alt_24h` score `29.234` n `44` status `ready` deltaP `38.4943` edge `2.2019` maxDD `-1.1222`
- `risk_on_high->crypto_alt_4h` score `4.298` n `48` status `ready` deltaP `19.9695` edge `0.2693` maxDD `-1.8746`
- `risk_on_and_context->crypto_alt_4h` score `4.298` n `48` status `ready` deltaP `19.9695` edge `0.2693` maxDD `-1.8746`
- `risk_on_high->crypto_major_4h` score `3.8788` n `48` status `ready` deltaP `33.1301` edge `0.3691` maxDD `-4.7483`
- `risk_on_and_context->crypto_major_4h` score `3.8788` n `48` status `ready` deltaP `33.1301` edge `0.3691` maxDD `-4.7483`
- `market_context_high->crypto_major_4h` score `3.4709` n `100` status `ready` deltaP `16.9634` edge `0.3454` maxDD `-8.5396`
- `market_context_high->crypto_alt_4h` score `3.0811` n `100` status `ready` deltaP `12.9695` edge `0.3396` maxDD `-9.5446`
- `market_context_high->crypto_alt_1h` score `1.6104` n `100` status `ready` deltaP `12.2036` edge `0.1503` maxDD `-5.1298`
- `risk_on_high->crypto_alt_1h` score `1.0126` n `48` status `ready` deltaP `6.5369` edge `0.1004` maxDD `-2.4342`
- `risk_on_and_context->crypto_alt_1h` score `1.0126` n `48` status `ready` deltaP `6.5369` edge `0.1004` maxDD `-2.4342`
- `market_context_high->crypto_major_1h` score `0.7396` n `100` status `ready` deltaP `4.1976` edge `0.1161` maxDD `-3.9296`
- `risk_on_high->crypto_major_1h` score `0.4486` n `48` status `ready` deltaP `5.3643` edge `0.0928` maxDD `-3.6837`
- `risk_on_and_context->crypto_major_1h` score `0.4486` n `48` status `ready` deltaP `5.3643` edge `0.0928` maxDD `-3.6837`
- `market_context_high->unknown_4h` score `-0.3016` n `100` status `ready` deltaP `-5.9939` edge `0.0743` maxDD `-1.4244`
- `market_context_high->metal_1h` score `-0.5552` n `100` status `ready` deltaP `-0.7006` edge `0.0025` maxDD `-1.5204`
- `risk_on_high->metal_1h` score `-1.0246` n `48` status `ready` deltaP `-8.0339` edge `-0.0094` maxDD `-1.4724`
- `risk_on_and_context->metal_1h` score `-1.0246` n `48` status `ready` deltaP `-8.0339` edge `-0.0094` maxDD `-1.4724`
- `market_context_high->metal_4h` score `-1.3638` n `100` status `ready` deltaP `4.1524` edge `-0.0379` maxDD `-7.1699`
- `risk_on_high->metal_4h` score `-2.6165` n `48` status `ready` deltaP `-10.2643` edge `-0.1024` maxDD `-7.1699`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

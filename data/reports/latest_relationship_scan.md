# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T04:37:31.308973+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9658`

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

- `market_context_high->unknown_24h` score `54.8686` n `54` status `ready` deltaP `-16.0879` edge `4.716` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `33.8177` n `119` status `ready` deltaP `-7.066` edge `2.9358` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.176` n `54` status `ready` deltaP `25.1158` edge `0.5774` maxDD `-2.0804`
- `market_context_high->crypto_major_24h` score `6.1612` n `54` status `ready` deltaP `7.118` edge `1.0408` maxDD `-16.5356`
- `market_context_high->index_24h` score `5.7593` n `54` status `ready` deltaP `49.0741` edge `0.1571` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.4223` n `44` status `ready` deltaP `32.8992` edge `0.3178` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.4223` n `44` status `ready` deltaP `32.8992` edge `0.3178` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `4.3435` n `44` status `ready` deltaP `19.9695` edge `0.2736` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `4.3435` n `44` status `ready` deltaP `19.9695` edge `0.2736` maxDD `-1.9151`
- `risk_on_high->metal_4h` score `2.9669` n `44` status `ready` deltaP `27.4114` edge `0.0877` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `2.9669` n `44` status `ready` deltaP `27.4114` edge `0.0877` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.3403` n `56` status `ready` deltaP `8.7575` edge `0.113` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.3403` n `56` status `ready` deltaP `8.7575` edge `0.113` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.0` n `56` status `ready` deltaP `8.7789` edge `0.0901` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.0` n `56` status `ready` deltaP `8.7789` edge `0.0901` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `0.6673` n `56` status `ready` deltaP `10.4042` edge `0.0185` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `0.6673` n `56` status `ready` deltaP `10.4042` edge `0.0185` maxDD `-0.2466`
- `market_context_high->crypto_major_4h` score `0.6311` n `119` status `ready` deltaP `9.6562` edge `0.2271` maxDD `-11.1784`
- `market_context_high->metal_4h` score `0.6053` n `119` status `ready` deltaP `13.4121` edge `0.0333` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.1546` n `131` status `ready` deltaP `5.0361` edge `0.0855` maxDD `-4.9401`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

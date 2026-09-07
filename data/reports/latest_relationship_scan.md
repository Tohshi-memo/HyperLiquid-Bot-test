# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-07T01:22:26.156984+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10761`

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

- `risk_on_high->unknown_24h` score `393.5993` n `102` status `ready` deltaP `26.7361` edge `32.6217` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `393.5993` n `102` status `ready` deltaP `26.7361` edge `32.6217` maxDD `0.0`
- `market_context_high->unknown_1h` score `21.1112` n `250` status `ready` deltaP `-3.3581` edge `1.8541` maxDD `-2.4626`
- `risk_on_high->crypto_major_24h` score `19.7963` n `102` status `ready` deltaP `33.5376` edge `1.4778` maxDD `-1.4687`
- `risk_on_and_context->crypto_major_24h` score `19.7963` n `102` status `ready` deltaP `33.5376` edge `1.4778` maxDD `-1.4687`
- `risk_on_high->crypto_alt_24h` score `13.7248` n `102` status `ready` deltaP `30.0347` edge `0.9435` maxDD `0.0`
- `risk_on_and_context->crypto_alt_24h` score `13.7248` n `102` status `ready` deltaP `30.0347` edge `0.9435` maxDD `0.0`
- `market_context_high->crypto_alt_24h` score `8.7486` n `191` status `ready` deltaP `23.752` edge `0.6282` maxDD `-2.5998`
- `market_context_high->equity_24h` score `6.6496` n `191` status `ready` deltaP `23.0903` edge `0.4002` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.2125` n `123` status `ready` deltaP `29.8781` edge `0.3291` maxDD `-0.5127`
- `risk_on_and_context->crypto_alt_4h` score `6.2125` n `123` status `ready` deltaP `29.8781` edge `0.3291` maxDD `-0.5127`
- `risk_on_high->equity_24h` score `5.7016` n `102` status `ready` deltaP `23.0903` edge `0.3212` maxDD `0.0`
- `risk_on_and_context->equity_24h` score `5.7016` n `102` status `ready` deltaP `23.0903` edge `0.3212` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.264` n `123` status `ready` deltaP `23.7297` edge `0.283` maxDD `-3.8693`
- `risk_on_and_context->crypto_major_4h` score `4.264` n `123` status `ready` deltaP `23.7297` edge `0.283` maxDD `-3.8693`
- `risk_on_high->index_24h` score `2.7647` n `102` status `ready` deltaP `23.4477` edge `0.0783` maxDD `-0.0051`
- `risk_on_and_context->index_24h` score `2.7647` n `102` status `ready` deltaP `23.4477` edge `0.0783` maxDD `-0.0051`
- `market_context_high->index_24h` score `2.6166` n `191` status `ready` deltaP `21.6769` edge `0.095` maxDD `-0.0505`
- `risk_on_high->crypto_alt_1h` score `0.8608` n `126` status `ready` deltaP `4.0752` edge `0.0798` maxDD `-1.1521`
- `risk_on_and_context->crypto_alt_1h` score `0.8608` n `126` status `ready` deltaP `4.0752` edge `0.0798` maxDD `-1.1521`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

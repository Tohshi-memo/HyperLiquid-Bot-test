# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T13:37:29.120238+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `7870`

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

- `market_context_high->crypto_alt_24h` score `30.4417` n `41` status `ready` deltaP `40.9553` edge `2.2896` maxDD `-1.3996`
- `market_context_high->crypto_major_24h` score `28.3134` n `41` status `ready` deltaP `50.3218` edge `2.0471` maxDD `-1.1833`
- `risk_on_high->crypto_alt_4h` score `3.9672` n `48` status `ready` deltaP `18.1911` edge `0.2541` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `3.9672` n `48` status `ready` deltaP `18.1911` edge `0.2541` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `3.5638` n `48` status `ready` deltaP `33.1301` edge `0.3213` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `3.5638` n `48` status `ready` deltaP `33.1301` edge `0.3213` maxDD `-4.1548`
- `market_context_high->metal_24h` score `3.4713` n `41` status `ready` deltaP `29.8188` edge `0.1042` maxDD `-0.0975`
- `market_context_high->crypto_alt_4h` score `2.9293` n `101` status `ready` deltaP `12.6011` edge `0.3166` maxDD `-10.1868`
- `market_context_high->crypto_major_4h` score `2.8053` n `101` status `ready` deltaP `16.3396` edge `0.2928` maxDD `-8.1029`
- `market_context_high->crypto_alt_1h` score `1.5786` n `101` status `ready` deltaP `12.4103` edge `0.1439` maxDD `-4.9401`
- `risk_on_high->crypto_alt_1h` score `0.9407` n `48` status `ready` deltaP `6.3872` edge `0.0955` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `0.9407` n `48` status `ready` deltaP `6.3872` edge `0.0955` maxDD `-2.4421`
- `market_context_high->crypto_major_1h` score `0.5996` n `101` status `ready` deltaP `3.8225` edge `0.1008` maxDD `-3.4384`
- `risk_on_high->crypto_major_1h` score `0.4163` n `48` status `ready` deltaP `5.514` edge `0.0819` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `0.4163` n `48` status `ready` deltaP `5.514` edge `0.0819` maxDD `-3.2233`
- `market_context_high->index_1h` score `-0.0309` n `101` status `ready` deltaP `4.0063` edge `0.0024` maxDD `-0.3122`
- `market_context_high->index_24h` score `-0.0362` n `41` status `ready` deltaP `7.4611` edge `0.0453` maxDD `-1.6413`
- `market_context_high->metal_1h` score `-0.0824` n `101` status `ready` deltaP `6.6772` edge `0.0047` maxDD `-0.4868`
- `market_context_high->unknown_4h` score `-0.2349` n `101` status `ready` deltaP `-5.0909` edge `0.079` maxDD `-1.8373`
- `risk_on_high->metal_1h` score `-0.2992` n `48` status `ready` deltaP `3.4182` edge `0.0042` maxDD `-0.4868`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

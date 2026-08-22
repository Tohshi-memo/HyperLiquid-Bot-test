# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T10:07:23.873545+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14748`

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

- `market_context_high->unknown_1h` score `1.175` n `139` status `ready` deltaP `7.7457` edge `0.069` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.4167` n `133` status `ready` deltaP `19.5661` edge `-0.0518` maxDD `-0.5133`
- `market_context_high->fx_4h` score `0.0955` n `133` status `ready` deltaP `7.9051` edge `0.0098` maxDD `-0.3539`
- `market_context_high->index_1h` score `0.0497` n `139` status `ready` deltaP `8.2152` edge `0.0047` maxDD `-0.9144`
- `market_context_high->fx_1h` score `-0.0928` n `139` status `ready` deltaP `2.9089` edge `0.0046` maxDD `-0.2043`
- `market_context_high->metal_1h` score `-0.2322` n `139` status `ready` deltaP `2.4889` edge `-0.0045` maxDD `-0.6822`
- `market_context_high->metal_4h` score `-0.2472` n `133` status `ready` deltaP `7.0809` edge `-0.0173` maxDD `-1.5942`
- `market_context_high->equity_1h` score `-0.2674` n `139` status `ready` deltaP `5.5206` edge `0.0359` maxDD `-5.2257`
- `market_context_high->index_4h` score `-0.6031` n `133` status `ready` deltaP `2.3164` edge `0.0108` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.6846` n `133` status `ready` deltaP `-1.1611` edge `0.005` maxDD `-2.4692`
- `market_context_high->commodity_1h` score `-0.7375` n `139` status `ready` deltaP `-5.4829` edge `-0.0014` maxDD `-1.1941`
- `market_context_high->crypto_alt_1h` score `-1.485` n `139` status `ready` deltaP `-1.4571` edge `-0.0131` maxDD `-4.0748`
- `market_context_high->crypto_alt_4h` score `-1.6351` n `133` status `ready` deltaP `5.2701` edge `-0.0444` maxDD `-5.4926`
- `market_context_high->commodity_24h` score `-1.6438` n `113` status `ready` deltaP `-4.3433` edge `0.0753` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.7031` n `133` status `ready` deltaP `-0.9055` edge `0.0682` maxDD `-16.1079`
- `market_context_high->fx_24h` score `-2.2094` n `113` status `ready` deltaP `-4.1298` edge `0.0044` maxDD `-2.2121`
- `market_context_high->crypto_major_1h` score `-2.6006` n `139` status `ready` deltaP `-3.7985` edge `-0.0889` maxDD `-4.1996`
- `market_context_high->index_24h` score `-4.3052` n `113` status `ready` deltaP `-6.4298` edge `-0.0493` maxDD `-19.4493`
- `market_context_high->crypto_major_4h` score `-5.1367` n `133` status `ready` deltaP `-1.3444` edge `-0.317` maxDD `-3.1677`
- `market_context_high->metal_24h` score `-5.2471` n `113` status `ready` deltaP `-22.1269` edge `-0.1944` maxDD `-11.4635`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

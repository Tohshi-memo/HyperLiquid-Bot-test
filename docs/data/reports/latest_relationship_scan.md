# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-09T03:52:26.738948+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `6599`

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

- `market_context_high->equity_24h` score `10.7828` n `32` status `ready` deltaP `17.7083` edge `1.0178` maxDD `-16.6495`
- `market_context_high->commodity_24h` score `2.8104` n `32` status `ready` deltaP `9.2014` edge `0.2316` maxDD `-1.6995`
- `market_context_high->index_24h` score `1.4934` n `32` status `ready` deltaP `17.8819` edge `0.1185` maxDD `-2.3671`
- `market_context_high->equity_1h` score `0.9103` n `71` status `ready` deltaP `4.0588` edge `0.1685` maxDD `-5.5762`
- `market_context_high->metal_1h` score `0.8285` n `71` status `ready` deltaP `10.264` edge `0.0334` maxDD `-0.6226`
- `market_context_high->fx_24h` score `0.6784` n `32` status `ready` deltaP `10.7639` edge `-0.0064` maxDD `-0.0397`
- `market_context_high->metal_4h` score `0.6719` n `59` status `ready` deltaP `9.7612` edge `0.0736` maxDD `-1.2025`
- `market_context_high->commodity_4h` score `0.391` n `59` status `ready` deltaP `2.5785` edge `0.0626` maxDD `-1.1102`
- `market_context_high->commodity_1h` score `0.1775` n `71` status `ready` deltaP `7.7802` edge `0.0217` maxDD `-1.7019`
- `market_context_high->index_4h` score `0.1063` n `59` status `ready` deltaP `12.1021` edge `0.0258` maxDD `-2.4279`
- `market_context_high->index_1h` score `-0.1304` n `71` status `ready` deltaP `3.7594` edge `0.0224` maxDD `-0.6664`
- `market_context_high->crypto_alt_1h` score `-0.5872` n `71` status `ready` deltaP `10.4685` edge `0.0442` maxDD `-10.1421`
- `market_context_high->fx_1h` score `-0.8514` n `71` status `ready` deltaP `-9.9308` edge `-0.0035` maxDD `-0.4893`
- `market_context_high->fx_4h` score `-1.3479` n `59` status `ready` deltaP `-5.8598` edge `-0.0044` maxDD `-1.3476`
- `market_context_high->metal_24h` score `-1.5129` n `32` status `ready` deltaP `1.0417` edge `-0.1456` maxDD `-1.4245`
- `market_context_high->crypto_major_1h` score `-1.8777` n `71` status `ready` deltaP `1.7795` edge `-0.0427` maxDD `-11.7911`
- `market_context_high->equity_4h` score `-3.4749` n `59` status `ready` deltaP `7.591` edge `0.0378` maxDD `-24.9053`
- `market_context_high->crypto_major_24h` score `-4.6786` n `32` status `ready` deltaP `-4.8611` edge `0.0068` maxDD `-23.1423`
- `market_context_high->crypto_alt_4h` score `-7.0462` n `59` status `ready` deltaP `6.4334` edge `-0.1632` maxDD `-30.6833`
- `market_context_high->crypto_alt_24h` score `-8.8954` n `32` status `ready` deltaP `-18.75` edge `-0.1584` maxDD `-29.9639`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

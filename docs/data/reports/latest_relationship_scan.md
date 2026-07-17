# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-17T11:22:25.933273+00:00`
- Price records: `672`
- Market context records: `7023`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11529`

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

- `market_context_high->fx_1h` score `-0.2727` n `221` status `ready` deltaP `1.8662` edge `0.0011` maxDD `-0.5468`
- `market_context_high->metal_1h` score `-0.6862` n `221` status `ready` deltaP `-1.7842` edge `0.0007` maxDD `-2.1427`
- `market_context_high->crypto_alt_1h` score `-0.6866` n `221` status `ready` deltaP `0.5426` edge `0.0256` maxDD `-4.5815`
- `market_context_high->unknown_24h` score `-0.7215` n `208` status `ready` deltaP `-6.5838` edge `0.4064` maxDD `-18.7342`
- `market_context_high->index_1h` score `-0.7528` n `221` status `ready` deltaP `-0.7194` edge `-0.0006` maxDD `-2.2895`
- `market_context_high->crypto_major_1h` score `-0.7684` n `221` status `ready` deltaP `2.1927` edge `0.0221` maxDD `-7.1523`
- `market_context_high->fx_4h` score `-0.8254` n `221` status `ready` deltaP `10.5632` edge `0.0066` maxDD `-1.9611`
- `market_context_high->unknown_1h` score `-1.3361` n `221` status `ready` deltaP `-2.9751` edge `-0.0014` maxDD `-3.2083`
- `market_context_high->commodity_1h` score `-1.3611` n `221` status `ready` deltaP `-3.5366` edge `-0.0177` maxDD `-2.4388`
- `market_context_high->commodity_4h` score `-1.5963` n `221` status `ready` deltaP `-4.509` edge `-0.0392` maxDD `-4.4984`
- `market_context_high->index_4h` score `-1.853` n `221` status `ready` deltaP `6.7714` edge `-0.0128` maxDD `-12.2591`
- `market_context_high->metal_4h` score `-1.9489` n `221` status `ready` deltaP `5.8299` edge `0.0096` maxDD `-5.5324`
- `market_context_high->unknown_4h` score `-2.2965` n `221` status `ready` deltaP `-5.9638` edge `0.0759` maxDD `-9.5347`
- `market_context_high->crypto_alt_4h` score `-2.7853` n `221` status `ready` deltaP `0.7125` edge `0.0167` maxDD `-22.2831`
- `market_context_high->commodity_24h` score `-2.787` n `208` status `ready` deltaP `-3.6859` edge `-0.0768` maxDD `-4.4704`
- `market_context_high->equity_1h` score `-3.0896` n `221` status `ready` deltaP `2.4514` edge `-0.0184` maxDD `-15.7664`
- `market_context_high->crypto_major_4h` score `-3.1617` n `221` status `ready` deltaP `1.7555` edge `0.0114` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-3.9936` n `208` status `ready` deltaP `-4.3803` edge `-0.0144` maxDD `-4.4689`
- `market_context_high->equity_4h` score `-11.5157` n `221` status `ready` deltaP `3.9331` edge `-0.0759` maxDD `-65.7968`
- `market_context_high->metal_24h` score `-13.493` n `208` status `ready` deltaP `-10.8573` edge `-0.0551` maxDD `-39.4213`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

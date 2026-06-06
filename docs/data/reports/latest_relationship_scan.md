# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T00:22:21.304098+00:00`
- Price records: `672`
- Market context records: `3020`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `21.3305` n `99` status `ready` deltaP `9.4223` edge `2.1064` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `12.5489` n `99` status `ready` deltaP `42.3769` edge `0.7873` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `12.4601` n `99` status `ready` deltaP `21.1964` edge `0.9435` maxDD `-1.7175`
- `market_context_high->equity_24h` score `6.8059` n `99` status `ready` deltaP `20.0758` edge `1.0139` maxDD `-18.3486`
- `market_context_high->index_24h` score `6.6835` n `99` status `ready` deltaP `19.6654` edge `0.5514` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.5076` n `111` status `ready` deltaP `18.5523` edge `0.15` maxDD `-2.8438`
- `market_context_high->equity_4h` score `0.5717` n `111` status `ready` deltaP `13.7704` edge `0.1724` maxDD `-12.9393`
- `market_context_high->crypto_alt_4h` score `0.4368` n `111` status `ready` deltaP `24.3299` edge `0.4486` maxDD `-38.7172`
- `market_context_high->index_4h` score `0.1505` n `111` status `ready` deltaP `16.5555` edge `0.0987` maxDD `-10.8483`
- `market_context_high->commodity_1h` score `-0.0394` n `123` status `ready` deltaP `2.097` edge `0.025` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.384` n `123` status `ready` deltaP `4.2573` edge `0.0238` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4042` n `123` status `ready` deltaP `3.2533` edge `0.0361` maxDD `-5.7692`
- `market_context_high->fx_1h` score `-0.4685` n `123` status `ready` deltaP `-3.594` edge `0.0005` maxDD `-0.2615`
- `market_context_high->crypto_alt_1h` score `-0.7187` n `123` status `ready` deltaP `5.8834` edge `0.0816` maxDD `-14.7034`
- `market_context_high->unknown_1h` score `-0.8625` n `123` status `ready` deltaP `4.0663` edge `-0.0259` maxDD `-3.1801`
- `market_context_high->fx_4h` score `-1.0443` n `111` status `ready` deltaP `-8.115` edge `-0.0008` maxDD `-0.6521`
- `market_context_high->unknown_4h` score `-1.1145` n `111` status `ready` deltaP `-1.1014` edge `0.0198` maxDD `-3.7602`
- `market_context_high->crypto_major_1h` score `-1.1827` n `123` status `ready` deltaP `3.6999` edge `0.05` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-1.2539` n `123` status `ready` deltaP `-3.3823` edge `-0.0064` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.7414` n `99` status `ready` deltaP `-4.9242` edge `-0.0251` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

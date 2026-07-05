# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-05T18:07:29.549202+00:00`
- Price records: `672`
- Market context records: `5798`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8128`

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

- `market_context_high->equity_24h` score `0.5525` n `248` status `ready` deltaP `15.3954` edge `0.4513` maxDD `-31.6316`
- `market_context_high->equity_4h` score `-0.0488` n `301` status `ready` deltaP `6.3295` edge `0.1176` maxDD `-7.4425`
- `market_context_high->fx_1h` score `-0.261` n `301` status `ready` deltaP `2.1266` edge `0.0009` maxDD `-0.5499`
- `market_context_high->index_1h` score `-0.6331` n `301` status `ready` deltaP `0.3118` edge `0.0036` maxDD `-0.9472`
- `market_context_high->equity_1h` score `-0.6337` n `301` status `ready` deltaP `3.1626` edge `0.0268` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.6457` n `301` status `ready` deltaP `2.2067` edge `-0.001` maxDD `-2.0682`
- `market_context_high->commodity_1h` score `-0.7711` n `301` status `ready` deltaP `-1.9914` edge `-0.0051` maxDD `-3.7721`
- `market_context_high->crypto_major_1h` score `-0.9526` n `301` status `ready` deltaP `2.988` edge `0.0328` maxDD `-6.2348`
- `market_context_high->crypto_alt_1h` score `-1.1288` n `301` status `ready` deltaP `1.3926` edge `0.0301` maxDD `-6.6758`
- `market_context_high->fx_24h` score `-1.164` n `248` status `ready` deltaP `12.8865` edge `0.037` maxDD `-4.771`
- `market_context_high->index_4h` score `-1.2029` n `301` status `ready` deltaP `0.6311` edge `0.0103` maxDD `-3.165`
- `market_context_high->fx_4h` score `-1.4701` n `301` status `ready` deltaP `0.4552` edge `0.0034` maxDD `-2.2593`
- `market_context_high->commodity_4h` score `-2.3325` n `301` status `ready` deltaP `-3.2144` edge `-0.0249` maxDD `-12.8834`
- `market_context_high->metal_4h` score `-2.4898` n `301` status `ready` deltaP `-5.349` edge `-0.0476` maxDD `-11.5426`
- `market_context_high->index_24h` score `-2.7972` n `248` status `ready` deltaP `3.7131` edge `0.0311` maxDD `-18.1572`
- `market_context_high->crypto_major_4h` score `-2.9573` n `301` status `ready` deltaP `7.6351` edge `0.1399` maxDD `-25.6458`
- `market_context_high->crypto_alt_4h` score `-4.554` n `301` status `ready` deltaP `5.4073` edge `0.0853` maxDD `-28.7346`
- `market_context_high->metal_24h` score `-6.6988` n `248` status `ready` deltaP `-7.0621` edge `-0.2494` maxDD `-25.3209`
- `market_context_high->crypto_major_24h` score `-8.6853` n `248` status `ready` deltaP `0.0728` edge `-0.1744` maxDD `-29.6555`
- `market_context_high->commodity_24h` score `-10.5177` n `248` status `ready` deltaP `-14.2977` edge `-0.0805` maxDD `-38.719`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

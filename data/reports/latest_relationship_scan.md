# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T10:22:19.114145+00:00`
- Price records: `672`
- Market context records: `965`
- Flow alert records: `2705`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `1440`

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

- `market_context_high->crypto_major_24h` score `14.993` n `151` status `ready` deltaP `33.8415` edge `1.0572` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.3689` n `151` status `ready` deltaP `10.4167` edge `0.7113` maxDD `0.0`
- `market_context_high->equity_24h` score `1.3206` n `151` status `ready` deltaP `1.1589` edge `0.3628` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.611` n `151` status `ready` deltaP `-0.4162` edge `0.2532` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.3289` n `204` status `ready` deltaP `2.3805` edge `0.0375` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3565` n `204` status `ready` deltaP `1.6908` edge `0.0011` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6393` n `204` status `ready` deltaP `1.1389` edge `0.016` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.6732` n `192` status `ready` deltaP `1.7149` edge `0.0019` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6959` n `204` status `ready` deltaP `3.2347` edge `0.0058` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-0.7909` n `204` status `ready` deltaP `-1.5792` edge `-0.0137` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.3192` n `192` status `ready` deltaP `1.9309` edge `0.0924` maxDD `-10.5498`
- `market_context_high->crypto_major_1h` score `-1.6266` n `204` status `ready` deltaP `6.4283` edge `-0.0061` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.637` n `192` status `ready` deltaP `-1.5371` edge `0.0261` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8962` n `204` status `ready` deltaP `-2.5155` edge `-0.0304` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-1.9376` n `204` status `ready` deltaP `1.2299` edge `-0.0257` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.4905` n `192` status `ready` deltaP `8.9939` edge `0.1031` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.6923` n `192` status `ready` deltaP `-0.7749` edge `0.0809` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.2284` n `192` status `ready` deltaP `7.3933` edge `-0.1305` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.2664` n `192` status `ready` deltaP `-2.2485` edge `0.0206` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-3.9965` n `151` status `ready` deltaP `5.551` edge `0.0012` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

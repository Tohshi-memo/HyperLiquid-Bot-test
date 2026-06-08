# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-08T01:52:25.554590+00:00`
- Price records: `672`
- Market context records: `3237`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9724`

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

- `market_context_high->crypto_alt_24h` score `14.4071` n `103` status `ready` deltaP `19.1713` edge `2.7034` maxDD `-70.3986`
- `market_context_high->commodity_24h` score `13.7689` n `103` status `ready` deltaP `49.7304` edge `0.8587` maxDD `-2.0927`
- `market_context_high->index_24h` score `9.7244` n `103` status `ready` deltaP `32.3574` edge `0.8501` maxDD `-16.1026`
- `market_context_high->equity_24h` score `6.71` n `103` status `ready` deltaP `19.9164` edge `1.5691` maxDD `-53.663`
- `market_context_high->crypto_major_24h` score `2.7794` n `103` status `ready` deltaP `23.242` edge `2.2713` maxDD `-152.2601`
- `risk_on_high->crypto_major_1h` score `2.611` n `31` status `ready` deltaP `10.677` edge `0.3705` maxDD `-5.8885`
- `risk_on_and_context->crypto_major_1h` score `2.611` n `31` status `ready` deltaP `10.677` edge `0.3705` maxDD `-5.8885`
- `market_context_high->commodity_4h` score `1.8614` n `135` status `ready` deltaP `16.7761` edge `0.1371` maxDD `-3.8391`
- `risk_on_high->crypto_alt_1h` score `0.7074` n `31` status `ready` deltaP `3.8584` edge `0.2087` maxDD `-8.1649`
- `risk_on_and_context->crypto_alt_1h` score `0.7074` n `31` status `ready` deltaP `3.8584` edge `0.2087` maxDD `-8.1649`
- `risk_on_high->metal_1h` score `0.488` n `31` status `ready` deltaP `8.2142` edge `0.0763` maxDD `-1.4793`
- `risk_on_and_context->metal_1h` score `0.488` n `31` status `ready` deltaP `8.2142` edge `0.0763` maxDD `-1.4793`
- `risk_on_high->equity_1h` score `0.3391` n `31` status `ready` deltaP `2.5111` edge `0.1171` maxDD `-3.5625`
- `risk_on_and_context->equity_1h` score `0.3391` n `31` status `ready` deltaP `2.5111` edge `0.1171` maxDD `-3.5625`
- `risk_on_high->index_1h` score `-0.1328` n `31` status `ready` deltaP `0.0338` edge `0.0451` maxDD `-1.3216`
- `risk_on_and_context->index_1h` score `-0.1328` n `31` status `ready` deltaP `0.0338` edge `0.0451` maxDD `-1.3216`
- `market_context_high->commodity_1h` score `-0.3975` n `147` status `ready` deltaP `4.0409` edge `0.0215` maxDD `-2.5251`
- `market_context_high->index_1h` score `-0.5636` n `147` status `ready` deltaP `3.3474` edge `0.0117` maxDD `-4.5023`
- `market_context_high->unknown_4h` score `-0.6804` n `135` status `ready` deltaP `10.2857` edge `0.1013` maxDD `-15.1257`
- `risk_on_high->fx_1h` score `-0.8118` n `31` status `ready` deltaP `-11.3724` edge `-0.0048` maxDD `-0.2106`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

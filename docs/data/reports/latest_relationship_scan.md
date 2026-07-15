# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T01:07:26.822337+00:00`
- Price records: `672`
- Market context records: `6767`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11700`

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

- `market_context_high->unknown_24h` score `1.0503` n `176` status `ready` deltaP `0.5366` edge `0.5063` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `-0.0147` n `176` status `ready` deltaP `8.144` edge `0.1313` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0622` n `176` status `ready` deltaP `7.3524` edge `0.029` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2443` n `176` status `ready` deltaP `4.7496` edge `0.0244` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.4053` n `176` status `ready` deltaP `-0.5648` edge `0.0003` maxDD `-0.5468`
- `market_context_high->commodity_1h` score `-0.5985` n `176` status `ready` deltaP `-0.0034` edge `-0.0084` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.6248` n `176` status `ready` deltaP `-1.3167` edge `0.0001` maxDD `-0.7136`
- `market_context_high->metal_1h` score `-0.7425` n `176` status `ready` deltaP `-5.7397` edge `-0.0044` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1915` n `176` status `ready` deltaP `3.1063` edge `-0.0173` maxDD `-3.8827`
- `market_context_high->fx_4h` score `-1.1987` n `176` status `ready` deltaP `7.8437` edge `0.0004` maxDD `-2.1765`
- `market_context_high->index_4h` score `-1.2389` n `176` status `ready` deltaP `6.2916` edge `-0.0128` maxDD `-5.7046`
- `market_context_high->commodity_4h` score `-1.437` n `176` status `ready` deltaP `-1.9263` edge `-0.0224` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.7465` n `176` status `ready` deltaP `-6.876` edge `-0.0096` maxDD `-3.2083`
- `market_context_high->crypto_major_4h` score `-2.6101` n `176` status `ready` deltaP `3.0488` edge `-0.0235` maxDD `-16.8495`
- `market_context_high->metal_4h` score `-2.7197` n `176` status `ready` deltaP `-7.234` edge `-0.0144` maxDD `-5.2172`
- `market_context_high->crypto_alt_4h` score `-2.7388` n `176` status `ready` deltaP `1.9124` edge `-0.0237` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.5325` n `176` status `ready` deltaP `-15.2578` edge `0.0439` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2198` n `176` status `ready` deltaP `2.7023` edge `-0.1321` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.2789` n `176` status `ready` deltaP `-7.702` edge `-0.0016` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-8.6292` n `176` status `ready` deltaP `-14.5045` edge `-0.1611` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T22:37:24.813349+00:00`
- Price records: `672`
- Market context records: `2604`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.9641` n `140` status `ready` deltaP `18.0903` edge `0.5759` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.4191` n `146` status `ready` deltaP `25.3488` edge `0.5505` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6744` n `146` status `ready` deltaP `15.5258` edge `0.3837` maxDD `-10.1468`
- `market_context_high->crypto_alt_1h` score `1.4659` n `146` status `ready` deltaP `11.8797` edge `0.1617` maxDD `-6.1656`
- `market_context_high->crypto_alt_24h` score `1.0259` n `140` status `ready` deltaP `2.6439` edge `0.7057` maxDD `-39.0265`
- `market_context_high->unknown_4h` score `0.8405` n `146` status `ready` deltaP `7.5321` edge `0.1248` maxDD `-3.7312`
- `market_context_high->crypto_major_1h` score `0.8108` n `146` status `ready` deltaP `9.1625` edge `0.1259` maxDD `-4.2199`
- `market_context_high->index_24h` score `0.7557` n `140` status `ready` deltaP `8.4524` edge `0.1047` maxDD `-2.5127`
- `market_context_high->index_4h` score `0.2144` n `146` status `ready` deltaP `8.8227` edge `0.0432` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.0676` n `146` status `ready` deltaP `4.6899` edge `0.0125` maxDD `-1.2855`
- `market_context_high->unknown_1h` score `-0.3804` n `146` status `ready` deltaP `2.0999` edge `0.0206` maxDD `-2.6375`
- `market_context_high->commodity_1h` score `-0.4734` n `146` status `ready` deltaP `4.9032` edge `0.0157` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.5589` n `146` status `ready` deltaP `1.86` edge `0.0158` maxDD `-2.9823`
- `market_context_high->metal_4h` score `-0.6182` n `146` status `ready` deltaP `4.6546` edge `0.0562` maxDD `-4.7664`
- `market_context_high->fx_1h` score `-0.6257` n `146` status `ready` deltaP `-0.3855` edge `0.0039` maxDD `-0.278`
- `market_context_high->equity_1h` score `-0.7558` n `146` status `ready` deltaP `0.2215` edge `0.0194` maxDD `-2.7085`
- `market_context_high->fx_4h` score `-0.8876` n `146` status `ready` deltaP `-0.0731` edge `0.0123` maxDD `-0.8621`
- `market_context_high->equity_24h` score `-0.9009` n `140` status `ready` deltaP `11.7361` edge `-0.0863` maxDD `-2.3615`
- `market_context_high->fx_24h` score `-0.9103` n `140` status `ready` deltaP `3.631` edge `-0.0007` maxDD `-1.6157`
- `market_context_high->commodity_4h` score `-1.1543` n `146` status `ready` deltaP `2.5768` edge `0.0291` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

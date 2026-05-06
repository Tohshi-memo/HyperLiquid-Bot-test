# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-06T14:22:19.004364+00:00`
- Price records: `461`
- Market context records: `551`
- Flow alert records: `1556`
- Minimum samples: `30`
- Pattern count: `96`

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

- `market_context_high->crypto_alt_24h` score `4.9546` n `138` status `ready` deltaP `7.7223` edge `0.3662` maxDD `-0.0508`
- `market_context_high->crypto_major_24h` score `3.0477` n `138` status `ready` deltaP `10.1054` edge `0.22` maxDD `-1.3382`
- `market_context_high->fx_4h` score `0.0549` n `146` status `ready` deltaP `10.8269` edge `0.022` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.3064` n `146` status `ready` deltaP `2.1032` edge `0.0045` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.5639` n `146` status `ready` deltaP `1.8083` edge `0.0384` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.5652` n `146` status `ready` deltaP `1.7978` edge `0.0009` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-0.9717` n `146` status `ready` deltaP `-3.2013` edge `0.0007` maxDD `-2.1602`
- `market_context_high->equity_1h` score `-1.0424` n `146` status `ready` deltaP `-0.4098` edge `-0.0031` maxDD `-4.4826`
- `market_context_high->crypto_alt_1h` score `-1.2791` n `146` status `ready` deltaP `4.6462` edge `-0.0061` maxDD `-8.1842`
- `market_context_high->index_24h` score `-1.8856` n `138` status `ready` deltaP `-6.0186` edge `0.0825` maxDD `-5.9609`
- `market_context_high->crypto_major_1h` score `-2.013` n `146` status `ready` deltaP `3.3527` edge `-0.0178` maxDD `-11.4508`
- `market_context_high->index_4h` score `-2.2154` n `146` status `ready` deltaP `0.4426` edge `-0.0353` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-2.7376` n `146` status `ready` deltaP `0.9066` edge `0.0228` maxDD `-15.2248`
- `market_context_high->unknown_4h` score `-3.1672` n `146` status `ready` deltaP `0.7773` edge `-0.0813` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.3123` n `146` status `ready` deltaP `-5.2092` edge `0.1088` maxDD `-13.0076`
- `market_context_high->equity_4h` score `-3.3212` n `146` status `ready` deltaP `-3.639` edge `-0.0373` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.327` n `146` status `ready` deltaP `-5.0284` edge `-0.0478` maxDD `-9.0076`
- `market_context_high->equity_24h` score `-3.7861` n `138` status `ready` deltaP `-10.3845` edge `0.0142` maxDD `-10.5047`
- `market_context_high->crypto_major_4h` score `-3.869` n `146` status `ready` deltaP `8.3223` edge `-0.0073` maxDD `-22.648`
- `market_context_high->fx_24h` score `-4.2464` n `138` status `ready` deltaP `-5.3779` edge `-0.039` maxDD `-17.2313`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

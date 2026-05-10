# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T11:37:14.274893+00:00`
- Price records: `672`
- Market context records: `971`
- Flow alert records: `2721`
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

- `market_context_high->crypto_major_24h` score `15.1651` n `150` status `ready` deltaP `34.6875` edge `1.0659` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.6124` n `150` status `ready` deltaP `11.2847` edge `0.7258` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2916` n `150` status `ready` deltaP `0.8264` edge `0.3626` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5999` n `150` status `ready` deltaP `-0.9444` edge `0.2558` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.2452` n `208` status `ready` deltaP `3.2617` edge `0.0386` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.3648` n `208` status `ready` deltaP `1.546` edge `0.001` maxDD `-0.3124`
- `market_context_high->fx_4h` score `-0.6203` n `196` status `ready` deltaP `2.7034` edge `0.0021` maxDD `-1.6381`
- `market_context_high->equity_1h` score `-0.6501` n `208` status `ready` deltaP `1.1083` edge `0.0153` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7426` n `208` status `ready` deltaP `2.755` edge `0.0051` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1036` n `208` status `ready` deltaP `5.7779` edge `-0.0077` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1924` n `208` status `ready` deltaP `-1.379` edge `-0.013` maxDD `-3.5069`
- `market_context_high->crypto_alt_1h` score `-1.3188` n `208` status `ready` deltaP `0.239` edge `-0.0267` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.4707` n `196` status `ready` deltaP `0.9675` edge `0.0862` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.6487` n `196` status `ready` deltaP `-1.2786` edge `0.0234` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8454` n `208` status `ready` deltaP `-1.6294` edge `-0.0298` maxDD `-9.0076`
- `market_context_high->crypto_major_4h` score `-2.5105` n `196` status `ready` deltaP `9.0437` edge `0.1011` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-2.9367` n `196` status `ready` deltaP `-1.1044` edge `0.0794` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-3.1474` n `196` status `ready` deltaP `7.9704` edge `-0.1276` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.1913` n `196` status `ready` deltaP `-1.3098` edge `0.0206` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0171` n `150` status `ready` deltaP `4.8402` edge `0.0033` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

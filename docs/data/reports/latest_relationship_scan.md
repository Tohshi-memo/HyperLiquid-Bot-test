# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-10T13:37:17.052809+00:00`
- Price records: `672`
- Market context records: `981`
- Flow alert records: `2745`
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

- `market_context_high->crypto_major_24h` score `15.3936` n `150` status `ready` deltaP `35.7292` edge `1.078` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `9.8805` n `150` status `ready` deltaP `12.3264` edge `0.7412` maxDD `0.0`
- `market_context_high->equity_24h` score `1.2172` n `150` status `ready` deltaP `0.8264` edge `0.3564` maxDD `-10.5047`
- `market_context_high->index_24h` score `0.5277` n `150` status `ready` deltaP `-1.2916` edge `0.2521` maxDD `-5.9609`
- `market_context_high->commodity_1h` score `-0.1972` n `210` status `ready` deltaP `3.7425` edge `0.0394` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5554` n `210` status `ready` deltaP `1.6182` edge `0.001` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6368` n `210` status `ready` deltaP `1.2746` edge `0.0153` maxDD `-4.4826`
- `market_context_high->fx_4h` score `-0.68` n `204` status `ready` deltaP `1.5244` edge `0.0023` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.6922` n `210` status `ready` deltaP `3.3704` edge `0.0052` maxDD `-2.8282`
- `market_context_high->crypto_major_1h` score `-1.1332` n `210` status `ready` deltaP `5.3735` edge `-0.0088` maxDD `-11.4508`
- `market_context_high->unknown_1h` score `-1.1776` n `210` status `ready` deltaP `-1.075` edge `-0.0138` maxDD `-3.5069`
- `market_context_high->equity_4h` score `-1.5679` n `204` status `ready` deltaP `1.2524` edge `0.0762` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.7712` n `204` status `ready` deltaP `-2.0594` edge `0.0184` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.8347` n `210` status `ready` deltaP `-1.3487` edge `-0.0303` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-1.9624` n `204` status `ready` deltaP `-1.354` edge `0.0742` maxDD `-13.0076`
- `market_context_high->crypto_alt_1h` score `-2.0997` n `210` status `ready` deltaP `-0.1654` edge `-0.0299` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.7812` n `204` status `ready` deltaP `7.5502` edge `0.0885` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2022` n `204` status `ready` deltaP `7.7355` edge `-0.1306` maxDD `-8.3588`
- `market_context_high->crypto_alt_4h` score `-3.4477` n `204` status `ready` deltaP `-2.4002` edge `0.0065` maxDD `-15.2248`
- `market_context_high->unknown_24h` score `-4.0663` n `150` status `ready` deltaP `4.493` edge `-0.0007` maxDD `-33.7129`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

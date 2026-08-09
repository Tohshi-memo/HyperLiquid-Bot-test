# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-09T20:07:31.169793+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10858`

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

- `market_context_high->equity_24h` score `1.6012` n `114` status `ready` deltaP `2.6133` edge `0.422` maxDD `-21.1456`
- `market_context_high->metal_24h` score `1.5568` n `114` status `ready` deltaP `7.4744` edge `0.1375` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.1972` n `143` status `ready` deltaP `15.2045` edge `0.0657` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7887` n `147` status `ready` deltaP `10.7886` edge `0.0281` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5914` n `114` status `ready` deltaP `20.3217` edge `0.027` maxDD `-1.9329`
- `market_context_high->index_24h` score `0.115` n `114` status `ready` deltaP `5.4733` edge `0.1314` maxDD `-5.9181`
- `market_context_high->index_1h` score `-0.4738` n `147` status `ready` deltaP `-2.4777` edge `-0.0053` maxDD `-0.7809`
- `market_context_high->fx_1h` score `-0.5623` n `147` status `ready` deltaP `1.0337` edge `-0.0042` maxDD `-0.9639`
- `market_context_high->metal_1h` score `-0.629` n `147` status `ready` deltaP `-3.7435` edge `-0.0061` maxDD `-0.9664`
- `market_context_high->fx_4h` score `-0.7416` n `143` status `ready` deltaP `2.7791` edge `-0.005` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.9586` n `143` status `ready` deltaP `-1.5254` edge `-0.0092` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-1.024` n `143` status `ready` deltaP `-1.9657` edge `-0.0173` maxDD `-2.7373`
- `market_context_high->equity_1h` score `-1.031` n `147` status `ready` deltaP `-1.2689` edge `0.0054` maxDD `-4.6286`
- `market_context_high->crypto_alt_1h` score `-1.929` n `147` status `ready` deltaP `-10.0157` edge `-0.0298` maxDD `-2.4677`
- `market_context_high->equity_4h` score `-2.5986` n `143` status `ready` deltaP `-2.0286` edge `-0.0693` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.239` n `147` status `ready` deltaP `-11.4974` edge `-0.0608` maxDD `-7.2638`
- `market_context_high->crypto_alt_4h` score `-4.1244` n `143` status `ready` deltaP `-9.0387` edge `-0.1178` maxDD `-6.585`
- `market_context_high->crypto_major_24h` score `-4.3511` n `114` status `ready` deltaP `1.1148` edge `-0.1206` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-6.0109` n `114` status `ready` deltaP `-17.2058` edge `-0.2419` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.9192` n `147` status `ready` deltaP `-7.2926` edge `-0.5666` maxDD `-1.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

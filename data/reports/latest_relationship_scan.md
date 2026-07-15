# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-15T04:52:25.807246+00:00`
- Price records: `672`
- Market context records: `6783`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11716`

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

- `market_context_high->unknown_24h` score `0.9008` n `176` status `ready` deltaP `-1.1995` edge `0.4987` maxDD `-12.3511`
- `market_context_high->commodity_24h` score `0.0489` n `176` status `ready` deltaP `8.144` edge `0.1366` maxDD `-5.2791`
- `market_context_high->crypto_major_1h` score `-0.0759` n `181` status `ready` deltaP `7.4338` edge `0.0267` maxDD `-4.2122`
- `market_context_high->crypto_alt_1h` score `-0.2567` n `181` status `ready` deltaP `4.7747` edge `0.0232` maxDD `-3.7803`
- `market_context_high->fx_1h` score `-0.366` n `181` status `ready` deltaP `0.1621` edge `0.0005` maxDD `-0.5468`
- `market_context_high->index_1h` score `-0.6065` n `181` status `ready` deltaP `-1.0711` edge `0.0008` maxDD `-0.7136`
- `market_context_high->commodity_1h` score `-0.6604` n `181` status `ready` deltaP `-1.014` edge `-0.0096` maxDD `-2.1314`
- `market_context_high->metal_1h` score `-0.7384` n `181` status `ready` deltaP `-5.6622` edge `-0.0044` maxDD `-1.2017`
- `market_context_high->equity_1h` score `-1.1581` n `181` status `ready` deltaP `3.0139` edge `-0.0139` maxDD `-3.8827`
- `market_context_high->index_4h` score `-1.2988` n `176` status `ready` deltaP `5.5294` edge `-0.0154` maxDD `-5.7046`
- `market_context_high->fx_4h` score `-1.3007` n `176` status `ready` deltaP `6.1669` edge `-0.0015` maxDD `-2.1765`
- `market_context_high->commodity_4h` score `-1.5161` n `176` status `ready` deltaP `-3.2982` edge `-0.0234` maxDD `-5.5853`
- `market_context_high->unknown_1h` score `-1.5786` n `181` status `ready` deltaP `-5.5125` edge `-0.0047` maxDD `-3.2083`
- `market_context_high->metal_4h` score `-2.6109` n `176` status `ready` deltaP `-5.862` edge `-0.0096` maxDD `-5.2172`
- `market_context_high->crypto_major_4h` score `-2.8719` n `176` status `ready` deltaP `2.439` edge `-0.053` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.9867` n `176` status `ready` deltaP `1.1502` edge `-0.0504` maxDD `-19.2145`
- `market_context_high->unknown_4h` score `-3.2813` n `176` status `ready` deltaP `-14.0383` edge `0.0567` maxDD `-10.2579`
- `market_context_high->equity_4h` score `-4.2918` n `176` status `ready` deltaP `2.3975` edge `-0.1393` maxDD `-27.1529`
- `market_context_high->fx_24h` score `-4.4308` n `176` status `ready` deltaP `-9.0909` edge `-0.005` maxDD `-5.6237`
- `market_context_high->metal_24h` score `-9.0104` n `176` status `ready` deltaP `-17.1086` edge `-0.1926` maxDD `-28.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

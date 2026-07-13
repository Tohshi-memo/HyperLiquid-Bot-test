# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T03:07:26.132049+00:00`
- Price records: `672`
- Market context records: `6564`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9872`

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

- `market_context_high->unknown_24h` score `6.257` n `144` status `ready` deltaP `11.032` edge `0.7779` maxDD `-15.0689`
- `market_context_high->unknown_1h` score `1.7512` n `210` status `ready` deltaP `-5.1243` edge `0.2702` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3857` n `144` status `ready` deltaP `13.3492` edge `0.2133` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.3548` n `210` status `ready` deltaP `0.8458` edge `-0.0004` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.3861` n `210` status `ready` deltaP `7.3489` edge `0.0281` maxDD `-6.7936`
- `market_context_high->crypto_alt_1h` score `-0.438` n `210` status `ready` deltaP `6.9368` edge `0.0289` maxDD `-5.8368`
- `market_context_high->index_1h` score `-0.557` n `210` status `ready` deltaP `-0.5331` edge `0.0041` maxDD `-0.7564`
- `market_context_high->commodity_1h` score `-0.5894` n `210` status `ready` deltaP `-0.398` edge `-0.0046` maxDD `-2.1314`
- `market_context_high->index_4h` score `-0.6024` n `206` status `ready` deltaP `8.974` edge `0.0126` maxDD `-3.973`
- `market_context_high->crypto_major_4h` score `-1.0086` n `206` status `ready` deltaP `8.9828` edge `0.0732` maxDD `-12.6576`
- `market_context_high->crypto_alt_4h` score `-1.0311` n `206` status `ready` deltaP `6.3107` edge `0.0792` maxDD `-13.6106`
- `market_context_high->equity_1h` score `-1.1177` n `210` status `ready` deltaP `2.2317` edge `0.003` maxDD `-4.2147`
- `market_context_high->metal_1h` score `-1.2247` n `210` status `ready` deltaP `-3.1414` edge `-0.0004` maxDD `-2.1239`
- `market_context_high->unknown_4h` score `-1.3695` n `206` status `ready` deltaP `-16.133` edge `0.234` maxDD `-10.5788`
- `market_context_high->commodity_4h` score `-1.3911` n `206` status `ready` deltaP `-2.411` edge `-0.0128` maxDD `-5.6246`
- `market_context_high->fx_4h` score `-1.8021` n `206` status `ready` deltaP `-0.7849` edge `-0.0046` maxDD `-3.3635`
- `market_context_high->metal_4h` score `-1.8213` n `206` status `ready` deltaP `-0.6197` edge `0.0272` maxDD `-4.1918`
- `market_context_high->metal_24h` score `-1.9489` n `144` status `ready` deltaP `6.0917` edge `0.09` maxDD `-5.7746`
- `market_context_high->equity_4h` score `-3.2422` n `206` status `ready` deltaP `7.193` edge `-0.007` maxDD `-19.2246`
- `market_context_high->index_24h` score `-3.7713` n `144` status `ready` deltaP `1.4429` edge `-0.0018` maxDD `-10.7676`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

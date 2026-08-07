# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T21:07:39.592138+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `6.5534` n `86` status `ready` deltaP `3.4361` edge `0.8292` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.7379` n `86` status `ready` deltaP `14.5932` edge `0.2718` maxDD `-2.2743`
- `market_context_high->commodity_4h` score `1.5301` n `107` status `ready` deltaP `16.0502` edge `0.0878` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.5118` n `86` status `ready` deltaP `12.4044` edge `0.1946` maxDD `-5.7715`
- `market_context_high->fx_24h` score `1.4089` n `86` status `ready` deltaP `29.5044` edge `0.0621` maxDD `-2.2531`
- `market_context_high->commodity_1h` score `1.0181` n `108` status `ready` deltaP `12.4861` edge `0.0359` maxDD `-0.7439`
- `market_context_high->equity_1h` score `0.0289` n `108` status `ready` deltaP `7.0304` edge `0.0384` maxDD `-4.6286`
- `market_context_high->fx_1h` score `-0.2936` n `108` status `ready` deltaP `4.3025` edge `-0.0036` maxDD `-0.9639`
- `market_context_high->index_1h` score `-0.3581` n `108` status `ready` deltaP `-1.2364` edge `-0.0029` maxDD `-0.7809`
- `market_context_high->fx_4h` score `-0.5175` n `107` status `ready` deltaP `4.6957` edge `0.0009` maxDD `-1.6928`
- `market_context_high->index_4h` score `-0.6686` n `107` status `ready` deltaP `1.3492` edge `-0.0042` maxDD `-1.1743`
- `market_context_high->metal_4h` score `-0.8149` n `107` status `ready` deltaP `0.7066` edge `-0.0083` maxDD `-2.7373`
- `market_context_high->crypto_alt_1h` score `-0.9032` n `108` status `ready` deltaP `-5.7718` edge `-0.0144` maxDD `-2.3669`
- `market_context_high->metal_1h` score `-0.9941` n `108` status `ready` deltaP `-4.0142` edge `-0.0065` maxDD `-0.9664`
- `market_context_high->equity_4h` score `-1.0816` n `107` status `ready` deltaP `7.1689` edge `-0.0042` maxDD `-7.6983`
- `market_context_high->crypto_major_24h` score `-2.1396` n `86` status `ready` deltaP `7.532` edge `-0.0751` maxDD `-14.2873`
- `market_context_high->crypto_major_1h` score `-2.1681` n `108` status `ready` deltaP `-5.855` edge `-0.042` maxDD `-4.6382`
- `market_context_high->crypto_alt_24h` score `-3.3759` n `86` status `ready` deltaP `-19.695` edge `-0.1572` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-3.4401` n `107` status `ready` deltaP `-5.5576` edge `-0.0848` maxDD `-6.5193`
- `market_context_high->crypto_major_4h` score `-7.2352` n `107` status `ready` deltaP `-9.3757` edge `-0.191` maxDD `-18.954`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

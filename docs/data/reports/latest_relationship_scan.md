# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-11T23:15:53.356993+00:00`
- Price records: `672`
- Market context records: `985`
- Flow alert records: `3164`
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

- `market_context_high->crypto_major_24h` score `13.1037` n `210` status `ready` deltaP `31.151` edge `0.9177` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `5.4857` n `210` status `ready` deltaP `10.5812` edge `0.3866` maxDD `0.0`
- `market_context_high->commodity_1h` score `-0.4095` n `210` status `ready` deltaP `3.3532` edge `0.0243` maxDD `-3.7959`
- `market_context_high->fx_1h` score `-0.5687` n `210` status `ready` deltaP `1.7068` edge `-0.0007` maxDD `-0.3124`
- `market_context_high->equity_1h` score `-0.6645` n `210` status `ready` deltaP `0.973` edge `0.015` maxDD `-4.4826`
- `market_context_high->index_24h` score `-0.712` n `210` status `ready` deltaP `2.6819` edge `0.1223` maxDD `-5.9609`
- `market_context_high->fx_4h` score `-0.7191` n `210` status `ready` deltaP `0.9978` edge `0.0008` maxDD `-1.6381`
- `market_context_high->index_1h` score `-0.7601` n `210` status `ready` deltaP `2.7614` edge `0.0036` maxDD `-2.8282`
- `market_context_high->unknown_1h` score `-1.1631` n `210` status `ready` deltaP `-0.9978` edge `-0.0131` maxDD `-3.5069`
- `market_context_high->crypto_major_1h` score `-1.2315` n `210` status `ready` deltaP `4.8619` edge `-0.018` maxDD `-11.4508`
- `market_context_high->equity_24h` score `-1.249` n `210` status `ready` deltaP `4.1686` edge `0.1286` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-1.5795` n `210` status `ready` deltaP `1.3768` edge `0.0744` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.8059` n `210` status `ready` deltaP `-2.1638` edge `0.0162` maxDD `-6.5149`
- `market_context_high->metal_1h` score `-1.9719` n `210` status `ready` deltaP `-1.6919` edge `-0.0456` maxDD `-9.0076`
- `market_context_high->crypto_alt_1h` score `-2.1686` n `210` status `ready` deltaP `-0.6522` edge `-0.0324` maxDD `-8.1842`
- `market_context_high->crypto_major_4h` score `-2.963` n `210` status `ready` deltaP `7.0031` edge `0.077` maxDD `-22.648`
- `market_context_high->unknown_4h` score `-3.2236` n `210` status `ready` deltaP `7.4828` edge `-0.1307` maxDD `-8.3588`
- `market_context_high->commodity_4h` score `-3.2675` n `210` status `ready` deltaP `-2.0594` edge `0.0582` maxDD `-13.0076`
- `market_context_high->crypto_alt_4h` score `-3.4771` n `210` status `ready` deltaP `-2.4221` edge `0.0042` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.5614` n `210` status `ready` deltaP `-1.0595` edge `-0.0216` maxDD `-20.2343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

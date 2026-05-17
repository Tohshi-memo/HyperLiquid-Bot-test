# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T20:22:26.502021+00:00`
- Price records: `672`
- Market context records: `1048`
- Flow alert records: `4921`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8652`

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

- `market_context_high->crypto_major_24h` score `14.2229` n `182` status `ready` deltaP `32.7291` edge `1.0259` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5469` n `182` status `ready` deltaP `11.5668` edge `0.4252` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.9332` n `182` status `ready` deltaP `10.2398` edge `0.255` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2731` n `182` status `ready` deltaP `9.5288` edge `0.2067` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.4953` n `182` status `ready` deltaP `-7.3435` edge `0.3621` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0878` n `184` status `ready` deltaP `5.1029` edge `0.0003` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4255` n `184` status `ready` deltaP `4.4454` edge `0.0129` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6072` n `184` status `ready` deltaP `-0.0521` edge `0.0254` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7054` n `184` status `ready` deltaP `0.7648` edge `0.0169` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9853` n `184` status `ready` deltaP `5.9067` edge `0.0025` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1543` n `182` status `ready` deltaP `0.2479` edge `0.0018` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2735` n `184` status `ready` deltaP `0.2343` edge `0.0009` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.34` n `182` status `ready` deltaP `-0.2144` edge `0.0374` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6339` n `182` status `ready` deltaP `1.3418` edge `0.0701` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8782` n `184` status `ready` deltaP `3.2121` edge `-0.0331` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.7121` n `182` status `ready` deltaP `1.7254` edge `0.0403` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.2188` n `182` status `ready` deltaP `2.4099` edge `-0.0211` maxDD `-19.2774`
- `market_context_high->crypto_major_4h` score `-3.2317` n `182` status `ready` deltaP `6.7492` edge `0.0563` maxDD `-22.648`
- `market_context_high->commodity_4h` score `-3.577` n `182` status `ready` deltaP `-4.9836` edge `0.0519` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9683` n `182` status `ready` deltaP `-0.8443` edge `-0.1598` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T20:37:18.847272+00:00`
- Price records: `672`
- Market context records: `1049`
- Flow alert records: `4925`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8668`

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

- `market_context_high->crypto_major_24h` score `14.2216` n `182` status `ready` deltaP `32.7874` edge `1.0254` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.5389` n `182` status `ready` deltaP `11.5864` edge `0.4244` maxDD `-9.5387`
- `market_context_high->equity_24h` score `2.8818` n `182` status `ready` deltaP `10.1071` edge `0.2516` maxDD `-3.6396`
- `market_context_high->index_24h` score `2.2444` n `182` status `ready` deltaP `9.3957` edge `0.2052` maxDD `-2.1308`
- `market_context_high->metal_24h` score `0.4262` n `182` status `ready` deltaP `-7.4718` edge `0.3572` maxDD `-14.7496`
- `market_context_high->fx_1h` score `-0.0878` n `184` status `ready` deltaP `5.1029` edge `0.0003` maxDD `-0.3124`
- `market_context_high->index_1h` score `-0.4267` n `184` status `ready` deltaP `4.4454` edge `0.0128` maxDD `-2.2395`
- `market_context_high->equity_1h` score `-0.6228` n `184` status `ready` deltaP `-0.2018` edge `0.0251` maxDD `-4.3858`
- `market_context_high->commodity_1h` score `-0.7042` n `184` status `ready` deltaP `0.7648` edge `0.017` maxDD `-3.7959`
- `market_context_high->crypto_major_1h` score `-0.9697` n `184` status `ready` deltaP `5.9067` edge `0.0038` maxDD `-7.9187`
- `market_context_high->fx_4h` score `-1.1339` n `183` status `ready` deltaP `0.5031` edge `0.0018` maxDD `-1.6381`
- `market_context_high->crypto_alt_1h` score `-1.2627` n `184` status `ready` deltaP `0.2343` edge `0.0018` maxDD `-5.3538`
- `market_context_high->index_4h` score `-1.3299` n `183` status `ready` deltaP `-0.0733` edge `0.0373` maxDD `-6.1444`
- `market_context_high->equity_4h` score `-1.6437` n `183` status `ready` deltaP `1.3244` edge `0.0694` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-1.8913` n `184` status `ready` deltaP `3.0624` edge `-0.0332` maxDD `-7.2528`
- `market_context_high->crypto_alt_4h` score `-2.739` n `183` status `ready` deltaP `1.5236` edge `0.0394` maxDD `-15.2248`
- `market_context_high->crypto_major_4h` score `-3.1961` n `183` status `ready` deltaP `6.8189` edge `0.0588` maxDD `-22.648`
- `market_context_high->fx_24h` score `-3.2159` n `182` status `ready` deltaP `2.4805` edge `-0.0212` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.5852` n `183` status `ready` deltaP `-5.0413` edge `0.0516` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-3.9972` n `183` status `ready` deltaP `-1.1596` edge `-0.1614` maxDD `-20.7994`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T23:07:31.637442+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7166`

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

- `news_risk_high->unknown_24h` score `2662.944` n `139` status `ready` deltaP `1.2153` edge `221.9039` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.3892` n `139` status `ready` deltaP `27.553` edge `1.1606` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.376` n `139` status `ready` deltaP `27.1507` edge `0.6893` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.6951` n `139` status `ready` deltaP `22.8105` edge `0.8493` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.5511` n `139` status `ready` deltaP `32.7825` edge `0.1469` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.8663` n `139` status `ready` deltaP `25.1624` edge `0.2566` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6505` n `139` status `ready` deltaP `27.631` edge `0.1976` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0939` n `139` status `ready` deltaP `9.108` edge `0.2964` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.713` n `139` status `ready` deltaP `7.317` edge `0.1017` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5787` n `139` status `ready` deltaP `7.8534` edge `0.062` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4719` n `139` status `ready` deltaP `8.9013` edge `0.009` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0613` n `139` status `ready` deltaP `7.8775` edge `0.0277` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4525` n `139` status `ready` deltaP `2.0893` edge `0.0113` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5396` n `139` status `ready` deltaP `0.7463` edge `0.0541` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2209` n `139` status `ready` deltaP `-9.8663` edge `-0.0027` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3416` n `139` status `ready` deltaP `8.1527` edge `-0.005` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3902` n `139` status `ready` deltaP `-8.6988` edge `0.0292` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8333` n `139` status `ready` deltaP `-5.2433` edge `0.0714` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0482` n `139` status `ready` deltaP `-12.1656` edge `-0.014` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.8054` n `139` status `ready` deltaP `-11.0173` edge `-0.0018` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

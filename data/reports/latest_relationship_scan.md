# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-28T23:22:37.360800+00:00`
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

- `news_risk_high->unknown_24h` score `2661.402` n `139` status `ready` deltaP `1.2153` edge `221.7754` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `11.5399` n `139` status `ready` deltaP `27.7266` edge `1.172` maxDD `-29.2814`
- `news_risk_high->equity_24h` score `7.4655` n `139` status `ready` deltaP `27.3243` edge `0.6956` maxDD `-11.1179`
- `news_risk_high->crypto_major_24h` score `6.757` n `139` status `ready` deltaP `22.9841` edge `0.8533` maxDD `-26.1424`
- `news_risk_high->index_24h` score `3.571` n `139` status `ready` deltaP `32.9561` edge `0.1474` maxDD `-2.2287`
- `news_risk_high->metal_24h` score `2.9054` n `139` status `ready` deltaP `25.336` edge `0.2587` maxDD `-6.8392`
- `news_risk_high->equity_4h` score `2.6651` n `139` status `ready` deltaP `27.7834` edge `0.1978` maxDD `-9.2079`
- `news_risk_high->crypto_alt_4h` score `1.0637` n `139` status `ready` deltaP `8.9555` edge `0.2949` maxDD `-15.9436`
- `news_risk_high->crypto_alt_1h` score `0.6974` n `139` status `ready` deltaP `7.317` edge `0.1004` maxDD `-4.2849`
- `news_risk_high->equity_1h` score `0.5823` n `139` status `ready` deltaP `7.8534` edge `0.0623` maxDD `-1.957`
- `news_risk_high->index_1h` score `0.4719` n `139` status `ready` deltaP `8.9013` edge `0.009` maxDD `-0.3214`
- `news_risk_high->index_4h` score `-0.0735` n `139` status `ready` deltaP `7.7251` edge `0.0277` maxDD `-1.493`
- `news_risk_high->metal_1h` score `-0.4405` n `139` status `ready` deltaP `2.239` edge `0.0113` maxDD `-0.7016`
- `news_risk_high->crypto_major_1h` score `-0.5552` n `139` status `ready` deltaP `0.5966` edge `0.0531` maxDD `-7.2607`
- `news_risk_high->fx_1h` score `-1.2216` n `139` status `ready` deltaP `-9.8663` edge `-0.0028` maxDD `-1.0436`
- `news_risk_high->fx_4h` score `-1.3432` n `139` status `ready` deltaP `8.1527` edge `-0.0052` maxDD `-3.0414`
- `news_risk_high->metal_4h` score `-1.3902` n `139` status `ready` deltaP `-8.6988` edge `0.0292` maxDD `-3.6214`
- `news_risk_high->crypto_major_4h` score `-1.8489` n `139` status `ready` deltaP `-5.2433` edge `0.0694` maxDD `-13.719`
- `news_risk_high->commodity_1h` score `-2.0396` n `139` status `ready` deltaP `-12.0159` edge `-0.0139` maxDD `-3.3986`
- `news_risk_high->commodity_4h` score `-3.7884` n `139` status `ready` deltaP `-10.8649` edge `-0.0014` maxDD `-8.6825`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

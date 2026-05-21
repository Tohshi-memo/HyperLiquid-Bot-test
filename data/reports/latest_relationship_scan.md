# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T06:07:15.682976+00:00`
- Price records: `672`
- Market context records: `1396`
- Flow alert records: `5932`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8784`

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

- `market_context_high->crypto_major_24h` score `12.6637` n `157` status `ready` deltaP `27.6595` edge `0.9841` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4743` n `157` status `ready` deltaP `28.8184` edge `0.9657` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2393` n `157` status `ready` deltaP `11.3886` edge `1.0274` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.9664` n `157` status `ready` deltaP `19.555` edge `0.3088` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2974` n `157` status `ready` deltaP `12.7256` edge `0.3393` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4311` n `192` status `ready` deltaP `8.1682` edge `0.1478` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0607` n `157` status `ready` deltaP `9.8803` edge `0.0441` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0116` n `204` status `ready` deltaP `4.8404` edge `0.0152` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0727` n `204` status `ready` deltaP `3.0439` edge `0.0295` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3005` n `204` status `ready` deltaP `3.5282` edge `-0.002` maxDD `-0.3914`
- `market_context_high->index_4h` score `-0.5225` n `192` status `ready` deltaP `0.8638` edge `0.0596` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.6762` n `204` status `ready` deltaP `4.8902` edge `-0.0018` maxDD `-5.0663`
- `market_context_high->crypto_alt_1h` score `-0.7754` n `204` status `ready` deltaP `0.411` edge `0.0197` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8884` n `204` status `ready` deltaP `-1.6878` edge `-0.0013` maxDD `-2.252`
- `market_context_high->metal_4h` score `-0.9831` n `192` status `ready` deltaP `7.4822` edge `0.0243` maxDD `-7.4886`
- `market_context_high->crypto_major_4h` score `-1.4225` n `192` status `ready` deltaP `4.6113` edge `0.1216` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.4292` n `192` status `ready` deltaP `7.0884` edge `0.1656` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.4733` n `204` status `ready` deltaP `-1.8228` edge `-0.0041` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5666` n `192` status `ready` deltaP `-3.6585` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.2813` n `192` status `ready` deltaP `-12.1062` edge `-0.0214` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T11:07:20.737391+00:00`
- Price records: `672`
- Market context records: `1417`
- Flow alert records: `5993`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8785`

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

- `market_context_high->crypto_major_24h` score `11.8856` n `154` status `ready` deltaP `27.3539` edge `0.9213` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4845` n `154` status `ready` deltaP `28.7811` edge `0.9668` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4084` n `154` status `ready` deltaP `10.7729` edge `1.0456` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.7113` n `154` status `ready` deltaP `19.3813` edge `0.2887` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2599` n `154` status `ready` deltaP `12.5271` edge `0.3375` maxDD `-14.2815`
- `market_context_high->equity_4h` score `0.8954` n `202` status `ready` deltaP `5.2373` edge `0.1227` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0419` n `154` status `ready` deltaP `9.3592` edge `0.046` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0675` n `203` status `ready` deltaP `4.3768` edge `0.0117` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.1435` n `203` status `ready` deltaP `2.7735` edge `0.0254` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2901` n `203` status `ready` deltaP `3.6127` edge `-0.0017` maxDD `-0.3914`
- `market_context_high->crypto_alt_1h` score `-0.5834` n `203` status `ready` deltaP `1.2802` edge `0.0299` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.7633` n `203` status `ready` deltaP `-1.0383` edge `0.0048` maxDD `-2.252`
- `market_context_high->metal_1h` score `-0.7662` n `203` status `ready` deltaP `4.772` edge `-0.0082` maxDD `-5.4142`
- `market_context_high->index_4h` score `-0.8258` n `202` status `ready` deltaP `-1.0821` edge `0.0473` maxDD `-3.7119`
- `market_context_high->crypto_major_4h` score `-1.4044` n `202` status `ready` deltaP `5.1376` edge `0.1196` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.4105` n `202` status `ready` deltaP `6.8869` edge `0.1685` maxDD `-19.5565`
- `market_context_high->crypto_major_1h` score `-1.493` n `203` status `ready` deltaP `-1.2699` edge `-0.0011` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5982` n `202` status `ready` deltaP `-3.9634` edge `-0.0097` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-2.5875` n `202` status `ready` deltaP `-10.0896` edge `-0.0098` maxDD `-8.04`
- `market_context_high->metal_4h` score `-2.8325` n `202` status `ready` deltaP `4.3015` edge `-0.0049` maxDD `-11.7852`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

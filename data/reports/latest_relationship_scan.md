# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T07:37:15.508867+00:00`
- Price records: `672`
- Market context records: `1402`
- Flow alert records: `5950`
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

- `market_context_high->crypto_major_24h` score `12.432` n `156` status `ready` deltaP `27.4038` edge `0.9665` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.4733` n `156` status `ready` deltaP `28.8061` edge `0.9657` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.2292` n `156` status `ready` deltaP `10.8574` edge `1.0301` maxDD `-6.3373`
- `market_context_high->index_24h` score `3.843` n `156` status `ready` deltaP `19.4978` edge `0.2989` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.2346` n `156` status `ready` deltaP `12.6603` edge `0.3345` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.1236` n `197` status `ready` deltaP `6.8295` edge `0.1311` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0566` n `156` status `ready` deltaP `9.7088` edge `0.0449` maxDD `-1.3925`
- `market_context_high->index_1h` score `-0.0229` n `204` status `ready` deltaP `4.6496` edge `0.0136` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0919` n `204` status `ready` deltaP `3.0439` edge `0.0279` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.2346` n `204` status `ready` deltaP `4.2767` edge `-0.0015` maxDD `-0.3914`
- `market_context_high->metal_1h` score `-0.6874` n `204` status `ready` deltaP `5.2307` edge `-0.0055` maxDD `-5.0663`
- `market_context_high->index_4h` score `-0.7115` n `197` status `ready` deltaP `-0.2236` edge `0.0511` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `-0.7526` n `204` status `ready` deltaP `0.411` edge `0.0216` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.8668` n `204` status `ready` deltaP `-1.6878` edge `0.0005` maxDD `-2.252`
- `market_context_high->crypto_major_1h` score `-1.5113` n `204` status `ready` deltaP `-1.8228` edge `-0.0031` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.5183` n `197` status `ready` deltaP `-3.0999` edge `-0.0088` maxDD `-1.4313`
- `market_context_high->crypto_major_4h` score `-1.5729` n `197` status `ready` deltaP `4.0067` edge `0.1131` maxDD `-13.3376`
- `market_context_high->crypto_alt_4h` score `-1.6175` n `197` status `ready` deltaP `5.8298` edge `0.1583` maxDD `-19.5565`
- `market_context_high->metal_4h` score `-2.0702` n `197` status `ready` deltaP `5.9884` edge `0.0055` maxDD `-10.4353`
- `market_context_high->commodity_4h` score `-4.0645` n `197` status `ready` deltaP `-10.5067` edge `-0.014` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

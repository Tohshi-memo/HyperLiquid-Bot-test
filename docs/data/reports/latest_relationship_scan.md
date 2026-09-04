# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-04T03:37:27.686492+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11538`

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

- `risk_on_high->unknown_4h` score `22.5589` n `133` status `ready` deltaP `9.4558` edge `1.8787` maxDD `-2.2797`
- `risk_on_and_context->unknown_4h` score `22.5589` n `133` status `ready` deltaP `9.4558` edge `1.8787` maxDD `-2.2797`
- `market_context_high->unknown_4h` score `15.7939` n `167` status `ready` deltaP `11.0541` edge `1.312` maxDD `-2.563`
- `risk_on_high->unknown_1h` score `13.7287` n `133` status `ready` deltaP `-0.4548` edge `1.2048` maxDD `-1.95`
- `risk_on_and_context->unknown_1h` score `13.7287` n `133` status `ready` deltaP `-0.4548` edge `1.2048` maxDD `-1.95`
- `market_context_high->unknown_1h` score `9.4222` n `173` status `ready` deltaP `0.6057` edge `0.8442` maxDD `-2.0446`
- `market_context_high->equity_24h` score `0.9128` n `142` status `ready` deltaP `16.4002` edge `0.4013` maxDD `-20.7654`
- `risk_on_high->equity_24h` score `0.5592` n `120` status `ready` deltaP `12.257` edge `0.3794` maxDD `-19.828`
- `risk_on_and_context->equity_24h` score `0.5592` n `120` status `ready` deltaP `12.257` edge `0.3794` maxDD `-19.828`
- `news_risk_high->commodity_4h` score `0.3026` n `67` status `ready` deltaP `5.6425` edge `0.0371` maxDD `-0.8733`
- `risk_on_high->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `risk_on_and_context->metal_1h` score `0.0782` n `133` status `ready` deltaP `11.9637` edge `0.0015` maxDD `-1.699`
- `news_risk_high->index_1h` score `-0.0811` n `67` status `ready` deltaP `4.176` edge `-0.0029` maxDD `-0.8275`
- `risk_on_high->index_1h` score `-0.1193` n `133` status `ready` deltaP `4.5912` edge `-0.0014` maxDD `-0.5605`
- `risk_on_and_context->index_1h` score `-0.1193` n `133` status `ready` deltaP `4.5912` edge `-0.0014` maxDD `-0.5605`
- `news_risk_high->commodity_24h` score `-0.1702` n `67` status `ready` deltaP `4.4517` edge `-0.0246` maxDD `-0.2074`
- `news_risk_high->commodity_1h` score `-0.2113` n `67` status `ready` deltaP `4.0084` edge `0.0003` maxDD `-0.9036`
- `risk_on_high->crypto_alt_1h` score `-0.2953` n `133` status `ready` deltaP `4.4516` edge `0.0474` maxDD `-5.4685`
- `risk_on_and_context->crypto_alt_1h` score `-0.2953` n `133` status `ready` deltaP `4.4516` edge `0.0474` maxDD `-5.4685`
- `news_risk_high->fx_4h` score `-0.3024` n `67` status `ready` deltaP `5.8405` edge `0.0015` maxDD `-1.2507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

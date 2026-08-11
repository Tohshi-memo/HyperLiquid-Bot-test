# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T18:52:26.018018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11856`

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

- `risk_on_high->commodity_4h` score `2.4869` n `32` status `ready` deltaP `17.6067` edge `0.1081` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.4869` n `32` status `ready` deltaP `17.6067` edge `0.1081` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.1461` n `32` status `ready` deltaP `12.3129` edge `0.0367` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.1461` n `32` status `ready` deltaP `12.3129` edge `0.0367` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.9719` n `32` status `ready` deltaP `11.2043` edge `0.0204` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.9719` n `32` status `ready` deltaP `11.2043` edge `0.0204` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.712` n `181` status `ready` deltaP `10.7524` edge `0.0515` maxDD `-2.1077`
- `market_context_high->commodity_1h` score `0.7062` n `181` status `ready` deltaP `9.8612` edge `0.0253` maxDD `-0.5752`
- `market_context_high->commodity_24h` score `0.4822` n `143` status `ready` deltaP `8.8667` edge `0.0614` maxDD `-2.4263`
- `risk_on_high->index_1h` score `0.3202` n `32` status `ready` deltaP `10.4042` edge `0.0092` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3202` n `32` status `ready` deltaP `10.4042` edge `0.0092` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.1382` n `32` status `ready` deltaP `4.753` edge `0.0026` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.1382` n `32` status `ready` deltaP `4.753` edge `0.0026` maxDD `-0.1547`
- `market_context_high->fx_24h` score `-0.0146` n `143` status `ready` deltaP `9.9042` edge `0.0212` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.101` n `181` status `ready` deltaP `4.3041` edge `0.0007` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.1232` n `181` status `ready` deltaP `5.8003` edge `0.006` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.3297` n `32` status `ready` deltaP `0.5335` edge `0.0124` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.3297` n `32` status `ready` deltaP `0.5335` edge `0.0124` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.6788` n `32` status `ready` deltaP `-3.4618` edge `-0.0096` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.6788` n `32` status `ready` deltaP `-3.4618` edge `-0.0096` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

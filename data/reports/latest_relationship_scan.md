# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T16:41:41.455360+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11808`

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

- `market_context_high->unknown_24h` score `13.8177` n `137` status `ready` deltaP `-21.1818` edge `1.5381` maxDD `-9.6329`
- `risk_on_high->commodity_4h` score `2.7464` n `32` status `ready` deltaP `18.8262` edge `0.1216` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.7464` n `32` status `ready` deltaP `18.8262` edge `0.1216` maxDD `-0.1258`
- `risk_on_high->commodity_1h` score `1.2648` n `32` status `ready` deltaP `12.9117` edge `0.0426` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2648` n `32` status `ready` deltaP `12.9117` edge `0.0426` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `1.0121` n `32` status `ready` deltaP `11.6616` edge `0.0207` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0121` n `32` status `ready` deltaP `11.6616` edge `0.0207` maxDD `-0.1285`
- `market_context_high->commodity_4h` score `0.9716` n `181` status `ready` deltaP `11.9719` edge `0.065` maxDD `-2.1077`
- `market_context_high->commodity_24h` score `0.8771` n `137` status `ready` deltaP `10.2481` edge `0.0851` maxDD `-2.4263`
- `market_context_high->commodity_1h` score `0.8249` n `181` status `ready` deltaP `10.46` edge `0.0312` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.2563` n `32` status `ready` deltaP `9.3563` edge `0.008` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2563` n `32` status `ready` deltaP `9.3563` edge `0.008` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.2029` n `32` status `ready` deltaP `5.5015` edge `0.003` maxDD `-0.1547`
- `market_context_high->fx_24h` score `0.1638` n `137` status `ready` deltaP `11.6206` edge `0.0243` maxDD `-1.4613`
- `market_context_high->fx_1h` score `-0.059` n `181` status `ready` deltaP `5.0526` edge `0.0011` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.0971` n `181` status `ready` deltaP `6.2576` edge `0.0063` maxDD `-0.504`
- `risk_on_high->index_4h` score `-0.4502` n `32` status `ready` deltaP `-0.8384` edge `0.0061` maxDD `-0.6579`
- `risk_on_and_context->index_4h` score `-0.4502` n `32` status `ready` deltaP `-0.8384` edge `0.0061` maxDD `-0.6579`
- `risk_on_high->equity_1h` score `-0.7349` n `32` status `ready` deltaP `-4.0606` edge `-0.0128` maxDD `-1.6811`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

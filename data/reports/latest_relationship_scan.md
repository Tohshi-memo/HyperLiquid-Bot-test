# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-24T19:37:32.053091+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `7726`

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

- `market_context_high->unknown_4h` score `15.5535` n `104` status `ready` deltaP `-2.5562` edge `1.3467` maxDD `-1.016`
- `market_context_high->commodity_24h` score `1.0521` n `76` status `ready` deltaP `17.3062` edge `0.0632` maxDD `-3.6055`
- `risk_on_high->fx_1h` score `0.7195` n `32` status `ready` deltaP `15.9431` edge `0.0035` maxDD `-0.0698`
- `risk_on_and_context->fx_1h` score `0.7195` n `32` status `ready` deltaP `15.9431` edge `0.0035` maxDD `-0.0698`
- `risk_on_high->commodity_24h` score `0.7068` n `32` status `ready` deltaP `16.3194` edge `0.0337` maxDD `-1.1503`
- `risk_on_and_context->commodity_24h` score `0.7068` n `32` status `ready` deltaP `16.3194` edge `0.0337` maxDD `-1.1503`
- `market_context_high->commodity_4h` score `0.6279` n `104` status `ready` deltaP `10.7411` edge `0.0405` maxDD `-1.449`
- `risk_on_high->index_1h` score `0.4572` n `32` status `ready` deltaP `12.6684` edge `0.0012` maxDD `-0.1637`
- `risk_on_and_context->index_1h` score `0.4572` n `32` status `ready` deltaP `12.6684` edge `0.0012` maxDD `-0.1637`
- `risk_on_high->equity_1h` score `0.3871` n `32` status `ready` deltaP `14.4648` edge `-0.0045` maxDD `-0.7172`
- `risk_on_and_context->equity_1h` score `0.3871` n `32` status `ready` deltaP `14.4648` edge `-0.0045` maxDD `-0.7172`
- `risk_on_high->fx_4h` score `0.1301` n `32` status `ready` deltaP `5.4878` edge `0.0065` maxDD `-0.1126`
- `risk_on_and_context->fx_4h` score `0.1301` n `32` status `ready` deltaP `5.4878` edge `0.0065` maxDD `-0.1126`
- `market_context_high->fx_1h` score `-0.1476` n `111` status `ready` deltaP `2.0917` edge `0.0026` maxDD `-0.1712`
- `market_context_high->commodity_1h` score `-0.2551` n `111` status `ready` deltaP `3.0143` edge `0.0056` maxDD `-1.0053`
- `risk_on_high->metal_4h` score `-0.4265` n `32` status `ready` deltaP `0.5335` edge `0.0169` maxDD `-0.3441`
- `risk_on_and_context->metal_4h` score `-0.4265` n `32` status `ready` deltaP `0.5335` edge `0.0169` maxDD `-0.3441`
- `market_context_high->fx_4h` score `-0.4462` n `104` status `ready` deltaP `-0.2814` edge `0.0053` maxDD `-0.5168`
- `risk_on_high->metal_1h` score `-0.4633` n `32` status `ready` deltaP `-2.9379` edge `0.0067` maxDD `-0.058`
- `risk_on_and_context->metal_1h` score `-0.4633` n `32` status `ready` deltaP `-2.9379` edge `0.0067` maxDD `-0.058`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

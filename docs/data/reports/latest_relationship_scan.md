# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-11T07:58:53.636979+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11760`

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

- `market_context_high->unknown_24h` score `47.0074` n `127` status `ready` deltaP `-18.7803` edge `4.2879` maxDD `-9.6329`
- `market_context_high->commodity_24h` score `2.4973` n `127` status `ready` deltaP `14.2047` edge `0.2021` maxDD `-3.0953`
- `risk_on_high->commodity_1h` score `1.2444` n `32` status `ready` deltaP `12.762` edge `0.0419` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.2444` n `32` status `ready` deltaP `12.762` edge `0.0419` maxDD `-0.1957`
- `market_context_high->commodity_1h` score `0.7851` n `181` status `ready` deltaP `10.3103` edge `0.0304` maxDD `-0.6965`
- `market_context_high->commodity_4h` score `0.7284` n `171` status `ready` deltaP `10.7491` edge `0.0605` maxDD `-2.7169`
- `market_context_high->fx_24h` score `0.4962` n `127` status `ready` deltaP `16.8875` edge `0.0318` maxDD `-1.4613`
- `risk_on_high->index_1h` score `0.2446` n `32` status `ready` deltaP `9.2066` edge `0.0075` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.2446` n `32` status `ready` deltaP `9.2066` edge `0.0075` maxDD `-0.3343`
- `risk_on_high->fx_1h` score `0.0963` n `32` status `ready` deltaP `4.3039` edge `0.0021` maxDD `-0.1547`
- `risk_on_and_context->fx_1h` score `0.0963` n `32` status `ready` deltaP `4.3039` edge `0.0021` maxDD `-0.1547`
- `market_context_high->fx_1h` score `-0.1275` n `181` status `ready` deltaP `3.855` edge `0.0003` maxDD `-0.3878`
- `market_context_high->fx_4h` score `-0.2386` n `171` status `ready` deltaP `3.8814` edge `0.004` maxDD `-0.504`
- `risk_on_high->equity_1h` score `-0.8206` n `32` status `ready` deltaP `-4.9588` edge `-0.0178` maxDD `-1.6811`
- `risk_on_and_context->equity_1h` score `-0.8206` n `32` status `ready` deltaP `-4.9588` edge `-0.0178` maxDD `-1.6811`
- `market_context_high->index_1h` score `-0.8935` n `181` status `ready` deltaP `-7.9895` edge `-0.0036` maxDD `-0.948`
- `market_context_high->metal_1h` score `-1.1334` n `181` status `ready` deltaP `-8.0251` edge `-0.0157` maxDD `-2.0884`
- `risk_on_high->crypto_major_1h` score `-1.397` n `32` status `ready` deltaP `1.3286` edge `-0.0671` maxDD `-2.6536`
- `risk_on_and_context->crypto_major_1h` score `-1.397` n `32` status `ready` deltaP `1.3286` edge `-0.0671` maxDD `-2.6536`
- `market_context_high->index_4h` score `-1.4342` n `171` status `ready` deltaP `-3.3135` edge `-0.008` maxDD `-1.4875`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T08:37:27.080757+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11176`

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

- `news_risk_high->unknown_4h` score `398.478` n `78` status `ready` deltaP `-22.1505` edge `33.4435` maxDD `-4.1464`
- `news_risk_high->unknown_24h` score `21.7995` n `78` status `ready` deltaP `18.2292` edge `1.6951` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.6081` n `78` status `ready` deltaP `44.8184` edge `1.541` maxDD `-1.4626`
- `news_risk_high->crypto_major_24h` score `16.2851` n `78` status `ready` deltaP `34.5219` edge `1.274` maxDD `-9.098`
- `news_risk_high->equity_24h` score `14.9444` n `78` status `ready` deltaP `48.117` edge `1.1026` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.6624` n `78` status `ready` deltaP `61.7655` edge `0.3277` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5114` n `78` status `ready` deltaP `38.3146` edge `0.3326` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `6.0076` n `52` status `ready` deltaP `38.1944` edge `0.246` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.0076` n `52` status `ready` deltaP `38.1944` edge `0.246` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.7106` n `137` status `ready` deltaP `30.8951` edge `0.2391` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.8474` n `52` status `ready` deltaP `44.2575` edge `0.0298` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.8474` n `52` status `ready` deltaP `44.2575` edge `0.0298` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.4504` n `137` status `ready` deltaP `41.0711` edge `0.0353` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.9507` n `52` status `ready` deltaP `25.0703` edge `0.0304` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.9507` n `52` status `ready` deltaP `25.0703` edge `0.0304` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.8505` n `149` status `ready` deltaP `21.5726` edge `0.0522` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.827` n `149` status `ready` deltaP `13.3666` edge `0.0175` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.6829` n `78` status `ready` deltaP `16.9637` edge `0.0373` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2502` n `52` status `ready` deltaP `8.2105` edge `0.0079` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2502` n `52` status `ready` deltaP `8.2105` edge `0.0079` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

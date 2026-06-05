# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T05:37:21.511108+00:00`
- Price records: `672`
- Market context records: `2940`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6940`

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

- `market_context_high->crypto_alt_24h` score `16.3966` n `141` status `ready` deltaP `15.939` edge `1.6518` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.8573` n `141` status `ready` deltaP `18.3067` edge `0.7331` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.8821` n `141` status `ready` deltaP `16.2271` edge `0.5118` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.7773` n `141` status `ready` deltaP `13.8778` edge `0.237` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.9941` n `141` status `ready` deltaP `15.8725` edge `0.3623` maxDD `-12.1553`
- `market_context_high->equity_4h` score `0.8181` n `142` status `ready` deltaP `8.2704` edge `0.151` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.7173` n `142` status `ready` deltaP `14.7308` edge `0.0779` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.1947` n `142` status `ready` deltaP `4.5087` edge `0.0915` maxDD `-3.7602`
- `market_context_high->crypto_alt_4h` score `0.0766` n `142` status `ready` deltaP `16.3775` edge `0.3575` maxDD `-30.8239`
- `market_context_high->index_1h` score `0.0029` n `142` status `ready` deltaP `4.6913` edge `0.0185` maxDD `-1.2855`
- `market_context_high->equity_1h` score `-0.4065` n `142` status `ready` deltaP `0.738` edge `0.0445` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4644` n `142` status `ready` deltaP `5.7392` edge `0.0782` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5371` n `142` status `ready` deltaP `-0.5376` edge `0.0032` maxDD `-0.2164`
- `market_context_high->unknown_1h` score `-0.5519` n `142` status `ready` deltaP `2.8338` edge `0.0082` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.6123` n `142` status `ready` deltaP `5.9163` edge `0.069` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.651` n `142` status `ready` deltaP `0.1771` edge `0.0041` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6763` n `142` status `ready` deltaP `-1.4801` edge `-0.0015` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.965` n `142` status `ready` deltaP `-1.372` edge `0.0066` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2776` n `142` status `ready` deltaP `1.5329` edge `0.018` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.332` n `141` status `ready` deltaP `-1.8765` edge `-0.0113` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

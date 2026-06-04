# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T19:07:23.113453+00:00`
- Price records: `672`
- Market context records: `2894`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6912`

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

- `market_context_high->crypto_alt_24h` score `10.2064` n `142` status `ready` deltaP `9.6465` edge `1.1779` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.5447` n `142` status `ready` deltaP `11.1649` edge `0.588` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.1168` n `142` status `ready` deltaP `10.2406` edge `0.4046` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.191` n `142` status `ready` deltaP `10.2382` edge `0.2124` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.74` n `142` status `ready` deltaP `15.5516` edge `0.3507` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5074` n `142` status `ready` deltaP `13.6057` edge `0.0585` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.3714` n `142` status `ready` deltaP `5.7282` edge `0.0981` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0734` n `142` status `ready` deltaP `3.7489` edge `0.015` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1657` n `142` status `ready` deltaP `4.5538` edge `0.0938` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.2642` n `142` status `ready` deltaP `4.3308` edge `0.0222` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.596` n `142` status `ready` deltaP `-0.5819` edge `0.0028` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.6281` n `142` status `ready` deltaP `-1.5855` edge `0.0026` maxDD `-0.2164`
- `market_context_high->crypto_alt_1h` score `-0.639` n `142` status `ready` deltaP `4.9465` edge `0.0611` maxDD `-10.747`
- `market_context_high->equity_1h` score `-0.7025` n `142` status `ready` deltaP `-1.5518` edge `0.0351` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.7081` n `142` status `ready` deltaP `14.1854` edge `0.2805` maxDD `-28.7261`
- `market_context_high->metal_1h` score `-0.7112` n `142` status `ready` deltaP `-0.9151` edge `-0.0005` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.7346` n `142` status `ready` deltaP `5.1236` edge `0.0586` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0954` n `142` status `ready` deltaP `3.972` edge `0.0251` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2089` n `142` status `ready` deltaP `-4.2103` edge `0.0052` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3471` n `142` status `ready` deltaP `-1.8852` edge `-0.0125` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

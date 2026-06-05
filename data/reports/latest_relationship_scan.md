# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T00:52:21.604964+00:00`
- Price records: `672`
- Market context records: `2920`
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

- `market_context_high->crypto_alt_24h` score `13.6191` n `142` status `ready` deltaP `12.9451` edge `1.4403` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.7162` n `142` status `ready` deltaP `15.1579` edge `0.659` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.0256` n `142` status `ready` deltaP `13.3656` edge `0.4595` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2873` n `142` status `ready` deltaP `10.9326` edge `0.2158` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8276` n `142` status `ready` deltaP `15.5516` edge `0.358` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5447` n `142` status `ready` deltaP `13.4533` edge `0.0643` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.4797` n `142` status `ready` deltaP `7.1453` edge `0.1303` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1019` n `142` status `ready` deltaP `4.2039` edge `0.0858` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0165` n `142` status `ready` deltaP `4.198` edge `0.0193` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0645` n `142` status `ready` deltaP `15.4049` edge `0.326` maxDD `-28.7261`
- `market_context_high->equity_1h` score `-0.344` n `142` status `ready` deltaP `0.8434` edge `0.049` maxDD `-2.6634`
- `market_context_high->unknown_1h` score `-0.3505` n `142` status `ready` deltaP `3.8817` edge `0.018` maxDD `-3.1801`
- `market_context_high->crypto_alt_1h` score `-0.4792` n `142` status `ready` deltaP `5.9944` edge `0.0746` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5395` n `142` status `ready` deltaP `-0.5376` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.5912` n `142` status `ready` deltaP `0.5819` edge `0.0049` maxDD `-3.0996`
- `market_context_high->commodity_1h` score `-0.6124` n `142` status `ready` deltaP `-0.7316` edge `0.0017` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6458` n `142` status `ready` deltaP `5.8721` edge `0.065` maxDD `-9.622`
- `market_context_high->fx_4h` score `-0.9874` n `142` status `ready` deltaP `-1.7713` edge `0.0074` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2646` n `142` status `ready` deltaP `2.1427` edge `0.0156` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2744` n `142` status `ready` deltaP `-1.7116` edge `-0.0076` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

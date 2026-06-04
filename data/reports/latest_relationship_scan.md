# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T17:22:26.928985+00:00`
- Price records: `672`
- Market context records: `2886`
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

- `market_context_high->crypto_alt_24h` score `9.2063` n `142` status `ready` deltaP `8.6048` edge `1.1015` maxDD `-22.6673`
- `market_context_high->equity_24h` score `5.0887` n `142` status `ready` deltaP `9.9496` edge `0.5581` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `4.9524` n `142` status `ready` deltaP `10.2406` edge `0.3909` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2911` n `142` status `ready` deltaP `11.2798` edge `0.2138` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7316` n `142` status `ready` deltaP `15.5516` edge `0.35` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.6378` n `142` status `ready` deltaP `14.6728` edge `0.0681` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.5926` n `142` status `ready` deltaP `6.0331` edge `0.1145` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0298` n `142` status `ready` deltaP `4.3477` edge `0.0166` maxDD `-1.2855`
- `market_context_high->equity_4h` score `-0.1658` n `142` status `ready` deltaP `4.4014` edge `0.0948` maxDD `-5.7037`
- `market_context_high->unknown_1h` score `-0.1982` n `142` status `ready` deltaP `4.3308` edge `0.0277` maxDD `-3.1801`
- `market_context_high->commodity_1h` score `-0.6054` n `142` status `ready` deltaP `-0.7316` edge `0.0026` maxDD `-4.3601`
- `market_context_high->crypto_alt_1h` score `-0.6258` n `142` status `ready` deltaP `5.0962` edge `0.0618` maxDD `-10.747`
- `market_context_high->crypto_alt_4h` score `-0.6333` n `142` status `ready` deltaP `14.4903` edge `0.2847` maxDD `-28.7261`
- `market_context_high->fx_1h` score `-0.6652` n `142` status `ready` deltaP `-2.0346` edge `0.0025` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6699` n `142` status `ready` deltaP `-0.3163` edge `0.0008` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7073` n `142` status `ready` deltaP `-1.5518` edge `0.0347` maxDD `-2.6634`
- `market_context_high->crypto_major_1h` score `-0.7307` n `142` status `ready` deltaP `5.1236` edge `0.0591` maxDD `-9.622`
- `market_context_high->commodity_4h` score `-1.0954` n `142` status `ready` deltaP `3.972` edge `0.0251` maxDD `-10.0279`
- `market_context_high->fx_4h` score `-1.2381` n `142` status `ready` deltaP `-4.5152` edge `0.0048` maxDD `-0.5631`
- `market_context_high->fx_24h` score `-1.3651` n `142` status `ready` deltaP `-1.8852` edge `-0.014` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

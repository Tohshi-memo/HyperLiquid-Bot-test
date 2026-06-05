# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T00:22:20.964269+00:00`
- Price records: `672`
- Market context records: `2918`
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

- `market_context_high->crypto_alt_24h` score `13.3453` n `142` status `ready` deltaP `12.5979` edge `1.4198` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.5924` n `142` status `ready` deltaP `14.8107` edge `0.651` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.9222` n `142` status `ready` deltaP `13.0183` edge `0.4532` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.2295` n `142` status `ready` deltaP `10.5854` edge `0.2133` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8084` n `142` status `ready` deltaP `15.5516` edge `0.3564` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.5094` n `142` status `ready` deltaP `13.1484` edge `0.0618` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.4037` n `142` status `ready` deltaP `6.8404` edge `0.126` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1297` n `142` status `ready` deltaP `4.3563` edge `0.0871` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0266` n `142` status `ready` deltaP `4.198` edge `0.018` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0825` n `142` status `ready` deltaP `15.4049` edge `0.3245` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.3025` n `142` status `ready` deltaP `4.1811` edge `0.02` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.3608` n `142` status `ready` deltaP `0.8434` edge `0.0476` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4637` n `142` status `ready` deltaP `6.1441` edge `0.0756` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5251` n `142` status `ready` deltaP `-0.3879` edge `0.0032` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6208` n `142` status `ready` deltaP `0.2825` edge `0.0031` maxDD `-3.0996`
- `market_context_high->crypto_major_1h` score `-0.6294` n `142` status `ready` deltaP `6.0218` edge `0.0661` maxDD `-9.622`
- `market_context_high->commodity_1h` score `-0.6326` n `142` status `ready` deltaP `-1.031` edge `0.0011` maxDD `-4.3601`
- `market_context_high->fx_4h` score `-0.9728` n `142` status `ready` deltaP `-1.6188` edge `0.0076` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2662` n `142` status `ready` deltaP `2.1427` edge `0.0154` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.272` n `142` status `ready` deltaP `-1.7116` edge `-0.0074` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

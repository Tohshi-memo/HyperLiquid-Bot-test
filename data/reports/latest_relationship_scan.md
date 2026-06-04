# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T23:52:23.122994+00:00`
- Price records: `672`
- Market context records: `2916`
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

- `market_context_high->crypto_alt_24h` score `13.02` n `142` status `ready` deltaP `12.2506` edge `1.395` maxDD `-22.6673`
- `market_context_high->equity_24h` score `6.4926` n `142` status `ready` deltaP `14.4635` edge `0.645` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `5.8093` n `142` status `ready` deltaP `12.6711` edge `0.4461` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.1862` n `142` status `ready` deltaP `10.2382` edge `0.212` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.7952` n `142` status `ready` deltaP `15.5516` edge `0.3553` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.4946` n `142` status `ready` deltaP `13.1484` edge `0.0599` maxDD `-2.3986`
- `market_context_high->equity_4h` score `0.3397` n `142` status `ready` deltaP `6.5355` edge `0.1227` maxDD `-5.7037`
- `market_context_high->unknown_4h` score `0.1515` n `142` status `ready` deltaP `4.5087` edge `0.0879` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0344` n `142` status `ready` deltaP `4.198` edge `0.017` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0993` n `142` status `ready` deltaP `15.4049` edge `0.3231` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.2594` n `142` status `ready` deltaP `4.3308` edge `0.0226` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.3776` n `142` status `ready` deltaP `0.8434` edge `0.0462` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.4644` n `142` status `ready` deltaP `6.1441` edge `0.0755` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5383` n `142` status `ready` deltaP `-0.5376` edge `0.0031` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6233` n `142` status `ready` deltaP `-0.8813` edge `0.0013` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.6287` n `142` status `ready` deltaP `6.0218` edge `0.0662` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.6504` n `142` status `ready` deltaP `-0.0169` edge `0.0013` maxDD `-3.0996`
- `market_context_high->fx_4h` score `-0.9838` n `142` status `ready` deltaP `-1.7713` edge `0.0077` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2464` n `142` status `ready` deltaP `2.4476` edge `0.0159` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.272` n `142` status `ready` deltaP `-1.7116` edge `-0.0074` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

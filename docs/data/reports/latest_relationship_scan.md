# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-03T15:22:37.424847+00:00`
- Price records: `672`
- Market context records: `2776`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9237`

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

- `market_context_high->unknown_24h` score `3.8871` n `138` status `ready` deltaP `7.9937` edge `0.3171` maxDD `-1.7175`
- `market_context_high->crypto_alt_24h` score `2.2886` n `138` status `ready` deltaP `4.4384` edge `0.6555` maxDD `-22.6673`
- `market_context_high->unknown_4h` score `0.953` n `142` status `ready` deltaP `6.338` edge `0.1425` maxDD `-3.7602`
- `market_context_high->commodity_24h` score `0.2648` n `138` status `ready` deltaP `10.16` edge `0.2756` maxDD `-12.4171`
- `market_context_high->index_4h` score `0.1242` n `142` status `ready` deltaP `11.4716` edge `0.0236` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `-0.0457` n `142` status `ready` deltaP `3.8817` edge `0.0434` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.1599` n `142` status `ready` deltaP `3.2998` edge `0.0069` maxDD `-1.2855`
- `market_context_high->fx_1h` score `-0.5862` n `142` status `ready` deltaP `-1.1364` edge `0.0031` maxDD `-0.2164`
- `market_context_high->commodity_1h` score `-0.6` n `142` status `ready` deltaP `0.1666` edge `-0.0027` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.6879` n `142` status `ready` deltaP `-0.0169` edge `-0.0035` maxDD `-3.0996`
- `market_context_high->crypto_alt_1h` score `-0.7069` n `142` status `ready` deltaP `5.0962` edge `0.0514` maxDD `-10.747`
- `market_context_high->crypto_major_1h` score `-0.9256` n `142` status `ready` deltaP `3.926` edge `0.0421` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.1605` n `142` status `ready` deltaP `-3.9054` edge `0.0072` maxDD `-0.5631`
- `market_context_high->equity_1h` score `-1.1617` n `142` status `ready` deltaP `-3.947` edge `0.0128` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-1.3911` n `142` status `ready` deltaP `14.0329` edge `0.2246` maxDD `-28.7261`
- `market_context_high->fx_24h` score `-1.4034` n `138` status `ready` deltaP `-1.3436` edge `-0.0208` maxDD `-0.6418`
- `market_context_high->commodity_4h` score `-1.5517` n `142` status `ready` deltaP `0.161` edge `-0.008` maxDD `-10.0279`
- `market_context_high->equity_4h` score `-1.8453` n `142` status `ready` deltaP `0.1331` edge `-0.0167` maxDD `-5.7037`
- `market_context_high->metal_4h` score `-2.3386` n `142` status `ready` deltaP `-1.9903` edge `-0.0315` maxDD `-11.4038`
- `market_context_high->crypto_major_4h` score `-2.596` n `142` status `ready` deltaP `5.1249` edge `0.1236` maxDD `-32.2466`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-04T11:07:24.571672+00:00`
- Price records: `672`
- Market context records: `2860`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9187`

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

- `market_context_high->crypto_alt_24h` score `4.7899` n `142` status `ready` deltaP `4.2645` edge `0.7624` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `3.5122` n `142` status `ready` deltaP `6.2475` edge `0.2975` maxDD `-1.7175`
- `market_context_high->equity_24h` score `2.0463` n `142` status `ready` deltaP `5.6093` edge `0.3335` maxDD `-12.6963`
- `market_context_high->commodity_24h` score `1.3986` n `142` status `ready` deltaP `14.51` edge `0.3292` maxDD `-12.4171`
- `market_context_high->index_24h` score `1.1745` n `142` status `ready` deltaP `7.8076` edge `0.1439` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `0.8718` n `142` status `ready` deltaP `5.7282` edge `0.1398` maxDD `-3.7602`
- `market_context_high->index_4h` score `0.4517` n `142` status `ready` deltaP `14.0631` edge `0.0483` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0994` n `142` status `ready` deltaP `4.4805` edge `0.0515` maxDD `-3.1801`
- `market_context_high->index_1h` score `-0.0618` n `142` status `ready` deltaP `4.3477` edge `0.0125` maxDD `-1.2855`
- `market_context_high->crypto_alt_1h` score `-0.593` n `142` status `ready` deltaP `5.0962` edge `0.066` maxDD `-10.747`
- `market_context_high->equity_4h` score `-0.599` n `142` status `ready` deltaP `3.4868` edge `0.0648` maxDD `-5.7037`
- `market_context_high->commodity_1h` score `-0.6163` n `142` status `ready` deltaP `-0.5819` edge `0.0002` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.67` n `142` status `ready` deltaP `-2.0346` edge `0.0021` maxDD `-0.2164`
- `market_context_high->crypto_major_1h` score `-0.7635` n `142` status `ready` deltaP `4.6745` edge `0.0579` maxDD `-9.622`
- `market_context_high->metal_1h` score `-0.7713` n `142` status `ready` deltaP `-0.6157` edge `-0.0102` maxDD `-3.0996`
- `market_context_high->equity_1h` score `-0.7996` n `142` status `ready` deltaP `-2.0009` edge `0.03` maxDD `-2.6634`
- `market_context_high->crypto_alt_4h` score `-0.8081` n `142` status `ready` deltaP `13.8805` edge `0.2742` maxDD `-28.7261`
- `market_context_high->fx_4h` score `-1.2393` n `142` status `ready` deltaP `-4.5152` edge `0.0047` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2675` n `142` status `ready` deltaP `2.4476` edge `0.0132` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.3927` n `142` status `ready` deltaP `-1.8852` edge `-0.0163` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

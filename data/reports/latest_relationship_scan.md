# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-21T05:07:17.553072+00:00`
- Price records: `672`
- Market context records: `1392`
- Flow alert records: `5919`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8804`

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

- `market_context_high->crypto_major_24h` score `13.0756` n `157` status `ready` deltaP `28.3539` edge `1.0138` maxDD `-8.0553`
- `market_context_high->crypto_alt_24h` score `11.6123` n `157` status `ready` deltaP `28.8184` edge `0.9772` maxDD `-15.1306`
- `market_context_high->metal_24h` score `11.4089` n `157` status `ready` deltaP `12.0831` edge `1.0369` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.1015` n `157` status `ready` deltaP `19.7286` edge `0.3189` maxDD `-5.3574`
- `market_context_high->equity_24h` score `2.4925` n `157` status `ready` deltaP `12.8992` edge `0.3544` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.5815` n `188` status `ready` deltaP `8.3679` edge `0.159` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.0475` n `157` status `ready` deltaP `9.8803` edge `0.043` maxDD `-1.3925`
- `market_context_high->index_1h` score `0.0274` n `200` status `ready` deltaP `5.024` edge `0.0153` maxDD `-1.7205`
- `market_context_high->equity_1h` score `-0.0364` n `200` status `ready` deltaP `3.3772` edge `0.0303` maxDD `-2.8014`
- `market_context_high->fx_1h` score `-0.3259` n `200` status `ready` deltaP `3.2545` edge `-0.0023` maxDD `-0.3914`
- `market_context_high->metal_4h` score `-0.4484` n `188` status `ready` deltaP `8.7344` edge `0.0475` maxDD `-6.4478`
- `market_context_high->index_4h` score `-0.4789` n `188` status `ready` deltaP `0.853` edge `0.0633` maxDD `-3.7119`
- `market_context_high->metal_1h` score `-0.5519` n `200` status `ready` deltaP `5.4581` edge `0.0007` maxDD `-4.2945`
- `market_context_high->crypto_alt_1h` score `-0.5579` n `200` status `ready` deltaP `1.509` edge `0.0305` maxDD `-3.6309`
- `market_context_high->commodity_1h` score `-0.9424` n `200` status `ready` deltaP `-2.1976` edge `-0.0024` maxDD `-2.252`
- `market_context_high->crypto_alt_4h` score `-1.2013` n `188` status `ready` deltaP `8.3323` edge `0.1763` maxDD `-19.5565`
- `market_context_high->crypto_major_4h` score `-1.2732` n `188` status `ready` deltaP `5.0824` edge `0.1309` maxDD `-13.3376`
- `market_context_high->crypto_major_1h` score `-1.3117` n `200` status `ready` deltaP `-0.7934` edge `0.0025` maxDD `-6.1883`
- `market_context_high->fx_4h` score `-1.6625` n `188` status `ready` deltaP `-4.7223` edge `-0.01` maxDD `-1.4313`
- `market_context_high->commodity_4h` score `-4.5386` n `188` status `ready` deltaP `-13.4471` edge `-0.0339` maxDD `-8.04`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

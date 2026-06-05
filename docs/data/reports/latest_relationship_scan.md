# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-05T02:07:21.078125+00:00`
- Price records: `672`
- Market context records: `2926`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6927`

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

- `market_context_high->crypto_alt_24h` score `14.2502` n `142` status `ready` deltaP `13.8131` edge `1.4871` maxDD `-22.6673`
- `market_context_high->equity_24h` score `7.0292` n `142` status `ready` deltaP `16.026` edge `0.6793` maxDD `-12.6963`
- `market_context_high->unknown_24h` score `6.1736` n `142` status `ready` deltaP `14.06` edge `0.4672` maxDD `-1.7175`
- `market_context_high->index_24h` score `2.4288` n `142` status `ready` deltaP `11.8007` edge `0.2218` maxDD `-2.5127`
- `market_context_high->commodity_24h` score `1.8571` n `142` status `ready` deltaP `15.7252` edge `0.3593` maxDD `-12.4171`
- `market_context_high->equity_4h` score `0.693` n `142` status `ready` deltaP `7.9075` edge `0.143` maxDD `-5.7037`
- `market_context_high->index_4h` score `0.6437` n `142` status `ready` deltaP `14.2155` edge `0.0719` maxDD `-2.3986`
- `market_context_high->unknown_4h` score `0.0511` n `142` status `ready` deltaP `3.899` edge `0.0836` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.0349` n `143` status `ready` deltaP `4.0985` edge `0.0176` maxDD `-1.2855`
- `market_context_high->crypto_alt_4h` score `-0.0651` n `142` status `ready` deltaP `14.9476` edge `0.329` maxDD `-28.7261`
- `market_context_high->unknown_1h` score `-0.4272` n `143` status `ready` deltaP `3.5981` edge `0.0135` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-0.4483` n `143` status `ready` deltaP `0.3047` edge `0.0439` maxDD `-2.6634`
- `market_context_high->crypto_alt_1h` score `-0.5405` n `143` status `ready` deltaP `5.5955` edge `0.0694` maxDD `-10.747`
- `market_context_high->fx_1h` score `-0.5722` n `143` status `ready` deltaP `-0.9463` edge `0.003` maxDD `-0.2164`
- `market_context_high->metal_1h` score `-0.6388` n `143` status `ready` deltaP `0.3967` edge `0.0042` maxDD `-3.4325`
- `market_context_high->commodity_1h` score `-0.6758` n `143` status `ready` deltaP `-1.5451` edge `-0.001` maxDD `-4.3601`
- `market_context_high->crypto_major_1h` score `-0.7224` n `143` status `ready` deltaP `5.1935` edge `0.0597` maxDD `-9.622`
- `market_context_high->fx_4h` score `-1.0116` n `142` status `ready` deltaP `-1.9237` edge `0.0064` maxDD `-0.5631`
- `market_context_high->commodity_4h` score `-1.2615` n `142` status `ready` deltaP `2.1427` edge `0.016` maxDD `-10.0279`
- `market_context_high->fx_24h` score `-1.2864` n `142` status `ready` deltaP `-1.7116` edge `-0.0086` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

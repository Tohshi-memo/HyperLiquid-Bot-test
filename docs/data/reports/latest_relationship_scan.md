# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-02T20:37:34.459089+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4876`

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

- `market_context_high->unknown_1h` score `365.143` n `50` status `ready` deltaP `10.5749` edge `30.363` maxDD `-0.0597`
- `market_context_high->unknown_4h` score `291.9013` n `50` status `ready` deltaP `10.3659` edge `24.256` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `16.3725` n `73` status `ready` deltaP `41.5311` edge `1.1084` maxDD `-1.005`
- `market_context_high->crypto_alt_24h` score `10.0472` n `50` status `ready` deltaP `18.2708` edge `0.8858` maxDD `-11.6271`
- `market_context_high->crypto_major_24h` score `9.0366` n `50` status `ready` deltaP `31.8264` edge `0.6825` maxDD `-9.3299`
- `news_risk_high->equity_24h` score `8.7271` n `73` status `ready` deltaP `31.1905` edge `0.5678` maxDD `-2.8784`
- `market_context_high->crypto_major_4h` score `7.6301` n `50` status `ready` deltaP `18.7622` edge `0.5811` maxDD `-3.294`
- `market_context_high->crypto_alt_4h` score `5.9639` n `50` status `ready` deltaP `16.9512` edge `0.5129` maxDD `-7.6465`
- `news_risk_high->crypto_alt_4h` score `5.7849` n `116` status `ready` deltaP `22.8133` edge `0.4644` maxDD `-6.4195`
- `market_context_high->crypto_alt_1h` score `3.3273` n `50` status `ready` deltaP `15.2515` edge `0.2419` maxDD `-3.6376`
- `market_context_high->crypto_major_1h` score `3.1211` n `50` status `ready` deltaP `14.4491` edge `0.2088` maxDD `-2.2692`
- `market_context_high->fx_4h` score `2.7263` n `50` status `ready` deltaP `30.4024` edge `0.038` maxDD `-0.0791`
- `news_risk_high->equity_4h` score `2.5387` n `116` status `ready` deltaP `22.4033` edge `0.1318` maxDD `-2.9013`
- `news_risk_high->crypto_major_24h` score `1.5386` n `73` status `ready` deltaP `5.9908` edge `0.4727` maxDD `-15.8971`
- `news_risk_high->crypto_major_4h` score `1.529` n `116` status `ready` deltaP `15.4174` edge `0.3242` maxDD `-10.477`
- `market_context_high->equity_24h` score `1.4992` n `50` status `ready` deltaP `7.4097` edge `0.329` maxDD `-11.8957`
- `market_context_high->fx_1h` score `1.4472` n `50` status `ready` deltaP `20.3413` edge `0.0114` maxDD `-0.113`
- `news_risk_high->metal_24h` score `1.3629` n `73` status `ready` deltaP `13.009` edge `0.2154` maxDD `-2.192`
- `news_risk_high->crypto_alt_1h` score `1.1798` n `116` status `ready` deltaP `6.1481` edge `0.1134` maxDD `-2.4854`
- `market_context_high->fx_24h` score `0.8797` n `50` status `ready` deltaP `18.5972` edge `0.0906` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

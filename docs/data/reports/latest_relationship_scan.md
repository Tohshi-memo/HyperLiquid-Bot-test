# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T13:22:33.519257+00:00`
- Price records: `672`
- Market context records: `5147`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5596`

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

- `market_context_high->unknown_24h` score `27.4039` n `66` status `ready` deltaP `32.5758` edge `2.1006` maxDD `-1.3955`
- `market_context_high->unknown_4h` score `6.4663` n `128` status `ready` deltaP `18.8072` edge `0.5157` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `5.6407` n `140` status `ready` deltaP `10.231` edge `0.466` maxDD `-2.7986`
- `market_context_high->crypto_alt_4h` score `5.2575` n `128` status `ready` deltaP `16.5968` edge `0.4874` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0849` n `128` status `ready` deltaP `14.5579` edge `0.4726` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `2.1911` n `66` status `ready` deltaP `17.9292` edge `0.6774` maxDD `-36.6143`
- `market_context_high->crypto_major_24h` score `1.8006` n `66` status `ready` deltaP `16.3352` edge `0.678` maxDD `-37.8178`
- `market_context_high->commodity_24h` score `1.4998` n `66` status `ready` deltaP `17.4242` edge `0.1321` maxDD `-5.1955`
- `market_context_high->equity_4h` score `1.2559` n `128` status `ready` deltaP `11.7188` edge `0.1904` maxDD `-7.4425`
- `market_context_high->crypto_major_1h` score `0.8839` n `140` status `ready` deltaP `8.2806` edge `0.143` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.861` n `140` status `ready` deltaP `5.8511` edge `0.1289` maxDD `-5.0257`
- `market_context_high->equity_1h` score `0.6155` n `140` status `ready` deltaP `7.0958` edge `0.0633` maxDD `-2.745`
- `market_context_high->metal_24h` score `0.3215` n `66` status `ready` deltaP `-0.7892` edge `0.2018` maxDD `-7.4254`
- `market_context_high->metal_1h` score `-0.0016` n `140` status `ready` deltaP `5.7699` edge `0.0179` maxDD `-1.8592`
- `market_context_high->index_1h` score `-0.1417` n `140` status `ready` deltaP `3.7896` edge `0.0133` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.3742` n `128` status `ready` deltaP `6.593` edge `0.0366` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.3832` n `66` status `ready` deltaP `5.4451` edge `0.0041` maxDD `-0.8294`
- `market_context_high->fx_1h` score `-0.4111` n `140` status `ready` deltaP `0.4491` edge `-0.0006` maxDD `-0.7412`
- `market_context_high->commodity_1h` score `-0.6591` n `140` status `ready` deltaP `-0.3807` edge `-0.0011` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7593` n `128` status `ready` deltaP `0.686` edge `0.0033` maxDD `-1.7512`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

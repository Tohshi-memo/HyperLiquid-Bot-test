# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T00:22:28.547026+00:00`
- Price records: `672`
- Market context records: `4775`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `7510`

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

- `market_context_high->unknown_1h` score `8.1145` n `122` status `ready` deltaP `12.4301` edge `0.6351` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3643` n `122` status `ready` deltaP `17.1956` edge `0.6201` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.838` n `107` status `ready` deltaP `11.52` edge `0.1687` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1655` n `122` status `ready` deltaP `12.425` edge `0.0556` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1142` n `122` status `ready` deltaP `5.3818` edge `0.0324` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4028` n `122` status `ready` deltaP `3.5836` edge `0.0021` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5463` n `122` status `ready` deltaP `5.1655` edge `0.0024` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.6416` n `122` status `ready` deltaP `5.7952` edge `0.0477` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8597` n `122` status `ready` deltaP `-0.5841` edge `-0.0028` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-1.0233` n `122` status `ready` deltaP `0.0712` edge `-0.009` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.5214` n `122` status `ready` deltaP `-2.6946` edge `-0.0084` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0316` n `107` status `ready` deltaP `21.1383` edge `0.1095` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3156` n `122` status `ready` deltaP `-1.3964` edge `-0.07` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2527` n `107` status `ready` deltaP `-14.2053` edge `-0.0214` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3594` n `122` status `ready` deltaP `-0.1497` edge `-0.055` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.7286` n `122` status `ready` deltaP `-0.5129` edge `-0.0816` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.2149` n `122` status `ready` deltaP `3.0688` edge `-0.0466` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.669` n `107` status `ready` deltaP `-5.1029` edge `-0.105` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5387` n `122` status `ready` deltaP `1.8293` edge `-0.1838` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6587` n `122` status `ready` deltaP `3.9434` edge `-0.3123` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

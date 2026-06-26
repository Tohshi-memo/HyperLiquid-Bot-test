# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T00:37:26.065203+00:00`
- Price records: `672`
- Market context records: `4776`
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

- `market_context_high->unknown_1h` score `8.1397` n `122` status `ready` deltaP `12.4301` edge `0.6372` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3571` n `122` status `ready` deltaP `17.1956` edge `0.6195` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8356` n `107` status `ready` deltaP `11.52` edge `0.1685` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1663` n `122` status `ready` deltaP `12.425` edge `0.0557` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.1142` n `122` status `ready` deltaP `5.3818` edge `0.0324` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4115` n `122` status `ready` deltaP `3.4311` edge `0.002` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5361` n `122` status `ready` deltaP `5.3179` edge `0.0027` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.6188` n `122` status `ready` deltaP `5.9476` edge `0.0496` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8609` n `122` status `ready` deltaP `-0.5841` edge `-0.0029` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.9909` n `122` status `ready` deltaP `0.2209` edge `-0.0073` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.5046` n `122` status `ready` deltaP `-2.5449` edge `-0.008` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.0507` n `107` status `ready` deltaP `20.9647` edge `0.1082` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3039` n `122` status `ready` deltaP `-1.2467` edge `-0.0695` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.2678` n `107` status `ready` deltaP `-14.3789` edge `-0.0215` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3246` n `122` status `ready` deltaP `0.0` edge `-0.0531` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.6902` n `122` status `ready` deltaP `-0.3632` edge `-0.0794` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.2056` n `122` status `ready` deltaP `3.0688` edge `-0.0454` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.669` n `107` status `ready` deltaP `-5.1029` edge `-0.105` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5285` n `122` status `ready` deltaP `1.8293` edge `-0.1825` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6445` n `122` status `ready` deltaP `4.0959` edge `-0.3115` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

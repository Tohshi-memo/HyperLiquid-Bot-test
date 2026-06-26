# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T01:37:32.641447+00:00`
- Price records: `672`
- Market context records: `4780`
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

- `market_context_high->unknown_1h` score `8.2572` n `122` status `ready` deltaP `12.8792` edge `0.644` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.4185` n `122` status `ready` deltaP `17.3481` edge `0.6236` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.88` n `107` status `ready` deltaP `11.52` edge `0.1722` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1167` n `122` status `ready` deltaP `11.8153` edge `0.0534` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0842` n `122` status `ready` deltaP `5.0824` edge `0.0319` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4456` n `122` status `ready` deltaP `2.8214` edge `0.0017` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.5227` n `122` status `ready` deltaP `5.4704` edge `0.0034` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5341` n `122` status `ready` deltaP `6.5574` edge `0.0564` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8873` n `122` status `ready` deltaP `-0.8835` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.9178` n `122` status `ready` deltaP `0.67` edge `-0.0042` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4746` n `122` status `ready` deltaP `-2.2455` edge `-0.0075` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.1313` n `107` status `ready` deltaP `20.2703` edge `0.1025` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3039` n `122` status `ready` deltaP `-1.2467` edge `-0.0695` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.3138` n `122` status `ready` deltaP `0.0` edge `-0.0522` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.3318` n `107` status `ready` deltaP `-15.0734` edge `-0.0222` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.641` n `122` status `ready` deltaP `-0.2135` edge `-0.0763` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.1766` n `122` status `ready` deltaP `3.2212` edge `-0.0427` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6834` n `107` status `ready` deltaP `-5.1029` edge `-0.1062` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.4855` n `122` status `ready` deltaP `1.9817` edge `-0.178` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.5964` n `122` status `ready` deltaP `4.7056` edge `-0.3094` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

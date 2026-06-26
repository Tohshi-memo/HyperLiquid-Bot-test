# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T01:22:39.542744+00:00`
- Price records: `672`
- Market context records: `4779`
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

- `market_context_high->unknown_1h` score `8.2261` n `122` status `ready` deltaP `12.7295` edge `0.6424` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.3811` n `122` status `ready` deltaP `17.1956` edge `0.6215` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.8692` n `107` status `ready` deltaP `11.52` edge `0.1713` maxDD `-4.7201`
- `market_context_high->commodity_4h` score `0.1316` n `122` status `ready` deltaP `11.9677` edge `0.0543` maxDD `-4.377`
- `market_context_high->commodity_1h` score `0.0866` n `122` status `ready` deltaP `5.0824` edge `0.0321` maxDD `-2.0345`
- `market_context_high->fx_4h` score `-0.4369` n `122` status `ready` deltaP `2.9738` edge `0.0018` maxDD `-1.5439`
- `market_context_high->index_4h` score `-0.533` n `122` status `ready` deltaP `5.3179` edge `0.0031` maxDD `-5.5505`
- `market_context_high->equity_4h` score `-0.5584` n `122` status `ready` deltaP `6.405` edge `0.0543` maxDD `-8.8203`
- `market_context_high->fx_1h` score `-0.8741` n `122` status `ready` deltaP `-0.7338` edge `-0.003` maxDD `-0.8626`
- `market_context_high->equity_1h` score `-0.9369` n `122` status `ready` deltaP `0.5203` edge `-0.0048` maxDD `-4.1397`
- `market_context_high->index_1h` score `-1.4914` n `122` status `ready` deltaP `-2.3952` edge `-0.0079` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.109` n `107` status `ready` deltaP `20.4439` edge `0.1042` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.3125` n `122` status `ready` deltaP `-1.3964` edge `-0.0696` maxDD `-14.0715`
- `market_context_high->fx_24h` score `-3.3155` n `107` status `ready` deltaP `-14.8998` edge `-0.022` maxDD `-3.3968`
- `market_context_high->crypto_alt_1h` score `-3.3222` n `122` status `ready` deltaP `0.0` edge `-0.0529` maxDD `-15.2495`
- `market_context_high->crypto_major_1h` score `-4.6566` n `122` status `ready` deltaP `-0.2135` edge `-0.0776` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-5.1993` n `122` status `ready` deltaP `3.0688` edge `-0.0446` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6822` n `107` status `ready` deltaP `-5.1029` edge `-0.1061` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.5129` n `122` status `ready` deltaP `1.8293` edge `-0.1805` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.6106` n `122` status `ready` deltaP `4.5532` edge `-0.3102` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-07T07:22:28.023873+00:00`
- Price records: `672`
- Market context records: `5958`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11184`

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

- `news_risk_high->fx_24h` score `6.9692` n `30` status `ready` deltaP `63.7153` edge `0.156` maxDD `0.0`
- `news_risk_high->commodity_24h` score `5.368` n `30` status `ready` deltaP `38.5764` edge `0.2107` maxDD `-0.3101`
- `news_risk_high->fx_4h` score `3.8576` n `30` status `ready` deltaP `40.0` edge `0.0594` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.1076` n `30` status `ready` deltaP `25.4291` edge `0.02` maxDD `-0.1113`
- `market_context_high->equity_4h` score `1.4494` n `227` status `ready` deltaP `9.3035` edge `0.1682` maxDD `-4.0887`
- `news_risk_high->crypto_major_1h` score `0.8403` n `30` status `ready` deltaP `10.1896` edge `0.0865` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.2075` n `30` status `ready` deltaP `5.3194` edge `0.0373` maxDD `-1.6923`
- `news_risk_high->index_24h` score `-0.1757` n `30` status `ready` deltaP `6.9791` edge `0.0181` maxDD `-2.3058`
- `market_context_high->equity_1h` score `-0.3262` n `239` status `ready` deltaP `5.0729` edge `0.0372` maxDD `-4.3608`
- `news_risk_high->metal_1h` score `-0.3534` n `30` status `ready` deltaP `2.4351` edge `-0.0249` maxDD `-1.2643`
- `market_context_high->metal_1h` score `-0.4629` n `239` status `ready` deltaP `2.6583` edge `0.0028` maxDD `-2.0564`
- `market_context_high->equity_24h` score `-0.497` n `213` status `ready` deltaP `20.7893` edge `0.3053` maxDD `-31.2762`
- `market_context_high->commodity_1h` score `-0.5799` n `239` status `ready` deltaP `-2.689` edge `-0.0007` maxDD `-1.4578`
- `market_context_high->index_1h` score `-0.6207` n `239` status `ready` deltaP `1.0153` edge `0.005` maxDD `-1.3078`
- `market_context_high->fx_1h` score `-0.6346` n `239` status `ready` deltaP `-0.2055` edge `-0.0004` maxDD `-0.756`
- `market_context_high->crypto_major_1h` score `-1.083` n `239` status `ready` deltaP `2.0864` edge `0.024` maxDD `-9.807`
- `market_context_high->crypto_alt_1h` score `-1.0938` n `239` status `ready` deltaP `2.2092` edge `0.0203` maxDD `-9.3536`
- `news_risk_high->index_1h` score `-1.1085` n `30` status `ready` deltaP `-10.4491` edge `-0.021` maxDD `-1.1161`
- `market_context_high->metal_4h` score `-1.5721` n `227` status `ready` deltaP `-1.9978` edge `-0.025` maxDD `-5.725`
- `market_context_high->commodity_4h` score `-1.592` n `227` status `ready` deltaP `-2.9501` edge `-0.0131` maxDD `-6.3734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-26T03:07:26.293400+00:00`
- Price records: `672`
- Market context records: `4787`
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

- `market_context_high->unknown_1h` score `8.0844` n `122` status `ready` deltaP `12.8792` edge `0.6296` maxDD `-1.674`
- `market_context_high->unknown_4h` score `7.6429` n `122` status `ready` deltaP `18.2627` edge `0.6362` maxDD `-4.6834`
- `market_context_high->unknown_24h` score `1.964` n `107` status `ready` deltaP `11.52` edge `0.1792` maxDD `-4.7201`
- `market_context_high->commodity_1h` score `0.1309` n `122` status `ready` deltaP `5.5315` edge `0.0328` maxDD `-2.0345`
- `market_context_high->commodity_4h` score `0.0823` n `122` status `ready` deltaP `11.8153` edge `0.049` maxDD `-4.377`
- `market_context_high->equity_4h` score `-0.3305` n `122` status `ready` deltaP `7.472` edge `0.0764` maxDD `-8.8203`
- `market_context_high->index_4h` score `-0.448` n `122` status `ready` deltaP `6.2325` edge `0.0079` maxDD `-5.5505`
- `market_context_high->fx_4h` score `-0.4614` n `122` status `ready` deltaP `2.5165` edge `0.0017` maxDD `-1.5439`
- `market_context_high->equity_1h` score `-0.7738` n `122` status `ready` deltaP `1.1191` edge `0.0048` maxDD `-4.1397`
- `market_context_high->fx_1h` score `-0.8992` n `122` status `ready` deltaP `-1.0332` edge `-0.0031` maxDD `-0.8626`
- `market_context_high->index_1h` score `-1.4219` n `122` status `ready` deltaP `-1.7964` edge `-0.0061` maxDD `-2.6999`
- `market_context_high->commodity_24h` score `-2.2424` n `107` status `ready` deltaP `19.2286` edge `0.0952` maxDD `-27.5371`
- `market_context_high->metal_1h` score `-2.272` n `122` status `ready` deltaP `-0.9473` edge `-0.0674` maxDD `-14.0715`
- `market_context_high->crypto_alt_1h` score `-3.0728` n `122` status `ready` deltaP `0.8982` edge `-0.0381` maxDD `-15.2495`
- `market_context_high->fx_24h` score `-3.4223` n `107` status `ready` deltaP `-16.115` edge `-0.0228` maxDD `-3.3968`
- `market_context_high->crypto_major_1h` score `-4.4035` n `122` status `ready` deltaP `0.6847` edge `-0.0625` maxDD `-22.0555`
- `market_context_high->crypto_alt_4h` score `-4.92` n `122` status `ready` deltaP `4.1358` edge `-0.0159` maxDD `-46.0617`
- `market_context_high->index_24h` score `-5.6594` n `107` status `ready` deltaP `-5.1029` edge `-0.1042` maxDD `-18.6716`
- `market_context_high->crypto_major_4h` score `-8.2258` n `122` status `ready` deltaP `2.8963` edge `-0.1508` maxDD `-68.5143`
- `market_context_high->metal_4h` score `-8.4576` n `122` status `ready` deltaP `5.6203` edge `-0.2977` maxDD `-61.2596`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T13:37:22.221807+00:00`
- Price records: `672`
- Market context records: `3078`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6893`

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

- `market_context_high->crypto_alt_24h` score `17.3335` n `88` status `ready` deltaP `11.8529` edge `2.5349` maxDD `-22.6673`
- `market_context_high->commodity_24h` score `15.3386` n `88` status `ready` deltaP `48.0429` edge `0.982` maxDD `-1.2589`
- `market_context_high->unknown_24h` score `13.9777` n `88` status `ready` deltaP `23.2165` edge `1.0565` maxDD `-1.7175`
- `market_context_high->index_24h` score `13.1619` n `88` status `ready` deltaP `32.6705` edge `0.9629` maxDD `-4.7103`
- `market_context_high->equity_24h` score `11.4491` n `88` status `ready` deltaP `25.1894` edge `1.5751` maxDD `-18.3486`
- `market_context_high->commodity_4h` score `2.6221` n `125` status `ready` deltaP `16.5122` edge `0.156` maxDD `-2.1389`
- `market_context_high->unknown_4h` score `-0.1591` n `125` status `ready` deltaP `3.0268` edge `0.0719` maxDD `-3.7602`
- `market_context_high->commodity_1h` score `-0.3518` n `125` status `ready` deltaP `-1.1485` edge `0.0206` maxDD `-1.7142`
- `market_context_high->index_1h` score `-0.6597` n `125` status `ready` deltaP `1.5461` edge `0.0114` maxDD `-4.5023`
- `market_context_high->fx_24h` score `-0.7442` n `88` status `ready` deltaP `-0.6787` edge `-0.0037` maxDD `-0.6418`
- `market_context_high->crypto_alt_1h` score `-0.7765` n `125` status `ready` deltaP `3.497` edge `0.0901` maxDD `-14.7034`
- `market_context_high->fx_1h` score `-1.0486` n `125` status `ready` deltaP `-7.2024` edge `-0.0021` maxDD `-0.3147`
- `market_context_high->unknown_1h` score `-1.0767` n `125` status `ready` deltaP `1.3593` edge `-0.0257` maxDD `-3.1801`
- `market_context_high->equity_1h` score `-1.1783` n `125` status `ready` deltaP `-0.8491` edge `0.0` maxDD `-8.6319`
- `market_context_high->fx_4h` score `-1.3345` n `125` status `ready` deltaP `-12.0939` edge `-0.0061` maxDD `-1.0829`
- `market_context_high->index_4h` score `-1.4319` n `125` status `ready` deltaP `8.5537` edge `0.0503` maxDD `-17.6057`
- `market_context_high->crypto_major_1h` score `-1.8455` n `125` status `ready` deltaP `0.8395` edge `0.0669` maxDD `-15.1032`
- `market_context_high->metal_1h` score `-2.2095` n `125` status `ready` deltaP `-5.9581` edge `-0.0076` maxDD `-7.278`
- `market_context_high->crypto_alt_4h` score `-3.0109` n `125` status `ready` deltaP `18.3098` edge `0.2964` maxDD `-58.6918`
- `market_context_high->equity_4h` score `-3.7633` n `125` status `ready` deltaP `6.7622` edge `-0.0037` maxDD `-36.242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T08:01:12.875157+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5964`

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

- `market_context_high->unknown_4h` score `42.5703` n `85` status `ready` deltaP `-12.9484` edge `3.6919` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5558` n `69` status `ready` deltaP `37.6509` edge `0.5882` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.3336` n `69` status `ready` deltaP `11.3149` edge `1.1796` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.7036` n `85` status `ready` deltaP `23.75` edge `0.012` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.4221` n `69` status `ready` deltaP `13.1793` edge `0.1059` maxDD `-1.5052`
- `market_context_high->fx_1h` score `0.2103` n `97` status `ready` deltaP `7.3477` edge `0.0022` maxDD `-0.271`
- `market_context_high->commodity_4h` score `-0.1001` n `85` status `ready` deltaP `5.1453` edge `0.0062` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.193` n `97` status `ready` deltaP `1.6282` edge `0.0065` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.3689` n `97` status `ready` deltaP `1.3797` edge `0.0324` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-0.4066` n `85` status `ready` deltaP `3.4845` edge `0.127` maxDD `-10.5224`
- `market_context_high->metal_1h` score `-0.5208` n `97` status `ready` deltaP `-1.2809` edge `0.0013` maxDD `-0.7626`
- `market_context_high->fx_24h` score `-0.8553` n `69` status `ready` deltaP `3.9704` edge `0.0052` maxDD `-1.6396`
- `market_context_high->metal_24h` score `-0.8785` n `69` status `ready` deltaP `-1.8192` edge `0.048` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.9205` n `97` status `ready` deltaP `-3.5095` edge `0.0213` maxDD `-4.9401`
- `market_context_high->index_4h` score `-1.3147` n `85` status `ready` deltaP `-11.3289` edge `0.0002` maxDD `-1.1242`
- `market_context_high->index_1h` score `-1.64` n `97` status `ready` deltaP `-7.1501` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->crypto_alt_24h` score `-1.7304` n `69` status `ready` deltaP `-2.7627` edge `0.4078` maxDD `-35.5652`
- `market_context_high->equity_1h` score `-1.7686` n `97` status `ready` deltaP `-7.9835` edge `-0.0072` maxDD `-2.2898`
- `market_context_high->metal_4h` score `-2.0196` n `85` status `ready` deltaP `-12.7242` edge `0.0138` maxDD `-1.1153`
- `market_context_high->equity_4h` score `-2.8145` n `85` status `ready` deltaP `-10.2152` edge `-0.0072` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T07:52:25.091772+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5984`

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

- `market_context_high->unknown_4h` score `42.5499` n `85` status `ready` deltaP `-12.9484` edge `3.6902` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.5647` n `70` status `ready` deltaP `37.8373` edge `0.5877` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `7.4111` n `70` status `ready` deltaP `11.8453` edge `1.186` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.7036` n `85` status `ready` deltaP `23.75` edge `0.012` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.3357` n `70` status `ready` deltaP `12.5248` edge `0.1042` maxDD `-1.5728`
- `market_context_high->fx_1h` score `0.2103` n `97` status `ready` deltaP `7.3477` edge `0.0022` maxDD `-0.271`
- `market_context_high->commodity_4h` score `-0.1557` n `85` status `ready` deltaP `4.1212` edge `0.0059` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `-0.193` n `97` status `ready` deltaP `1.6282` edge `0.0065` maxDD `-0.3417`
- `market_context_high->crypto_major_1h` score `-0.3059` n `97` status `ready` deltaP `2.2609` edge `0.0346` maxDD `-3.7778`
- `market_context_high->crypto_major_4h` score `-0.3879` n `85` status `ready` deltaP `3.4845` edge `0.1294` maxDD `-10.5224`
- `market_context_high->metal_1h` score `-0.5666` n `97` status `ready` deltaP `-2.1622` edge `0.0013` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.8445` n `70` status `ready` deltaP `-1.136` edge `0.0478` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.9119` n `97` status `ready` deltaP `-3.5095` edge `0.0224` maxDD `-4.9401`
- `market_context_high->fx_24h` score `-0.9387` n `70` status `ready` deltaP `3.2043` edge `0.0045` maxDD `-1.6968`
- `market_context_high->index_4h` score `-1.3695` n `85` status `ready` deltaP `-12.3529` edge `0.0` maxDD `-1.1242`
- `market_context_high->crypto_alt_24h` score `-1.6398` n `70` status `ready` deltaP `-1.9346` edge `0.4139` maxDD `-35.5652`
- `market_context_high->index_1h` score `-1.64` n `97` status `ready` deltaP `-7.1501` edge `-0.0028` maxDD `-0.5627`
- `market_context_high->equity_1h` score `-1.7662` n `97` status `ready` deltaP `-7.9835` edge `-0.007` maxDD `-2.2898`
- `market_context_high->metal_4h` score `-2.1552` n `85` status `ready` deltaP `-13.7483` edge `0.0135` maxDD `-1.1153`
- `market_context_high->equity_4h` score `-2.9024` n `85` status `ready` deltaP `-11.2392` edge `-0.0077` maxDD `-6.4057`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

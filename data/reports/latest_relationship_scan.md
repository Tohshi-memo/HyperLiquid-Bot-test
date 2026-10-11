# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T09:22:30.292395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `6933`

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

- `market_context_high->unknown_4h` score `42.6579` n `85` status `ready` deltaP `-12.9484` edge `3.6992` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.4323` n `64` status `ready` deltaP `36.6319` edge `0.5847` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `6.7605` n `64` status `ready` deltaP `8.3333` edge `1.126` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.3675` n `85` status `ready` deltaP `19.6539` edge `0.0113` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.8691` n `64` status `ready` deltaP `17.0139` edge `0.1138` maxDD `-1.2639`
- `market_context_high->commodity_4h` score `0.1977` n `85` status `ready` deltaP `9.2414` edge `0.0082` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.1843` n `96` status `ready` deltaP `4.884` edge `0.0079` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0581` n `96` status `ready` deltaP `4.4349` edge `0.0021` maxDD `-0.271`
- `market_context_high->crypto_major_1h` score `-0.3544` n `96` status `ready` deltaP `1.7777` edge `0.0316` maxDD `-3.7778`
- `market_context_high->fx_24h` score `-0.4031` n `64` status `ready` deltaP `7.9861` edge `0.0106` maxDD `-1.2415`
- `market_context_high->crypto_major_4h` score `-0.8271` n `85` status `ready` deltaP `-0.6115` edge `0.1011` maxDD `-10.5785`
- `market_context_high->metal_4h` score `-0.877` n `85` status `ready` deltaP `-7.604` edge `0.0147` maxDD `-1.1153`
- `market_context_high->metal_1h` score `-0.9019` n `96` status `ready` deltaP `-2.5387` edge `0.0013` maxDD `-0.7626`
- `market_context_high->crypto_alt_1h` score `-1.0028` n `96` status `ready` deltaP `-4.9276` edge `0.0202` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.1102` n `64` status `ready` deltaP `-5.5556` edge `0.0432` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.3147` n `85` status `ready` deltaP `-11.3289` edge `0.0002` maxDD `-1.1242`
- `market_context_high->equity_1h` score `-1.4415` n `96` status `ready` deltaP `-4.0606` edge `-0.0061` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.472` n `96` status `ready` deltaP `-5.0649` edge `-0.0027` maxDD `-0.5627`
- `market_context_high->crypto_alt_24h` score `-2.4004` n `64` status `ready` deltaP `-7.2917` edge `0.3521` maxDD `-35.5652`
- `market_context_high->crypto_alt_4h` score `-2.4169` n `85` status `ready` deltaP `-12.482` edge `0.0292` maxDD `-13.8008`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

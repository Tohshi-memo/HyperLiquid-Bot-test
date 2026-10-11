# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T09:37:32.361369+00:00`
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

- `market_context_high->unknown_4h` score `42.5715` n `85` status `ready` deltaP `-12.9484` edge `3.692` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.3964` n `63` status `ready` deltaP `36.4087` edge `0.5832` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `6.5884` n `63` status `ready` deltaP `7.6636` edge `1.1084` maxDD `-17.8526`
- `market_context_high->fx_4h` score `1.3639` n `85` status `ready` deltaP `19.6539` edge `0.011` maxDD `-0.2692`
- `market_context_high->index_24h` score `0.9654` n `63` status `ready` deltaP `18.006` edge `0.1151` maxDD `-1.2426`
- `market_context_high->commodity_4h` score `0.288` n `85` status `ready` deltaP `10.2655` edge `0.0089` maxDD `-1.6002`
- `market_context_high->commodity_1h` score `0.2271` n `95` status `ready` deltaP `5.3593` edge `0.0083` maxDD `-0.3417`
- `market_context_high->fx_1h` score `0.0358` n `95` status `ready` deltaP `4.0073` edge `0.0021` maxDD `-0.271`
- `market_context_high->fx_24h` score `-0.3058` n `63` status `ready` deltaP `8.9038` edge `0.0118` maxDD `-1.1625`
- `market_context_high->crypto_major_1h` score `-0.3816` n `95` status `ready` deltaP `1.434` edge `0.0304` maxDD `-3.7778`
- `market_context_high->metal_4h` score `-0.7897` n `85` status `ready` deltaP `-6.58` edge `0.0149` maxDD `-1.1153`
- `market_context_high->crypto_major_4h` score `-0.9118` n `85` status `ready` deltaP `-1.6356` edge `0.0978` maxDD `-10.6368`
- `market_context_high->metal_1h` score `-0.9329` n `95` status `ready` deltaP `-2.9262` edge `0.0013` maxDD `-0.7626`
- `market_context_high->crypto_alt_1h` score `-1.0251` n `95` status `ready` deltaP `-5.3262` edge `0.02` maxDD `-4.9401`
- `market_context_high->metal_24h` score `-1.1692` n `63` status `ready` deltaP `-6.3741` edge `0.0411` maxDD `-3.5466`
- `market_context_high->index_4h` score `-1.3139` n `85` status `ready` deltaP `-11.3289` edge `0.0003` maxDD `-1.1242`
- `market_context_high->equity_1h` score `-1.4088` n `95` status `ready` deltaP `-3.6511` edge `-0.0061` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.4442` n `95` status `ready` deltaP `-4.7321` edge `-0.0026` maxDD `-0.5627`
- `market_context_high->crypto_alt_4h` score `-2.3098` n `85` status `ready` deltaP `-11.4581` edge `0.0361` maxDD `-13.8008`
- `market_context_high->crypto_alt_24h` score `-2.5955` n `63` status `ready` deltaP `-8.2838` edge `0.3337` maxDD `-35.5652`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

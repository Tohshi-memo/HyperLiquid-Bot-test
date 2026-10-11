# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T04:22:25.600695+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5927`

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

- `market_context_high->unknown_4h` score `43.7058` n `85` status `ready` deltaP `-6.8041` edge `3.7414` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.8524` n `84` status `ready` deltaP `38.4176` edge `0.6078` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.8576` n `84` status `ready` deltaP `18.378` edge `1.3279` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.4039` n `85` status `ready` deltaP `16.797` edge `0.2062` maxDD `-7.3883`
- `market_context_high->fx_4h` score `0.3653` n `85` status `ready` deltaP `12.4856` edge `0.0089` maxDD `-0.2692`
- `market_context_high->fx_1h` score `0.2033` n `97` status `ready` deltaP `7.3477` edge `0.0013` maxDD `-0.271`
- `market_context_high->crypto_alt_24h` score `0.0865` n `84` status `ready` deltaP `6.5724` edge `0.5785` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.0539` n `97` status `ready` deltaP `8.4295` edge `0.0396` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.1845` n `97` status `ready` deltaP `0.747` edge `0.0048` maxDD `-0.3417`
- `market_context_high->index_24h` score `-0.3976` n `84` status `ready` deltaP `7.2421` edge `0.0917` maxDD `-1.9432`
- `market_context_high->commodity_4h` score `-0.402` n `85` status `ready` deltaP `1.0491` edge `-0.0052` maxDD `-1.6002`
- `market_context_high->metal_1h` score `-0.4116` n `97` status `ready` deltaP `-0.3997` edge `0.0011` maxDD `-0.7626`
- `market_context_high->metal_24h` score `-0.4683` n `84` status `ready` deltaP `5.6796` edge `0.0506` maxDD `-3.5466`
- `market_context_high->crypto_alt_1h` score `-0.8783` n `97` status `ready` deltaP `-1.747` edge `0.014` maxDD `-4.863`
- `market_context_high->metal_4h` score `-1.1786` n `85` status `ready` deltaP `-9.6521` edge `0.014` maxDD `-1.0609`
- `market_context_high->equity_4h` score `-1.3972` n `85` status `ready` deltaP `-5.0951` edge `0.003` maxDD `-5.5198`
- `market_context_high->crypto_alt_4h` score `-1.4591` n `85` status `ready` deltaP `-9.41` edge `0.0792` maxDD `-9.6159`
- `market_context_high->equity_1h` score `-1.4734` n `97` status `ready` deltaP `-4.4586` edge `-0.0061` maxDD `-2.2898`
- `market_context_high->index_1h` score `-1.7846` n `97` status `ready` deltaP `-8.9126` edge `-0.0031` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.931` n `85` status `ready` deltaP `-10.3049` edge `0.001` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

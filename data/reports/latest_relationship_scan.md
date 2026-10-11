# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-11T04:07:33.577404+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `5751`

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

- `market_context_high->unknown_4h` score `43.7502` n `85` status `ready` deltaP `-6.8041` edge `3.7451` maxDD `-2.3109`
- `market_context_high->equity_24h` score `9.8978` n `85` status `ready` deltaP `38.3701` edge `0.6119` maxDD `-1.0977`
- `market_context_high->crypto_major_24h` score `8.9631` n `85` status `ready` deltaP `18.6806` edge `1.3394` maxDD `-17.8526`
- `market_context_high->crypto_major_4h` score `1.5473` n `85` status `ready` deltaP `17.821` edge `0.2126` maxDD `-6.9761`
- `market_context_high->fx_1h` score `0.314` n `97` status `ready` deltaP `7.3477` edge `0.0014` maxDD `-0.271`
- `market_context_high->fx_4h` score `0.229` n `85` status `ready` deltaP `11.4617` edge `0.0087` maxDD `-0.2825`
- `market_context_high->crypto_alt_24h` score `0.2247` n `85` status `ready` deltaP `7.1466` edge `0.5924` maxDD `-35.5652`
- `market_context_high->crypto_major_1h` score `0.0625` n `97` status `ready` deltaP `8.4295` edge `0.0407` maxDD `-3.7778`
- `market_context_high->commodity_1h` score `-0.217` n `97` status `ready` deltaP `0.747` edge `0.0048` maxDD `-0.3417`
- `market_context_high->metal_1h` score `-0.3657` n `97` status `ready` deltaP `0.4815` edge `0.0011` maxDD `-0.7626`
- `market_context_high->index_24h` score `-0.3783` n `85` status `ready` deltaP `7.6287` edge `0.0916` maxDD `-1.9432`
- `market_context_high->metal_24h` score `-0.44` n `85` status `ready` deltaP `5.9682` edge `0.0523` maxDD `-3.5466`
- `market_context_high->commodity_4h` score `-0.4662` n `85` status `ready` deltaP `0.0251` edge `-0.0066` maxDD `-1.6002`
- `market_context_high->crypto_alt_1h` score `-0.8058` n `97` status `ready` deltaP `-0.8658` edge `0.0163` maxDD `-4.7735`
- `market_context_high->metal_4h` score `-1.1779` n `85` status `ready` deltaP `-9.6521` edge `0.0141` maxDD `-1.0609`
- `market_context_high->crypto_alt_4h` score `-1.2068` n `85` status `ready` deltaP `-8.3859` edge `0.0945` maxDD `-8.7986`
- `market_context_high->equity_4h` score `-1.3211` n `85` status `ready` deltaP `-4.071` edge `0.0047` maxDD `-5.4217`
- `market_context_high->equity_1h` score `-1.3905` n `97` status `ready` deltaP `-3.5774` edge `-0.0056` maxDD `-2.2475`
- `market_context_high->index_1h` score `-1.7129` n `97` status `ready` deltaP `-8.0314` edge `-0.003` maxDD `-0.5627`
- `market_context_high->index_4h` score `-1.8467` n `85` status `ready` deltaP `-9.2808` edge `0.0012` maxDD `-1.1242`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

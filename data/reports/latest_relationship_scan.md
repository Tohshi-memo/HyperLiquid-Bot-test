# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T00:07:26.687199+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10906`

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

- `market_context_high->commodity_4h` score `1.2879` n `151` status `ready` deltaP `15.2732` edge `0.0728` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8144` n `163` status `ready` deltaP `10.6453` edge `0.0312` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.4212` n `130` status `ready` deltaP `17.9648` edge `0.0209` maxDD `-1.9329`
- `market_context_high->metal_24h` score `0.1392` n `130` status `ready` deltaP `1.2794` edge `0.069` maxDD `-2.2743`
- `market_context_high->equity_24h` score `-0.1523` n `130` status `ready` deltaP `2.1741` edge `0.2788` maxDD `-21.1456`
- `market_context_high->index_24h` score `-0.2751` n `130` status `ready` deltaP `2.5908` edge `0.1006` maxDD `-5.9181`
- `market_context_high->fx_1h` score `-0.4996` n `163` status `ready` deltaP `1.7128` edge `-0.0035` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.6919` n `151` status `ready` deltaP `2.9801` edge `-0.0022` maxDD `-1.6928`
- `market_context_high->metal_1h` score `-0.7101` n `163` status `ready` deltaP `-3.9905` edge `-0.009` maxDD `-1.4345`
- `market_context_high->index_4h` score `-0.716` n `151` status `ready` deltaP `-3.1175` edge `-0.0105` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.9517` n `163` status `ready` deltaP `-3.8702` edge `-0.0058` maxDD `-0.8168`
- `market_context_high->equity_1h` score `-1.1698` n `163` status `ready` deltaP `-1.5392` edge `-0.0002` maxDD `-4.6286`
- `market_context_high->metal_4h` score `-1.2147` n `151` status `ready` deltaP `-3.5121` edge `-0.0225` maxDD `-3.4518`
- `market_context_high->crypto_alt_1h` score `-1.6461` n `163` status `ready` deltaP `-9.4972` edge `-0.0456` maxDD `-5.5029`
- `market_context_high->equity_4h` score `-2.8049` n `151` status `ready` deltaP `-3.917` edge `-0.0739` maxDD `-7.6983`
- `market_context_high->crypto_major_1h` score `-3.8226` n `163` status `ready` deltaP `-11.6197` edge `-0.0677` maxDD `-10.5372`
- `market_context_high->crypto_major_24h` score `-4.3539` n `130` status `ready` deltaP `0.7799` edge `-0.1186` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-4.6179` n `151` status `ready` deltaP `-9.9399` edge `-0.1343` maxDD `-8.074`
- `market_context_high->crypto_alt_24h` score `-4.7043` n `130` status `ready` deltaP `-12.8873` edge `-0.1618` maxDD `-4.5445`
- `market_context_high->unknown_1h` score `-7.5596` n `163` status `ready` deltaP `-5.065` edge `-0.5505` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-16T22:52:25.788993+00:00`
- Price records: `672`
- Market context records: `6967`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11735`

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

- `market_context_high->fx_1h` score `-0.2429` n `237` status `ready` deltaP `2.3339` edge `0.0018` maxDD `-0.5468`
- `market_context_high->crypto_alt_1h` score `-0.391` n `237` status `ready` deltaP `2.1306` edge `0.0221` maxDD `-4.5815`
- `market_context_high->metal_1h` score `-0.71` n `237` status `ready` deltaP `-1.7907` edge `-0.0023` maxDD `-2.1427`
- `market_context_high->index_1h` score `-0.7333` n `237` status `ready` deltaP `-0.3885` edge `-0.0003` maxDD `-2.2895`
- `market_context_high->fx_4h` score `-0.9141` n `237` status `ready` deltaP `12.0877` edge `0.0086` maxDD `-2.1765`
- `market_context_high->crypto_major_1h` score `-1.2185` n `237` status `ready` deltaP `2.7294` edge `0.0155` maxDD `-7.1523`
- `market_context_high->commodity_1h` score `-1.3341` n `237` status `ready` deltaP `-3.4229` edge `-0.0162` maxDD `-2.4388`
- `market_context_high->unknown_1h` score `-1.6357` n `237` status `ready` deltaP `-2.2803` edge `-0.031` maxDD `-3.2083`
- `market_context_high->unknown_24h` score `-1.6657` n `224` status `ready` deltaP `-9.2014` edge `0.3028` maxDD `-18.7342`
- `market_context_high->commodity_4h` score `-1.6687` n `237` status `ready` deltaP `-4.4329` edge `-0.0354` maxDD `-5.5853`
- `market_context_high->index_4h` score `-1.8481` n `237` status `ready` deltaP `7.2096` edge `-0.0151` maxDD `-12.2591`
- `market_context_high->equity_1h` score `-2.017` n `237` status `ready` deltaP `2.0888` edge `-0.0171` maxDD `-15.7664`
- `market_context_high->metal_4h` score `-2.0559` n `237` status `ready` deltaP `4.5661` edge `0.0043` maxDD `-5.5324`
- `market_context_high->crypto_alt_4h` score `-3.1661` n `237` status `ready` deltaP `-0.5512` edge `-0.0237` maxDD `-22.2831`
- `market_context_high->unknown_4h` score `-3.3487` n `237` status `ready` deltaP `-8.7154` edge `0.0156` maxDD `-10.2579`
- `market_context_high->commodity_24h` score `-3.7693` n `224` status `ready` deltaP `-6.4485` edge `-0.0843` maxDD `-5.2791`
- `market_context_high->crypto_major_4h` score `-3.8399` n `237` status `ready` deltaP `-1.8061` edge `-0.0518` maxDD `-24.6094`
- `market_context_high->fx_24h` score `-4.4269` n `224` status `ready` deltaP `-7.3661` edge `-0.0151` maxDD `-5.7093`
- `market_context_high->equity_4h` score `-7.718` n `237` status `ready` deltaP `3.8586` edge `-0.0935` maxDD `-66.7371`
- `market_context_high->index_24h` score `-12.2736` n `224` status `ready` deltaP `-6.0515` edge `-0.1262` maxDD `-59.5597`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

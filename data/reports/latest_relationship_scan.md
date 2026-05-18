# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T15:22:21.105205+00:00`
- Price records: `672`
- Market context records: `1129`
- Flow alert records: `5155`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8733`

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

- `market_context_high->crypto_major_24h` score `19.5131` n `150` status `ready` deltaP `41.7223` edge `1.3943` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `9.3103` n `150` status `ready` deltaP `18.0833` edge `0.7787` maxDD `-9.5387`
- `market_context_high->equity_24h` score `7.2543` n `150` status `ready` deltaP `17.5625` edge `0.5371` maxDD `-3.6396`
- `market_context_high->index_24h` score `5.6535` n `150` status `ready` deltaP `16.1736` edge `0.3941` maxDD `-2.1308`
- `market_context_high->metal_24h` score `5.5727` n `150` status `ready` deltaP `-1.8889` edge `0.6437` maxDD `-6.3373`
- `market_context_high->equity_4h` score `1.7356` n `168` status `ready` deltaP `9.8795` edge `0.1451` maxDD `-3.6396`
- `market_context_high->index_4h` score `0.7662` n `168` status `ready` deltaP `7.2227` edge `0.084` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.4343` n `168` status `ready` deltaP `6.8969` edge `0.0219` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.3532` n `168` status `ready` deltaP `2.8799` edge `0.048` maxDD `-1.3546`
- `market_context_high->fx_1h` score `0.1603` n `168` status `ready` deltaP `8.6149` edge `0.0015` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `0.0909` n `168` status `ready` deltaP `7.1322` edge `0.0366` maxDD `-4.1256`
- `market_context_high->crypto_major_4h` score `-0.0046` n `168` status `ready` deltaP `7.9994` edge `0.1382` maxDD `-8.3693`
- `market_context_high->metal_1h` score `-0.2448` n `168` status `ready` deltaP `6.651` edge `-0.0037` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2574` n `168` status `ready` deltaP `2.9441` edge `0.0432` maxDD `-3.4088`
- `market_context_high->fx_4h` score `-0.7207` n `168` status `ready` deltaP `0.9364` edge `0.001` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.7403` n `168` status `ready` deltaP `-1.775` edge `-0.0023` maxDD `-3.7959`
- `market_context_high->crypto_alt_4h` score `-1.0897` n `168` status `ready` deltaP `5.2338` edge `0.1219` maxDD `-16.7194`
- `market_context_high->metal_4h` score `-2.5238` n `168` status `ready` deltaP `5.9378` edge `-0.0545` maxDD `-9.2991`
- `market_context_high->commodity_4h` score `-3.095` n `168` status `ready` deltaP `-11.1208` edge `-0.0059` maxDD `-13.0076`
- `market_context_high->unknown_24h` score `-3.2248` n `150` status `ready` deltaP `2.1944` edge `-0.0104` maxDD `-10.1706`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

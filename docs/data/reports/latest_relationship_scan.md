# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T22:37:30.793960+00:00`
- Price records: `672`
- Market context records: `6547`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9854`

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

- `market_context_high->unknown_24h` score `6.4147` n `144` status `ready` deltaP `11.8934` edge `0.7853` maxDD `-15.0689`
- `news_risk_high->fx_4h` score `3.7372` n `34` status `ready` deltaP `39.4548` edge `0.053` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.2829` n `34` status `ready` deltaP `28.1701` edge `0.0205` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `2.0058` n `200` status `ready` deltaP `-5.497` edge `0.2939` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `1.3201` n `144` status `ready` deltaP `12.784` edge `0.2116` maxDD `-5.2791`
- `news_risk_high->crypto_major_1h` score `0.4986` n `34` status `ready` deltaP `4.5351` edge `0.0874` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.4655` n `192` status `ready` deltaP `12.0046` edge `0.0264` maxDD `-0.4108`
- `market_context_high->crypto_alt_4h` score `0.1827` n `192` status `ready` deltaP `9.0447` edge `0.1103` maxDD `-6.7632`
- `news_risk_high->crypto_alt_1h` score `-0.2407` n `34` status `ready` deltaP `-2.6418` edge `0.0377` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.2942` n `192` status `ready` deltaP `10.8104` edge `0.0601` maxDD `-8.2573`
- `market_context_high->fx_1h` score `-0.4536` n `200` status `ready` deltaP `-0.8593` edge `-0.0017` maxDD `-0.7249`
- `market_context_high->crypto_major_4h` score `-0.4777` n `192` status `ready` deltaP `11.5219` edge `0.091` maxDD `-12.6576`
- `market_context_high->commodity_1h` score `-0.5322` n `200` status `ready` deltaP `0.506` edge `-0.0033` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.535` n `200` status `ready` deltaP `-0.0509` edge `0.0037` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.6266` n `200` status `ready` deltaP `5.7994` edge `0.0123` maxDD `-5.8368`
- `market_context_high->crypto_major_1h` score `-0.6326` n `200` status `ready` deltaP `5.6527` edge `0.0078` maxDD `-6.7936`
- `market_context_high->equity_1h` score `-0.7171` n `200` status `ready` deltaP `2.6527` edge `0.0014` maxDD `-4.2147`
- `news_risk_high->metal_1h` score `-0.9138` n `34` status `ready` deltaP `-4.9313` edge `-0.0219` maxDD `-1.6568`
- `market_context_high->metal_4h` score `-1.064` n `192` status `ready` deltaP `0.7876` edge `0.0375` maxDD `-2.6662`
- `market_context_high->unknown_4h` score `-1.0765` n `192` status `ready` deltaP `-18.8008` edge `0.2762` maxDD `-10.5788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

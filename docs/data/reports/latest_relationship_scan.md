# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T09:22:30.798238+00:00`
- Price records: `672`
- Market context records: `6170`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11132`

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

- `news_risk_high->crypto_alt_24h` score `12.6459` n `32` status `ready` deltaP `42.5514` edge `0.7849` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.2953` n `32` status `ready` deltaP `64.0411` edge `0.181` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.0747` n `32` status `ready` deltaP `42.4432` edge `0.0612` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.328` n `32` status `ready` deltaP `28.0643` edge `0.0208` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.7595` n `195` status `ready` deltaP `1.1912` edge `0.2395` maxDD `-3.7317`
- `news_risk_high->crypto_major_24h` score `1.5864` n `32` status `ready` deltaP `15.9675` edge `0.1749` maxDD `-4.2368`
- `news_risk_high->crypto_major_1h` score `1.1937` n `32` status `ready` deltaP `12.8597` edge `0.114` maxDD `-2.0691`
- `news_risk_high->crypto_alt_1h` score `0.6059` n `32` status `ready` deltaP `8.1044` edge `0.0698` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.3301` n `195` status `ready` deltaP `-0.9091` edge `0.2868` maxDD `-11.925`
- `market_context_high->metal_24h` score `0.1982` n `195` status `ready` deltaP `20.7833` edge `0.1437` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.0485` n `32` status `ready` deltaP `9.8459` edge `0.0153` maxDD `-2.3058`
- `market_context_high->equity_4h` score `-0.0893` n `195` status `ready` deltaP `2.7273` edge `0.0661` maxDD `-2.671`
- `market_context_high->fx_1h` score `-0.3169` n `195` status `ready` deltaP `0.7566` edge `-0.0011` maxDD `-0.5659`
- `news_risk_high->commodity_24h` score `-0.6277` n `32` status `ready` deltaP `12.7997` edge `-0.1171` maxDD `-0.3101`
- `market_context_high->metal_4h` score `-0.6519` n `195` status `ready` deltaP `3.7296` edge `0.0103` maxDD `-3.4996`
- `market_context_high->commodity_1h` score `-0.7042` n `195` status `ready` deltaP `-1.6121` edge `-0.0033` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.8164` n `32` status `ready` deltaP `-3.6622` edge `-0.0305` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.8903` n `195` status `ready` deltaP `1.7224` edge `-0.0058` maxDD `-2.0564`
- `market_context_high->crypto_alt_1h` score `-0.97` n `195` status `ready` deltaP `3.0884` edge `0.0303` maxDD `-9.3536`
- `market_context_high->equity_1h` score `-0.9874` n `195` status `ready` deltaP `-2.571` edge `0.0021` maxDD `-4.2573`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

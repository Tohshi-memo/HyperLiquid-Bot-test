# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T15:22:27.984158+00:00`
- Price records: `672`
- Market context records: `8209`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5920`

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

- `news_risk_high->unknown_24h` score `8110.9443` n `43` status `ready` deltaP `36.9792` edge `675.6655` maxDD `0.0`
- `market_context_high->equity_24h` score `21.0314` n `34` status `ready` deltaP `40.0123` edge `1.5769` maxDD `-4.9489`
- `market_context_high->crypto_alt_24h` score `14.7525` n `34` status `ready` deltaP `28.7684` edge `1.1327` maxDD `-3.9428`
- `market_context_high->crypto_major_24h` score `14.3827` n `34` status `ready` deltaP `28.2476` edge `1.162` maxDD `-8.4739`
- `market_context_high->equity_4h` score `8.7965` n `34` status `ready` deltaP `47.0588` edge `0.4236` maxDD `-0.0094`
- `market_context_high->metal_24h` score `8.1601` n `34` status `ready` deltaP `44.9755` edge `0.3903` maxDD `-0.4771`
- `news_risk_high->equity_4h` score `7.2557` n `54` status `ready` deltaP `25.9259` edge `0.4915` maxDD `-3.4427`
- `market_context_high->crypto_major_4h` score `4.9482` n `34` status `ready` deltaP `21.763` edge `0.3217` maxDD `-2.0217`
- `market_context_high->index_24h` score `4.7489` n `34` status `ready` deltaP `29.1156` edge `0.2594` maxDD `-0.9546`
- `market_context_high->crypto_alt_4h` score `4.312` n `34` status `ready` deltaP `19.1266` edge `0.2604` maxDD `-0.6195`
- `market_context_high->index_4h` score `3.7699` n `34` status `ready` deltaP `37.6704` edge `0.0673` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.6572` n `34` status `ready` deltaP `36.2536` edge `0.0809` maxDD `-0.0926`
- `news_risk_high->equity_1h` score `3.1985` n `54` status `ready` deltaP `22.7268` edge `0.1459` maxDD `-1.1366`
- `news_risk_high->index_4h` score `2.6821` n `54` status `ready` deltaP `22.4198` edge `0.0931` maxDD `-0.191`
- `news_risk_high->crypto_major_4h` score `2.6574` n `54` status `ready` deltaP `13.3752` edge `0.3209` maxDD `-2.8833`
- `market_context_high->equity_1h` score `2.4517` n `34` status `ready` deltaP `13.3586` edge `0.1299` maxDD `-0.1718`
- `market_context_high->fx_24h` score `2.0765` n `34` status `ready` deltaP `36.7545` edge `0.0725` maxDD `-0.4381`
- `news_risk_high->crypto_major_1h` score `1.9362` n `54` status `ready` deltaP `13.3012` edge `0.1124` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8518` n `54` status `ready` deltaP `15.0033` edge `0.0977` maxDD `-1.1388`
- `news_risk_high->crypto_alt_4h` score `1.44` n `54` status `ready` deltaP `17.3837` edge `0.2079` maxDD `-5.8012`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

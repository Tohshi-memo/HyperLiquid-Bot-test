# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-31T14:52:29.182276+00:00`
- Price records: `672`
- Market context records: `8524`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5898`

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

- `news_risk_high->unknown_24h` score `6279.6561` n `52` status `ready` deltaP `44.7383` edge `523.0485` maxDD `-2.0332`
- `news_risk_high->equity_4h` score `5.5856` n `64` status `ready` deltaP `21.2652` edge `0.3834` maxDD `-3.4427`
- `news_risk_high->index_4h` score `2.0217` n `64` status `ready` deltaP `16.654` edge `0.0765` maxDD `-0.191`
- `news_risk_high->equity_1h` score `1.7098` n `64` status `ready` deltaP `15.8028` edge `0.0848` maxDD `-2.4803`
- `news_risk_high->crypto_major_4h` score `0.8542` n `64` status `ready` deltaP `5.8308` edge `0.1482` maxDD `-3.5385`
- `news_risk_high->crypto_alt_4h` score `0.8009` n `64` status `ready` deltaP `14.6341` edge `0.1443` maxDD `-5.8012`
- `market_context_high->crypto_alt_4h` score `0.5044` n `40` status `ready` deltaP `7.1341` edge `0.102` maxDD `-4.7914`
- `news_risk_high->crypto_alt_1h` score `0.5038` n `64` status `ready` deltaP `8.8604` edge `0.0582` maxDD `-1.8813`
- `news_risk_high->crypto_major_1h` score `0.301` n `64` status `ready` deltaP `6.3155` edge `0.0477` maxDD `-2.0972`
- `news_risk_high->fx_1h` score `0.115` n `64` status `ready` deltaP `5.7354` edge `0.0046` maxDD `-0.2475`
- `news_risk_high->metal_4h` score `0.058` n `64` status `ready` deltaP `2.782` edge `0.0365` maxDD `-0.8085`
- `news_risk_high->index_1h` score `0.0519` n `64` status `ready` deltaP `4.3694` edge `0.0092` maxDD `-0.5338`
- `news_risk_high->fx_4h` score `0.0266` n `64` status `ready` deltaP `11.471` edge `0.0215` maxDD `-0.6604`
- `market_context_high->crypto_major_4h` score `-0.0249` n `40` status `ready` deltaP `3.0183` edge `0.0762` maxDD `-4.961`
- `news_risk_high->metal_1h` score `-0.0856` n `64` status `ready` deltaP `3.7051` edge `0.0085` maxDD `-0.5599`
- `market_context_high->commodity_1h` score `-0.1986` n `52` status `ready` deltaP `4.468` edge `0.0073` maxDD `-2.0038`
- `market_context_high->fx_4h` score `-0.2846` n `40` status `ready` deltaP `2.4085` edge `0.0021` maxDD `-0.7045`
- `market_context_high->commodity_4h` score `-0.4145` n `40` status `ready` deltaP `7.7134` edge `0.0469` maxDD `-5.4508`
- `market_context_high->metal_1h` score `-0.681` n `52` status `ready` deltaP `-2.5449` edge `-0.0209` maxDD `-1.6224`
- `market_context_high->index_4h` score `-0.8537` n `40` status `ready` deltaP `-2.4085` edge `-0.0335` maxDD `-2.1247`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

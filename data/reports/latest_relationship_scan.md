# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T07:52:32.202200+00:00`
- Price records: `672`
- Market context records: `8175`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5904`

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

- `news_risk_high->unknown_24h` score `8781.2482` n `42` status `ready` deltaP `37.1528` edge `731.523` maxDD `0.0`
- `market_context_high->equity_24h` score `19.0014` n `55` status `ready` deltaP `43.9614` edge `1.3814` maxDD `-4.9489`
- `market_context_high->equity_4h` score `9.3038` n `56` status `ready` deltaP `38.0226` edge `0.5453` maxDD `-0.5442`
- `news_risk_high->equity_4h` score `8.4031` n `46` status `ready` deltaP `31.7338` edge `0.5177` maxDD `-1.3202`
- `market_context_high->metal_24h` score `8.2107` n `55` status `ready` deltaP `42.7083` edge `0.3995` maxDD `0.0`
- `market_context_high->index_4h` score `4.0728` n `56` status `ready` deltaP `36.912` edge `0.0976` maxDD `-0.0092`
- `market_context_high->equity_1h` score `3.4017` n `56` status `ready` deltaP `18.734` edge `0.1789` maxDD `-0.6254`
- `news_risk_high->equity_1h` score `3.3867` n `50` status `ready` deltaP `25.3054` edge `0.1444` maxDD `-1.1366`
- `news_risk_high->crypto_major_4h` score `3.3773` n `46` status `ready` deltaP `18.7235` edge `0.3687` maxDD `-2.1767`
- `news_risk_high->index_4h` score `2.7026` n `46` status `ready` deltaP `22.3158` edge `0.0955` maxDD `-0.191`
- `market_context_high->index_1h` score `2.0343` n `56` status `ready` deltaP `23.5137` edge `0.0266` maxDD `-0.1069`
- `news_risk_high->crypto_major_1h` score `1.8427` n `50` status `ready` deltaP `11.5928` edge `0.116` maxDD `-1.1783`
- `market_context_high->index_24h` score `1.8152` n `55` status `ready` deltaP `15.9217` edge `0.1936` maxDD `-1.3621`
- `news_risk_high->metal_4h` score `1.8128` n `46` status `ready` deltaP `16.9737` edge `0.0847` maxDD `-0.7433`
- `market_context_high->metal_4h` score `1.6738` n `56` status `ready` deltaP `20.6228` edge `0.0588` maxDD `-0.8772`
- `news_risk_high->crypto_alt_1h` score `1.6029` n `50` status `ready` deltaP `12.0419` edge `0.0967` maxDD `-1.1388`
- `market_context_high->crypto_alt_24h` score `1.4157` n `55` status `ready` deltaP `4.0625` edge `0.5497` maxDD `-20.6231`
- `news_risk_high->crypto_alt_4h` score `1.3498` n `46` status `ready` deltaP `15.2903` edge `0.2103` maxDD `-5.8012`
- `market_context_high->fx_24h` score `0.8403` n `55` status `ready` deltaP `18.6269` edge `0.0539` maxDD `-0.6283`
- `news_risk_high->index_1h` score `0.596` n `50` status `ready` deltaP `8.2994` edge `0.0232` maxDD `-0.3089`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

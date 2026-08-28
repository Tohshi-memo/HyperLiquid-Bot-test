# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-28T15:52:25.413653+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11634`

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

- `news_risk_high->unknown_24h` score `53.8052` n `50` status `ready` deltaP `11.7851` edge `4.4052` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `31.8442` n `50` status `ready` deltaP `43.1404` edge `2.4102` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `11.09` n `56` status `ready` deltaP `23.1272` edge `0.7842` maxDD `-0.1374`
- `news_risk_high->equity_24h` score `5.4991` n `50` status `ready` deltaP `30.1005` edge `0.3504` maxDD `-4.7584`
- `news_risk_high->crypto_major_24h` score `4.4199` n `50` status `ready` deltaP `21.6083` edge `0.2736` maxDD `-2.6128`
- `news_risk_high->metal_24h` score `4.3333` n `50` status `ready` deltaP `43.5806` edge `0.0748` maxDD `-0.0053`
- `news_risk_high->fx_4h` score `4.0017` n `56` status `ready` deltaP `46.5156` edge `0.0324` maxDD `-0.0559`
- `market_context_high->metal_24h` score `3.0726` n `121` status `ready` deltaP `28.2252` edge `0.1698` maxDD `-3.1535`
- `market_context_high->unknown_24h` score `3.0187` n `121` status `ready` deltaP `5.1735` edge `0.2903` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.7159` n `121` status `ready` deltaP `18.139` edge `0.1461` maxDD `-0.5894`
- `news_risk_high->unknown_1h` score `2.5933` n `59` status `ready` deltaP `12.1512` edge `0.1708` maxDD `-0.8558`
- `news_risk_high->index_24h` score `2.3602` n `50` status `ready` deltaP `26.9948` edge `0.0318` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.5871` n `59` status `ready` deltaP `21.1864` edge `0.008` maxDD `-0.0257`
- `market_context_high->unknown_1h` score `1.1958` n `121` status `ready` deltaP `9.4757` edge `0.0815` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.818` n `56` status `ready` deltaP `19.7518` edge `0.0495` maxDD `-2.105`
- `news_risk_high->metal_4h` score `0.6301` n `56` status `ready` deltaP `13.6978` edge `0.0143` maxDD `-0.249`
- `news_risk_high->commodity_1h` score `0.5203` n `59` status `ready` deltaP `14.0592` edge `0.005` maxDD `-0.5618`
- `news_risk_high->equity_1h` score `0.2569` n `59` status `ready` deltaP `12.2095` edge `-0.0029` maxDD `-1.6451`
- `news_risk_high->metal_1h` score `0.2163` n `59` status `ready` deltaP `5.6328` edge `0.0038` maxDD `-0.1994`
- `news_risk_high->index_4h` score `0.1014` n `56` status `ready` deltaP `7.2518` edge `0.0` maxDD `-0.1919`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

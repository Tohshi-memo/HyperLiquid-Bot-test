# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-08T00:07:22.830387+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4416`

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

- `market_context_high->unknown_4h` score `120.7247` n `37` status `ready` deltaP `-7.5972` edge `10.1558` maxDD `-0.9139`
- `market_context_high->fx_4h` score `3.48` n `37` status `ready` deltaP `37.8873` edge `0.0464` maxDD `-0.0521`
- `market_context_high->equity_1h` score `3.1646` n `37` status `ready` deltaP `9.4595` edge `0.2466` maxDD `-2.3425`
- `market_context_high->index_4h` score `1.8721` n `37` status `ready` deltaP `24.6787` edge `0.0385` maxDD `-2.4279`
- `news_risk_high->fx_24h` score `1.713` n `52` status `ready` deltaP `10.2831` edge `0.0963` maxDD `-0.1014`
- `news_risk_high->equity_4h` score `0.8484` n `52` status `ready` deltaP `6.8363` edge `0.1371` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.6992` n `37` status `ready` deltaP `9.0023` edge `0.0568` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.52` n `37` status `ready` deltaP `8.27` edge `0.0153` maxDD `-0.1681`
- `market_context_high->crypto_alt_1h` score `0.3953` n `37` status `ready` deltaP `10.3496` edge `0.0632` maxDD `-3.1881`
- `news_risk_high->index_4h` score `0.2543` n `52` status `ready` deltaP `8.9822` edge `0.0205` maxDD `-0.4888`
- `market_context_high->index_1h` score `0.2362` n `37` status `ready` deltaP `1.2017` edge `0.0387` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.2025` n `52` status `ready` deltaP `6.851` edge `0.1471` maxDD `-6.6786`
- `news_risk_high->fx_4h` score `0.1698` n `52` status `ready` deltaP `8.6773` edge `0.0078` maxDD `-0.1771`
- `market_context_high->commodity_1h` score `0.1265` n `37` status `ready` deltaP `9.1682` edge `0.0097` maxDD `-1.7019`
- `market_context_high->commodity_4h` score `-0.0116` n `37` status `ready` deltaP `3.1395` edge `0.023` maxDD `-1.633`
- `news_risk_high->index_1h` score `-0.038` n `52` status `ready` deltaP `5.6195` edge `0.003` maxDD `-0.2931`
- `market_context_high->metal_1h` score `-0.0575` n `37` status `ready` deltaP `1.3514` edge `0.0164` maxDD `-0.6226`
- `news_risk_high->fx_1h` score `-0.2795` n `52` status `ready` deltaP `-0.046` edge `0.003` maxDD `-0.0826`
- `news_risk_high->equity_1h` score `-0.3018` n `52` status `ready` deltaP `-3.8462` edge `0.0419` maxDD `-1.396`
- `market_context_high->equity_4h` score `-0.7748` n `37` status `ready` deltaP `21.3374` edge `0.0864` maxDD `-24.9053`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

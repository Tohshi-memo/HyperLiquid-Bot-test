# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-28T12:37:38.509618+00:00`
- Price records: `672`
- Market context records: `8197`
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

- `news_risk_high->unknown_24h` score `8391.4887` n `43` status `ready` deltaP `36.9792` edge `699.0442` maxDD `0.0`
- `market_context_high->equity_24h` score `21.0132` n `44` status `ready` deltaP `43.6238` edge `1.5513` maxDD `-4.9489`
- `market_context_high->equity_4h` score `11.3383` n `45` status `ready` deltaP `46.101` edge `0.6418` maxDD `-0.0094`
- `market_context_high->metal_24h` score `9.0062` n `44` status `ready` deltaP `46.0069` edge `0.4438` maxDD `0.0`
- `news_risk_high->equity_4h` score `7.4126` n `52` status `ready` deltaP `27.1694` edge `0.4767` maxDD `-2.209`
- `market_context_high->crypto_alt_24h` score `5.9013` n `44` status `ready` deltaP `14.0625` edge `0.8835` maxDD `-10.3206`
- `market_context_high->index_4h` score `4.3778` n `45` status `ready` deltaP `38.7601` edge `0.1107` maxDD `-0.0092`
- `market_context_high->metal_4h` score `3.9473` n `45` status `ready` deltaP `38.2148` edge `0.092` maxDD `-0.0926`
- `market_context_high->equity_1h` score `3.6939` n `45` status `ready` deltaP `19.0153` edge `0.1957` maxDD `-0.1718`
- `news_risk_high->equity_1h` score `2.9478` n `54` status `ready` deltaP `21.9783` edge `0.13` maxDD `-1.1366`
- `market_context_high->crypto_major_24h` score `2.8882` n `44` status `ready` deltaP `13.5417` edge `0.6785` maxDD `-24.5466`
- `news_risk_high->crypto_major_4h` score `2.8284` n `52` status `ready` deltaP `14.341` edge `0.335` maxDD `-2.773`
- `news_risk_high->index_4h` score `2.816` n `52` status `ready` deltaP `24.273` edge `0.0919` maxDD `-0.191`
- `market_context_high->index_24h` score `2.3868` n `44` status `ready` deltaP `20.7071` edge `0.2342` maxDD `-1.2995`
- `news_risk_high->crypto_major_1h` score `2.0237` n `54` status `ready` deltaP `13.9` edge `0.1157` maxDD `-1.1783`
- `news_risk_high->crypto_alt_1h` score `1.8722` n `54` status `ready` deltaP `15.153` edge `0.0984` maxDD `-1.1388`
- `market_context_high->fx_24h` score `1.4816` n `44` status `ready` deltaP `28.346` edge `0.0658` maxDD `-0.5196`
- `news_risk_high->crypto_alt_4h` score `1.378` n `52` status `ready` deltaP `16.4165` edge `0.2064` maxDD `-5.8012`
- `market_context_high->index_1h` score `1.3651` n `45` status `ready` deltaP `24.2315` edge `0.0273` maxDD `-0.1069`
- `news_risk_high->metal_4h` score `1.0973` n `52` status `ready` deltaP `10.5652` edge `0.0678` maxDD `-0.7433`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

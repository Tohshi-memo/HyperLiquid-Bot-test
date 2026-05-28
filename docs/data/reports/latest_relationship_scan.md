# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T22:52:16.545077+00:00`
- Price records: `672`
- Market context records: `2186`
- Flow alert records: `8186`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9188`

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

- `market_context_high->crypto_alt_4h` score `12.7651` n `132` status `ready` deltaP `36.5392` edge `0.9138` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7499` n `132` status `ready` deltaP `42.1286` edge `0.7513` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4503` n `132` status `ready` deltaP `21.3738` edge `0.3796` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8332` n `43` status `ready` deltaP `32.0051` edge `0.3452` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.7918` n `132` status `ready` deltaP `29.5455` edge `0.6005` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.5596` n `132` status `ready` deltaP `24.1778` edge `0.2449` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2386` n `132` status `ready` deltaP `17.7146` edge `0.1995` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9974` n `132` status `ready` deltaP `16.2085` edge `0.2281` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.8727` n `132` status `ready` deltaP `23.5726` edge `0.1506` maxDD `-1.8022`
- `market_context_high->crypto_major_24h` score `2.7446` n `132` status `ready` deltaP `21.1016` edge `1.0394` maxDD `-60.2561`
- `market_context_high->index_24h` score `2.6156` n `132` status `ready` deltaP `10.9059` edge `0.2681` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1842` n `43` status `ready` deltaP `27.7368` edge `0.0155` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.5507` n `132` status `ready` deltaP `18.5052` edge `0.1446` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4635` n `43` status `ready` deltaP `21.4942` edge `0.0256` maxDD `-1.7548`
- `market_context_high->equity_24h` score `1.3715` n `132` status `ready` deltaP `22.3327` edge `0.45` maxDD `-33.1007`
- `news_risk_high->equity_4h` score `1.3313` n `43` status `ready` deltaP `-2.5312` edge `0.3083` maxDD `-4.6598`
- `news_risk_high->unknown_4h` score `1.2867` n `43` status `ready` deltaP `14.4675` edge `0.0831` maxDD `-2.7857`
- `news_risk_high->commodity_1h` score `0.7346` n `43` status `ready` deltaP `10.4651` edge `0.0924` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4897` n `43` status `ready` deltaP `8.4389` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3028` n `132` status `ready` deltaP `9.041` edge `0.0438` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

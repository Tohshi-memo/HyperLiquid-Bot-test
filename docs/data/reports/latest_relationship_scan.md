# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T20:07:21.477623+00:00`
- Price records: `672`
- Market context records: `2174`
- Flow alert records: `8152`
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

- `market_context_high->crypto_alt_4h` score `12.7668` n `133` status `ready` deltaP `36.3653` edge `0.9151` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7656` n `133` status `ready` deltaP `42.0549` edge `0.7531` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5072` n `133` status `ready` deltaP `22.2217` edge `0.3857` maxDD `-2.6599`
- `news_risk_high->commodity_4h` score `3.8113` n `43` status `ready` deltaP `31.8526` edge `0.3434` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.6387` n `133` status `ready` deltaP `24.5965` edge `0.2487` maxDD `-5.0894`
- `market_context_high->unknown_24h` score `3.4251` n `133` status `ready` deltaP `28.7738` edge `0.595` maxDD `-34.1119`
- `market_context_high->crypto_major_1h` score `3.2452` n `133` status `ready` deltaP `17.6624` edge `0.2004` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.0287` n `133` status `ready` deltaP `16.4648` edge `0.229` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.7393` n `133` status `ready` deltaP `22.6251` edge `0.1458` maxDD `-1.8022`
- `market_context_high->crypto_major_24h` score `2.6766` n `133` status `ready` deltaP `20.8594` edge `1.0449` maxDD `-61.2646`
- `market_context_high->index_24h` score `2.6574` n `133` status `ready` deltaP `11.1281` edge `0.2701` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1562` n `43` status `ready` deltaP `27.4319` edge `0.0152` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.8539` n `133` status `ready` deltaP `23.5106` edge `0.4876` maxDD `-33.1875`
- `news_risk_high->unknown_4h` score `1.5381` n `43` status `ready` deltaP `15.8395` edge `0.0949` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.4401` n `133` status `ready` deltaP `17.558` edge `0.1417` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4048` n `43` status `ready` deltaP `21.1948` edge `0.0227` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.39` n `43` status `ready` deltaP `-2.2264` edge `0.3138` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7058` n `43` status `ready` deltaP `10.1657` edge `0.0907` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4621` n `43` status `ready` deltaP `8.1395` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.4016` n `133` status `ready` deltaP `9.8848` edge `0.0464` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

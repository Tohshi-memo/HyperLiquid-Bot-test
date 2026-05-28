# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T23:52:20.193452+00:00`
- Price records: `672`
- Market context records: `2191`
- Flow alert records: `8199`
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

- `market_context_high->crypto_alt_4h` score `12.7471` n `132` status `ready` deltaP `36.5392` edge `0.9123` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7174` n `132` status `ready` deltaP `41.9762` edge `0.7496` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4371` n `132` status `ready` deltaP `21.3738` edge `0.3785` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8206` n `43` status `ready` deltaP `31.8526` edge `0.3446` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.6512` n `132` status `ready` deltaP `29.1983` edge `0.5911` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.5272` n `132` status `ready` deltaP `24.1778` edge `0.2422` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2326` n `132` status `ready` deltaP `17.7146` edge `0.199` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.031` n `132` status `ready` deltaP `16.5079` edge `0.2289` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.9527` n `132` status `ready` deltaP `24.1824` edge `0.1532` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5892` n `132` status `ready` deltaP `10.9059` edge `0.2659` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.5611` n `132` status `ready` deltaP `20.4072` edge `1.0205` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.5167` n `132` status `ready` deltaP `18.2003` edge `0.1438` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4623` n `43` status `ready` deltaP `21.4942` edge `0.0255` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.3102` n `43` status `ready` deltaP `-2.5312` edge `0.3056` maxDD `-4.6598`
- `news_risk_high->unknown_4h` score `1.2735` n `43` status `ready` deltaP `14.4675` edge `0.082` maxDD `-2.7857`
- `market_context_high->equity_24h` score `1.0172` n `132` status `ready` deltaP `21.6382` edge `0.4251` maxDD `-33.1007`
- `news_risk_high->commodity_1h` score `0.758` n `43` status `ready` deltaP `10.7645` edge `0.0934` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4525` n `43` status `ready` deltaP `7.9898` edge `0.0101` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2525` n `132` status `ready` deltaP `8.5919` edge `0.0426` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

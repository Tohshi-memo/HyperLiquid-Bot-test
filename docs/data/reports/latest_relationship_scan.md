# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T22:07:18.307760+00:00`
- Price records: `672`
- Market context records: `2183`
- Flow alert records: `8177`
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

- `market_context_high->crypto_alt_4h` score `12.6877` n `132` status `ready` deltaP `36.0819` edge `0.9104` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7052` n `132` status `ready` deltaP `41.8237` edge `0.7496` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5011` n `132` status `ready` deltaP `21.6787` edge `0.3818` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8494` n `132` status `ready` deltaP `29.5455` edge `0.6053` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.8191` n `43` status `ready` deltaP `31.8526` edge `0.3444` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.5608` n `132` status `ready` deltaP `24.1778` edge `0.245` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.1847` n `132` status `ready` deltaP `17.4152` edge `0.197` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9051` n `132` status `ready` deltaP `15.7594` edge `0.2234` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8187` n `132` status `ready` deltaP `21.1016` edge `1.0489` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.8181` n `132` status `ready` deltaP `23.1153` edge `0.1491` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.624` n `132` status `ready` deltaP `10.9059` edge `0.2688` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1842` n `43` status `ready` deltaP `27.7368` edge `0.0155` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.598` n `132` status `ready` deltaP `22.8535` edge `0.4654` maxDD `-33.1007`
- `market_context_high->metal_4h` score `1.5361` n `132` status `ready` deltaP `18.3527` edge `0.1444` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4515` n `43` status `ready` deltaP `21.3445` edge `0.0256` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.3375` n `43` status `ready` deltaP `14.7724` edge `0.0853` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3321` n `43` status `ready` deltaP `-2.5312` edge `0.3084` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7315` n `43` status `ready` deltaP `10.4651` edge `0.092` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4897` n `43` status `ready` deltaP `8.4389` edge `0.0102` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3004` n `132` status `ready` deltaP `9.041` edge `0.0436` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

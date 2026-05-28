# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T20:22:24.470553+00:00`
- Price records: `672`
- Market context records: `2175`
- Flow alert records: `8155`
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

- `market_context_high->crypto_alt_4h` score `12.7575` n `132` status `ready` deltaP `36.2343` edge `0.9152` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8873` n `132` status `ready` deltaP `42.5859` edge `0.7597` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.6775` n `132` status `ready` deltaP `22.5933` edge `0.3904` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8631` n `132` status `ready` deltaP `29.3719` edge `0.6076` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.8097` n `43` status `ready` deltaP `31.8526` edge `0.3432` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.6416` n `132` status `ready` deltaP `24.4826` edge `0.2497` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.3057` n `132` status `ready` deltaP `18.1637` edge `0.2021` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9962` n `132` status `ready` deltaP `16.3582` edge `0.227` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8855` n `132` status `ready` deltaP `21.2752` edge `1.0563` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.7515` n `132` status `ready` deltaP `22.658` edge `0.1466` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.6072` n `132` status `ready` deltaP `10.9059` edge `0.2674` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1684` n `43` status `ready` deltaP `27.5843` edge `0.0152` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.9753` n `132` status `ready` deltaP `23.8952` edge `0.4899` maxDD `-33.1007`
- `news_risk_high->unknown_4h` score `1.5139` n `43` status `ready` deltaP `15.687` edge `0.0939` maxDD `-2.7857`
- `market_context_high->metal_4h` score `1.4949` n `132` status `ready` deltaP `18.0478` edge `0.143` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4024` n `43` status `ready` deltaP `21.1948` edge `0.0225` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.3846` n `43` status `ready` deltaP `-2.2264` edge `0.3131` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.6934` n `43` status `ready` deltaP `10.016` edge `0.0901` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4633` n `43` status `ready` deltaP `8.1395` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.376` n `132` status `ready` deltaP `9.6398` edge `0.0459` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

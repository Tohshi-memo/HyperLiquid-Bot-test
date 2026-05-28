# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T20:37:27.471387+00:00`
- Price records: `672`
- Market context records: `2176`
- Flow alert records: `8158`
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

- `market_context_high->crypto_alt_4h` score `12.7443` n `132` status `ready` deltaP `36.2343` edge `0.9141` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.8475` n `132` status `ready` deltaP `42.4335` edge `0.7574` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.6401` n `132` status `ready` deltaP `22.4409` edge `0.3883` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8523` n `132` status `ready` deltaP `29.3719` edge `0.6067` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.7995` n `43` status `ready` deltaP `31.7002` edge `0.3429` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.6308` n `132` status `ready` deltaP `24.4826` edge `0.2488` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2878` n `132` status `ready` deltaP `18.014` edge `0.2016` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9974` n `132` status `ready` deltaP `16.3582` edge `0.2271` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8878` n `132` status `ready` deltaP `21.2752` edge `1.0566` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.7539` n `132` status `ready` deltaP `22.658` edge `0.1468` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.612` n `132` status `ready` deltaP `10.9059` edge `0.2678` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1696` n `43` status `ready` deltaP `27.5843` edge `0.0153` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.9453` n `132` status `ready` deltaP `23.8952` edge `0.4874` maxDD `-33.1007`
- `market_context_high->metal_4h` score `1.4937` n `132` status `ready` deltaP `18.0478` edge `0.1429` maxDD `-4.7664`
- `news_risk_high->unknown_4h` score `1.4765` n `43` status `ready` deltaP `15.5346` edge `0.0918` maxDD `-2.7857`
- `news_risk_high->unknown_1h` score `1.3784` n `43` status `ready` deltaP `21.0451` edge `0.0215` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.3776` n `43` status `ready` deltaP `-2.2264` edge `0.3122` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.6754` n `43` status `ready` deltaP `9.8663` edge `0.0888` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4633` n `43` status `ready` deltaP `8.1395` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3772` n `132` status `ready` deltaP `9.6398` edge `0.046` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

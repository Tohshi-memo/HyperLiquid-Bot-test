# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-28T21:27:27.780846+00:00`
- Price records: `672`
- Market context records: `2180`
- Flow alert records: `8169`
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

- `market_context_high->crypto_alt_4h` score `12.6901` n `132` status `ready` deltaP `36.0819` edge `0.9106` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.7474` n `132` status `ready` deltaP `41.9762` edge `0.7521` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.5785` n `132` status `ready` deltaP `22.136` edge `0.3852` maxDD `-2.4317`
- `market_context_high->unknown_24h` score `3.8547` n `132` status `ready` deltaP `29.3719` edge `0.6069` maxDD `-32.8525`
- `news_risk_high->commodity_4h` score `3.8152` n `43` status `ready` deltaP `31.8526` edge `0.3439` maxDD `-3.0367`
- `market_context_high->equity_4h` score `3.5692` n `132` status `ready` deltaP `24.1778` edge `0.2457` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.205` n `132` status `ready` deltaP `17.5649` edge `0.1977` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.9099` n `132` status `ready` deltaP `15.9091` edge `0.2228` maxDD `-4.9097`
- `market_context_high->crypto_major_24h` score `2.8894` n `132` status `ready` deltaP `21.2752` edge `1.0568` maxDD `-60.2561`
- `market_context_high->index_4h` score `2.7745` n `132` status `ready` deltaP `22.8104` edge `0.1475` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.6144` n `132` status `ready` deltaP `10.9059` edge `0.268` maxDD `-4.1604`
- `news_risk_high->fx_4h` score `2.1708` n `43` status `ready` deltaP `27.5843` edge `0.0154` maxDD `-0.1382`
- `market_context_high->equity_24h` score `1.7788` n `132` status `ready` deltaP `23.3743` edge `0.477` maxDD `-33.1007`
- `market_context_high->metal_4h` score `1.4925` n `132` status `ready` deltaP `18.0478` edge `0.1428` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.418` n `43` status `ready` deltaP `21.0451` edge `0.0248` maxDD `-1.7548`
- `news_risk_high->unknown_4h` score `1.4149` n `43` status `ready` deltaP `15.2297` edge `0.0887` maxDD `-2.7857`
- `news_risk_high->equity_4h` score `1.3375` n `43` status `ready` deltaP `-2.5312` edge `0.3091` maxDD `-4.6598`
- `news_risk_high->commodity_1h` score `0.7082` n `43` status `ready` deltaP `10.1657` edge `0.091` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4633` n `43` status `ready` deltaP `8.1395` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.3148` n `132` status `ready` deltaP `9.1907` edge `0.0438` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

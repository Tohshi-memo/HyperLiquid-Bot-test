# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T00:07:19.749794+00:00`
- Price records: `672`
- Market context records: `2192`
- Flow alert records: `8202`
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

- `market_context_high->crypto_alt_4h` score `12.7085` n `132` status `ready` deltaP `36.3868` edge `0.9101` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6896` n `132` status `ready` deltaP `41.8237` edge `0.7483` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4214` n `132` status `ready` deltaP `21.2214` edge `0.3782` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8191` n `43` status `ready` deltaP `31.8526` edge `0.3444` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.6313` n `132` status `ready` deltaP `29.0247` edge `0.5906` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.503` n `132` status `ready` deltaP `24.0253` edge `0.2412` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2326` n `132` status `ready` deltaP `17.7146` edge `0.199` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `3.013` n `132` status `ready` deltaP `16.3582` edge `0.2284` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.9709` n `132` status `ready` deltaP `24.3348` edge `0.1537` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5784` n `132` status `ready` deltaP `10.9059` edge `0.265` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.5162` n `132` status `ready` deltaP `20.2336` edge `1.0159` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.4961` n `132` status `ready` deltaP `18.0478` edge `0.1431` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4419` n `43` status `ready` deltaP `21.3445` edge `0.0248` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.2945` n `43` status `ready` deltaP `-2.6837` edge `0.3046` maxDD `-4.6598`
- `news_risk_high->unknown_4h` score `1.2578` n `43` status `ready` deltaP `14.3151` edge `0.0817` maxDD `-2.7857`
- `market_context_high->equity_24h` score `0.9229` n `132` status `ready` deltaP `21.4646` edge `0.4184` maxDD `-33.1007`
- `news_risk_high->commodity_1h` score `0.7533` n `43` status `ready` deltaP `10.7645` edge `0.0928` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4393` n `43` status `ready` deltaP `7.8401` edge `0.01` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2513` n `132` status `ready` deltaP `8.5919` edge `0.0425` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T00:17:55.348382+00:00`
- Price records: `672`
- Market context records: `2193`
- Flow alert records: `8205`
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

- `market_context_high->crypto_alt_4h` score `12.6819` n `132` status `ready` deltaP `36.2343` edge `0.9089` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `11.6654` n `132` status `ready` deltaP `41.6713` edge `0.7473` maxDD `-1.9063`
- `market_context_high->unknown_4h` score `5.4202` n `132` status `ready` deltaP `21.2214` edge `0.3781` maxDD `-2.4317`
- `news_risk_high->commodity_4h` score `3.8214` n `43` status `ready` deltaP `31.8526` edge `0.3447` maxDD `-3.0367`
- `market_context_high->unknown_24h` score `3.5874` n `132` status `ready` deltaP `28.8511` edge `0.5881` maxDD `-32.8525`
- `market_context_high->equity_4h` score `3.4946` n `132` status `ready` deltaP `24.0253` edge `0.2405` maxDD `-5.0894`
- `market_context_high->crypto_major_1h` score `3.2146` n `132` status `ready` deltaP `17.5649` edge `0.1985` maxDD `-1.817`
- `market_context_high->crypto_alt_1h` score `2.989` n `132` status `ready` deltaP `16.2085` edge `0.2274` maxDD `-4.9097`
- `market_context_high->index_4h` score `2.9757` n `132` status `ready` deltaP `24.3348` edge `0.1541` maxDD `-1.8022`
- `market_context_high->index_24h` score `2.5664` n `132` status `ready` deltaP `10.9059` edge `0.264` maxDD `-4.1604`
- `market_context_high->crypto_major_24h` score `2.4744` n `132` status `ready` deltaP `20.0599` edge `1.0117` maxDD `-60.2561`
- `news_risk_high->fx_4h` score `2.1976` n `43` status `ready` deltaP `27.8892` edge `0.0156` maxDD `-0.1382`
- `market_context_high->metal_4h` score `1.4755` n `132` status `ready` deltaP `17.8954` edge `0.1424` maxDD `-4.7664`
- `news_risk_high->unknown_1h` score `1.4192` n `43` status `ready` deltaP `21.1948` edge `0.0239` maxDD `-1.7548`
- `news_risk_high->equity_4h` score `1.289` n `43` status `ready` deltaP `-2.6837` edge `0.3039` maxDD `-4.6598`
- `news_risk_high->unknown_4h` score `1.2566` n `43` status `ready` deltaP `14.3151` edge `0.0816` maxDD `-2.7857`
- `market_context_high->equity_24h` score `0.8262` n `132` status `ready` deltaP `21.291` edge `0.4115` maxDD `-33.1007`
- `news_risk_high->commodity_1h` score `0.7533` n `43` status `ready` deltaP `10.7645` edge `0.0928` maxDD `-2.1052`
- `news_risk_high->fx_1h` score `0.4381` n `43` status `ready` deltaP `7.8401` edge `0.0099` maxDD `-0.0524`
- `market_context_high->equity_1h` score `0.2525` n `132` status `ready` deltaP `8.5919` edge `0.0426` maxDD `-2.6402`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

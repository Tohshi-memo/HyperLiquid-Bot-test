# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-29T12:52:21.007434+00:00`
- Price records: `672`
- Market context records: `2246`
- Flow alert records: `8358`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9227`

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

- `news_risk_high->crypto_alt_24h` score `25.0018` n `41` status `ready` deltaP `55.1914` edge `1.7744` maxDD `-4.3757`
- `news_risk_high->metal_24h` score `16.3206` n `41` status `ready` deltaP `44.9568` edge `1.1043` maxDD `-3.1836`
- `news_risk_high->equity_24h` score `15.6837` n `41` status `ready` deltaP `35.9291` edge `1.0989` maxDD `-2.1831`
- `market_context_high->crypto_alt_4h` score `11.8149` n `131` status `ready` deltaP `31.6713` edge `0.8754` maxDD `-5.1574`
- `market_context_high->crypto_major_4h` score `10.6039` n `131` status `ready` deltaP `37.9363` edge `0.697` maxDD `-2.9664`
- `news_risk_high->unknown_24h` score `9.832` n `41` status `ready` deltaP `36.0942` edge `0.6013` maxDD `-1.4744`
- `market_context_high->unknown_24h` score `9.6301` n `117` status `ready` deltaP `30.7158` edge `0.6669` maxDD `-3.8663`
- `news_risk_high->crypto_major_24h` score `8.8737` n `41` status `ready` deltaP `24.5427` edge `1.0321` maxDD `-3.3119`
- `market_context_high->crypto_major_24h` score `6.7628` n `117` status `ready` deltaP `18.6432` edge `1.132` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `5.645` n `131` status `ready` deltaP `21.4497` edge `0.3728` maxDD `-1.6306`
- `market_context_high->index_4h` score `4.1221` n `131` status `ready` deltaP `31.5409` edge `0.1706` maxDD `-0.3228`
- `news_risk_high->commodity_4h` score `3.899` n `43` status `ready` deltaP `33.2246` edge `0.3455` maxDD `-3.0367`
- `news_risk_high->index_24h` score `3.6753` n `41` status `ready` deltaP `13.1182` edge `0.2607` maxDD `-1.3507`
- `news_risk_high->fx_24h` score `3.575` n `41` status `ready` deltaP `36.2085` edge `0.075` maxDD `-0.1442`
- `market_context_high->equity_4h` score `3.4977` n `131` status `ready` deltaP `21.9268` edge `0.2335` maxDD `-3.0566`
- `market_context_high->index_24h` score `3.4571` n `117` status `ready` deltaP `14.5566` edge `0.2428` maxDD `-1.4737`
- `market_context_high->equity_24h` score `3.3399` n `117` status `ready` deltaP `22.1288` edge `0.2835` maxDD `-6.8828`
- `market_context_high->crypto_alt_1h` score `2.514` n `143` status `ready` deltaP `14.6351` edge `0.1983` maxDD `-4.9097`
- `news_risk_high->fx_4h` score `2.1366` n `43` status `ready` deltaP `27.127` edge `0.0156` maxDD `-0.1382`
- `market_context_high->crypto_major_1h` score `2.0931` n `143` status `ready` deltaP `13.5359` edge `0.1702` maxDD `-3.2144`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

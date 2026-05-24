# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-24T17:22:16.190750+00:00`
- Price records: `672`
- Market context records: `1759`
- Flow alert records: `6963`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8872`

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

- `market_context_high->metal_24h` score `7.1876` n `168` status `ready` deltaP `27.505` edge `0.6582` maxDD `-12.7414`
- `market_context_high->crypto_alt_4h` score `6.1062` n `195` status `ready` deltaP `21.49` edge `0.5422` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.5676` n `195` status `ready` deltaP `22.9042` edge `0.4685` maxDD `-10.9117`
- `market_context_high->index_24h` score `4.1458` n `168` status `ready` deltaP `19.0228` edge `0.3415` maxDD `-4.1604`
- `market_context_high->unknown_24h` score `3.6174` n `168` status `ready` deltaP `15.1042` edge `0.7328` maxDD `-35.8966`
- `market_context_high->equity_4h` score `3.1373` n `195` status `ready` deltaP `16.9035` edge `0.2582` maxDD `-5.0894`
- `news_risk_high->commodity_1h` score `3.1175` n `30` status `ready` deltaP `24.4212` edge `0.1287` maxDD `-1.2043`
- `market_context_high->unknown_4h` score `2.9566` n `195` status `ready` deltaP `12.8697` edge `0.3877` maxDD `-11.1695`
- `market_context_high->equity_24h` score `2.9236` n `168` status `ready` deltaP `17.3363` edge `0.6179` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.9551` n `195` status `ready` deltaP `12.163` edge `0.1074` maxDD `-3.7119`
- `market_context_high->crypto_alt_1h` score `0.7882` n `195` status `ready` deltaP `7.4328` edge `0.1185` maxDD `-4.1892`
- `market_context_high->crypto_major_24h` score `0.7193` n `168` status `ready` deltaP `19.5189` edge `0.7884` maxDD `-62.3533`
- `market_context_high->crypto_major_1h` score `0.2311` n `195` status `ready` deltaP `4.7413` edge `0.095` maxDD `-3.9211`
- `market_context_high->equity_1h` score `0.0892` n `195` status `ready` deltaP `5.1428` edge `0.054` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.162` n `195` status `ready` deltaP `4.2254` edge `0.0215` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.2038` n `195` status `ready` deltaP `12.758` edge `0.158` maxDD `-12.5349`
- `news_risk_high->fx_1h` score `-0.5091` n `30` status `ready` deltaP `-5.7285` edge `-0.0009` maxDD `-0.0948`
- `market_context_high->metal_1h` score `-0.5172` n `195` status `ready` deltaP `5.7255` edge `0.0291` maxDD `-6.3532`
- `news_risk_high->unknown_1h` score `-0.5713` n `30` status `ready` deltaP `15.8084` edge `-0.1314` maxDD `-2.1115`
- `market_context_high->fx_24h` score `-0.5872` n `168` status `ready` deltaP `7.3164` edge `0.0072` maxDD `-1.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

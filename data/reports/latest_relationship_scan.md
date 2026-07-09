# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-09T06:07:29.578932+00:00`
- Price records: `672`
- Market context records: `6160`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11099`

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

- `news_risk_high->crypto_alt_24h` score `12.3275` n `30` status `ready` deltaP `42.4712` edge `0.7589` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `7.5064` n `30` status `ready` deltaP `66.0345` edge `0.1853` maxDD `0.0`
- `news_risk_high->fx_4h` score `4.2078` n `32` status `ready` deltaP `43.8068` edge `0.0632` maxDD `-0.0345`
- `news_risk_high->fx_1h` score `2.4214` n `32` status `ready` deltaP `29.1106` edge `0.0216` maxDD `-0.1113`
- `market_context_high->unknown_1h` score `1.6684` n `195` status `ready` deltaP `1.0418` edge `0.2329` maxDD `-3.7317`
- `news_risk_high->crypto_major_1h` score `1.2279` n `32` status `ready` deltaP `13.1586` edge `0.1164` maxDD `-2.0691`
- `news_risk_high->crypto_major_24h` score `0.9861` n `30` status `ready` deltaP `14.023` edge `0.1109` maxDD `-4.2368`
- `news_risk_high->crypto_alt_1h` score `0.6339` n `32` status `ready` deltaP `8.4034` edge `0.0714` maxDD `-1.6923`
- `market_context_high->unknown_4h` score `0.1285` n `195` status `ready` deltaP `-0.9091` edge `0.27` maxDD `-11.925`
- `market_context_high->equity_4h` score `0.0262` n `195` status `ready` deltaP `3.0303` edge `0.0737` maxDD `-2.671`
- `market_context_high->metal_24h` score `-0.0125` n `195` status `ready` deltaP `19.8055` edge `0.1232` maxDD `-11.8809`
- `news_risk_high->index_24h` score `-0.2344` n `30` status `ready` deltaP `7.4712` edge `0.0073` maxDD `-2.3058`
- `market_context_high->fx_1h` score `-0.2563` n `195` status `ready` deltaP `1.8029` edge `-0.0003` maxDD `-0.5659`
- `market_context_high->metal_4h` score `-0.5753` n `195` status `ready` deltaP `4.1842` edge `0.0171` maxDD `-3.4996`
- `news_risk_high->commodity_24h` score `-0.5895` n `30` status `ready` deltaP `13.9081` edge `-0.1213` maxDD `-0.3101`
- `market_context_high->commodity_1h` score `-0.7245` n `195` status `ready` deltaP `-1.7615` edge `-0.004` maxDD `-0.5708`
- `news_risk_high->metal_1h` score `-0.7681` n `32` status `ready` deltaP `-3.0643` edge `-0.0283` maxDD `-1.6464`
- `market_context_high->metal_1h` score `-0.816` n `195` status `ready` deltaP `2.3203` edge `-0.0036` maxDD `-2.0564`
- `market_context_high->equity_1h` score `-0.8877` n `195` status `ready` deltaP `-1.8237` edge `0.0099` maxDD `-4.2573`
- `market_context_high->crypto_alt_1h` score `-0.942` n `195` status `ready` deltaP `3.3874` edge `0.0319` maxDD `-9.3536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

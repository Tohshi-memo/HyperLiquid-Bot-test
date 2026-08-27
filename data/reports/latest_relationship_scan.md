# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-27T17:37:46.935501+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14777`

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

- `news_risk_high->unknown_24h` score `52.131` n `50` status `ready` deltaP `11.6319` edge `4.2667` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `21.1926` n `50` status `ready` deltaP `37.8403` edge `1.5579` maxDD `-2.8629`
- `news_risk_high->unknown_4h` score `13.1069` n `50` status `ready` deltaP `27.5366` edge `0.9186` maxDD `-0.1279`
- `news_risk_high->metal_24h` score `4.7524` n `50` status `ready` deltaP `46.0903` edge `0.093` maxDD `-0.0053`
- `news_risk_high->equity_24h` score `4.5379` n `50` status `ready` deltaP `25.8403` edge `0.2987` maxDD `-4.7584`
- `news_risk_high->fx_4h` score `4.0235` n `50` status `ready` deltaP `46.878` edge `0.0318` maxDD `-0.0559`
- `news_risk_high->unknown_1h` score `3.1062` n `50` status `ready` deltaP `17.4251` edge `0.1783` maxDD `-0.8495`
- `market_context_high->unknown_24h` score `2.7066` n `128` status `ready` deltaP `5.3819` edge `0.2629` maxDD `-3.1917`
- `market_context_high->unknown_4h` score `2.6639` n `148` status `ready` deltaP `20.6988` edge `0.1247` maxDD `-0.5894`
- `news_risk_high->index_24h` score `2.6311` n `50` status `ready` deltaP `29.8403` edge `0.0354` maxDD `-0.2064`
- `news_risk_high->fx_1h` score `1.5815` n `50` status `ready` deltaP `21.1018` edge `0.0081` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `1.1415` n `50` status `ready` deltaP `16.6647` edge `0.0119` maxDD `-0.2301`
- `market_context_high->unknown_1h` score `0.9828` n `148` status `ready` deltaP `9.7224` edge `0.0621` maxDD `-1.6015`
- `news_risk_high->equity_4h` score `0.7553` n `50` status `ready` deltaP `18.6829` edge `0.0147` maxDD `-2.105`
- `news_risk_high->commodity_1h` score `0.5292` n `50` status `ready` deltaP `14.5988` edge `0.0018` maxDD `-0.5024`
- `news_risk_high->index_1h` score `0.1296` n `50` status `ready` deltaP `7.509` edge `0.0005` maxDD `-0.0486`
- `news_risk_high->metal_1h` score `0.0695` n `50` status `ready` deltaP `4.9521` edge `-0.0015` maxDD `-0.1413`
- `news_risk_high->metal_4h` score `-0.0811` n `50` status `ready` deltaP `7.4634` edge `-0.0034` maxDD `-0.249`
- `news_risk_high->index_4h` score `-0.1451` n `50` status `ready` deltaP `4.4939` edge `-0.0024` maxDD `-0.1719`
- `market_context_high->metal_4h` score `-0.4339` n `148` status `ready` deltaP `6.3283` edge `-0.0061` maxDD `-3.3377`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

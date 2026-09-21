# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T05:22:27.557050+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9296`

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

- `market_context_high->unknown_4h` score `36.3757` n `58` status `ready` deltaP `1.23` edge `3.0381` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.2965` n `98` status `ready` deltaP `12.0961` edge `2.6299` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.0545` n `98` status `ready` deltaP `12.8366` edge `1.9904` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.636` n `101` status `ready` deltaP `20.291` edge `0.372` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.0081` n `101` status `ready` deltaP `21.358` edge `0.3174` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.7642` n `101` status `ready` deltaP `16.3811` edge `0.1677` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1623` n `101` status `ready` deltaP `18.4769` edge `0.1093` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1811` n `98` status `ready` deltaP `23.2958` edge `0.1267` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0632` n `58` status `ready` deltaP `7.9548` edge `0.0609` maxDD `-0.36`
- `market_context_high->index_1h` score `0.855` n `58` status `ready` deltaP `12.2238` edge `0.0153` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6329` n `101` status `ready` deltaP `14.7477` edge `0.0146` maxDD `-0.8144`
- `market_context_high->index_4h` score `0.4402` n `58` status `ready` deltaP `16.4582` edge `0.0104` maxDD `-1.0949`
- `news_risk_high->metal_4h` score `0.4152` n `101` status `ready` deltaP `15.422` edge `0.0372` maxDD `-2.0994`
- `market_context_high->metal_1h` score `0.3549` n `58` status `ready` deltaP `6.2978` edge `0.0184` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.2816` n `58` status `ready` deltaP `8.0271` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1663` n `101` status `ready` deltaP `8.1834` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0117` n `101` status `ready` deltaP `3.5676` edge `0.0158` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.1226` n `58` status `ready` deltaP `-1.3421` edge `0.0706` maxDD `-2.7494`
- `news_risk_high->fx_1h` score `-0.2675` n `101` status `ready` deltaP `2.3937` edge `0.0061` maxDD `-0.2147`
- `news_risk_high->metal_24h` score `-0.3123` n `98` status `ready` deltaP `10.1226` edge `-0.0231` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

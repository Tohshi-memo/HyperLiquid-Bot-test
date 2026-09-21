# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T04:37:26.896150+00:00`
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

- `market_context_high->unknown_4h` score `24.5757` n `56` status `ready` deltaP `1.0453` edge `2.056` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `24.5062` n `98` status `ready` deltaP `12.617` edge `2.6439` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `19.3758` n `98` status `ready` deltaP `13.3574` edge `2.0137` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `4.6868` n `101` status `ready` deltaP `20.5958` edge `0.3742` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.9295` n `101` status `ready` deltaP `20.9007` edge `0.3139` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.757` n `101` status `ready` deltaP `16.3811` edge `0.1671` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.1719` n `101` status `ready` deltaP `18.6266` edge `0.1091` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.1275` n `98` status `ready` deltaP `22.775` edge `0.1233` maxDD `-3.4467`
- `market_context_high->equity_1h` score `1.0512` n `58` status `ready` deltaP `7.8051` edge `0.0609` maxDD `-0.36`
- `market_context_high->index_1h` score `0.8418` n `58` status `ready` deltaP `12.0741` edge `0.0152` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.6448` n `101` status `ready` deltaP `14.8974` edge `0.0146` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.4406` n `101` status `ready` deltaP `15.5744` edge `0.0383` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.427` n `56` status `ready` deltaP `16.115` edge `0.011` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.3669` n `58` status `ready` deltaP `6.4475` edge `0.0184` maxDD `-0.1314`
- `market_context_high->fx_1h` score `0.2935` n `58` status `ready` deltaP `8.1768` edge `0.0056` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.1663` n `101` status `ready` deltaP `8.1834` edge `0.0229` maxDD `-0.421`
- `news_risk_high->equity_1h` score `-0.0236` n `101` status `ready` deltaP `3.4179` edge `0.0158` maxDD `-0.9112`
- `market_context_high->crypto_major_1h` score `-0.113` n `58` status `ready` deltaP `-1.1924` edge `0.0704` maxDD `-2.7494`
- `news_risk_high->equity_24h` score `-0.2545` n `98` status `ready` deltaP `13.0987` edge `0.0324` maxDD `-4.941`
- `news_risk_high->fx_1h` score `-0.2555` n `101` status `ready` deltaP `2.5434` edge `0.0061` maxDD `-0.2147`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-04T15:07:31.645217+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5032`

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

- `market_context_high->unknown_4h` score `98.1612` n `90` status `ready` deltaP `3.1741` edge `8.1901` maxDD `-0.4928`
- `market_context_high->unknown_1h` score `96.0356` n `97` status `ready` deltaP `-0.6096` edge `8.0485` maxDD `-0.9839`
- `news_risk_high->crypto_major_4h` score `10.5675` n `65` status `ready` deltaP `37.5821` edge `0.6504` maxDD `-0.6258`
- `market_context_high->crypto_alt_24h` score `10.3505` n `46` status `ready` deltaP `26.6154` edge `0.8124` maxDD `-8.1838`
- `market_context_high->crypto_major_24h` score `10.1403` n `46` status `ready` deltaP `33.054` edge `0.6899` maxDD `-4.5519`
- `news_risk_high->equity_24h` score `8.3898` n `65` status `ready` deltaP `24.0545` edge `0.5488` maxDD `-0.1344`
- `news_risk_high->crypto_alt_4h` score `7.3247` n `65` status `ready` deltaP `24.3598` edge `0.5824` maxDD `-6.4195`
- `market_context_high->crypto_major_4h` score `5.1568` n `90` status `ready` deltaP `21.9411` edge `0.3538` maxDD `-3.294`
- `news_risk_high->index_24h` score `3.9547` n `65` status `ready` deltaP `27.0833` edge `0.149` maxDD `0.0`
- `news_risk_high->equity_4h` score `3.8188` n `65` status `ready` deltaP `25.9123` edge `0.2065` maxDD `-2.881`
- `news_risk_high->index_4h` score `3.1306` n `65` status `ready` deltaP `34.0479` edge `0.0601` maxDD `-0.4296`
- `news_risk_high->crypto_major_1h` score `2.8729` n `65` status `ready` deltaP `12.4113` edge `0.1922` maxDD `-1.5096`
- `news_risk_high->metal_4h` score `2.5878` n `65` status `ready` deltaP `22.2796` edge `0.1087` maxDD `-0.993`
- `market_context_high->crypto_major_1h` score `2.1344` n `97` status `ready` deltaP `15.3297` edge `0.1207` maxDD `-2.2692`
- `news_risk_high->index_1h` score `2.1213` n `65` status `ready` deltaP `26.0663` edge `0.018` maxDD `-0.1997`
- `market_context_high->equity_24h` score `1.8485` n `46` status `ready` deltaP `4.1213` edge `0.2257` maxDD `-6.264`
- `market_context_high->crypto_alt_4h` score `1.5727` n `90` status `ready` deltaP `5.4709` edge `0.2735` maxDD `-7.6465`
- `news_risk_high->crypto_alt_1h` score `1.4611` n `65` status `ready` deltaP `4.719` edge `0.1422` maxDD `-2.4854`
- `market_context_high->fx_4h` score `1.4483` n `90` status `ready` deltaP `25.4641` edge `0.0266` maxDD `-0.3868`
- `market_context_high->fx_24h` score `1.3607` n `46` status `ready` deltaP `25.536` edge `0.106` maxDD `-1.8102`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

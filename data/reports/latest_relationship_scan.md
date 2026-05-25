# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T00:52:14.312940+00:00`
- Price records: `672`
- Market context records: `1794`
- Flow alert records: `7059`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8892`

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

- `market_context_high->metal_24h` score `7.3258` n `191` status `ready` deltaP `28.7376` edge `0.6615` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.3906` n `30` status `ready` deltaP `28.9533` edge `0.405` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.7868` n `195` status `ready` deltaP `21.6979` edge `0.5142` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.3883` n `195` status `ready` deltaP `22.6548` edge `0.4485` maxDD `-10.3739`
- `market_context_high->unknown_4h` score `3.7866` n `195` status `ready` deltaP `15.8216` edge `0.4295` maxDD `-10.5542`
- `news_risk_high->commodity_1h` score `3.2566` n `30` status `ready` deltaP `24.8703` edge `0.1373` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9747` n `195` status `ready` deltaP `16.4462` edge `0.2477` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.6459` n `191` status `ready` deltaP `13.609` edge `0.2526` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.4242` n `191` status `ready` deltaP `15.3642` edge `0.5061` maxDD `-33.1875`
- `market_context_high->index_4h` score `0.904` n `195` status `ready` deltaP `12.6203` edge `0.1001` maxDD `-3.7119`
- `news_risk_high->fx_4h` score `0.8474` n `30` status `ready` deltaP `20.874` edge `-0.0033` maxDD `-0.1774`
- `market_context_high->unknown_24h` score `0.7277` n `191` status `ready` deltaP `12.0874` edge `0.5121` maxDD `-35.8966`
- `news_risk_high->unknown_4h` score `0.4622` n `30` status `ready` deltaP `10.437` edge `0.062` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3291` n `198` status `ready` deltaP `6.9573` edge `0.0922` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.1029` n `198` status `ready` deltaP `4.5258` edge `0.0813` maxDD `-3.5652`
- `market_context_high->equity_1h` score `-0.0428` n `198` status `ready` deltaP `4.6922` edge `0.046` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.3223` n `198` status `ready` deltaP `2.8973` edge `0.017` maxDD `-1.7205`
- `market_context_high->metal_4h` score `-0.3776` n `195` status `ready` deltaP `12.3562` edge `0.1384` maxDD `-12.5349`
- `market_context_high->fx_24h` score `-0.3986` n `191` status `ready` deltaP `8.7888` edge `0.0131` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4154` n `30` status `ready` deltaP `17.006` edge `-0.1194` maxDD `-2.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T04:22:19.845376+00:00`
- Price records: `672`
- Market context records: `1808`
- Flow alert records: `7102`
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

- `market_context_high->crypto_alt_4h` score `7.1908` n `184` status `ready` deltaP `23.4756` edge `0.5572` maxDD `-5.1574`
- `market_context_high->metal_24h` score `6.8636` n `179` status `ready` deltaP `27.6846` edge `0.63` maxDD `-12.7414`
- `market_context_high->crypto_major_4h` score `6.6027` n `184` status `ready` deltaP `27.2733` edge `0.5007` maxDD `-5.2502`
- `news_risk_high->commodity_4h` score `6.5221` n `30` status `ready` deltaP `29.563` edge `0.4119` maxDD `-3.5713`
- `market_context_high->unknown_4h` score `4.5673` n `184` status `ready` deltaP `17.2985` edge `0.4734` maxDD `-9.9822`
- `market_context_high->index_24h` score `3.589` n `179` status `ready` deltaP `17.4038` edge `0.3059` maxDD `-4.1604`
- `news_risk_high->commodity_1h` score `3.3213` n `30` status `ready` deltaP `25.1697` edge `0.1407` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.9508` n `184` status `ready` deltaP `15.7874` edge `0.2501` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.88` n `179` status `ready` deltaP `18.8615` edge `0.6041` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `2.1478` n `179` status `ready` deltaP `12.5582` edge `0.6273` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9081` n `30` status `ready` deltaP `21.6362` edge `-0.0006` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8062` n `184` status `ready` deltaP `11.5324` edge `0.0992` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.4041` n `186` status `ready` deltaP `5.9687` edge `0.0925` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.3909` n `30` status `ready` deltaP `9.9796` edge `0.0559` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3034` n `186` status `ready` deltaP `6.5337` edge `0.0931` maxDD `-4.9097`
- `market_context_high->equity_1h` score `-0.1288` n `186` status `ready` deltaP `4.1321` edge `0.0411` maxDD `-2.6836`
- `market_context_high->crypto_major_24h` score `-0.2625` n `179` status `ready` deltaP `18.0759` edge `0.7162` maxDD `-62.3533`
- `market_context_high->fx_24h` score `-0.4449` n `179` status `ready` deltaP `9.2596` edge `0.0061` maxDD `-1.3925`
- `market_context_high->unknown_1h` score `-0.4546` n `186` status `ready` deltaP `3.5461` edge `0.0426` maxDD `-4.3299`
- `news_risk_high->fx_1h` score `-0.4546` n `30` status `ready` deltaP `-4.8303` edge `0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

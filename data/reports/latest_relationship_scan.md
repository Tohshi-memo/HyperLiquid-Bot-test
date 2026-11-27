# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-27T09:22:27.633749+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `2886`

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

- `news_risk_high->unknown_1h` score `3225.1753` n `31` status `ready` deltaP `1.6322` edge `268.7713` maxDD `-0.7395`
- `news_risk_high->unknown_4h` score `3183.8002` n `31` status `ready` deltaP `3.7864` edge `265.2971` maxDD `-0.1191`
- `news_risk_high->crypto_major_24h` score `19.697` n `31` status `ready` deltaP `29.6875` edge `1.4435` maxDD `0.0`
- `news_risk_high->equity_24h` score `17.6141` n `31` status `ready` deltaP `29.1667` edge `1.2734` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `14.6944` n `31` status `ready` deltaP `28.8194` edge `1.0324` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.7299` n `31` status `ready` deltaP `21.2726` edge `0.6727` maxDD `-5.2957`
- `news_risk_high->equity_4h` score `6.5173` n `31` status `ready` deltaP `30.6698` edge `0.3867` maxDD `-2.178`
- `news_risk_high->crypto_major_4h` score `5.551` n `31` status `ready` deltaP `14.3391` edge `0.7578` maxDD `-7.6714`
- `news_risk_high->metal_24h` score `5.0489` n `31` status `ready` deltaP `17.1035` edge `0.3342` maxDD `-0.1986`
- `news_risk_high->fx_24h` score `4.6334` n `31` status `ready` deltaP `38.5865` edge `0.1417` maxDD `-0.0262`
- `news_risk_high->index_24h` score `3.1783` n `31` status `ready` deltaP `30.7292` edge `0.06` maxDD `0.0`
- `news_risk_high->index_4h` score `2.564` n `31` status `ready` deltaP `29.9076` edge `0.0403` maxDD `-0.4146`
- `news_risk_high->equity_1h` score `2.5345` n `31` status `ready` deltaP `15.9455` edge `0.1236` maxDD `-0.1621`
- `news_risk_high->index_1h` score `2.3691` n `31` status `ready` deltaP `28.6991` edge `0.0146` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.0332` n `31` status `ready` deltaP `6.4178` edge `0.264` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `1.8403` n `31` status `ready` deltaP `9.5615` edge `0.2079` maxDD `-1.5232`
- `news_risk_high->metal_1h` score `1.1301` n `31` status `ready` deltaP `24.6426` edge `0.0085` maxDD `-0.2315`
- `news_risk_high->metal_4h` score `0.3807` n `31` status `ready` deltaP `11.9001` edge `0.0252` maxDD `-0.7918`
- `news_risk_high->commodity_4h` score `-0.0666` n `31` status `ready` deltaP `5.9304` edge `-0.0083` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.6971` n `31` status `ready` deltaP `-5.2057` edge `0.0028` maxDD `-0.0947`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

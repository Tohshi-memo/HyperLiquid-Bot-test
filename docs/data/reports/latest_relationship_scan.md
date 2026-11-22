# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T21:07:23.910680+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5126`

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

- `market_context_high->unknown_1h` score `12031.3568` n `106` status `ready` deltaP `-0.1978` edge `1002.6342` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7676.5168` n `104` status `ready` deltaP `-2.4508` edge `639.7566` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1388.4814` n `31` status `ready` deltaP `3.728` edge `115.6995` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1214.5129` n `31` status `ready` deltaP `3.9388` edge `101.1888` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1448` n `31` status `ready` deltaP `40.2734` edge `0.7918` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0695` n `31` status `ready` deltaP `25.6933` edge `0.8382` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8337` n `31` status `ready` deltaP `15.711` edge `0.9131` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9894` n `31` status `ready` deltaP `19.5383` edge `0.2209` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.5862` n `31` status `ready` deltaP `37.2247` edge `0.0767` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7358` n `31` status `ready` deltaP `31.9925` edge `0.0232` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4829` n `31` status `ready` deltaP `9.7112` edge `0.2997` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0939` n `31` status `ready` deltaP `8.6633` edge `0.2464` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.6504` n `31` status `ready` deltaP `22.1135` edge `0.1199` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.582` n `31` status `ready` deltaP `29.7324` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7723` n `31` status `ready` deltaP `17.6682` edge `0.021` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.369` n `106` status `ready` deltaP `1.7653` edge `0.0074` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4602` n `106` status `ready` deltaP `1.3473` edge `0.0014` maxDD `-1.2322`
- `market_context_high->fx_1h` score `-1.352` n `106` status `ready` deltaP `-10.2135` edge `-0.0016` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5657` n `104` status `ready` deltaP `-1.1726` edge `0.0043` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

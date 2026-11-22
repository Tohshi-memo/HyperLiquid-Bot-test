# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T20:52:26.639882+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5110`

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

- `market_context_high->unknown_1h` score `12013.6388` n `106` status `ready` deltaP `-0.1978` edge `1001.1577` maxDD `-0.9188`
- `market_context_high->unknown_4h` score `7569.4469` n `105` status `ready` deltaP `-2.3592` edge `630.8335` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1391.8234` n `31` status `ready` deltaP `3.728` edge `115.978` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1214.5009` n `31` status `ready` deltaP `3.9388` edge `101.1878` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.1244` n `31` status `ready` deltaP `40.2734` edge `0.7901` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0381` n `31` status `ready` deltaP `25.5409` edge `0.8366` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8228` n `31` status `ready` deltaP `15.711` edge `0.9117` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `3.9882` n `31` status `ready` deltaP `19.5383` edge `0.2208` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.5704` n `31` status `ready` deltaP `37.0722` edge `0.0764` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7346` n `31` status `ready` deltaP `31.9925` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4829` n `31` status `ready` deltaP `9.7112` edge `0.2997` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.09` n `31` status `ready` deltaP `8.6633` edge `0.2459` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.637` n `31` status `ready` deltaP `21.961` edge `0.1192` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5734` n `31` status `ready` deltaP `29.5827` edge `0.0324` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7754` n `31` status `ready` deltaP `17.6682` edge `0.0214` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0669` n `31` status `ready` deltaP `1.3811` edge `0.0114` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.3239` n `106` status `ready` deltaP `2.559` edge `0.0079` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.459` n `106` status `ready` deltaP `1.3473` edge `0.0015` maxDD `-1.2322`
- `market_context_high->fx_1h` score `-1.2874` n `106` status `ready` deltaP `-9.4199` edge `-0.0015` maxDD `-0.4384`
- `market_context_high->fx_4h` score `-1.5424` n `105` status `ready` deltaP `-0.739` edge `0.0044` maxDD `-1.444`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

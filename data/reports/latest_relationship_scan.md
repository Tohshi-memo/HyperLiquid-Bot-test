# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-22T22:22:26.869435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5108`

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

- `market_context_high->unknown_1h` score `12347.9495` n `104` status `ready` deltaP `0.4145` edge `1029.0092` maxDD `-0.6271`
- `market_context_high->unknown_4h` score `8241.6061` n `99` status `ready` deltaP `-2.7839` edge `686.8496` maxDD `-0.7759`
- `news_risk_high->unknown_1h` score `1377.0538` n `31` status `ready` deltaP `3.5783` edge `114.7482` maxDD `-0.7389`
- `news_risk_high->unknown_4h` score `1211.4843` n `31` status `ready` deltaP `4.0913` edge `100.9354` maxDD `-0.119`
- `news_risk_high->equity_4h` score `12.2146` n `31` status `ready` deltaP `40.4259` edge `0.7966` maxDD `-2.1911`
- `news_risk_high->crypto_alt_4h` score `11.0829` n `31` status `ready` deltaP `25.8457` edge `0.8383` maxDD `-5.2957`
- `news_risk_high->crypto_major_4h` score `6.8211` n `31` status `ready` deltaP `15.5586` edge `0.9125` maxDD `-7.6714`
- `news_risk_high->equity_1h` score `4.0206` n `31` status `ready` deltaP `19.8377` edge `0.2215` maxDD `-0.163`
- `news_risk_high->index_4h` score `3.6336` n `31` status `ready` deltaP `37.682` edge `0.0776` maxDD `-0.4146`
- `news_risk_high->index_1h` score `2.7346` n `31` status `ready` deltaP `31.9925` edge `0.0231` maxDD `-0.0136`
- `news_risk_high->crypto_major_1h` score `2.4938` n `31` status `ready` deltaP `9.8609` edge `0.3001` maxDD `-1.6897`
- `news_risk_high->crypto_alt_1h` score `2.0768` n `31` status `ready` deltaP `8.3639` edge `0.2462` maxDD `-1.5232`
- `news_risk_high->metal_4h` score `1.7096` n `31` status `ready` deltaP `22.8757` edge `0.1224` maxDD `-0.7918`
- `news_risk_high->metal_1h` score `1.5664` n `31` status `ready` deltaP `29.433` edge `0.0325` maxDD `-0.2315`
- `news_risk_high->commodity_4h` score `0.7598` n `31` status `ready` deltaP `17.6682` edge `0.0194` maxDD `-0.5151`
- `news_risk_high->commodity_1h` score `-0.0801` n `31` status `ready` deltaP `1.2314` edge `0.0113` maxDD `-0.0947`
- `market_context_high->metal_1h` score `-0.2884` n `104` status `ready` deltaP `3.3164` edge `0.0074` maxDD `-2.6517`
- `market_context_high->index_1h` score `-0.4625` n `104` status `ready` deltaP `1.3473` edge `0.0013` maxDD `-1.2394`
- `market_context_high->fx_4h` score `-1.3113` n `99` status `ready` deltaP `0.1601` edge `0.0051` maxDD `-1.2764`
- `market_context_high->fx_1h` score `-1.3725` n `104` status `ready` deltaP `-10.6172` edge `-0.0011` maxDD `-0.3997`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

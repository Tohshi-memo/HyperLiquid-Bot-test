# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T01:52:18.124191+00:00`
- Price records: `672`
- Market context records: `1798`
- Flow alert records: `7072`
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

- `market_context_high->metal_24h` score `7.0562` n `188` status `ready` deltaP `28.487` edge `0.6407` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4726` n `30` status `ready` deltaP `29.2582` edge `0.4098` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `5.733` n `192` status `ready` deltaP `21.2652` edge `0.5126` maxDD `-9.1295`
- `market_context_high->crypto_major_4h` score `4.6543` n `192` status `ready` deltaP `23.7678` edge `0.4568` maxDD `-9.8583`
- `market_context_high->unknown_4h` score `4.1166` n `192` status `ready` deltaP `16.438` edge `0.4491` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2482` n `30` status `ready` deltaP `24.7206` edge `0.1376` maxDD `-1.2043`
- `market_context_high->equity_4h` score `2.8942` n `192` status `ready` deltaP `16.0696` edge `0.2435` maxDD `-5.0894`
- `market_context_high->index_24h` score `2.7647` n `188` status `ready` deltaP `13.8039` edge `0.2612` maxDD `-4.1604`
- `market_context_high->equity_24h` score `1.6473` n `188` status `ready` deltaP `15.8134` edge `0.5217` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.0163` n `188` status `ready` deltaP `12.0493` edge `0.5364` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.8869` n `30` status `ready` deltaP `21.4838` edge `-0.0023` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8505` n `192` status `ready` deltaP `12.1316` edge `0.0989` maxDD `-3.7119`
- `news_risk_high->unknown_4h` score `0.3721` n `30` status `ready` deltaP `9.9796` edge `0.0535` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.3422` n `194` status `ready` deltaP `7.0159` edge `0.0929` maxDD `-4.8924`
- `market_context_high->crypto_major_1h` score `0.2816` n `194` status `ready` deltaP `5.3368` edge `0.0865` maxDD `-3.2225`
- `market_context_high->equity_1h` score `-0.1537` n `194` status `ready` deltaP `4.0713` edge `0.0409` maxDD `-2.8014`
- `news_risk_high->unknown_1h` score `-0.4021` n `30` status `ready` deltaP `17.1557` edge `-0.1187` maxDD `-2.1115`
- `market_context_high->index_1h` score `-0.4074` n `194` status `ready` deltaP `2.0434` edge `0.0156` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.4268` n `188` status `ready` deltaP `8.7507` edge `0.011` maxDD `-1.3925`
- `news_risk_high->fx_1h` score `-0.4796` n `30` status `ready` deltaP `-5.2794` edge `-0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-25T02:52:15.580346+00:00`
- Price records: `672`
- Market context records: `1802`
- Flow alert records: `7084`
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

- `market_context_high->metal_24h` score `6.9274` n `185` status `ready` deltaP `28.2282` edge `0.6317` maxDD `-12.7414`
- `news_risk_high->commodity_4h` score `6.4666` n `30` status `ready` deltaP `29.2582` edge `0.4093` maxDD `-3.5713`
- `market_context_high->crypto_alt_4h` score `6.1808` n `190` status `ready` deltaP `21.717` edge `0.5226` maxDD `-7.8518`
- `market_context_high->crypto_major_4h` score `5.2451` n `190` status `ready` deltaP `24.6646` edge `0.4672` maxDD `-8.23`
- `market_context_high->unknown_4h` score `4.1583` n `190` status `ready` deltaP `16.4939` edge `0.4522` maxDD `-10.2508`
- `news_risk_high->commodity_1h` score `3.2338` n `30` status `ready` deltaP `24.5709` edge `0.1374` maxDD `-1.2043`
- `market_context_high->index_24h` score `3.0037` n `185` status `ready` deltaP `14.7222` edge `0.275` maxDD `-4.1604`
- `market_context_high->equity_4h` score `2.9215` n `190` status `ready` deltaP `16.1858` edge `0.245` maxDD `-5.0894`
- `market_context_high->equity_24h` score `2.0849` n `185` status `ready` deltaP `17.0223` edge `0.5501` maxDD `-33.1875`
- `market_context_high->unknown_24h` score `1.3665` n `185` status `ready` deltaP `11.9876` edge `0.566` maxDD `-35.8966`
- `news_risk_high->fx_4h` score `0.9003` n `30` status `ready` deltaP `21.6362` edge `-0.0016` maxDD `-0.1774`
- `market_context_high->index_4h` score `0.8489` n `190` status `ready` deltaP `12.1711` edge `0.0985` maxDD `-3.7119`
- `market_context_high->crypto_major_1h` score `0.3847` n `190` status `ready` deltaP `6.0259` edge `0.0905` maxDD `-3.2225`
- `news_risk_high->unknown_4h` score `0.365` n `30` status `ready` deltaP `9.8272` edge `0.0536` maxDD `-2.7857`
- `market_context_high->crypto_alt_1h` score `0.2609` n `190` status `ready` deltaP `6.4797` edge `0.0897` maxDD `-4.8924`
- `market_context_high->equity_1h` score `-0.2038` n `190` status `ready` deltaP `3.6448` edge `0.0381` maxDD `-2.6836`
- `market_context_high->index_1h` score `-0.4112` n `190` status `ready` deltaP `2.0564` edge `0.0152` maxDD `-1.7205`
- `market_context_high->fx_24h` score `-0.457` n `185` status `ready` deltaP `8.689` edge `0.0089` maxDD `-1.3925`
- `news_risk_high->unknown_1h` score `-0.4707` n `30` status `ready` deltaP `16.5569` edge `-0.1235` maxDD `-2.1115`
- `news_risk_high->fx_1h` score `-0.4718` n `30` status `ready` deltaP `-5.1297` edge `-0.0001` maxDD `-0.0948`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

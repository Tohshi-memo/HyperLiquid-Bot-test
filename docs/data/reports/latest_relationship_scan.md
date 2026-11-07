# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-07T10:37:28.714991+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4001`

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

- `market_context_high->equity_1h` score `4.0278` n `30` status `ready` deltaP `12.8842` edge `0.2957` maxDD `-2.3425`
- `news_risk_high->equity_4h` score `1.2668` n `62` status `ready` deltaP `11.8361` edge `0.1574` maxDD `-4.2454`
- `market_context_high->crypto_major_1h` score `0.6746` n `30` status `ready` deltaP `11.9461` edge `0.0654` maxDD `-3.0172`
- `market_context_high->fx_1h` score `0.6592` n `30` status `ready` deltaP `9.5908` edge `0.0181` maxDD `-0.1681`
- `news_risk_high->index_4h` score `0.6519` n `62` status `ready` deltaP `12.1656` edge `0.021` maxDD `-0.4888`
- `market_context_high->crypto_alt_1h` score `0.6498` n `30` status `ready` deltaP `12.994` edge `0.0782` maxDD `-3.1881`
- `market_context_high->index_1h` score `0.5974` n `30` status `ready` deltaP `4.3812` edge `0.0476` maxDD `-0.1621`
- `news_risk_high->index_24h` score `0.3345` n `62` status `ready` deltaP `9.9294` edge `0.1435` maxDD `-6.6786`
- `market_context_high->metal_1h` score `0.2229` n `30` status `ready` deltaP `5.9182` edge `0.0219` maxDD `-0.6226`
- `news_risk_high->fx_24h` score `0.0669` n `62` status `ready` deltaP `-2.5706` edge `0.0669` maxDD `-0.2016`
- `news_risk_high->index_1h` score `0.0629` n `62` status `ready` deltaP `7.4995` edge `0.0034` maxDD `-0.2931`
- `news_risk_high->equity_1h` score `-0.0854` n `62` status `ready` deltaP `-0.4491` edge `0.047` maxDD `-1.396`
- `market_context_high->commodity_1h` score `-0.1383` n `30` status `ready` deltaP `4.7206` edge `0.0054` maxDD `-1.7019`
- `news_risk_high->fx_1h` score `-0.1402` n `62` status `ready` deltaP `2.7091` edge `0.0025` maxDD `-0.0826`
- `news_risk_high->fx_4h` score `-0.1945` n `62` status `ready` deltaP `2.2718` edge `0.0045` maxDD `-0.2336`
- `news_risk_high->metal_1h` score `-0.5392` n `62` status `ready` deltaP `-3.9743` edge `-0.0069` maxDD `-0.5256`
- `news_risk_high->metal_4h` score `-0.9554` n `62` status `ready` deltaP `1.2687` edge `-0.0404` maxDD `-1.5773`
- `news_risk_high->crypto_alt_1h` score `-1.1681` n `62` status `ready` deltaP `-1.8447` edge `-0.0219` maxDD `-5.2444`
- `news_risk_high->crypto_major_4h` score `-1.2596` n `62` status `ready` deltaP `-3.0094` edge `0.019` maxDD `-8.5004`
- `news_risk_high->commodity_1h` score `-1.6362` n `62` status `ready` deltaP `-11.6235` edge `-0.0029` maxDD `-1.1434`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

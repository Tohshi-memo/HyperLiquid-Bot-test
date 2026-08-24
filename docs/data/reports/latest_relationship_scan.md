# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T09:22:31.528352+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14760`

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

- `news_risk_high->unknown_24h` score `49.4355` n `51` status `ready` deltaP `17.0139` edge `4.0062` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.1403` n `51` status `ready` deltaP `40.237` edge `1.0032` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `13.0383` n `51` status `ready` deltaP `24.2587` edge `0.9294` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.698` n `51` status `ready` deltaP `48.9481` edge `0.1637` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.7644` n `51` status `ready` deltaP `27.2328` edge `0.2092` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.6173` n `51` status `ready` deltaP `16.9337` edge `0.219` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.209` n `51` status `ready` deltaP `37.778` edge `0.029` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `1.9034` n `140` status `ready` deltaP `19.7909` edge `0.0675` maxDD `-0.5994`
- `market_context_high->unknown_24h` score `1.6507` n `84` status `ready` deltaP `3.9187` edge `0.1621` maxDD `-1.0533`
- `news_risk_high->metal_24h` score `1.5556` n `51` status `ready` deltaP `32.935` edge `-0.0857` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2314` n `51` status `ready` deltaP `16.8457` edge `0.0073` maxDD `-0.0257`
- `news_risk_high->index_4h` score `0.9727` n `51` status `ready` deltaP `14.1589` edge `0.0264` maxDD `-0.1788`
- `news_risk_high->equity_1h` score `0.967` n `51` status `ready` deltaP `18.6421` edge `0.0361` maxDD `-0.9128`
- `news_risk_high->index_1h` score `0.2504` n `51` status `ready` deltaP `9.4223` edge `0.0046` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.2207` n `51` status `ready` deltaP `8.8382` edge `-0.0097` maxDD `-0.4666`
- `market_context_high->metal_4h` score `0.1746` n `140` status `ready` deltaP `10.8058` edge `-0.0116` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `0.0384` n `140` status `ready` deltaP `11.0094` edge `-0.0253` maxDD `-1.5916`
- `news_risk_high->metal_1h` score `-0.1138` n `51` status `ready` deltaP `2.1927` edge `-0.0069` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.2203` n `51` status `ready` deltaP `6.7582` edge `-0.0103` maxDD `-0.249`
- `news_risk_high->crypto_alt_24h` score `-0.352` n `51` status `ready` deltaP `22.5694` edge `-0.1798` maxDD `0.0`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

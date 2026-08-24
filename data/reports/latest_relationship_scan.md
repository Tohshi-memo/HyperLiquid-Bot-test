# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T04:07:24.606657+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14856`

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

- `news_risk_high->unknown_24h` score `51.8626` n `51` status `ready` deltaP `17.1875` edge `4.2073` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3995` n `51` status `ready` deltaP `40.237` edge `1.0248` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9593` n `51` status `ready` deltaP `23.4965` edge `0.9279` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.83` n `51` status `ready` deltaP `48.9481` edge `0.1747` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.2865` n `51` status `ready` deltaP `25.0986` edge `0.1836` maxDD `-2.164`
- `news_risk_high->fx_4h` score `3.2115` n `51` status `ready` deltaP `37.778` edge `0.0292` maxDD `-0.0746`
- `news_risk_high->unknown_1h` score `2.9275` n `51` status `ready` deltaP `15.7361` edge `0.1695` maxDD `-0.7693`
- `market_context_high->unknown_4h` score `2.182` n `145` status `ready` deltaP `21.3194` edge `0.0534` maxDD `-0.0956`
- `news_risk_high->metal_24h` score `2.0141` n `51` status `ready` deltaP `36.5809` edge `-0.0718` maxDD `-0.0053`
- `news_risk_high->crypto_alt_24h` score `1.9592` n `51` status `ready` deltaP `26.2153` edge `-0.0115` maxDD `0.0`
- `market_context_high->unknown_1h` score `1.6338` n `157` status `ready` deltaP `9.8163` edge `0.1156` maxDD `-1.5916`
- `news_risk_high->fx_1h` score `1.2566` n `51` status `ready` deltaP `17.1451` edge `0.0074` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.8852` n `51` status `ready` deltaP `17.5942` edge `0.0326` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.8001` n `51` status `ready` deltaP `12.482` edge `0.0232` maxDD `-0.1788`
- `news_risk_high->index_1h` score `0.2239` n `51` status `ready` deltaP `8.9732` edge `0.0042` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1943` n `51` status `ready` deltaP `8.5388` edge `-0.0099` maxDD `-0.4666`
- `market_context_high->commodity_24h` score `0.0755` n `92` status `ready` deltaP `-3.3967` edge `0.0898` maxDD `-1.5979`
- `market_context_high->fx_24h` score `0.0133` n `92` status `ready` deltaP `10.2129` edge `0.0146` maxDD `-1.4788`
- `news_risk_high->metal_4h` score `-0.0525` n `51` status `ready` deltaP `8.435` edge `-0.0075` maxDD `-0.249`
- `news_risk_high->metal_1h` score `-0.1302` n `51` status `ready` deltaP `1.8933` edge `-0.007` maxDD `-0.1184`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

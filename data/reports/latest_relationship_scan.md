# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T00:07:21.938154+00:00`
- Price records: `672`
- Market context records: `2510`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9280`

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

- `market_context_high->unknown_24h` score `5.2023` n `121` status `ready` deltaP `19.6869` edge `0.3351` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.5936` n `150` status `ready` deltaP `21.3902` edge `0.5081` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8413` n `150` status `ready` deltaP `17.6565` edge `0.3834` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1659` n `121` status `ready` deltaP `11.9003` edge `0.5876` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `1.9627` n `150` status `ready` deltaP `11.315` edge `0.1931` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.7409` n `160` status `ready` deltaP `7.1819` edge `0.1326` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.4799` n `160` status `ready` deltaP `7.1557` edge `0.1117` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.1618` n `121` status `ready` deltaP `1.7533` edge `0.7048` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0396` n `121` status `ready` deltaP `3.6716` edge `0.0769` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1421` n `121` status `ready` deltaP `18.0685` edge `0.0204` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1544` n `150` status `ready` deltaP `6.4918` edge `0.028` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.3121` n `160` status `ready` deltaP `1.3735` edge `0.0043` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.4287` n `160` status `ready` deltaP `1.1976` edge `0.013` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.4289` n `160` status `ready` deltaP `2.1033` edge `0.0222` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4674` n `160` status `ready` deltaP `2.7021` edge `0.0099` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5975` n `160` status `ready` deltaP `-0.5389` edge `0.0032` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6669` n `150` status `ready` deltaP `-1.2947` edge `0.0091` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8158` n `121` status `ready` deltaP `4.0103` edge `0.0051` maxDD `-2.5804`
- `market_context_high->equity_1h` score `-0.8847` n `160` status `ready` deltaP `-0.2507` edge `0.0118` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.1675` n `150` status `ready` deltaP `2.3984` edge `0.0286` maxDD `-10.2078`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

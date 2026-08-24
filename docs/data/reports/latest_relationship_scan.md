# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-24T06:22:22.745500+00:00`
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

- `news_risk_high->unknown_24h` score `50.7579` n `51` status `ready` deltaP `17.0139` edge `4.1164` maxDD `0.0`
- `news_risk_high->equity_24h` score `14.3503` n `51` status `ready` deltaP `40.237` edge `1.0207` maxDD `-4.7801`
- `news_risk_high->unknown_4h` score `12.9243` n `51` status `ready` deltaP `23.3441` edge `0.926` maxDD `-0.0348`
- `news_risk_high->index_24h` score `5.7868` n `51` status `ready` deltaP `48.9481` edge `0.1711` maxDD `-0.2147`
- `news_risk_high->equity_4h` score `3.653` n `51` status `ready` deltaP `26.4706` edge `0.205` maxDD `-2.164`
- `news_risk_high->unknown_1h` score `3.5694` n `51` status `ready` deltaP `16.1852` edge `0.22` maxDD `-0.7693`
- `news_risk_high->fx_4h` score `3.2516` n `51` status `ready` deltaP `38.2353` edge `0.0295` maxDD `-0.0746`
- `market_context_high->unknown_4h` score `2.2536` n `145` status `ready` deltaP `21.8566` edge `0.0601` maxDD `-0.4407`
- `news_risk_high->metal_24h` score `1.8219` n `51` status `ready` deltaP `35.0184` edge `-0.0774` maxDD `-0.0053`
- `news_risk_high->fx_1h` score `1.2578` n `51` status `ready` deltaP `17.1451` edge `0.0075` maxDD `-0.0257`
- `news_risk_high->equity_1h` score `0.96` n `51` status `ready` deltaP `18.4924` edge `0.0362` maxDD `-0.9128`
- `news_risk_high->index_4h` score `0.9265` n `51` status `ready` deltaP `13.7015` edge `0.0256` maxDD `-0.1788`
- `news_risk_high->crypto_alt_24h` score `0.7602` n `51` status `ready` deltaP `24.6528` edge `-0.101` maxDD `0.0`
- `news_risk_high->index_1h` score `0.2675` n `51` status `ready` deltaP `9.7217` edge `0.0048` maxDD `-0.1583`
- `news_risk_high->commodity_1h` score `0.1775` n `51` status `ready` deltaP `8.3891` edge `-0.0103` maxDD `-0.4666`
- `news_risk_high->metal_1h` score `-0.1123` n `51` status `ready` deltaP `2.1927` edge `-0.0067` maxDD `-0.1184`
- `news_risk_high->metal_4h` score `-0.1267` n `51` status `ready` deltaP `7.6728` edge `-0.0086` maxDD `-0.249`
- `market_context_high->metal_4h` score `-0.2631` n `145` status `ready` deltaP `5.8337` edge `-0.0184` maxDD `-1.3378`
- `market_context_high->unknown_1h` score `-0.2847` n `152` status `ready` deltaP `9.4902` edge `-0.0421` maxDD `-1.5916`
- `market_context_high->metal_1h` score `-0.4108` n `152` status `ready` deltaP `-1.4064` edge `-0.0056` maxDD `-0.6822`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

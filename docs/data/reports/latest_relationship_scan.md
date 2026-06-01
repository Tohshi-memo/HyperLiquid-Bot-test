# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T00:37:22.049380+00:00`
- Price records: `672`
- Market context records: `2512`
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

- `market_context_high->unknown_24h` score `5.1759` n `121` status `ready` deltaP `19.6869` edge `0.3329` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.6769` n `151` status `ready` deltaP `21.5756` edge `0.5138` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.8815` n `151` status `ready` deltaP `17.8596` edge `0.3854` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.1776` n `121` status `ready` deltaP `11.9003` edge `0.5891` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.0347` n `151` status `ready` deltaP `11.5843` edge `0.1973` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `0.871` n `162` status `ready` deltaP `7.668` edge `0.1402` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5662` n `162` status `ready` deltaP `7.6495` edge `0.1156` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.2032` n `121` status `ready` deltaP `1.7533` edge `0.7101` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0564` n `121` status `ready` deltaP `3.6716` edge `0.0783` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1265` n `121` status `ready` deltaP `18.0685` edge `0.0217` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1361` n `151` status `ready` deltaP `6.7214` edge `0.028` maxDD `-2.3986`
- `market_context_high->fx_1h` score `-0.2781` n `162` status `ready` deltaP `1.9831` edge `0.0046` maxDD `-0.278`
- `market_context_high->metal_1h` score `-0.3929` n `162` status `ready` deltaP `1.3473` edge `0.0166` maxDD `-3.0759`
- `market_context_high->unknown_1h` score `-0.4494` n `162` status `ready` deltaP `2.057` edge `0.0208` maxDD `-3.0902`
- `market_context_high->commodity_1h` score `-0.4603` n `162` status `ready` deltaP `2.9737` edge `0.009` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.5303` n `162` status `ready` deltaP `0.0167` edge `0.0051` maxDD `-1.2855`
- `market_context_high->fx_4h` score `-0.6677` n `151` status `ready` deltaP `-1.2508` edge `0.0087` maxDD `-0.8774`
- `market_context_high->fx_24h` score `-0.8264` n `121` status `ready` deltaP `3.8367` edge `0.0049` maxDD `-2.5804`
- `market_context_high->equity_1h` score `-0.9001` n `162` status `ready` deltaP `-0.3973` edge `0.0115` maxDD `-2.7085`
- `market_context_high->metal_4h` score `-1.1031` n `151` status `ready` deltaP `1.8929` edge `0.0342` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

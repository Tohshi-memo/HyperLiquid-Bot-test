# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T02:07:24.310398+00:00`
- Price records: `672`
- Market context records: `2519`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->unknown_24h` score `4.9787` n `119` status `ready` deltaP `19.548` edge `0.3174` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7742` n `154` status `ready` deltaP `22.1175` edge `0.5183` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.7085` n `154` status `ready` deltaP `17.0019` edge `0.3767` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2563` n `119` status `ready` deltaP `11.8099` edge `0.5998` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.1598` n `154` status `ready` deltaP `12.2189` edge `0.2035` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0823` n `162` status `ready` deltaP `8.7344` edge `0.1507` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6957` n `162` status `ready` deltaP `8.2483` edge `0.1224` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0196` n `119` status `ready` deltaP `0.8782` edge `0.6924` maxDD `-43.6595`
- `market_context_high->index_24h` score `-0.0126` n `119` status `ready` deltaP `3.1994` edge `0.0757` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1562` n `119` status `ready` deltaP `17.8324` edge `0.0208` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.1679` n `154` status `ready` deltaP `6.3985` edge `0.0275` maxDD `-2.3986`
- `market_context_high->commodity_1h` score `-0.3875` n `162` status `ready` deltaP `3.9089` edge `0.0121` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4171` n `162` status `ready` deltaP `1.1015` edge `0.0073` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4648` n `162` status `ready` deltaP `1.0294` edge `0.0095` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4782` n `162` status `ready` deltaP `1.3843` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5229` n `162` status `ready` deltaP `2.0385` edge `0.0148` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.785` n `162` status `ready` deltaP `0.2015` edge `0.0171` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8289` n `119` status `ready` deltaP `3.6006` edge `0.0048` maxDD `-2.4729`
- `market_context_high->fx_4h` score `-0.8922` n `154` status `ready` deltaP `0.1524` edge `0.0106` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-1.0038` n `154` status `ready` deltaP `2.3539` edge `0.0394` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

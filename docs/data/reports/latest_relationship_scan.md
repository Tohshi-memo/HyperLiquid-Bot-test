# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T02:04:52.311395+00:00`
- Price records: `672`
- Market context records: `2518`
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

- `market_context_high->unknown_24h` score `4.9823` n `119` status `ready` deltaP `19.548` edge `0.3177` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.7598` n `154` status `ready` deltaP `22.1175` edge `0.5171` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.6965` n `154` status `ready` deltaP `17.0019` edge `0.3757` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.2594` n `119` status `ready` deltaP `11.8099` edge `0.6002` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.1214` n `154` status `ready` deltaP `12.2189` edge `0.2003` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0871` n `162` status `ready` deltaP `8.7344` edge `0.1511` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6981` n `162` status `ready` deltaP `8.2483` edge `0.1226` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0317` n `119` status `ready` deltaP `1.0519` edge `0.6928` maxDD `-43.6595`
- `market_context_high->index_24h` score `-0.0162` n `119` status `ready` deltaP `3.1994` edge `0.0754` maxDD `-2.5127`
- `market_context_high->index_4h` score `-0.1198` n `154` status `ready` deltaP `6.8954` edge `0.0282` maxDD `-2.3986`
- `market_context_high->equity_24h` score `-0.1562` n `119` status `ready` deltaP `17.8324` edge `0.0208` maxDD `-6.8828`
- `market_context_high->commodity_1h` score `-0.3875` n `162` status `ready` deltaP `3.9089` edge `0.0121` maxDD `-4.3601`
- `market_context_high->index_1h` score `-0.4315` n `162` status `ready` deltaP `0.9518` edge `0.0071` maxDD `-1.2855`
- `market_context_high->metal_1h` score `-0.4632` n `162` status `ready` deltaP `1.0294` edge `0.0097` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.4782` n `162` status `ready` deltaP `1.3843` edge `0.0044` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5132` n `162` status `ready` deltaP `2.0385` edge `0.0156` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.785` n `162` status `ready` deltaP `0.2015` edge `0.0171` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8289` n `119` status `ready` deltaP `3.6006` edge `0.0048` maxDD `-2.4729`
- `market_context_high->fx_4h` score `-0.8922` n `154` status `ready` deltaP `0.1524` edge `0.0106` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-1.0146` n `154` status `ready` deltaP `2.3539` edge `0.0385` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T21:07:27.926395+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8252`

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

- `market_context_high->unknown_24h` score `686.8317` n `54` status `ready` deltaP `3.9861` edge `57.2094` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.1649` n `50` status `ready` deltaP `50.565` edge `3.5806` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.9184` n `54` status `ready` deltaP `44.0465` edge `3.2704` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.4549` n `54` status `ready` deltaP `61.7883` edge `2.567` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.775` n `50` status `ready` deltaP `45.0017` edge `2.7342` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `11.8736` n `50` status `ready` deltaP `37.5427` edge `0.8522` maxDD `-7.0416`
- `market_context_high->crypto_major_24h` score `11.5467` n `54` status `ready` deltaP `16.6313` edge `1.4474` maxDD `-43.0171`
- `news_risk_high->crypto_alt_24h` score `9.452` n `50` status `ready` deltaP `20.6031` edge `1.525` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.1175` n `54` status `ready` deltaP `48.6905` edge `0.3605` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6587` n `50` status `ready` deltaP `42.2461` edge `0.3036` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.421` n `54` status `ready` deltaP `62.2441` edge `0.4974` maxDD `-3.7989`
- `news_risk_high->commodity_24h` score `6.4026` n `50` status `ready` deltaP `41.7678` edge `0.2551` maxDD `0.0`
- `news_risk_high->metal_4h` score `4.853` n `50` status `ready` deltaP `43.9268` edge `0.1492` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.779` n `50` status `ready` deltaP `21.6037` edge `0.3918` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.223` n `50` status `ready` deltaP `26.2317` edge `0.3206` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.9132` n `50` status `ready` deltaP `20.8982` edge `0.2498` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6612` n `50` status `ready` deltaP `33.9817` edge `0.1039` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4444` n `50` status `ready` deltaP `23.5793` edge `0.0815` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1322` n `50` status `ready` deltaP `24.3952` edge `0.0405` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2519` n `50` status `ready` deltaP `16.7485` edge `0.0228` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

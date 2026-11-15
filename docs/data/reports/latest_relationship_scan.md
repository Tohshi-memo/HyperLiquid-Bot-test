# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T13:22:34.574638+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9980`

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

- `market_context_high->unknown_24h` score `545.4446` n `64` status `ready` deltaP `3.8128` edge `45.4283` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.4554` n `50` status `ready` deltaP `48.8319` edge `3.4497` maxDD `-3.6503`
- `market_context_high->equity_24h` score `39.7729` n `64` status `ready` deltaP `45.2069` edge `3.1672` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `32.6161` n `64` status `ready` deltaP `60.4636` edge `2.4226` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.6411` n `50` status `ready` deltaP `46.3882` edge `2.836` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.1931` n `50` status `ready` deltaP `38.7622` edge `0.8707` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `8.5849` n `50` status `ready` deltaP `16.9636` edge `1.4381` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.9572` n `64` status `ready` deltaP `48.1721` edge `0.3506` maxDD `-0.0251`
- `news_risk_high->commodity_24h` score `6.9706` n `50` status `ready` deltaP `45.9272` edge `0.2747` maxDD `0.0`
- `market_context_high->metal_24h` score `6.3932` n `64` status `ready` deltaP `60.2849` edge `0.5069` maxDD `-3.7989`
- `news_risk_high->index_24h` score `6.363` n `50` status `ready` deltaP `40.8596` edge `0.2882` maxDD `-0.4279`
- `news_risk_high->crypto_major_4h` score `5.1745` n `50` status `ready` deltaP `23.128` edge `0.4146` maxDD `-9.0062`
- `market_context_high->crypto_major_24h` score `5.071` n `64` status `ready` deltaP `13.3882` edge `1.2671` maxDD `-69.0352`
- `news_risk_high->metal_4h` score `4.8954` n `50` status `ready` deltaP `44.2317` edge `0.1507` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.4508` n `50` status `ready` deltaP `26.9939` edge `0.3345` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0151` n `50` status `ready` deltaP `21.6467` edge `0.2533` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6672` n `50` status `ready` deltaP `33.9817` edge `0.1044` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.6719` n `50` status `ready` deltaP `26.0183` edge `0.0842` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2484` n `50` status `ready` deltaP `25.7425` edge `0.0412` maxDD `-0.3692`
- `news_risk_high->index_1h` score `1.2831` n `50` status `ready` deltaP `17.0479` edge `0.0234` maxDD `-0.4103`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T21:52:28.120827+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8264`

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

- `market_context_high->unknown_24h` score `740.0469` n `51` status `ready` deltaP `3.9861` edge `61.644` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.3569` n `50` status `ready` deltaP `50.565` edge `3.5966` maxDD `-3.6503`
- `market_context_high->equity_24h` score `40.2769` n `51` status `ready` deltaP `42.9572` edge `3.2242` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `34.3647` n `51` status `ready` deltaP `60.9168` edge `2.5653` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `22.5257` n `50` status `ready` deltaP `44.4818` edge `2.7057` maxDD `-6.8139`
- `market_context_high->unknown_4h` score `13.9651` n `71` status `ready` deltaP `8.9939` edge `1.1038` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `13.3334` n `51` status `ready` deltaP `17.8543` edge `1.504` maxDD `-36.286`
- `news_risk_high->equity_4h` score `11.7662` n `50` status `ready` deltaP `37.0854` edge `0.8463` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.367` n `50` status `ready` deltaP `20.6031` edge `1.5141` maxDD `-29.0448`
- `market_context_high->index_24h` score `8.0061` n `51` status `ready` deltaP `48.3637` edge `0.3534` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.6875` n `50` status `ready` deltaP `42.2461` edge `0.306` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.3334` n `50` status `ready` deltaP `41.2478` edge `0.2528` maxDD `0.0`
- `market_context_high->metal_24h` score `6.1546` n `51` status `ready` deltaP `61.1548` edge `0.4705` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.8626` n `50` status `ready` deltaP `43.9268` edge `0.15` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.5852` n `50` status `ready` deltaP `21.1463` edge `0.3787` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0916` n `50` status `ready` deltaP `25.7744` edge `0.3127` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `3.8581` n `50` status `ready` deltaP `20.4491` edge `0.2482` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.6344` n `50` status `ready` deltaP `33.6768` edge `0.1037` maxDD `-0.3611`
- `news_risk_high->index_4h` score `2.4006` n `50` status `ready` deltaP `23.122` edge `0.0809` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1574` n `50` status `ready` deltaP `24.6946` edge `0.0406` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

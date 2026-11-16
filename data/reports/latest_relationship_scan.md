# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-16T00:22:27.502095+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8592`

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

- `market_context_high->unknown_24h` score `998.9817` n `41` status `ready` deltaP `3.9861` edge `83.2219` maxDD `0.0`
- `news_risk_high->equity_24h` score `46.9641` n `50` status `ready` deltaP `50.565` edge `3.6472` maxDD `-3.6503`
- `market_context_high->unknown_4h` score `44.9383` n `64` status `ready` deltaP `8.9939` edge `3.6849` maxDD `0.0`
- `market_context_high->equity_24h` score `36.0687` n `41` status `ready` deltaP `38.1748` edge `2.9054` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.5495` n `41` status `ready` deltaP `57.0909` edge `2.3562` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `21.8203` n `50` status `ready` deltaP `43.4419` edge `2.6222` maxDD `-6.8139`
- `market_context_high->crypto_major_24h` score `12.9147` n `41` status `ready` deltaP `14.7102` edge `1.4137` maxDD `-30.1765`
- `news_risk_high->equity_4h` score `11.6972` n `50` status `ready` deltaP `36.628` edge `0.8436` maxDD `-7.0416`
- `news_risk_high->crypto_alt_24h` score `9.1533` n `50` status `ready` deltaP `20.6031` edge `1.4867` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.313` n `41` status `ready` deltaP `46.929` edge `0.3052` maxDD `-0.0251`
- `news_risk_high->index_24h` score `6.7751` n `50` status `ready` deltaP `42.2461` edge `0.3133` maxDD `-0.4279`
- `news_risk_high->commodity_24h` score `6.268` n `50` status `ready` deltaP `41.0745` edge `0.2485` maxDD `0.0`
- `market_context_high->metal_24h` score `4.9449` n `41` status `ready` deltaP `56.3724` edge `0.3473` maxDD `-3.7989`
- `news_risk_high->metal_4h` score `4.9118` n `50` status `ready` deltaP `43.9268` edge `0.1541` maxDD `-1.0104`
- `news_risk_high->crypto_major_4h` score `4.2864` n `50` status `ready` deltaP `20.2317` edge `0.3599` maxDD `-9.0062`
- `news_risk_high->crypto_alt_4h` score `4.0188` n `50` status `ready` deltaP `25.1646` edge `0.3107` maxDD `-9.4848`
- `news_risk_high->commodity_4h` score `3.6754` n `50` status `ready` deltaP `33.8293` edge `0.1061` maxDD `-0.3611`
- `news_risk_high->equity_1h` score `3.6567` n `50` status `ready` deltaP `19.4012` edge `0.2384` maxDD `-3.7082`
- `news_risk_high->index_4h` score `2.4018` n `50` status `ready` deltaP `23.122` edge `0.081` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.1023` n `50` status `ready` deltaP `24.2455` edge `0.039` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

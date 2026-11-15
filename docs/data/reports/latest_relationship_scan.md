# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-15T11:07:26.217345+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `9954`

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

- `market_context_high->unknown_24h` score `531.8393` n `66` status `ready` deltaP `2.9463` edge `44.3003` maxDD `0.0`
- `news_risk_high->equity_24h` score `44.3918` n `50` status `ready` deltaP `48.8319` edge `3.4444` maxDD `-3.6503`
- `market_context_high->equity_24h` score `38.1607` n `66` status `ready` deltaP `42.6501` edge `3.0499` maxDD `-9.0005`
- `market_context_high->crypto_alt_24h` score `31.126` n `66` status `ready` deltaP `57.8121` edge `2.3161` maxDD `-6.2814`
- `news_risk_high->crypto_major_24h` score `23.741` n `50` status `ready` deltaP `46.3882` edge `2.8488` maxDD `-6.8139`
- `news_risk_high->equity_4h` score `12.3165` n `50` status `ready` deltaP `39.5244` edge `0.8759` maxDD `-7.0416`
- `market_context_high->unknown_4h` score `9.4397` n `81` status `ready` deltaP `8.8415` edge `0.7277` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.34` n `50` status `ready` deltaP `16.9636` edge `1.4067` maxDD `-29.0448`
- `market_context_high->index_24h` score `7.5244` n `66` status `ready` deltaP `44.9372` edge `0.3366` maxDD `-0.0653`
- `news_risk_high->commodity_24h` score `7.177` n `50` status `ready` deltaP `47.487` edge `0.2815` maxDD `0.0`
- `news_risk_high->index_24h` score `6.3281` n `50` status `ready` deltaP `40.513` edge `0.2876` maxDD `-0.4279`
- `market_context_high->metal_24h` score `6.2658` n `66` status `ready` deltaP `59.1986` edge `0.4978` maxDD `-3.7989`
- `news_risk_high->crypto_major_4h` score `5.5233` n `50` status `ready` deltaP `23.7378` edge `0.4396` maxDD `-9.0062`
- `news_risk_high->metal_4h` score `5.0109` n `50` status `ready` deltaP `45.4512` edge `0.1522` maxDD `-1.0104`
- `news_risk_high->crypto_alt_4h` score `4.857` n `50` status `ready` deltaP `28.3659` edge `0.3592` maxDD `-9.4848`
- `news_risk_high->equity_1h` score `4.0127` n `50` status `ready` deltaP `21.6467` edge `0.2531` maxDD `-3.7082`
- `news_risk_high->commodity_4h` score `3.5734` n `50` status `ready` deltaP `32.9146` edge `0.1037` maxDD `-0.3611`
- `market_context_high->crypto_major_24h` score `3.0557` n `66` status `ready` deltaP `12.6306` edge `1.203` maxDD `-76.2717`
- `news_risk_high->index_4h` score `2.7766` n `50` status `ready` deltaP `27.2378` edge `0.0848` maxDD `-0.7999`
- `news_risk_high->metal_1h` score `2.2736` n `50` status `ready` deltaP `26.0419` edge `0.0413` maxDD `-0.3692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

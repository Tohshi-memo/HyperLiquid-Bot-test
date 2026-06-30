# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T23:07:31.343180+00:00`
- Price records: `672`
- Market context records: `5295`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9650`

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

- `market_context_high->unknown_24h` score `22.3952` n `153` status `ready` deltaP `26.1234` edge `1.7011` maxDD `-0.3859`
- `market_context_high->crypto_major_24h` score `7.5932` n `153` status `ready` deltaP `25.7353` edge `0.8762` maxDD `-26.5332`
- `market_context_high->equity_24h` score `4.565` n `153` status `ready` deltaP `19.9653` edge `0.8102` maxDD `-40.0306`
- `market_context_high->crypto_alt_4h` score `4.0145` n `182` status `ready` deltaP `15.4383` edge `0.3957` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9178` n `182` status `ready` deltaP `16.2641` edge `0.4473` maxDD `-14.0065`
- `market_context_high->equity_4h` score `1.4974` n `182` status `ready` deltaP `11.2118` edge `0.2139` maxDD `-7.4425`
- `market_context_high->unknown_4h` score `0.9834` n `182` status `ready` deltaP `14.7849` edge `0.0856` maxDD `-5.5109`
- `market_context_high->fx_24h` score `0.5493` n `153` status `ready` deltaP `13.3068` edge `0.0466` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.3087` n `193` status `ready` deltaP `3.8519` edge `0.0962` maxDD `-5.0257`
- `market_context_high->index_24h` score `0.2911` n `153` status `ready` deltaP `20.8231` edge `0.062` maxDD `-7.413`
- `market_context_high->crypto_major_1h` score `0.1513` n `193` status `ready` deltaP `5.3489` edge `0.1015` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.1479` n `193` status `ready` deltaP `8.1226` edge `0.0547` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0177` n `193` status `ready` deltaP `5.774` edge `0.0104` maxDD `-1.0296`
- `market_context_high->index_4h` score `-0.3108` n `182` status `ready` deltaP `6.8095` edge `0.0265` maxDD `-2.9391`
- `market_context_high->metal_1h` score `-0.3519` n `193` status `ready` deltaP `2.2052` edge `0.0077` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.3866` n `193` status `ready` deltaP `-0.0636` edge `-0.0002` maxDD `-0.5823`
- `market_context_high->fx_4h` score `-0.739` n `182` status `ready` deltaP `0.9566` edge `0.0018` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.4817` n `193` status `ready` deltaP `-3.7479` edge `-0.0067` maxDD `-3.3428`
- `market_context_high->metal_4h` score `-1.8407` n `182` status `ready` deltaP `-4.8278` edge `-0.0002` maxDD `-9.6218`
- `market_context_high->crypto_alt_24h` score `-2.907` n `153` status `ready` deltaP `13.3476` edge `0.3793` maxDD `-53.6115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

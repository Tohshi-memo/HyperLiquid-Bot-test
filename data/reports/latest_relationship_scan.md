# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-01T19:37:33.789693+00:00`
- Price records: `672`
- Market context records: `5381`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11510`

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

- `market_context_high->unknown_24h` score `7.29` n `184` status `ready` deltaP `16.8328` edge `0.5083` maxDD `-0.3748`
- `market_context_high->crypto_major_24h` score `5.5056` n `184` status `ready` deltaP `22.9695` edge `0.7597` maxDD `-29.6555`
- `market_context_high->crypto_major_4h` score `3.3262` n `205` status `ready` deltaP `14.3293` edge `0.4109` maxDD `-14.0065`
- `market_context_high->crypto_alt_4h` score `2.8145` n `205` status `ready` deltaP `11.4634` edge `0.3222` maxDD `-9.46`
- `market_context_high->equity_24h` score `2.2846` n `184` status `ready` deltaP `12.1453` edge `0.6723` maxDD `-40.0306`
- `market_context_high->equity_4h` score `2.0429` n `205` status `ready` deltaP `10.3659` edge `0.265` maxDD `-7.4425`
- `market_context_high->equity_1h` score `0.2378` n `205` status `ready` deltaP `6.7117` edge `0.0716` maxDD `-5.0555`
- `market_context_high->crypto_alt_1h` score `-0.0215` n `205` status `ready` deltaP `2.079` edge `0.0805` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.0415` n `205` status `ready` deltaP `4.8277` edge `0.0137` maxDD `-0.9472`
- `market_context_high->crypto_major_1h` score `-0.0494` n `205` status `ready` deltaP `4.0251` edge `0.0936` maxDD `-6.9639`
- `market_context_high->fx_24h` score `-0.1179` n `184` status `ready` deltaP `7.3219` edge `0.0309` maxDD `-0.8294`
- `market_context_high->index_24h` score `-0.1874` n `184` status `ready` deltaP `16.0326` edge `0.0912` maxDD `-9.0959`
- `market_context_high->unknown_4h` score `-0.3699` n `205` status `ready` deltaP `8.5975` edge `0.0303` maxDD `-6.1421`
- `market_context_high->fx_1h` score `-0.4485` n `205` status `ready` deltaP `-1.1034` edge `-0.0012` maxDD `-0.5823`
- `market_context_high->metal_1h` score `-0.5298` n `205` status `ready` deltaP `1.6299` edge `0.0125` maxDD `-2.0682`
- `market_context_high->index_4h` score `-1.1193` n `205` status `ready` deltaP `5.1829` edge `0.0331` maxDD `-2.874`
- `market_context_high->fx_4h` score `-1.1937` n `205` status `ready` deltaP `0.3964` edge `0.0008` maxDD `-1.567`
- `market_context_high->commodity_1h` score `-1.5334` n `205` status `ready` deltaP `-3.9192` edge `-0.0072` maxDD `-3.5563`
- `market_context_high->metal_4h` score `-2.4959` n `205` status `ready` deltaP `-5.9147` edge `-0.0281` maxDD `-12.8631`
- `market_context_high->crypto_alt_24h` score `-3.1709` n `184` status `ready` deltaP `13.6172` edge `0.3724` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

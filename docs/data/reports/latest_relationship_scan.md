# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T17:52:27.109998+00:00`
- Price records: `672`
- Market context records: `5167`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5650`

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

- `market_context_high->unknown_24h` score `28.984` n `66` status `ready` deltaP `33.0019` edge `2.2143` maxDD `-0.8515`
- `market_context_high->unknown_4h` score `5.8225` n `142` status `ready` deltaP `20.0747` edge `0.4536` maxDD `-5.5109`
- `market_context_high->crypto_major_24h` score `4.9573` n `66` status `ready` deltaP `18.7973` edge `0.8764` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `4.9218` n `66` status `ready` deltaP `20.565` edge `0.8326` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.7339` n `142` status `ready` deltaP `14.9261` edge `0.4549` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0944` n `142` status `ready` deltaP `13.8226` edge `0.4783` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `3.7593` n `149` status `ready` deltaP `9.6492` edge `0.3131` maxDD `-2.7986`
- `market_context_high->crypto_major_1h` score `0.76` n `149` status `ready` deltaP `7.8879` edge `0.1353` maxDD `-6.9639`
- `market_context_high->commodity_24h` score `0.7564` n `66` status `ready` deltaP `17.4242` edge `0.1348` maxDD `-6.6519`
- `market_context_high->crypto_alt_1h` score `0.7254` n `149` status `ready` deltaP `5.1159` edge `0.1225` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.6864` n `142` status `ready` deltaP `8.5451` edge `0.1641` maxDD `-7.4425`
- `market_context_high->metal_24h` score `0.3402` n `66` status `ready` deltaP `-0.7892` edge `0.2149` maxDD `-7.2822`
- `market_context_high->equity_1h` score `0.2803` n `149` status `ready` deltaP `7.5734` edge `0.0694` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0633` n `149` status `ready` deltaP `4.7392` edge `0.0135` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0952` n `149` status `ready` deltaP `4.8266` edge `0.0148` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.1952` n `149` status `ready` deltaP `2.9428` edge `0.0006` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.3893` n `142` status `ready` deltaP `4.8201` edge `0.0297` maxDD `-2.9391`
- `market_context_high->fx_24h` score `-0.422` n `66` status `ready` deltaP `6.8656` edge `0.0086` maxDD `-0.8294`
- `market_context_high->fx_4h` score `-0.4572` n `142` status `ready` deltaP `5.5909` edge `0.0075` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5527` n `149` status `ready` deltaP `1.3061` edge `0.0013` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

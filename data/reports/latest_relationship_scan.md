# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T20:52:30.342249+00:00`
- Price records: `672`
- Market context records: `5180`
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

- `market_context_high->unknown_24h` score `23.4234` n `78` status `ready` deltaP `32.719` edge `1.7528` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.454` n `78` status `ready` deltaP `24.6395` edge `1.1564` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.5218` n `78` status `ready` deltaP `25.7078` edge `0.9608` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.9547` n `149` status `ready` deltaP `20.0462` edge `0.4648` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.8867` n `149` status `ready` deltaP `14.9165` edge `0.4677` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.5262` n `149` status `ready` deltaP `13.8791` edge `0.5139` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6395` n `155` status `ready` deltaP `9.5866` edge `0.2202` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2636` n `149` status `ready` deltaP `8.6348` edge `0.2116` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5517` n `155` status `ready` deltaP `4.3539` edge `0.1131` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5417` n `155` status `ready` deltaP `6.553` edge `0.126` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3388` n `155` status `ready` deltaP `8.3639` edge `0.069` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.037` n `155` status `ready` deltaP `5.933` edge `0.0139` maxDD `-1.0296`
- `market_context_high->fx_24h` score `0.0137` n `78` status `ready` deltaP `10.3766` edge `0.0215` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.0358` n `155` status `ready` deltaP `5.4587` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.258` n `155` status `ready` deltaP `1.809` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4575` n `149` status `ready` deltaP `5.6116` edge `0.0362` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5455` n `149` status `ready` deltaP `3.9982` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6133` n `155` status `ready` deltaP `0.4259` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.1485` n `78` status `ready` deltaP `4.9279` edge `-0.0166` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2781` n `149` status `ready` deltaP `0.1473` edge `0.0355` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

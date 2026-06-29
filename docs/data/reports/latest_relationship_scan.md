# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T20:37:30.130381+00:00`
- Price records: `672`
- Market context records: `5179`
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

- `market_context_high->unknown_24h` score `24.0385` n `77` status `ready` deltaP `32.6524` edge `1.8045` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.2078` n `77` status `ready` deltaP `24.247` edge `1.1385` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.4296` n `77` status `ready` deltaP `25.3653` edge `0.9554` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.9655` n `149` status `ready` deltaP `20.0462` edge `0.4657` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.9169` n `149` status `ready` deltaP `15.0689` edge `0.4692` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.5708` n `149` status `ready` deltaP `14.0316` edge `0.5166` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6635` n `155` status `ready` deltaP `9.7363` edge `0.2212` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.3034` n `149` status `ready` deltaP `8.7872` edge `0.2139` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5517` n `155` status `ready` deltaP `4.3539` edge `0.1131` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5369` n `155` status `ready` deltaP `6.553` edge `0.1256` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3532` n `155` status `ready` deltaP `8.5136` edge `0.0692` maxDD `-5.0555`
- `market_context_high->index_1h` score `0.037` n `155` status `ready` deltaP `5.933` edge `0.0139` maxDD `-1.0296`
- `market_context_high->fx_24h` score `-0.02` n `77` status `ready` deltaP `10.1506` edge `0.0202` maxDD `-0.8294`
- `market_context_high->metal_1h` score `-0.0351` n `155` status `ready` deltaP `5.4587` edge `0.0183` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2495` n `155` status `ready` deltaP `1.9587` edge `0.0002` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4393` n `149` status `ready` deltaP `5.764` edge `0.0367` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5534` n `149` status `ready` deltaP `3.8458` edge `0.0068` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6211` n `155` status `ready` deltaP `0.2762` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.1778` n `77` status `ready` deltaP `4.4688` edge `-0.0173` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2671` n `149` status `ready` deltaP `0.2997` edge `0.0359` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T05:07:32.613312+00:00`
- Price records: `672`
- Market context records: `5217`
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

- `market_context_high->unknown_24h` score `18.9471` n `111` status `ready` deltaP `33.3756` edge `1.3754` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.1432` n `111` status `ready` deltaP `31.8694` edge `1.3323` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.0129` n `111` status `ready` deltaP `27.4306` edge `0.9069` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.2223` n `155` status `ready` deltaP `13.5415` edge `0.4215` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1622` n `155` status `ready` deltaP `14.0696` edge `0.4823` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.9775` n `155` status `ready` deltaP `18.507` edge `0.3103` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.9833` n `155` status `ready` deltaP `8.8381` edge `0.1705` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5872` n `111` status `ready` deltaP `13.7951` edge `0.0465` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5816` n `155` status `ready` deltaP `4.6533` edge `0.1136` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5537` n `155` status `ready` deltaP `6.553` edge `0.127` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.1557` n `155` status `ready` deltaP `6.6355` edge `0.1326` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1706` n `155` status `ready` deltaP `3.5126` edge `0.0139` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.221` n `155` status `ready` deltaP `4.7711` edge `0.0463` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2518` n `155` status `ready` deltaP `1.9587` edge `-0.0001` maxDD `-0.6194`
- `market_context_high->index_1h` score `-0.2625` n `155` status `ready` deltaP `2.939` edge `0.0089` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.4366` n `111` status `ready` deltaP `13.6825` edge `0.0163` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6081` n `155` status `ready` deltaP `3.034` edge `0.0052` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6164` n `155` status `ready` deltaP `0.4259` edge `-0.001` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.8085` n `155` status `ready` deltaP `3.9241` edge `0.0182` maxDD `-2.9391`
- `market_context_high->equity_24h` score `-0.9384` n `111` status `ready` deltaP `15.7611` edge `0.3375` maxDD `-40.0306`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T03:52:26.236959+00:00`
- Price records: `672`
- Market context records: `5212`
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

- `market_context_high->unknown_24h` score `15.5084` n `106` status `ready` deltaP `33.7264` edge `1.0865` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.4486` n `106` status `ready` deltaP `31.2926` edge `1.3616` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.6881` n `106` status `ready` deltaP `28.2658` edge `0.9576` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.0651` n `155` status `ready` deltaP `18.8119` edge `0.3989` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4879` n `155` status `ready` deltaP `13.8464` edge `0.4416` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3614` n `155` status `ready` deltaP `14.0696` edge `0.4989` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6948` n `155` status `ready` deltaP `8.9878` edge `0.2288` maxDD `-2.7986`
- `market_context_high->crypto_alt_1h` score `0.6488` n `155` status `ready` deltaP `4.9527` edge `0.1172` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5992` n `155` status `ready` deltaP `6.7027` edge `0.1298` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.5762` n `106` status `ready` deltaP `13.6432` edge `0.0466` maxDD `-0.8294`
- `market_context_high->equity_4h` score `0.4194` n `155` status `ready` deltaP `7.3977` edge `0.1495` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.0748` n `155` status `ready` deltaP `5.5196` edge `0.0535` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1153` n `155` status `ready` deltaP `4.2611` edge `0.016` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.181` n `155` status `ready` deltaP `3.6875` edge `0.0107` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2682` n `155` status `ready` deltaP `1.6593` edge `-0.0002` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.5675` n `106` status `ready` deltaP `12.9356` edge `0.0045` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6097` n `155` status `ready` deltaP `3.034` edge `0.005` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6327` n `155` status `ready` deltaP `0.1265` edge `-0.0011` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.6924` n `155` status `ready` deltaP `4.6863` edge `0.0228` maxDD `-2.9391`
- `market_context_high->metal_4h` score `-1.3551` n `155` status `ready` deltaP `-0.1023` edge `0.0273` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

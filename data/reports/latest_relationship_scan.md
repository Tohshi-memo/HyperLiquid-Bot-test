# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T23:52:33.359095+00:00`
- Price records: `672`
- Market context records: `5195`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5644`

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

- `market_context_high->unknown_24h` score `19.2601` n `90` status `ready` deltaP `33.4028` edge `1.4013` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.2086` n `90` status `ready` deltaP `28.368` edge `1.3611` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.8027` n `90` status `ready` deltaP `28.9237` edge `1.0461` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.4539` n `155` status `ready` deltaP `19.7266` edge `0.4252` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.4861` n `155` status `ready` deltaP `13.3891` edge `0.4445` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3766` n `155` status `ready` deltaP `13.7648` edge `0.5022` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.594` n `155` status `ready` deltaP `9.2872` edge `0.2184` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.9366` n `155` status `ready` deltaP `8.3123` edge `0.1865` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5624` n `155` status `ready` deltaP `4.6533` edge `0.112` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5333` n `155` status `ready` deltaP `6.553` edge `0.1253` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.3589` n `90` status `ready` deltaP `12.3958` edge `0.0368` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.1674` n `155` status `ready` deltaP `7.0166` edge `0.0637` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0481` n `155` status `ready` deltaP `5.0348` edge `0.0128` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0935` n `155` status `ready` deltaP `4.5605` edge `0.0168` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2409` n `155` status `ready` deltaP `2.1084` edge `0.0003` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.5179` n `155` status `ready` deltaP `4.5584` edge `0.0066` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.5208` n `155` status `ready` deltaP `5.6009` edge `0.031` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.9198` n `90` status `ready` deltaP `9.3403` edge `-0.0167` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.3348` n `155` status `ready` deltaP `-0.1023` edge `0.0299` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

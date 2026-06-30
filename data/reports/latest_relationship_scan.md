# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T06:37:30.181239+00:00`
- Price records: `672`
- Market context records: `5223`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5600`

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

- `market_context_high->unknown_24h` score `19.9305` n `114` status `ready` deltaP `32.6023` edge `1.4625` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.9071` n `114` status `ready` deltaP `31.6337` edge `1.3142` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.7733` n `114` status `ready` deltaP `27.9606` edge `0.8834` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `3.9947` n `155` status `ready` deltaP `12.9318` edge `0.4066` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9894` n `155` status `ready` deltaP `14.0696` edge `0.4679` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.8868` n `155` status `ready` deltaP `17.5924` edge `0.2255` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8945` n `155` status `ready` deltaP `8.6884` edge `0.1641` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5338` n `114` status `ready` deltaP `13.3224` edge `0.0452` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4973` n `155` status `ready` deltaP `6.553` edge `0.1223` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4737` n `155` status `ready` deltaP `4.3539` edge `0.1066` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.0325` n `155` status `ready` deltaP `6.0257` edge `0.1264` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1807` n `155` status `ready` deltaP `3.5126` edge `0.0126` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.1935` n `155` status `ready` deltaP `5.0705` edge `0.0466` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2553` n `155` status `ready` deltaP `3.0887` edge `0.0085` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2596` n `155` status `ready` deltaP `1.809` edge `-0.0001` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.3924` n `114` status `ready` deltaP `13.8889` edge `0.0206` maxDD `-7.413`
- `market_context_high->equity_24h` score `-0.4011` n `114` status `ready` deltaP `16.1641` edge `0.4037` maxDD `-40.0306`
- `market_context_high->commodity_1h` score `-0.611` n `155` status `ready` deltaP `0.5756` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6271` n `155` status `ready` deltaP `2.7291` edge `0.0048` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8825` n `155` status `ready` deltaP `3.3143` edge `0.0161` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

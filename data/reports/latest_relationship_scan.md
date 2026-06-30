# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T07:07:32.140028+00:00`
- Price records: `672`
- Market context records: `5225`
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

- `market_context_high->unknown_24h` score `20.537` n `116` status `ready` deltaP `32.4892` edge `1.5138` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.7753` n `116` status `ready` deltaP `31.8008` edge `1.3021` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.4857` n `116` status `ready` deltaP `26.796` edge `0.8672` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `3.9635` n `155` status `ready` deltaP `12.9318` edge `0.404` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.9474` n `155` status `ready` deltaP `14.0696` edge `0.4644` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.56` n `155` status `ready` deltaP `17.2875` edge `0.2003` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8993` n `155` status `ready` deltaP `8.6884` edge `0.1645` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5422` n `116` status `ready` deltaP `13.3381` edge `0.0458` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4853` n `155` status `ready` deltaP `6.553` edge `0.1213` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4689` n `155` status `ready` deltaP `4.3539` edge `0.1062` maxDD `-5.0257`
- `market_context_high->equity_4h` score `-0.0087` n `155` status `ready` deltaP `5.7208` edge `0.125` maxDD `-7.4425`
- `market_context_high->equity_24h` score `-0.1904` n `116` status `ready` deltaP `16.4212` edge `0.429` maxDD `-40.0306`
- `market_context_high->equity_1h` score `-0.1971` n `155` status `ready` deltaP `5.0705` edge `0.0463` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.215` n `155` status `ready` deltaP `3.2132` edge `0.0102` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.2434` n `155` status `ready` deltaP `3.2384` edge `0.0085` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.2767` n `155` status `ready` deltaP `1.5096` edge `-0.0003` maxDD `-0.6194`
- `market_context_high->index_24h` score `-0.3438` n `116` status `ready` deltaP `14.4636` edge `0.023` maxDD `-7.413`
- `market_context_high->commodity_1h` score `-0.6195` n `155` status `ready` deltaP `0.4259` edge `-0.0014` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.6461` n `155` status `ready` deltaP `2.4243` edge `0.0044` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.9117` n `155` status `ready` deltaP `3.0094` edge `0.0157` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

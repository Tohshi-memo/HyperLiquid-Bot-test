# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T21:22:26.620274+00:00`
- Price records: `672`
- Market context records: `5183`
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

- `market_context_high->unknown_24h` score `22.5469` n `80` status `ready` deltaP `32.8472` edge `1.6789` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.9346` n `80` status `ready` deltaP `25.3819` edge `1.1915` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `9.7164` n `80` status `ready` deltaP `26.3542` edge `0.9727` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.7255` n `151` status `ready` deltaP `19.5516` edge `0.449` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.7047` n `151` status `ready` deltaP `14.081` edge `0.4581` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.4667` n `151` status `ready` deltaP `13.5711` edge `0.511` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6395` n `155` status `ready` deltaP `9.5866` edge `0.2202` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.2877` n `151` status `ready` deltaP `8.8455` edge `0.2122` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5577` n `155` status `ready` deltaP `4.3539` edge `0.1136` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5477` n `155` status `ready` deltaP `6.553` edge `0.1265` maxDD `-6.9639`
- `market_context_high->equity_1h` score `0.3232` n `155` status `ready` deltaP `8.2142` edge `0.0687` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.0763` n `80` status `ready` deltaP `10.7986` edge `0.0239` maxDD `-0.8294`
- `market_context_high->index_1h` score `0.0358` n `155` status `ready` deltaP `5.933` edge `0.0138` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0358` n `155` status `ready` deltaP `5.4587` edge `0.0182` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2736` n `155` status `ready` deltaP `1.5096` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4297` n `151` status `ready` deltaP `5.929` edge `0.0364` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.5432` n `151` status `ready` deltaP `4.0573` edge `0.0067` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6055` n `155` status `ready` deltaP `0.5756` edge `-0.0006` maxDD `-2.4692`
- `market_context_high->index_24h` score `-1.0931` n `80` status `ready` deltaP `5.7986` edge `-0.0153` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2389` n `151` status `ready` deltaP `0.6158` edge `0.0374` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

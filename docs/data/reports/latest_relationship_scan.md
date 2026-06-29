# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-29T23:07:29.030718+00:00`
- Price records: `672`
- Market context records: `5191`
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

- `market_context_high->unknown_24h` score `20.179` n `87` status `ready` deltaP `33.2495` edge `1.4789` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.7717` n `87` status `ready` deltaP `27.5862` edge `1.3299` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `10.6426` n `87` status `ready` deltaP `28.2567` edge `1.0372` maxDD `-23.4292`
- `market_context_high->unknown_4h` score `5.5081` n `155` status `ready` deltaP `19.879` edge `0.4287` maxDD `-5.5109`
- `market_context_high->crypto_alt_4h` score `4.3955` n `155` status `ready` deltaP `12.9318` edge `0.44` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.3186` n `155` status `ready` deltaP `13.4599` edge `0.4994` maxDD `-14.0065`
- `market_context_high->unknown_1h` score `2.6335` n `155` status `ready` deltaP `9.5866` edge `0.2197` maxDD `-2.7986`
- `market_context_high->equity_4h` score `1.0968` n `155` status `ready` deltaP `8.7696` edge `0.1968` maxDD `-7.4425`
- `market_context_high->crypto_alt_1h` score `0.5253` n `155` status `ready` deltaP `4.3539` edge `0.1109` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.5117` n `155` status `ready` deltaP `6.4033` edge `0.1245` maxDD `-6.9639`
- `market_context_high->fx_24h` score `0.2886` n `87` status `ready` deltaP `11.9971` edge `0.0336` maxDD `-0.8294`
- `market_context_high->equity_1h` score `0.2226` n `155` status `ready` deltaP `7.316` edge `0.0663` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.0025` n `155` status `ready` deltaP `5.4839` edge `0.0136` maxDD `-1.0296`
- `market_context_high->metal_1h` score `-0.0709` n `155` status `ready` deltaP `4.8599` edge `0.0177` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2565` n `155` status `ready` deltaP `1.809` edge `0.0003` maxDD `-0.6194`
- `market_context_high->index_4h` score `-0.4602` n `155` status `ready` deltaP `6.0582` edge `0.033` maxDD `-2.9391`
- `market_context_high->fx_4h` score `-0.4918` n `155` status `ready` deltaP `5.0157` edge `0.0069` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.5884` n `155` status `ready` deltaP `0.875` edge `-0.0004` maxDD `-2.4692`
- `market_context_high->index_24h` score `-0.9653` n `87` status `ready` deltaP `8.4051` edge `-0.0163` maxDD `-7.413`
- `market_context_high->metal_4h` score `-1.2806` n `155` status `ready` deltaP `0.355` edge `0.0338` maxDD `-9.3609`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

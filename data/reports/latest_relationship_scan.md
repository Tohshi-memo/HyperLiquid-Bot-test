# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T08:37:27.466495+00:00`
- Price records: `672`
- Market context records: `5231`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5602`

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

- `market_context_high->unknown_24h` score `22.1404` n `122` status `ready` deltaP `32.3116` edge `1.6486` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.4114` n `122` status `ready` deltaP `32.5478` edge `1.2668` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `7.6067` n `122` status `ready` deltaP `23.8787` edge `0.8134` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0035` n `155` status `ready` deltaP `13.2367` edge `0.4053` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `3.926` n `155` status `ready` deltaP `14.2221` edge `0.4616` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.1564` n `155` status `ready` deltaP `16.9827` edge `0.1687` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.813` n `155` status `ready` deltaP `8.0896` edge `0.1613` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5631` n `122` status `ready` deltaP `13.314` edge `0.0477` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4448` n `155` status `ready` deltaP `4.6533` edge `0.1022` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4168` n `155` status `ready` deltaP `6.7027` edge `0.1146` maxDD `-6.9639`
- `market_context_high->equity_24h` score `0.3752` n `122` status `ready` deltaP `17.142` edge `0.4967` maxDD `-40.0306`
- `market_context_high->equity_4h` score `0.0481` n `155` status `ready` deltaP `6.0257` edge `0.1277` maxDD `-7.4425`
- `market_context_high->equity_1h` score `-0.1995` n `155` status `ready` deltaP `5.2202` edge `0.0451` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.2002` n `155` status `ready` deltaP `3.5126` edge `0.0101` maxDD `-2.0682`
- `market_context_high->index_24h` score `-0.2272` n `122` status `ready` deltaP `16.0747` edge `0.0272` maxDD `-7.413`
- `market_context_high->index_1h` score `-0.2314` n `155` status `ready` deltaP `3.3881` edge `0.0085` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3188` n `155` status `ready` deltaP `0.7611` edge `-0.0007` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.6468` n `155` status `ready` deltaP `-0.0232` edge `-0.0019` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7022` n `155` status `ready` deltaP `1.5096` edge `0.0033` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8995` n `155` status `ready` deltaP `3.1619` edge `0.0157` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

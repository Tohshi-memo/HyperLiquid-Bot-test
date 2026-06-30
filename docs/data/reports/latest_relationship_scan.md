# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T13:22:31.357762+00:00`
- Price records: `672`
- Market context records: `5251`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7576`

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

- `market_context_high->unknown_24h` score `25.1261` n `140` status `ready` deltaP `30.3026` edge `1.9108` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `11.4451` n `140` status `ready` deltaP `30.7837` edge `1.1147` maxDD `-22.6266`
- `market_context_high->crypto_alt_4h` score `4.5305` n `155` status `ready` deltaP `15.2184` edge `0.436` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.2216` n `155` status `ready` deltaP `15.4416` edge `0.4781` maxDD `-14.0065`
- `market_context_high->crypto_alt_24h` score `3.3546` n `140` status `ready` deltaP `18.0208` edge `0.6149` maxDD `-27.7723`
- `market_context_high->equity_24h` score `2.5973` n `140` status `ready` deltaP `18.9335` edge `0.6531` maxDD `-40.0306`
- `market_context_high->unknown_4h` score `2.1926` n `155` status `ready` deltaP `17.1351` edge `0.1707` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `0.5653` n `162` status `ready` deltaP `8.1541` edge `0.0569` maxDD `-2.7986`
- `market_context_high->equity_4h` score `0.5608` n `155` status `ready` deltaP `8.1599` edge `0.1562` maxDD `-7.4425`
- `market_context_high->fx_24h` score `0.5341` n `140` status `ready` deltaP `12.8918` edge `0.0481` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.4878` n `162` status `ready` deltaP `4.8459` edge `0.1045` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.3671` n `162` status `ready` deltaP `6.1562` edge `0.1141` maxDD `-6.9639`
- `market_context_high->index_24h` score `0.059` n `140` status `ready` deltaP `20.0793` edge `0.0372` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0598` n `162` status `ready` deltaP `6.0971` edge `0.0509` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.1199` n `162` status `ready` deltaP `4.5465` edge `0.0135` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.1691` n `162` status `ready` deltaP `4.077` edge `0.0091` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3492` n `162` status `ready` deltaP `0.2052` edge `-0.0009` maxDD `-0.6194`
- `market_context_high->fx_4h` score `-0.8066` n `155` status `ready` deltaP `-0.1672` edge `0.0011` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8205` n `155` status `ready` deltaP `3.9241` edge `0.0172` maxDD `-2.9391`
- `market_context_high->commodity_1h` score `-1.1828` n `162` status `ready` deltaP `-1.8149` edge `-0.0056` maxDD `-2.4692`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

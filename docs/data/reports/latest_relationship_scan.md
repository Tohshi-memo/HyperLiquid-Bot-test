# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T05:37:33.638805+00:00`
- Price records: `672`
- Market context records: `5219`
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

- `market_context_high->unknown_24h` score `20.1004` n `113` status `ready` deltaP `33.0921` edge `1.4734` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.088` n `113` status `ready` deltaP `32.0643` edge `1.3264` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.8715` n `113` status `ready` deltaP `27.6733` edge `0.8935` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.1309` n `155` status `ready` deltaP `13.3891` edge `0.4149` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0914` n `155` status `ready` deltaP `14.0696` edge `0.4764` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.5763` n `155` status `ready` deltaP `18.2022` edge `0.2789` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8693` n `155` status `ready` deltaP `8.6884` edge `0.162` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5876` n `113` status `ready` deltaP `13.8305` edge `0.0463` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5108` n `155` status `ready` deltaP `4.5036` edge `0.1087` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4985` n `155` status `ready` deltaP `6.4033` edge `0.1234` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.0857` n `155` status `ready` deltaP `6.3306` edge `0.1288` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1721` n `155` status `ready` deltaP `3.5126` edge `0.0137` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2425` n `155` status `ready` deltaP `2.1084` edge `0.0001` maxDD `-0.6194`
- `market_context_high->equity_1h` score `-0.2594` n `155` status `ready` deltaP `4.6214` edge `0.0441` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2829` n `155` status `ready` deltaP `2.7893` edge `0.0082` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.392` n `113` status `ready` deltaP `13.9411` edge `0.0203` maxDD `-7.413`
- `market_context_high->fx_4h` score `-0.6074` n `155` status `ready` deltaP `3.034` edge `0.0053` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6187` n `155` status `ready` deltaP `0.4259` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->equity_24h` score `-0.6513` n `113` status `ready` deltaP `16.0322` edge `0.3725` maxDD `-40.0306`
- `market_context_high->index_4h` score `-0.8461` n `155` status `ready` deltaP `3.6192` edge `0.0171` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

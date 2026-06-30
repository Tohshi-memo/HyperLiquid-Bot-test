# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T05:52:30.957035+00:00`
- Price records: `672`
- Market context records: `5220`
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

- `market_context_high->unknown_24h` score `20.563` n `114` status `ready` deltaP `32.9495` edge `1.5129` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `14.04` n `114` status `ready` deltaP `32.1546` edge `1.3218` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.781` n `114` status `ready` deltaP `27.787` edge `0.8852` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0913` n `155` status `ready` deltaP `13.3891` edge `0.4116` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.053` n `155` status `ready` deltaP `14.0696` edge `0.4732` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.3961` n `155` status `ready` deltaP `18.0497` edge `0.2649` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8765` n `155` status `ready` deltaP `8.6884` edge `0.1626` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.591` n `114` status `ready` deltaP `13.8432` edge `0.0465` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.488` n `155` status `ready` deltaP `4.5036` edge `0.1068` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4829` n `155` status `ready` deltaP `6.4033` edge `0.1221` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.0555` n `155` status `ready` deltaP `6.1782` edge `0.1273` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1721` n `155` status `ready` deltaP `3.5126` edge `0.0137` maxDD `-2.0682`
- `market_context_high->fx_1h` score `-0.2331` n `155` status `ready` deltaP `2.2581` edge `0.0003` maxDD `-0.6194`
- `market_context_high->equity_1h` score `-0.2618` n `155` status `ready` deltaP `4.6214` edge `0.0439` maxDD `-5.0555`
- `market_context_high->index_1h` score `-0.2853` n `155` status `ready` deltaP `2.7893` edge `0.008` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.3771` n `114` status `ready` deltaP `14.0625` edge `0.0214` maxDD `-7.413`
- `market_context_high->equity_24h` score `-0.5282` n `114` status `ready` deltaP `16.1641` edge `0.3874` maxDD `-40.0306`
- `market_context_high->fx_4h` score `-0.6074` n `155` status `ready` deltaP `3.034` edge `0.0053` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6187` n `155` status `ready` deltaP `0.4259` edge `-0.0013` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.8643` n `155` status `ready` deltaP `3.4667` edge `0.0166` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T06:22:26.110353+00:00`
- Price records: `672`
- Market context records: `5222`
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

- `market_context_high->unknown_24h` score `20.1327` n `114` status `ready` deltaP `32.7759` edge `1.4782` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `13.9522` n `114` status `ready` deltaP `31.8073` edge `1.3168` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `8.7793` n `114` status `ready` deltaP `27.9606` edge `0.8839` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.0273` n `155` status `ready` deltaP `13.0842` edge `0.4083` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.0134` n `155` status `ready` deltaP `14.0696` edge `0.4699` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `3.0502` n `155` status `ready` deltaP `17.7449` edge `0.2381` maxDD `-5.5109`
- `market_context_high->unknown_1h` score `1.8861` n `155` status `ready` deltaP `8.6884` edge `0.1634` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5525` n `114` status `ready` deltaP `13.496` edge `0.0456` maxDD `-0.8294`
- `market_context_high->crypto_major_1h` score `0.4997` n `155` status `ready` deltaP `6.553` edge `0.1225` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `0.4761` n `155` status `ready` deltaP `4.3539` edge `0.1068` maxDD `-5.0257`
- `market_context_high->equity_4h` score `0.0507` n `155` status `ready` deltaP `6.1782` edge `0.1269` maxDD `-7.4425`
- `market_context_high->metal_1h` score `-0.1737` n `155` status `ready` deltaP `3.5126` edge `0.0135` maxDD `-2.0682`
- `market_context_high->equity_1h` score `-0.2127` n `155` status `ready` deltaP `4.9208` edge `0.046` maxDD `-5.0555`
- `market_context_high->fx_1h` score `-0.2503` n `155` status `ready` deltaP `1.9587` edge `0.0001` maxDD `-0.6194`
- `market_context_high->index_1h` score `-0.2697` n `155` status `ready` deltaP `2.939` edge `0.0083` maxDD `-1.0296`
- `market_context_high->index_24h` score `-0.3924` n `114` status `ready` deltaP `13.8889` edge `0.0206` maxDD `-7.413`
- `market_context_high->equity_24h` score `-0.4456` n `114` status `ready` deltaP `16.1641` edge `0.398` maxDD `-40.0306`
- `market_context_high->fx_4h` score `-0.6176` n `155` status `ready` deltaP `2.8816` edge `0.005` maxDD `-1.6047`
- `market_context_high->commodity_1h` score `-0.6195` n `155` status `ready` deltaP `0.4259` edge `-0.0014` maxDD `-2.4692`
- `market_context_high->index_4h` score `-0.8813` n `155` status `ready` deltaP `3.3143` edge `0.0162` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-30T11:07:28.897674+00:00`
- Price records: `672`
- Market context records: `5242`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `64`

- Symbol pattern count: `7568`

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

- `market_context_high->unknown_24h` score `24.1811` n `132` status `ready` deltaP `31.3447` edge `1.8251` maxDD `-0.8515`
- `market_context_high->crypto_major_24h` score `12.7065` n `132` status `ready` deltaP `32.7967` edge `1.2064` maxDD `-22.6266`
- `market_context_high->crypto_alt_24h` score `5.9437` n `132` status `ready` deltaP `20.4861` edge `0.7266` maxDD `-23.4292`
- `market_context_high->crypto_alt_4h` score `4.2993` n `155` status `ready` deltaP `14.6086` edge `0.4208` maxDD `-9.46`
- `market_context_high->crypto_major_4h` score `4.1074` n `155` status `ready` deltaP `15.2892` edge `0.4696` maxDD `-14.0065`
- `market_context_high->unknown_4h` score `2.2408` n `155` status `ready` deltaP `17.2875` edge `0.1737` maxDD `-5.5109`
- `market_context_high->equity_24h` score `1.78` n `132` status `ready` deltaP `18.1976` edge `0.5899` maxDD `-40.0306`
- `market_context_high->unknown_1h` score `1.3166` n `158` status `ready` deltaP `8.6504` edge `0.1162` maxDD `-2.7986`
- `market_context_high->fx_24h` score `0.5904` n `132` status `ready` deltaP `13.4154` edge `0.0493` maxDD `-0.8294`
- `market_context_high->crypto_alt_1h` score `0.5051` n `158` status `ready` deltaP `5.0765` edge `0.1044` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `0.4481` n `158` status `ready` deltaP `6.9885` edge `0.1153` maxDD `-6.9639`
- `market_context_high->equity_4h` score `0.3134` n `155` status `ready` deltaP `7.0928` edge `0.1427` maxDD `-7.4425`
- `market_context_high->index_24h` score `-0.071` n `132` status `ready` deltaP `18.4343` edge `0.0315` maxDD `-7.413`
- `market_context_high->equity_1h` score `-0.0806` n `158` status `ready` deltaP `6.1662` edge `0.0487` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.151` n `158` status `ready` deltaP `4.1442` edge `0.0122` maxDD `-2.0682`
- `market_context_high->index_1h` score `-0.159` n `158` status `ready` deltaP `4.2333` edge `0.0089` maxDD `-1.0296`
- `market_context_high->fx_1h` score `-0.3108` n `158` status `ready` deltaP `0.8849` edge `-0.0005` maxDD `-0.6194`
- `market_context_high->commodity_1h` score `-0.7026` n `158` status `ready` deltaP `-0.9323` edge `-0.003` maxDD `-2.4692`
- `market_context_high->fx_4h` score `-0.7932` n `155` status `ready` deltaP `-0.0148` edge `0.0018` maxDD `-1.6047`
- `market_context_high->index_4h` score `-0.8241` n `155` status `ready` deltaP `3.9241` edge `0.0169` maxDD `-2.9391`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

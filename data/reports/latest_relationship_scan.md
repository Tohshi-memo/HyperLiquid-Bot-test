# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-22T08:22:23.222609+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14742`

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

- `market_context_high->unknown_1h` score `1.3657` n `133` status `ready` deltaP `7.9387` edge `0.0836` maxDD `-0.4843`
- `market_context_high->unknown_4h` score `0.5051` n `133` status `ready` deltaP `20.1758` edge `-0.0485` maxDD `-0.5133`
- `market_context_high->index_1h` score `0.1374` n `133` status `ready` deltaP `9.8577` edge `0.005` maxDD `-0.9144`
- `market_context_high->fx_4h` score `0.1034` n `133` status `ready` deltaP `8.0575` edge `0.0098` maxDD `-0.3539`
- `market_context_high->fx_1h` score `-0.1704` n `133` status `ready` deltaP `1.4306` edge `0.0045` maxDD `-0.2043`
- `market_context_high->equity_1h` score `-0.175` n `133` status `ready` deltaP `7.0134` edge `0.0378` maxDD `-5.2257`
- `market_context_high->metal_4h` score `-0.2298` n `133` status `ready` deltaP `7.3858` edge `-0.0171` maxDD `-1.5942`
- `market_context_high->metal_1h` score `-0.288` n `133` status `ready` deltaP `1.4306` edge `-0.0046` maxDD `-0.6822`
- `market_context_high->commodity_1h` score `-0.6386` n `133` status `ready` deltaP `-3.6727` edge `-0.0008` maxDD `-1.1941`
- `market_context_high->index_4h` score `-0.6537` n `133` status `ready` deltaP `1.4018` edge `0.0104` maxDD `-2.618`
- `market_context_high->commodity_4h` score `-0.7123` n `133` status `ready` deltaP `-1.6184` edge `0.0045` maxDD `-2.4692`
- `market_context_high->crypto_alt_1h` score `-0.873` n `133` status `ready` deltaP `-0.3286` edge `0.0096` maxDD `-2.413`
- `market_context_high->crypto_major_1h` score `-1.4626` n `133` status `ready` deltaP `-2.4481` edge `-0.0687` maxDD `-4.1996`
- `market_context_high->commodity_24h` score `-1.5855` n `106` status `ready` deltaP `-5.3852` edge `0.0871` maxDD `-4.666`
- `market_context_high->equity_4h` score `-1.7442` n `133` status `ready` deltaP `-1.5152` edge `0.067` maxDD `-16.1079`
- `market_context_high->crypto_alt_4h` score `-1.8959` n `133` status `ready` deltaP `4.9652` edge `-0.0641` maxDD `-5.4926`
- `market_context_high->fx_24h` score `-2.5318` n `106` status `ready` deltaP `-7.5898` edge `0.0006` maxDD `-2.2121`
- `market_context_high->index_24h` score `-4.1744` n `106` status `ready` deltaP `-4.6646` edge `-0.0532` maxDD `-18.7377`
- `market_context_high->metal_24h` score `-5.0552` n `106` status `ready` deltaP `-20.0111` edge `-0.1839` maxDD `-11.4635`
- `market_context_high->crypto_major_4h` score `-5.3895` n `133` status `ready` deltaP `-1.9542` edge `-0.334` maxDD `-3.1677`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

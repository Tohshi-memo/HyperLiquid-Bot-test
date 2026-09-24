# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T20:37:32.275246+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9669`

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

- `market_context_high->unknown_1h` score `84.8623` n `47` status `ready` deltaP `10.116` edge `7.0115` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.2705` n `47` status `ready` deltaP `30.4226` edge `3.609` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.0892` n `47` status `ready` deltaP `24.782` edge `2.3802` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.0278` n `47` status `ready` deltaP `31.6378` edge `1.9103` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8859` n `47` status `ready` deltaP `35.2837` edge `0.4349` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `7.8742` n `112` status `ready` deltaP `-4.3787` edge `0.7098` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.0363` n `47` status `ready` deltaP `34.3639` edge `0.1311` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.4429` n `112` status `ready` deltaP `16.7612` edge `0.2242` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9145` n `47` status `ready` deltaP `33.4166` edge `0.0355` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.7054` n `105` status `ready` deltaP `17.3853` edge `0.3227` maxDD `-13.719`
- `news_risk_high->crypto_major_1h` score `2.6424` n `112` status `ready` deltaP `17.2209` edge `0.1489` maxDD `-1.8141`
- `news_risk_high->crypto_alt_4h` score `2.6374` n `105` status `ready` deltaP `8.9271` edge `0.4054` maxDD `-15.9436`
- `market_context_high->equity_4h` score `2.3709` n `47` status `ready` deltaP `16.992` edge `0.1261` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.2227` n `81` status `ready` deltaP `23.0324` edge `0.0915` maxDD `-1.7857`
- `news_risk_high->fx_4h` score `1.6309` n `105` status `ready` deltaP `23.6411` edge `0.0419` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.614` n `112` status `ready` deltaP `20.5517` edge `0.026` maxDD `-0.6142`
- `news_risk_high->crypto_major_24h` score `1.5912` n `81` status `ready` deltaP `-3.9351` edge `1.1345` maxDD `-63.6743`
- `market_context_high->index_1h` score `1.011` n `47` status `ready` deltaP `15.2089` edge `0.0107` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.969` n `47` status `ready` deltaP `11.9155` edge `0.0416` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7781` n `81` status `ready` deltaP `22.8588` edge `0.0922` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

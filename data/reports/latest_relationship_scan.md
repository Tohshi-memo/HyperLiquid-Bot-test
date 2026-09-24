# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T20:46:48.166492+00:00`
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

- `market_context_high->unknown_1h` score `84.7939` n `47` status `ready` deltaP `10.116` edge `7.0058` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `45.3797` n `47` status `ready` deltaP `30.4226` edge `3.6181` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `30.1444` n `47` status `ready` deltaP `24.782` edge `2.3848` maxDD `-2.7051`
- `market_context_high->equity_24h` score `25.0753` n `47` status `ready` deltaP `31.8114` edge `1.9131` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.9046` n `47` status `ready` deltaP `35.4573` edge `0.4353` maxDD `-0.3705`
- `news_risk_high->unknown_1h` score `6.9706` n `113` status `ready` deltaP `-4.2128` edge `0.6334` maxDD `-0.9543`
- `market_context_high->metal_24h` score `4.061` n `47` status `ready` deltaP `34.5375` edge `0.132` maxDD `-0.2401`
- `news_risk_high->crypto_alt_1h` score `3.3303` n `113` status `ready` deltaP `16.0895` edge `0.2193` maxDD `-1.5895`
- `market_context_high->index_4h` score `2.9145` n `47` status `ready` deltaP `33.4166` edge `0.0355` maxDD `-0.2323`
- `news_risk_high->crypto_major_4h` score `2.7248` n `105` status `ready` deltaP `17.5378` edge `0.3233` maxDD `-13.719`
- `news_risk_high->crypto_alt_4h` score `2.664` n `105` status `ready` deltaP `9.0796` edge `0.4066` maxDD `-15.9436`
- `news_risk_high->crypto_major_1h` score `2.5455` n `113` status `ready` deltaP `16.5651` edge `0.1452` maxDD `-1.8141`
- `market_context_high->equity_4h` score `2.3709` n `47` status `ready` deltaP `16.992` edge `0.1261` maxDD `-1.3444`
- `news_risk_high->commodity_24h` score `2.1908` n `81` status `ready` deltaP `22.8588` edge `0.09` maxDD `-1.7857`
- `news_risk_high->crypto_major_24h` score `1.6622` n `81` status `ready` deltaP `-3.9351` edge `1.1436` maxDD `-63.6743`
- `news_risk_high->fx_4h` score `1.6321` n `105` status `ready` deltaP `23.6411` edge `0.042` maxDD `-0.421`
- `news_risk_high->metal_1h` score `1.5707` n `113` status `ready` deltaP `20.1009` edge `0.0254` maxDD `-0.6142`
- `market_context_high->index_1h` score `1.0242` n `47` status `ready` deltaP `15.3586` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9846` n `47` status `ready` deltaP `12.0652` edge `0.0419` maxDD `-1.5564`
- `news_risk_high->metal_24h` score `0.7941` n `81` status `ready` deltaP `23.0324` edge `0.0931` maxDD `-7.2536`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-01T02:37:17.640637+00:00`
- Price records: `672`
- Market context records: `2521`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9312`

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

- `market_context_high->unknown_24h` score `4.9475` n `119` status `ready` deltaP `19.548` edge `0.3148` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `4.742` n `156` status `ready` deltaP `22.3147` edge `0.5143` maxDD `-15.4319`
- `market_context_high->crypto_major_4h` score `3.5155` n `156` status `ready` deltaP `16.1194` edge `0.3665` maxDD `-10.1468`
- `market_context_high->crypto_major_24h` score `2.261` n `119` status `ready` deltaP `11.8099` edge `0.6004` maxDD `-25.1408`
- `market_context_high->unknown_4h` score `2.155` n `156` status `ready` deltaP `11.9332` edge `0.205` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.1003` n `162` status `ready` deltaP `8.8841` edge `0.1512` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.6969` n `162` status `ready` deltaP `8.2483` edge `0.1225` maxDD `-4.2199`
- `market_context_high->crypto_alt_24h` score `0.0399` n `119` status `ready` deltaP `0.8782` edge `0.695` maxDD `-43.6595`
- `market_context_high->index_24h` score `0.0253` n `119` status `ready` deltaP `3.373` edge `0.0777` maxDD `-2.5127`
- `market_context_high->equity_24h` score `-0.1646` n `119` status `ready` deltaP `17.8324` edge `0.0201` maxDD `-6.8828`
- `market_context_high->index_4h` score `-0.2617` n `156` status `ready` deltaP `5.8709` edge `0.0232` maxDD `-2.3986`
- `market_context_high->index_1h` score `-0.3728` n `162` status `ready` deltaP `1.4009` edge `0.009` maxDD `-1.2855`
- `market_context_high->commodity_1h` score `-0.3875` n `162` status `ready` deltaP `3.9089` edge `0.0121` maxDD `-4.3601`
- `market_context_high->metal_1h` score `-0.4874` n `162` status `ready` deltaP `0.73` edge `0.0086` maxDD `-3.0759`
- `market_context_high->fx_1h` score `-0.5057` n `162` status `ready` deltaP `1.0849` edge `0.0041` maxDD `-0.278`
- `market_context_high->unknown_1h` score `-0.5624` n `162` status `ready` deltaP `1.8888` edge `0.0125` maxDD `-3.0902`
- `market_context_high->equity_1h` score `-0.7874` n `162` status `ready` deltaP `0.2015` edge `0.0169` maxDD `-2.7085`
- `market_context_high->fx_24h` score `-0.8493` n `119` status `ready` deltaP `3.2534` edge `0.0045` maxDD `-2.4729`
- `market_context_high->fx_4h` score `-0.8605` n `156` status `ready` deltaP `0.4886` edge `0.011` maxDD `-0.8774`
- `market_context_high->metal_4h` score `-0.9214` n `156` status `ready` deltaP `2.74` edge `0.0437` maxDD `-4.7664`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

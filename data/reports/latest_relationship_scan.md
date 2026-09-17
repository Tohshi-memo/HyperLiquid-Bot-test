# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T04:07:38.036279+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `384.756` n `83` status `ready` deltaP `-20.9007` edge `32.2918` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.1224` n `83` status `ready` deltaP `37.6569` edge `1.2304` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.7655` n `83` status `ready` deltaP `29.723` edge `1.2318` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.0231` n `83` status `ready` deltaP `38.9559` edge `0.8363` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.8855` n `52` status `ready` deltaP `43.9236` edge `0.3643` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8855` n `52` status `ready` deltaP `43.9236` edge `0.3643` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5863` n `149` status `ready` deltaP `37.2122` edge `0.3533` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.4044` n `83` status `ready` deltaP `44.3859` edge `0.2554` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.5918` n `83` status `ready` deltaP `31.9905` edge `0.2148` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5946` n `52` status `ready` deltaP `33.6672` edge `-0.004` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5946` n `52` status `ready` deltaP `33.6672` edge `-0.004` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4597` n `149` status `ready` deltaP `30.8923` edge `0.0206` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1591` n `52` status `ready` deltaP `27.5094` edge `0.0315` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1591` n `52` status `ready` deltaP `27.5094` edge `0.0315` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0588` n `149` status `ready` deltaP `24.0117` edge `0.0533` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8916` n `149` status `ready` deltaP `14.1151` edge `0.0179` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.384` n `83` status `ready` deltaP `12.0408` edge `0.0318` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2684` n `52` status `ready` deltaP `7.1972` edge `0.0096` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2684` n `52` status `ready` deltaP `7.1972` edge `0.0096` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1264` n `52` status `ready` deltaP `5.965` edge `0.007` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

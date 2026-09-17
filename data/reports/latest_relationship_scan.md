# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T19:22:35.697781+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9036`

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

- `news_risk_high->unknown_4h` score `421.6493` n `77` status `ready` deltaP `-18.5896` edge `35.3425` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.3076` n `52` status `ready` deltaP `50.0` edge `0.4423` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3076` n `52` status `ready` deltaP `50.0` edge `0.4423` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1932` n `69` status `ready` deltaP `27.5665` edge `0.6369` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0085` n `149` status `ready` deltaP `43.2886` edge `0.4313` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.3034` n `69` status `ready` deltaP `26.3889` edge `0.6101` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.2568` n `69` status `ready` deltaP `35.6205` edge `0.2182` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.9432` n `69` status `ready` deltaP `18.4103` edge `0.7105` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.4237` n `69` status `ready` deltaP `25.2944` edge `0.1621` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9697` n `52` status `ready` deltaP `32.6923` edge `0.0645` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9697` n `52` status `ready` deltaP `32.6923` edge `0.0645` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8694` n `149` status `ready` deltaP `29.1946` edge `0.0863` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.9209` n `52` status `ready` deltaP `26.8963` edge `-0.015` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.9209` n `52` status `ready` deltaP `26.8963` edge `-0.015` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.786` n `149` status `ready` deltaP `24.1214` edge `0.0096` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.2994` n `77` status `ready` deltaP `19.0014` edge `0.0282` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.1697` n `149` status `ready` deltaP `16.5103` edge `0.0251` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.5924` edge `0.0168` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.5924` edge `0.0168` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

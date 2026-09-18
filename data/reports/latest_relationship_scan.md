# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T20:07:27.108942+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8194`

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

- `market_context_high->unknown_4h` score `38.0788` n `149` status `ready` deltaP `-0.9208` edge `3.2027` maxDD `-0.5326`
- `news_risk_high->crypto_alt_24h` score `35.4565` n `39` status `ready` deltaP `33.7073` edge `2.8679` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `22.6653` n `39` status `ready` deltaP `13.5016` edge `2.9317` maxDD `-6.6058`
- `risk_on_high->unknown_4h` score `11.9575` n `52` status `ready` deltaP `-8.1614` edge `1.0734` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.9575` n `52` status `ready` deltaP `-8.1614` edge `1.0734` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5949` n `52` status `ready` deltaP `47.9167` edge `0.3968` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `8.2984` n `85` status `ready` deltaP `27.4551` edge `0.6211` maxDD `-7.675`
- `market_context_high->commodity_24h` score `7.2958` n `149` status `ready` deltaP `41.2053` edge `0.3858` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `5.4811` n `39` status `ready` deltaP `21.5278` edge `0.4102` maxDD `-3.4232`
- `risk_on_high->commodity_4h` score `2.8453` n `52` status `ready` deltaP `32.9972` edge `0.0521` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8453` n `52` status `ready` deltaP `32.9972` edge `0.0521` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.745` n `149` status `ready` deltaP `29.4995` edge `0.0739` maxDD `-0.345`
- `news_risk_high->crypto_major_4h` score `2.3474` n `85` status `ready` deltaP `18.2819` edge `0.3488` maxDD `-10.9113`
- `news_risk_high->equity_4h` score `1.9736` n `85` status `ready` deltaP `17.6488` edge `0.1368` maxDD `-4.1995`
- `news_risk_high->metal_24h` score `1.4039` n `39` status `ready` deltaP `10.4968` edge `0.0753` maxDD `-0.2629`
- `market_context_high->commodity_1h` score `1.166` n `149` status `ready` deltaP `16.66` edge `0.0238` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `1.093` n `85` status `ready` deltaP `13.4008` edge `0.0423` maxDD `-0.9112`
- `news_risk_high->crypto_alt_1h` score `1.0559` n `85` status `ready` deltaP `11.8193` edge `0.1353` maxDD `-3.6312`
- `news_risk_high->fx_4h` score `0.9416` n `85` status `ready` deltaP `11.3755` edge `0.0301` maxDD `-0.1976`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

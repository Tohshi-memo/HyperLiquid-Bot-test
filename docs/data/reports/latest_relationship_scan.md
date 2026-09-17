# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T23:52:32.093535+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8686`

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

- `market_context_high->unknown_4h` score `35.7086` n `149` status `ready` deltaP `-0.1586` edge `3.0001` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `19.5141` n `71` status `ready` deltaP `-9.8098` edge `1.7562` maxDD `-3.1699`
- `risk_on_high->unknown_4h` score `9.5873` n `52` status `ready` deltaP `-7.3992` edge `0.8708` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5873` n `52` status `ready` deltaP `-7.3992` edge `0.8708` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.1336` n `52` status `ready` deltaP `50.0` edge `0.4278` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1336` n `52` status `ready` deltaP `50.0` edge `0.4278` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.9978` n `51` status `ready` deltaP `32.404` edge `0.6717` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8345` n `149` status `ready` deltaP `43.2886` edge `0.4168` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.3159` n `51` status `ready` deltaP `29.9939` edge `0.1773` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.2665` n `51` status `ready` deltaP `14.6242` edge `0.4987` maxDD `-6.5262`
- `risk_on_high->commodity_4h` score `3.0377` n `52` status `ready` deltaP `33.3021` edge `0.0661` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0377` n `52` status `ready` deltaP `33.3021` edge `0.0661` maxDD `-0.1313`
- `news_risk_high->crypto_major_24h` score `2.9463` n `51` status `ready` deltaP `8.1801` edge `0.5227` maxDD `-13.2931`
- `market_context_high->commodity_4h` score `2.9374` n `149` status `ready` deltaP `29.8044` edge `0.0879` maxDD `-0.345`
- `news_risk_high->metal_24h` score `1.9812` n `51` status `ready` deltaP `14.5527` edge `0.1135` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.7788` n `52` status `ready` deltaP `25.8547` edge `-0.0199` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.7788` n `52` status `ready` deltaP `25.8547` edge `-0.0199` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6439` n `149` status `ready` deltaP `23.0798` edge `0.0047` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2811` n `149` status `ready` deltaP `17.5582` edge `0.0274` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.8853` n `71` status `ready` deltaP `14.0201` edge `0.0269` maxDD `-0.3938`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

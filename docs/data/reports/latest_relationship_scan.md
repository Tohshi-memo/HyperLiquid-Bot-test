# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T00:29:33.595317+00:00`
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

- `market_context_high->unknown_4h` score `35.6446` n `149` status `ready` deltaP `-0.4634` edge `2.9968` maxDD `-0.5326`
- `news_risk_high->unknown_4h` score `20.1505` n `71` status `ready` deltaP `-7.2977` edge `1.7836` maxDD `-2.4592`
- `risk_on_high->unknown_4h` score `9.5233` n `52` status `ready` deltaP `-7.704` edge `0.8675` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.5233` n `52` status `ready` deltaP `-7.704` edge `0.8675` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `9.1096` n `52` status `ready` deltaP `50.0` edge `0.4258` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1096` n `52` status `ready` deltaP `50.0` edge `0.4258` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.907` n `49` status `ready` deltaP `31.7638` edge `0.6684` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.8105` n `149` status `ready` deltaP `43.2886` edge `0.4148` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `4.6153` n `49` status `ready` deltaP `12.7834` edge `0.4768` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.1722` n `49` status `ready` deltaP `29.1135` edge `0.1712` maxDD `-0.075`
- `risk_on_high->commodity_4h` score `3.0353` n `52` status `ready` deltaP `33.3021` edge `0.0659` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0353` n `52` status `ready` deltaP `33.3021` edge `0.0659` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.935` n `149` status `ready` deltaP `29.8044` edge `0.0877` maxDD `-0.345`
- `news_risk_high->crypto_major_24h` score `2.5527` n `49` status `ready` deltaP `6.5795` edge `0.4829` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `1.7604` n `49` status `ready` deltaP `12.8721` edge `0.1063` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.739` n `52` status `ready` deltaP `25.5075` edge `-0.0209` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.739` n `52` status `ready` deltaP `25.5075` edge `-0.0209` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6041` n `149` status `ready` deltaP `22.7326` edge `0.0037` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2787` n `149` status `ready` deltaP `17.5582` edge `0.0272` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6554` n `52` status `ready` deltaP `10.6403` edge `0.0189` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

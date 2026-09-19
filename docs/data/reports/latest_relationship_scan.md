# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T06:22:33.166694+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8452`

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

- `news_risk_high->crypto_major_24h` score `58.6516` n `62` status `ready` deltaP `35.3887` edge `4.7409` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `52.2145` n `62` status `ready` deltaP `38.4633` edge `4.2327` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `35.9657` n `149` status `ready` deltaP `-1.8354` edge `3.0327` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `13.4458` n `62` status `ready` deltaP `47.7431` edge `0.8022` maxDD `0.0`
- `risk_on_high->unknown_4h` score `9.8443` n `52` status `ready` deltaP `-9.076` edge `0.9034` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `9.8443` n `52` status `ready` deltaP `-9.076` edge `0.9034` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2628` n `52` status `ready` deltaP `44.9653` edge `0.3888` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2628` n `52` status `ready` deltaP `44.9653` edge `0.3888` maxDD `0.0`
- `news_risk_high->crypto_alt_4h` score `7.6301` n `78` status `ready` deltaP `25.0117` edge `0.5817` maxDD `-7.675`
- `market_context_high->commodity_24h` score `6.9637` n `149` status `ready` deltaP `38.2539` edge `0.3778` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.2008` n `78` status `ready` deltaP `21.7128` edge `0.4061` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.1339` n `62` status `ready` deltaP `34.4926` edge `0.1304` maxDD `-0.2687`
- `news_risk_high->crypto_alt_1h` score `3.3273` n `81` status `ready` deltaP `17.3006` edge `0.2085` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6257` n `81` status `ready` deltaP `20.0691` edge `0.1373` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.416` n `78` status `ready` deltaP `15.8224` edge `0.0344` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.1561` n `62` status `ready` deltaP `6.5468` edge `0.0569` maxDD `-0.0029`
- `market_context_high->commodity_1h` score `1.0271` n `149` status `ready` deltaP `15.3127` edge `0.0212` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

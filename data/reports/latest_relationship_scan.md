# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T21:53:05.838018+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8146`

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

- `news_risk_high->crypto_major_24h` score `43.9002` n `39` status `ready` deltaP `22.7164` edge `3.5961` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `42.1705` n `39` status `ready` deltaP `33.7073` edge `3.4274` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.732` n `149` status `ready` deltaP `-0.9208` edge `3.1738` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `11.6107` n `52` status `ready` deltaP `-8.1614` edge `1.0445` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.6107` n `52` status `ready` deltaP `-8.1614` edge `1.0445` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.8664` n `81` status `ready` deltaP `29.6052` edge `0.6541` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5829` n `52` status `ready` deltaP `47.9167` edge `0.3958` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.2509` n `39` status `ready` deltaP `30.5689` edge `0.5514` maxDD `-2.4096`
- `market_context_high->commodity_24h` score `7.2838` n `149` status `ready` deltaP `41.2053` edge `0.3848` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `3.1533` n `81` status `ready` deltaP `20.933` edge `0.3883` maxDD `-8.5536`
- `risk_on_high->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8429` n `52` status `ready` deltaP `32.9972` edge `0.0519` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7426` n `149` status `ready` deltaP `29.4995` edge `0.0737` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.4` n `39` status `ready` deltaP `17.6683` edge `0.1105` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `2.1733` n `81` status `ready` deltaP `13.4472` edge `0.1516` maxDD `-2.8111`
- `news_risk_high->equity_4h` score `1.7897` n `81` status `ready` deltaP `15.9497` edge `0.1328` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.2242` n `81` status `ready` deltaP `13.6781` edge `0.0328` maxDD `-0.0909`
- `news_risk_high->crypto_major_1h` score `1.1401` n `81` status `ready` deltaP `16.7018` edge `0.1042` maxDD `-3.5505`
- `market_context_high->commodity_1h` score `1.1337` n `149` status `ready` deltaP `16.3606` edge `0.0231` maxDD `-0.3491`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

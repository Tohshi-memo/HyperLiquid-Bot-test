# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-15T09:52:31.051055+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11184`

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

- `news_risk_high->unknown_4h` score `396.8254` n `78` status `ready` deltaP `-22.303` edge `33.3068` maxDD `-4.1464`
- `news_risk_high->crypto_alt_24h` score `21.9139` n `78` status `ready` deltaP `45.6864` edge `1.5607` maxDD `-1.4626`
- `news_risk_high->unknown_24h` score `21.6869` n `78` status `ready` deltaP `18.5764` edge `1.6834` maxDD `0.0`
- `news_risk_high->crypto_major_24h` score `16.6221` n `78` status `ready` deltaP `35.39` edge `1.2963` maxDD `-9.098`
- `news_risk_high->equity_24h` score `15.1402` n `78` status `ready` deltaP `48.4642` edge `1.1166` maxDD `-6.5742`
- `news_risk_high->index_24h` score `8.7185` n `78` status `ready` deltaP `62.2863` edge `0.3289` maxDD `-0.075`
- `news_risk_high->metal_24h` score `6.5909` n `78` status `ready` deltaP `39.0091` edge `0.3346` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.957` n `52` status `ready` deltaP `37.8472` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.957` n `52` status `ready` deltaP `37.8472` edge `0.2441` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.66` n `137` status `ready` deltaP `30.5479` edge `0.2372` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `3.7431` n `52` status `ready` deltaP `43.3894` edge `0.0269` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `3.7431` n `52` status `ready` deltaP `43.3894` edge `0.0269` maxDD `-0.0054`
- `market_context_high->fx_24h` score `3.3461` n `137` status `ready` deltaP `40.203` edge `0.0324` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `1.8961` n `52` status `ready` deltaP `24.613` edge `0.0289` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `1.8961` n `52` status `ready` deltaP `24.613` edge `0.0289` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `1.7959` n `149` status `ready` deltaP `21.1153` edge `0.0507` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8018` n `149` status `ready` deltaP `13.0672` edge `0.0174` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.7327` n `78` status `ready` deltaP `17.7259` edge `0.0386` maxDD `-0.6935`
- `risk_on_high->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`
- `risk_on_and_context->metal_1h` score `0.2494` n `52` status `ready` deltaP `8.2105` edge `0.0078` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

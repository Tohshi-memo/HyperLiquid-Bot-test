# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T23:52:26.237266+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8098`

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

- `news_risk_high->crypto_major_24h` score `60.2616` n `39` status `ready` deltaP `32.2783` edge `4.8958` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `55.0477` n `39` status `ready` deltaP `33.7073` edge `4.5005` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.8903` n `149` status `ready` deltaP `-1.0732` edge `3.188` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.2051` n `39` status `ready` deltaP `49.6928` edge `0.8599` maxDD `-0.2611`
- `risk_on_high->unknown_4h` score `11.7689` n `52` status `ready` deltaP `-8.3138` edge `1.0587` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `11.7689` n `52` status `ready` deltaP `-8.3138` edge `1.0587` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.9274` n `73` status `ready` deltaP `28.5228` edge `0.6664` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.5492` n `52` status `ready` deltaP `47.5694` edge `0.3953` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.5492` n `52` status `ready` deltaP `47.5694` edge `0.3953` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.25` n `149` status `ready` deltaP `40.858` edge `0.3843` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `6.0696` n `73` status `ready` deltaP `25.1775` edge `0.4554` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.5495` n `39` status `ready` deltaP `32.0112` edge `0.1815` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2285` n `73` status `ready` deltaP `17.8349` edge `0.1967` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.8921` n `73` status `ready` deltaP `22.0942` edge `0.146` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.7809` n `52` status `ready` deltaP `32.3874` edge `0.0508` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7809` n `52` status `ready` deltaP `32.3874` edge `0.0508` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6806` n `149` status `ready` deltaP `28.8897` edge `0.0726` maxDD `-0.345`
- `news_risk_high->fx_24h` score `1.6461` n `39` status `ready` deltaP `7.0246` edge `0.0946` maxDD `-0.0069`
- `news_risk_high->equity_4h` score `1.5515` n `73` status `ready` deltaP `12.7026` edge `0.1346` maxDD `-4.1995`
- `news_risk_high->fx_4h` score `1.5209` n `73` status `ready` deltaP `16.6535` edge `0.0376` maxDD `-0.084`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-18T09:37:36.113829+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8338`

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

- `market_context_high->unknown_4h` score `39.6084` n `149` status `ready` deltaP `-0.311` edge `3.3261` maxDD `-0.5326`
- `risk_on_high->unknown_4h` score `13.4871` n `52` status `ready` deltaP `-7.5516` edge `1.1968` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `13.4871` n `52` status `ready` deltaP `-7.5516` edge `1.1968` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.8744` n `52` status `ready` deltaP `50.0` edge `0.4062` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.8744` n `52` status `ready` deltaP `50.0` edge `0.4062` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.5753` n `149` status `ready` deltaP `43.2886` edge `0.3952` maxDD `-0.8682`
- `risk_on_high->commodity_4h` score `2.8511` n `52` status `ready` deltaP `32.8447` edge `0.0536` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8511` n `52` status `ready` deltaP `32.8447` edge `0.0536` maxDD `-0.1313`
- `news_risk_high->crypto_alt_4h` score `2.7914` n `82` status `ready` deltaP `19.0549` edge `0.4459` maxDD `-12.8718`
- `market_context_high->commodity_4h` score `2.7508` n `149` status `ready` deltaP `29.347` edge `0.0754` maxDD `-0.345`
- `news_risk_high->equity_4h` score `1.2643` n `82` status `ready` deltaP `15.7012` edge `0.1411` maxDD `-3.3619`
- `market_context_high->commodity_1h` score `1.1684` n `149` status `ready` deltaP `16.66` edge `0.024` maxDD `-0.3491`
- `risk_on_high->fx_24h` score `1.0103` n `52` status `ready` deltaP `19.0838` edge `-0.0388` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.0103` n `52` status `ready` deltaP `19.0838` edge `-0.0388` maxDD `-0.0054`
- `market_context_high->fx_24h` score `0.8754` n `149` status `ready` deltaP `16.3089` edge `-0.0142` maxDD `-0.0593`
- `risk_on_high->commodity_1h` score `0.5452` n `52` status `ready` deltaP `9.7421` edge `0.0157` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5452` n `52` status `ready` deltaP `9.7421` edge `0.0157` maxDD `-0.1507`
- `news_risk_high->equity_1h` score `0.331` n `94` status `ready` deltaP `10.4567` edge `0.0249` maxDD `-1.8403`
- `news_risk_high->fx_4h` score `0.2749` n `82` status `ready` deltaP `8.5366` edge `0.023` maxDD `-0.2398`
- `market_context_high->fx_1h` score `-0.0511` n `149` status `ready` deltaP `2.8554` edge `0.0002` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

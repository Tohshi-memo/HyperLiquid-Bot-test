# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T17:07:41.147880+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `11689`

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

- `news_risk_high->unknown_4h` score `367.153` n `83` status `ready` deltaP `-21.0531` edge `30.8259` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `22.3208` n `79` status `ready` deltaP `46.6662` edge `1.6011` maxDD `-2.5048`
- `news_risk_high->crypto_major_24h` score `19.9848` n `79` status `ready` deltaP `38.7241` edge `1.5543` maxDD `-9.098`
- `news_risk_high->equity_24h` score `13.9573` n `79` status `ready` deltaP `45.018` edge `1.0404` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.3126` n `79` status `ready` deltaP `50.8328` edge `0.2881` maxDD `-0.075`
- `news_risk_high->metal_24h` score `5.8482` n `79` status `ready` deltaP `34.63` edge `0.3019` maxDD `-0.6334`
- `risk_on_high->commodity_24h` score `5.772` n `52` status `ready` deltaP `36.2847` edge `0.2391` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.772` n `52` status `ready` deltaP `36.2847` edge `0.2391` maxDD `0.0`
- `market_context_high->commodity_24h` score `4.4728` n `149` status `ready` deltaP `29.5733` edge `0.2281` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3825` n `52` status `ready` deltaP `31.9311` edge `-0.0101` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3825` n `52` status `ready` deltaP `31.9311` edge `-0.0101` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2476` n `149` status `ready` deltaP `29.1562` edge `0.0145` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.2432` n `52` status `ready` deltaP `28.5764` edge `0.0314` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2432` n `52` status `ready` deltaP `28.5764` edge `0.0314` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.1429` n `149` status `ready` deltaP `25.0787` edge `0.0532` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8881` n `149` status `ready` deltaP `13.9654` edge `0.0186` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.4304` n `52` status `ready` deltaP `9.8499` edge `0.151` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4304` n `52` status `ready` deltaP `9.8499` edge `0.151` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.374` n `83` status `ready` deltaP `12.1933` edge `0.0295` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2648` n `52` status `ready` deltaP `7.0475` edge `0.0103` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

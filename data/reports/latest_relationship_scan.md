# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-16T17:37:39.113808+00:00`
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

- `news_risk_high->unknown_4h` score `366.595` n `83` status `ready` deltaP `-21.0531` edge `30.7794` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `21.2417` n `80` status `ready` deltaP `45.5903` edge `1.5521` maxDD `-5.2046`
- `news_risk_high->crypto_major_24h` score `19.183` n `80` status `ready` deltaP `37.7431` edge `1.5154` maxDD `-10.8086`
- `news_risk_high->equity_24h` score `13.9238` n `80` status `ready` deltaP `45.0347` edge `1.0375` maxDD `-6.5262`
- `news_risk_high->index_24h` score `7.2807` n `80` status `ready` deltaP `50.6597` edge `0.2866` maxDD `-0.075`
- `risk_on_high->commodity_24h` score `5.8598` n `52` status `ready` deltaP `36.6319` edge `0.2441` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `5.8598` n `52` status `ready` deltaP `36.6319` edge `0.2441` maxDD `0.0`
- `news_risk_high->metal_24h` score `5.8109` n `80` status `ready` deltaP `34.5833` edge `0.2991` maxDD `-0.6334`
- `market_context_high->commodity_24h` score `4.5606` n `149` status `ready` deltaP `29.9205` edge `0.2331` maxDD `-0.8682`
- `risk_on_high->fx_24h` score `2.3861` n `52` status `ready` deltaP `31.9311` edge `-0.0098` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3861` n `52` status `ready` deltaP `31.9311` edge `-0.0098` maxDD `-0.0054`
- `risk_on_high->commodity_4h` score `2.2576` n `52` status `ready` deltaP `28.5764` edge `0.0326` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.2576` n `52` status `ready` deltaP `28.5764` edge `0.0326` maxDD `-0.1313`
- `market_context_high->fx_24h` score `2.2512` n `149` status `ready` deltaP `29.1562` edge `0.0148` maxDD `-0.0593`
- `market_context_high->commodity_4h` score `2.1573` n `149` status `ready` deltaP `25.0787` edge `0.0544` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8857` n `149` status `ready` deltaP `13.9654` edge `0.0184` maxDD `-0.3491`
- `risk_on_high->crypto_alt_4h` score `0.4288` n `52` status `ready` deltaP `9.8499` edge `0.1508` maxDD `-6.2526`
- `risk_on_and_context->crypto_alt_4h` score `0.4288` n `52` status `ready` deltaP `9.8499` edge `0.1508` maxDD `-6.2526`
- `news_risk_high->index_4h` score `0.374` n `83` status `ready` deltaP `12.1933` edge `0.0295` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2624` n `52` status `ready` deltaP `7.0475` edge `0.0101` maxDD `-0.1507`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

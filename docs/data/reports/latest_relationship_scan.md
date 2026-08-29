# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-29T13:52:29.551118+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11396`

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

- `news_risk_high->unknown_24h` score `50.6147` n `56` status `ready` deltaP `16.0218` edge `4.1656` maxDD `-2.3617`
- `news_risk_high->crypto_alt_24h` score `24.799` n `56` status `ready` deltaP `37.2768` edge `2.0387` maxDD `-14.9839`
- `market_context_high->unknown_24h` score `8.2718` n `105` status `ready` deltaP `19.1171` edge `0.6351` maxDD `-3.1917`
- `news_risk_high->unknown_4h` score `6.3679` n `80` status `ready` deltaP `11.5854` edge `0.5124` maxDD `-1.7183`
- `market_context_high->metal_24h` score `4.3406` n `105` status `ready` deltaP `31.8205` edge `0.2515` maxDD `-3.1535`
- `news_risk_high->equity_24h` score `2.9397` n `56` status `ready` deltaP `25.0` edge `0.3994` maxDD `-12.4677`
- `news_risk_high->unknown_1h` score `2.6619` n `80` status `ready` deltaP `5.6737` edge `0.2197` maxDD `-0.8558`
- `news_risk_high->crypto_major_24h` score `2.6058` n `56` status `ready` deltaP `21.3542` edge `0.4316` maxDD `-16.524`
- `market_context_high->unknown_4h` score `2.4771` n `113` status `ready` deltaP `17.1164` edge `0.1355` maxDD `-0.788`
- `news_risk_high->fx_4h` score `2.4303` n `80` status `ready` deltaP `35.2744` edge `0.0223` maxDD `-0.3953`
- `news_risk_high->metal_24h` score `1.8881` n `56` status `ready` deltaP `38.3681` edge `0.0577` maxDD `-3.7137`
- `news_risk_high->index_24h` score `1.5514` n `56` status `ready` deltaP `21.2797` edge `0.0294` maxDD `-1.0255`
- `market_context_high->unknown_1h` score `1.1459` n `125` status `ready` deltaP `9.3737` edge `0.0811` maxDD `-1.5148`
- `news_risk_high->fx_1h` score `0.7735` n `80` status `ready` deltaP `14.6407` edge `0.0057` maxDD `-0.108`
- `news_risk_high->commodity_1h` score `0.3925` n `80` status `ready` deltaP `11.6018` edge `0.005` maxDD `-0.5618`
- `market_context_high->crypto_major_4h` score `-0.2409` n `113` status `ready` deltaP `17.6545` edge `0.2073` maxDD `-20.9394`
- `market_context_high->metal_4h` score `-0.3527` n `113` status `ready` deltaP `5.79` edge `0.0079` maxDD `-3.3377`
- `news_risk_high->index_1h` score `-0.391` n `80` status `ready` deltaP `0.3069` edge `-0.0085` maxDD `-0.8275`
- `market_context_high->commodity_1h` score `-0.4592` n `125` status `ready` deltaP `0.3018` edge `0.0085` maxDD `-1.5507`
- `news_risk_high->index_4h` score `-0.5364` n `80` status `ready` deltaP `1.7683` edge `-0.0164` maxDD `-1.7996`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

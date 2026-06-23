# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T12:07:32.459514+00:00`
- Price records: `672`
- Market context records: `4514`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9771`

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

- `risk_on_high->unknown_4h` score `128.3945` n `48` status `ready` deltaP `5.8435` edge `10.8142` maxDD `-8.9559`
- `risk_on_and_context->unknown_4h` score `128.3945` n `48` status `ready` deltaP `5.8435` edge `10.8142` maxDD `-8.9559`
- `market_context_high->unknown_1h` score `44.0494` n `195` status `ready` deltaP `4.8212` edge `3.7605` maxDD `-7.4156`
- `market_context_high->unknown_4h` score `25.7989` n `195` status `ready` deltaP `5.8435` edge `2.2854` maxDD `-8.9559`
- `risk_on_high->equity_4h` score `5.0959` n `48` status `ready` deltaP `41.7683` edge `0.1462` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0959` n `48` status `ready` deltaP `41.7683` edge `0.1462` maxDD `0.0`
- `risk_on_high->crypto_major_4h` score `4.399` n `48` status `ready` deltaP `26.1687` edge `0.2513` maxDD `-2.4005`
- `risk_on_and_context->crypto_major_4h` score `4.399` n `48` status `ready` deltaP `26.1687` edge `0.2513` maxDD `-2.4005`
- `risk_on_high->metal_24h` score `2.8712` n `48` status `ready` deltaP `-11.1111` edge `0.5401` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `2.8712` n `48` status `ready` deltaP `-11.1111` edge `0.5401` maxDD `-4.834`
- `risk_on_high->unknown_24h` score `2.6005` n `48` status `ready` deltaP `11.4583` edge `0.2028` maxDD `-3.9982`
- `risk_on_and_context->unknown_24h` score `2.6005` n `48` status `ready` deltaP `11.4583` edge `0.2028` maxDD `-3.9982`
- `risk_on_high->metal_4h` score `2.1814` n `48` status `ready` deltaP `16.9716` edge `0.1022` maxDD `-1.3516`
- `risk_on_and_context->metal_4h` score `2.1814` n `48` status `ready` deltaP `16.9716` edge `0.1022` maxDD `-1.3516`
- `risk_on_high->equity_1h` score `1.2611` n `48` status `ready` deltaP `15.4441` edge `0.0364` maxDD `-0.7415`
- `risk_on_and_context->equity_1h` score `1.2611` n `48` status `ready` deltaP `15.4441` edge `0.0364` maxDD `-0.7415`
- `risk_on_high->index_24h` score `1.2191` n `48` status `ready` deltaP `21.1805` edge `0.0121` maxDD `-2.4702`
- `risk_on_and_context->index_24h` score `1.2191` n `48` status `ready` deltaP `21.1805` edge `0.0121` maxDD `-2.4702`
- `risk_on_high->fx_4h` score `0.6164` n `48` status `ready` deltaP `15.3963` edge `0.0078` maxDD `-0.3925`
- `risk_on_and_context->fx_4h` score `0.6164` n `48` status `ready` deltaP `15.3963` edge `0.0078` maxDD `-0.3925`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T19:52:28.417143+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9318`

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

- `market_context_high->crypto_major_4h` score `1.9336` n `112` status `ready` deltaP `20.5575` edge `0.4513` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8837` n `112` status `ready` deltaP `17.8991` edge `0.1228` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.6221` n `79` status `ready` deltaP `19.4475` edge `0.0853` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.6221` n `79` status `ready` deltaP `19.4475` edge `0.0853` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.5822` n `79` status `ready` deltaP `21.7216` edge `0.3061` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5822` n `79` status `ready` deltaP `21.7216` edge `0.3061` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.6055` n `112` status `ready` deltaP `7.2926` edge `0.1179` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1611` n `79` status `ready` deltaP `7.9903` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1611` n `79` status `ready` deltaP `7.9903` edge `0.0058` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2345` n `79` status `ready` deltaP `10.6284` edge `0.0287` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2345` n `79` status `ready` deltaP `10.6284` edge `0.0287` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.391` n `112` status `ready` deltaP `1.0746` edge `0.0927` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.4893` n `79` status `ready` deltaP `-3.1646` edge `-0.0036` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.4893` n `79` status `ready` deltaP `-3.1646` edge `-0.0036` maxDD `-0.376`
- `market_context_high->index_1h` score `-0.5734` n `112` status `ready` deltaP `3.786` edge `0.0018` maxDD `-1.3195`
- `risk_on_high->crypto_major_1h` score `-0.5841` n `79` status `ready` deltaP `2.0484` edge `0.0296` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.5841` n `79` status `ready` deltaP `2.0484` edge `0.0296` maxDD `-4.6876`
- `risk_on_high->metal_1h` score `-0.6888` n `79` status `ready` deltaP `-2.7704` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.6888` n `79` status `ready` deltaP `-2.7704` edge `0.0033` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.7062` n `112` status `ready` deltaP `-5.3571` edge `-0.0027` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

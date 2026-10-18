# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T12:37:25.682435+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9246`

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

- `market_context_high->commodity_24h` score `2.3651` n `128` status `ready` deltaP `19.6565` edge `0.1512` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.8185` n `90` status `ready` deltaP `20.5071` edge `0.0946` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8185` n `90` status `ready` deltaP `20.5071` edge `0.0946` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `1.7874` n `138` status `ready` deltaP `16.3198` edge `0.3806` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.784` n `138` status `ready` deltaP `5.8991` edge `0.1149` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.245` n `91` status `ready` deltaP `14.0663` edge `0.1857` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.245` n `91` status `ready` deltaP `14.0663` edge `0.1857` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `-0.0125` n `138` status `ready` deltaP `5.1679` edge `0.1145` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0184` n `91` status `ready` deltaP `4.7058` edge `0.0055` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0184` n `91` status `ready` deltaP `4.7058` edge `0.0055` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2398` n `91` status `ready` deltaP `1.4982` edge `-0.0027` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2398` n `91` status `ready` deltaP `1.4982` edge `-0.0027` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.4022` n `138` status `ready` deltaP `4.018` edge `0.0086` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.4343` n `138` status `ready` deltaP `5.2553` edge `0.0036` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.438` n `91` status `ready` deltaP `9.5585` edge `0.0294` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.438` n `91` status `ready` deltaP `9.5585` edge `0.0294` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5101` n `91` status `ready` deltaP `0.5461` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5101` n `91` status `ready` deltaP `0.5461` edge `0.0041` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6424` n `138` status `ready` deltaP `5.2603` edge `0.0451` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.717` n `138` status `ready` deltaP `-0.8748` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

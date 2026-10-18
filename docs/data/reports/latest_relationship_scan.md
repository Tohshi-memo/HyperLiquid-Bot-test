# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T21:07:29.456219+00:00`
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

- `market_context_high->crypto_major_4h` score `1.999` n `107` status `ready` deltaP `19.609` edge `0.466` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8857` n `107` status `ready` deltaP `17.1134` edge `0.1282` maxDD `-1.8119`
- `risk_on_high->crypto_major_4h` score `1.5636` n `74` status `ready` deltaP `20.089` edge `0.3146` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5636` n `74` status `ready` deltaP `20.089` edge `0.3146` maxDD `-11.1788`
- `risk_on_high->commodity_24h` score `1.0326` n `74` status `ready` deltaP `18.3384` edge `0.0899` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.0326` n `74` status `ready` deltaP `18.3384` edge `0.0899` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.8088` n `107` status `ready` deltaP `8.8785` edge `0.1334` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.3234` n `74` status `ready` deltaP `11.1112` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.3234` n `74` status `ready` deltaP `11.1112` edge `0.0058` maxDD `-0.7394`
- `market_context_high->crypto_alt_1h` score `-0.1181` n `107` status `ready` deltaP `3.0528` edge `0.1145` maxDD `-7.3329`
- `risk_on_high->crypto_major_1h` score `-0.1466` n `74` status `ready` deltaP `4.0541` edge `0.0461` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.1466` n `74` status `ready` deltaP `4.0541` edge `0.0461` maxDD `-4.6876`
- `risk_on_high->equity_1h` score `-0.2104` n `74` status `ready` deltaP `12.6127` edge `0.028` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2104` n `74` status `ready` deltaP `12.6127` edge `0.028` maxDD `-5.3696`
- `risk_on_high->fx_1h` score `-0.3818` n `74` status `ready` deltaP `-1.3514` edge `-0.0027` maxDD `-0.3121`
- `risk_on_and_context->fx_1h` score `-0.3818` n `74` status `ready` deltaP `-1.3514` edge `-0.0027` maxDD `-0.3121`
- `market_context_high->index_1h` score `-0.4263` n `107` status `ready` deltaP `5.6552` edge `0.0016` maxDD `-1.3195`
- `market_context_high->metal_4h` score `-0.5893` n `107` status `ready` deltaP `1.5671` edge `0.0477` maxDD `-1.6961`
- `market_context_high->metal_1h` score `-0.9065` n `107` status `ready` deltaP `0.4351` edge `0.0085` maxDD `-0.9556`
- `risk_on_high->metal_4h` score `-0.9157` n `74` status `ready` deltaP `-5.4549` edge `0.0235` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

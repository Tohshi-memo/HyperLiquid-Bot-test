# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T20:22:30.284683+00:00`
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

- `market_context_high->crypto_major_4h` score `1.9625` n `110` status `ready` deltaP `20.1968` edge `0.4574` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.8798` n `110` status `ready` deltaP `17.6996` edge `0.1238` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.5965` n `77` status `ready` deltaP `19.1282` edge `0.0853` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.5965` n `77` status `ready` deltaP `19.1282` edge `0.0853` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.5798` n `77` status `ready` deltaP `21.1059` edge `0.3099` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5798` n `77` status `ready` deltaP `21.1059` edge `0.3099` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.6496` n `110` status `ready` deltaP `7.5721` edge `0.1217` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2288` n `77` status `ready` deltaP `9.3055` edge `0.0057` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2288` n `77` status `ready` deltaP `9.3055` edge `0.0057` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.233` n `77` status `ready` deltaP `10.762` edge `0.028` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.233` n `77` status `ready` deltaP `10.762` edge `0.028` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.2996` n `110` status `ready` deltaP `1.9025` edge `0.0989` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.4799` n `77` status `ready` deltaP `-3.0966` edge `-0.0032` maxDD `-0.3479`
- `risk_on_and_context->fx_1h` score `-0.4799` n `77` status `ready` deltaP `-3.0966` edge `-0.0032` maxDD `-0.3479`
- `market_context_high->index_1h` score `-0.5083` n `110` status `ready` deltaP `4.6301` edge `0.0016` maxDD `-1.3195`
- `market_context_high->metal_4h` score `-0.5263` n `110` status `ready` deltaP `2.6136` edge `0.0488` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.5417` n `77` status `ready` deltaP `2.2475` edge `0.0318` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.5417` n `77` status `ready` deltaP `2.2475` edge `0.0318` maxDD `-4.6876`
- `risk_on_high->metal_1h` score `-0.7502` n `77` status `ready` deltaP `-3.9506` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.7502` n `77` status `ready` deltaP `-3.9506` edge `0.0033` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

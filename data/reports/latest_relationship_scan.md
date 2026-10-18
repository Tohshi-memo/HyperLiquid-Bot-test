# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T19:07:47.736850+00:00`
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

- `market_context_high->commodity_24h` score `1.9012` n `115` status `ready` deltaP `18.087` edge `0.123` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8349` n `115` status `ready` deltaP `20.3381` edge `0.4401` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.6798` n `82` status `ready` deltaP `19.7943` edge `0.0878` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.6798` n `82` status `ready` deltaP `19.7943` edge `0.0878` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `1.5009` n `82` status `ready` deltaP `21.4939` edge `0.2972` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `1.5009` n `82` status `ready` deltaP `21.4939` edge `0.2972` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.5209` n `115` status `ready` deltaP `6.5217` edge `0.1122` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.284` n `82` status `ready` deltaP `8.4267` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.284` n `82` status `ready` deltaP `8.4267` edge `0.0059` maxDD `-0.7394`
- `risk_on_high->equity_1h` score `-0.2282` n `82` status `ready` deltaP `12.0303` edge `0.0304` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2282` n `82` status `ready` deltaP `12.0303` edge `0.0304` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3561` n `115` status `ready` deltaP `2.0463` edge `0.0907` maxDD `-7.3329`
- `risk_on_high->fx_1h` score `-0.4092` n `82` status `ready` deltaP `-1.67` edge `-0.0033` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.4092` n `82` status `ready` deltaP `-1.67` edge `-0.0033` maxDD `-0.376`
- `risk_on_high->crypto_major_1h` score `-0.4516` n `82` status `ready` deltaP `1.2195` edge `0.0259` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.4516` n `82` status `ready` deltaP `1.2195` edge `0.0259` maxDD `-4.6876`
- `market_context_high->metal_1h` score `-0.5249` n `115` status `ready` deltaP `1.7183` edge `0.0082` maxDD `-0.9556`
- `market_context_high->index_1h` score `-0.542` n `115` status `ready` deltaP `4.1637` edge `0.0019` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.5913` n `82` status `ready` deltaP `-0.9858` edge `0.0039` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5913` n `82` status `ready` deltaP `-0.9858` edge `0.0039` maxDD `-0.8513`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

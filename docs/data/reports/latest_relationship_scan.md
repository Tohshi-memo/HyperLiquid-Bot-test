# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-20T03:37:13.595359+00:00`
- Price records: `672`
- Market context records: `1283`
- Flow alert records: `5604`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8820`

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

- `market_context_high->crypto_major_24h` score `17.7061` n `128` status `ready` deltaP `41.5798` edge `1.3115` maxDD `-8.0553`
- `market_context_high->metal_24h` score `11.3264` n `128` status `ready` deltaP `7.8125` edge `1.0585` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `8.9645` n `128` status `ready` deltaP `25.7812` edge `0.7768` maxDD `-15.1306`
- `market_context_high->index_24h` score `5.5139` n `128` status `ready` deltaP `28.8194` edge `0.376` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.8941` n `128` status `ready` deltaP `25.1736` edge `0.5641` maxDD `-14.2815`
- `market_context_high->unknown_4h` score `3.2767` n `141` status `ready` deltaP `3.5158` edge `0.416` maxDD `-8.3107`
- `market_context_high->equity_4h` score `2.5905` n `141` status `ready` deltaP `12.8103` edge `0.1968` maxDD `-3.6396`
- `market_context_high->unknown_24h` score `2.3514` n `128` status `ready` deltaP `1.5625` edge `0.4585` maxDD `-10.1706`
- `market_context_high->commodity_24h` score `1.5337` n `128` status `ready` deltaP `-13.3681` edge `0.3651` maxDD `-6.8535`
- `market_context_high->index_4h` score `0.5257` n `141` status `ready` deltaP `8.3096` edge `0.0983` maxDD `-2.5703`
- `market_context_high->metal_4h` score `0.3457` n `141` status `ready` deltaP `14.7314` edge `0.0737` maxDD `-6.4478`
- `market_context_high->equity_1h` score `0.3311` n `152` status `ready` deltaP `4.4714` edge `0.0405` maxDD `-1.7505`
- `market_context_high->fx_24h` score `0.2988` n `128` status `ready` deltaP `5.4688` edge `0.0349` maxDD `-0.3831`
- `market_context_high->index_1h` score `0.1472` n `152` status `ready` deltaP `6.7169` edge `0.0195` maxDD `-1.6329`
- `market_context_high->metal_1h` score `0.0646` n `152` status `ready` deltaP `10.0733` edge `0.0072` maxDD `-2.8509`
- `market_context_high->crypto_alt_1h` score `-0.3392` n `152` status `ready` deltaP `0.8943` edge `0.0376` maxDD `-3.6309`
- `market_context_high->fx_1h` score `-0.5449` n `152` status `ready` deltaP `0.5949` edge `-0.0038` maxDD `-0.3124`
- `market_context_high->crypto_major_1h` score `-0.7469` n `152` status `ready` deltaP `-0.1182` edge `0.0071` maxDD `-5.8323`
- `market_context_high->crypto_major_4h` score `-0.7475` n `141` status `ready` deltaP `4.6823` edge `0.1307` maxDD `-12.9533`
- `market_context_high->crypto_alt_4h` score `-0.8847` n `141` status `ready` deltaP `8.6003` edge `0.1612` maxDD `-19.5565`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

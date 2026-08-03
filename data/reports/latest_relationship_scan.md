# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-03T05:22:29.147808+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5935`

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

- `news_risk_high->unknown_24h` score `2199.2619` n `41` status `ready` deltaP `20.6258` edge `183.1764` maxDD `-2.0332`
- `market_context_high->crypto_alt_24h` score `13.4655` n `40` status `ready` deltaP `51.4583` edge `0.8188` maxDD `-2.1786`
- `market_context_high->commodity_24h` score `11.0634` n `40` status `ready` deltaP `51.3194` edge `0.5926` maxDD `-0.6889`
- `news_risk_high->equity_4h` score `1.1902` n `41` status `ready` deltaP `-1.372` edge `0.2381` maxDD `-3.4427`
- `news_risk_high->index_4h` score `0.6791` n `41` status `ready` deltaP `6.0976` edge `0.054` maxDD `-0.3783`
- `market_context_high->commodity_1h` score `0.3728` n `47` status `ready` deltaP `7.7143` edge `0.0338` maxDD `-1.3282`
- `market_context_high->commodity_4h` score `0.3232` n `47` status `ready` deltaP `5.0338` edge `0.0925` maxDD `-2.7703`
- `news_risk_high->commodity_1h` score `0.3083` n `41` status `ready` deltaP `13.3708` edge `-0.0122` maxDD `-1.3268`
- `news_risk_high->metal_1h` score `0.0873` n `41` status `ready` deltaP `4.6006` edge `0.0086` maxDD `-0.5599`
- `market_context_high->fx_4h` score `0.0584` n `47` status `ready` deltaP `14.1801` edge `-0.004` maxDD `-1.8531`
- `market_context_high->fx_1h` score `-0.0007` n `47` status `ready` deltaP `7.1155` edge `-0.0086` maxDD `-0.7804`
- `news_risk_high->metal_4h` score `-0.1397` n `41` status `ready` deltaP `2.7439` edge `-0.0011` maxDD `-0.8085`
- `news_risk_high->fx_1h` score `-0.1959` n `41` status `ready` deltaP `0.5769` edge `0.0033` maxDD `-0.2475`
- `market_context_high->crypto_alt_4h` score `-0.2071` n `47` status `ready` deltaP `2.2963` edge `0.0487` maxDD `-4.9116`
- `news_risk_high->crypto_alt_1h` score `-0.3279` n `41` status `ready` deltaP `5.0058` edge `-0.0072` maxDD `-3.1233`
- `news_risk_high->index_1h` score `-0.4446` n `41` status `ready` deltaP `-0.5769` edge `-0.0009` maxDD `-0.5845`
- `news_risk_high->fx_24h` score `-0.5088` n `41` status `ready` deltaP `5.1109` edge `0.0272` maxDD `-3.1205`
- `news_risk_high->equity_1h` score `-0.6685` n `41` status `ready` deltaP `-2.3733` edge `0.0424` maxDD `-2.916`
- `market_context_high->fx_24h` score `-0.6875` n `40` status `ready` deltaP `0.6597` edge `0.0363` maxDD `-2.506`
- `news_risk_high->fx_4h` score `-0.7034` n `41` status `ready` deltaP `-3.0488` edge `0.0259` maxDD `-0.6604`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

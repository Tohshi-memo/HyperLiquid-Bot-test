# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-12T03:22:27.668565+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9598`

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

- `market_context_high->unknown_24h` score `606.6726` n `53` status `ready` deltaP `-16.4373` edge `50.702` maxDD `-1.2425`
- `market_context_high->unknown_4h` score `35.0593` n `118` status `ready` deltaP `-7.2654` edge `3.0406` maxDD `-2.3109`
- `market_context_high->equity_24h` score `8.6425` n `53` status `ready` deltaP `26.3398` edge `0.5875` maxDD `-1.0977`
- `market_context_high->index_24h` score `5.9232` n `53` status `ready` deltaP `50.7174` edge `0.1598` maxDD `-0.012`
- `risk_on_high->crypto_major_4h` score `5.4019` n `39` status `ready` deltaP `31.039` edge `0.3285` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.4019` n `39` status `ready` deltaP `31.039` edge `0.3285` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `5.0701` n `39` status `ready` deltaP `24.7616` edge `0.3022` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.0701` n `39` status `ready` deltaP `24.7616` edge `0.3022` maxDD `-1.9151`
- `market_context_high->crypto_major_24h` score `4.494` n `53` status `ready` deltaP `-0.7828` edge `0.8962` maxDD `-17.8526`
- `risk_on_high->metal_4h` score `3.3239` n `39` status `ready` deltaP `30.3745` edge `0.0977` maxDD `-0.1896`
- `risk_on_and_context->metal_4h` score `3.3239` n `39` status `ready` deltaP `30.3745` edge `0.0977` maxDD `-0.1896`
- `risk_on_high->crypto_alt_1h` score `1.5456` n `51` status `ready` deltaP `10.664` edge `0.1174` maxDD `-2.4421`
- `risk_on_and_context->crypto_alt_1h` score `1.5456` n `51` status `ready` deltaP `10.664` edge `0.1174` maxDD `-2.4421`
- `risk_on_high->crypto_major_1h` score `1.3294` n `51` status `ready` deltaP `12.1463` edge `0.0951` maxDD `-3.2233`
- `risk_on_and_context->crypto_major_1h` score `1.3294` n `51` status `ready` deltaP `12.1463` edge `0.0951` maxDD `-3.2233`
- `risk_on_high->metal_1h` score `1.3008` n `51` status `ready` deltaP `16.382` edge `0.0231` maxDD `-0.2466`
- `risk_on_and_context->metal_1h` score `1.3008` n `51` status `ready` deltaP `16.382` edge `0.0231` maxDD `-0.2466`
- `market_context_high->metal_4h` score `0.4373` n `118` status `ready` deltaP `11.8825` edge `0.0295` maxDD `-1.1153`
- `market_context_high->crypto_alt_1h` score `0.3156` n `130` status `ready` deltaP `5.9581` edge `0.09` maxDD `-4.9401`
- `market_context_high->crypto_major_4h` score `0.3052` n `118` status `ready` deltaP `6.6583` edge `0.2053` maxDD `-11.1784`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

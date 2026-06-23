# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-23T15:52:35.033070+00:00`
- Price records: `672`
- Market context records: `4531`
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

- `risk_on_high->unknown_4h` score `197.5989` n `33` status `ready` deltaP `20.995` edge `16.4457` maxDD `-7.5275`
- `risk_on_and_context->unknown_4h` score `197.5989` n `33` status `ready` deltaP `20.995` edge `16.4457` maxDD `-7.5275`
- `market_context_high->unknown_1h` score `52.2406` n `180` status `ready` deltaP `6.8297` edge `4.3579` maxDD `-2.3371`
- `market_context_high->unknown_4h` score `30.0706` n `180` status `ready` deltaP `8.6212` edge `2.605` maxDD `-7.5275`
- `risk_on_high->metal_24h` score `7.1212` n `33` status `ready` deltaP `-0.7261` edge `0.6962` maxDD `-4.834`
- `risk_on_and_context->metal_24h` score `7.1212` n `33` status `ready` deltaP `-0.7261` edge `0.6962` maxDD `-4.834`
- `risk_on_high->crypto_major_4h` score `6.98` n `33` status `ready` deltaP `36.8117` edge `0.3456` maxDD `-0.0812`
- `risk_on_and_context->crypto_major_4h` score `6.98` n `33` status `ready` deltaP `36.8117` edge `0.3456` maxDD `-0.0812`
- `risk_on_high->unknown_24h` score `5.1379` n `33` status `ready` deltaP `18.9236` edge `0.302` maxDD `0.0`
- `risk_on_and_context->unknown_24h` score `5.1379` n `33` status `ready` deltaP `18.9236` edge `0.302` maxDD `0.0`
- `risk_on_high->equity_4h` score `5.0676` n `33` status `ready` deltaP `42.2256` edge `0.1408` maxDD `0.0`
- `risk_on_and_context->equity_4h` score `5.0676` n `33` status `ready` deltaP `42.2256` edge `0.1408` maxDD `0.0`
- `risk_on_high->crypto_major_24h` score `4.0789` n `33` status `ready` deltaP `0.9944` edge `0.4476` maxDD `-5.4789`
- `risk_on_and_context->crypto_major_24h` score `4.0789` n `33` status `ready` deltaP `0.9944` edge `0.4476` maxDD `-5.4789`
- `risk_on_high->crypto_major_1h` score `2.171` n `33` status `ready` deltaP `11.5406` edge `0.1257` maxDD `-0.7379`
- `risk_on_and_context->crypto_major_1h` score `2.171` n `33` status `ready` deltaP `11.5406` edge `0.1257` maxDD `-0.7379`
- `risk_on_high->crypto_alt_4h` score `2.1348` n `33` status `ready` deltaP `11.6547` edge `0.1568` maxDD `-1.8615`
- `risk_on_and_context->crypto_alt_4h` score `2.1348` n `33` status `ready` deltaP `11.6547` edge `0.1568` maxDD `-1.8615`
- `risk_on_high->equity_1h` score `2.0463` n `33` status `ready` deltaP `20.9672` edge `0.0504` maxDD `-0.2389`
- `risk_on_and_context->equity_1h` score `2.0463` n `33` status `ready` deltaP `20.9672` edge `0.0504` maxDD `-0.2389`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

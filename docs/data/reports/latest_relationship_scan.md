# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-14T01:07:27.901159+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9807`

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

- `market_context_high->crypto_alt_4h` score `7.0424` n `117` status `ready` deltaP `17.1526` edge `0.6174` maxDD `-9.2574`
- `market_context_high->crypto_major_4h` score `6.3772` n `117` status `ready` deltaP `21.8008` edge `0.542` maxDD `-7.4722`
- `risk_on_high->commodity_24h` score `6.3484` n `52` status `ready` deltaP `32.0` edge `0.3157` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `6.3484` n `52` status `ready` deltaP `32.0` edge `0.3157` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `5.6313` n `54` status `ready` deltaP `19.4318` edge `0.3845` maxDD `-1.9151`
- `risk_on_and_context->crypto_alt_4h` score `5.6313` n `54` status `ready` deltaP `19.4318` edge `0.3845` maxDD `-1.9151`
- `risk_on_high->crypto_major_4h` score `4.685` n `54` status `ready` deltaP `34.9062` edge `0.4532` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.685` n `54` status `ready` deltaP `34.9062` edge `0.4532` maxDD `-4.1548`
- `market_context_high->unknown_4h` score `4.2717` n `117` status `ready` deltaP `-3.7934` edge `0.4459` maxDD `-1.8373`
- `market_context_high->crypto_alt_1h` score `1.9654` n `117` status `ready` deltaP `14.4647` edge `0.1741` maxDD `-5.8734`
- `market_context_high->crypto_major_1h` score `1.4492` n `117` status `ready` deltaP `7.3085` edge `0.1526` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3588` n `117` status `ready` deltaP `14.6002` edge `0.0371` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2144` n `54` status `ready` deltaP `2.7501` edge `0.0264` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2144` n `54` status `ready` deltaP `2.7501` edge `0.0264` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3047` n `117` status `ready` deltaP `1.5477` edge `0.0023` maxDD `-0.3742`
- `market_context_high->metal_1h` score `-0.3087` n `117` status `ready` deltaP `8.0135` edge `0.0078` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.415` n `54` status `ready` deltaP `2.6004` edge `0.0026` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.415` n `54` status `ready` deltaP `2.6004` edge `0.0026` maxDD `-0.8513`
- `risk_on_high->crypto_alt_1h` score `-0.4557` n `54` status `ready` deltaP `4.2083` edge `0.0161` maxDD `-5.8734`
- `risk_on_and_context->crypto_alt_1h` score `-0.4557` n `54` status `ready` deltaP `4.2083` edge `0.0161` maxDD `-5.8734`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T06:37:26.080489+00:00`
- Price records: `672`
- Market context records: `7538`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14490`

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

- `risk_on_high->crypto_major_4h` score `7.79` n `36` status `ready` deltaP `41.2094` edge `0.3937` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.79` n `36` status `ready` deltaP `41.2094` edge `0.3937` maxDD `-0.8742`
- `risk_on_high->crypto_alt_4h` score `5.2057` n `36` status `ready` deltaP `31.1654` edge `0.2504` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.2057` n `36` status `ready` deltaP `31.1654` edge `0.2504` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.6171` n `36` status `ready` deltaP `15.6504` edge `0.3234` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.6171` n `36` status `ready` deltaP `15.6504` edge `0.3234` maxDD `-0.4384`
- `risk_on_high->crypto_major_24h` score `3.7342` n `36` status `ready` deltaP `9.7222` edge `0.3485` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `3.7342` n `36` status `ready` deltaP `9.7222` edge `0.3485` maxDD `-5.8371`
- `risk_on_high->crypto_major_1h` score `1.7402` n `36` status `ready` deltaP `24.8503` edge `0.0819` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.7402` n `36` status `ready` deltaP `24.8503` edge `0.0819` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.9067` n `35` status `ready` deltaP `21.2195` edge `0.0204` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.9067` n `35` status `ready` deltaP `21.2195` edge `0.0204` maxDD `-1.3162`
- `risk_on_high->crypto_alt_24h` score `0.8601` n `36` status `ready` deltaP `10.5903` edge `0.1325` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `0.8601` n `36` status `ready` deltaP `10.5903` edge `0.1325` maxDD `-5.0938`
- `risk_on_high->equity_1h` score `0.6385` n `36` status `ready` deltaP `9.91` edge `0.0535` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.6385` n `36` status `ready` deltaP `9.91` edge `0.0535` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.4577` n `36` status `ready` deltaP `5.7807` edge `0.0277` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.4577` n `36` status `ready` deltaP `5.7807` edge `0.0277` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.3529` n `36` status `ready` deltaP `3.5263` edge `0.0588` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.3529` n `36` status `ready` deltaP `3.5263` edge `0.0588` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

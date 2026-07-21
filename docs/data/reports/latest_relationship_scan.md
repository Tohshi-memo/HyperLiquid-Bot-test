# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T07:24:27.719461+00:00`
- Price records: `672`
- Market context records: `7435`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14659`

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

- `risk_on_high->crypto_major_4h` score `6.121` n `32` status `ready` deltaP `35.5261` edge `0.2925` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `6.121` n `32` status `ready` deltaP `35.5261` edge `0.2925` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `5.7899` n `32` status `ready` deltaP `16.7732` edge `0.4728` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `5.7899` n `32` status `ready` deltaP `16.7732` edge `0.4728` maxDD `-5.8371`
- `risk_on_high->unknown_4h` score `4.9127` n `32` status `ready` deltaP `15.6107` edge `0.3483` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.9127` n `32` status `ready` deltaP `15.6107` edge `0.3483` maxDD `-0.4384`
- `risk_on_high->crypto_alt_4h` score `4.6121` n `32` status `ready` deltaP `27.1357` edge `0.2278` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `4.6121` n `32` status `ready` deltaP `27.1357` edge `0.2278` maxDD `-0.9492`
- `risk_on_high->crypto_alt_24h` score `2.5959` n `32` status `ready` deltaP `17.0927` edge `0.3117` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.5959` n `32` status `ready` deltaP `17.0927` edge `0.3117` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.3451` n `36` status `ready` deltaP `21.5569` edge `0.0532` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.3451` n `36` status `ready` deltaP `21.5569` edge `0.0532` maxDD `-0.957`
- `risk_on_high->equity_24h` score `1.0665` n `31` status `ready` deltaP `13.0996` edge `0.2729` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `1.0665` n `31` status `ready` deltaP `13.0996` edge `0.2729` maxDD `-19.375`
- `risk_on_high->commodity_1h` score `0.6426` n `36` status `ready` deltaP `7.5825` edge `0.0311` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.6426` n `36` status `ready` deltaP `7.5825` edge `0.0311` maxDD `-0.2479`
- `risk_on_high->equity_1h` score `0.509` n `36` status `ready` deltaP `8.5586` edge `0.0459` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.509` n `36` status `ready` deltaP `8.5586` edge `0.0459` maxDD `-1.3497`
- `risk_on_high->fx_24h` score `0.1661` n `31` status `ready` deltaP `11.2819` edge `-0.0083` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.1661` n `31` status `ready` deltaP `11.2819` edge `-0.0083` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

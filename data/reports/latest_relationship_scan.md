# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T14:52:32.685046+00:00`
- Price records: `672`
- Market context records: `7467`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14727`

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

- `risk_on_high->crypto_major_4h` score `7.0391` n `36` status `ready` deltaP `37.7033` edge `0.3545` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.0391` n `36` status `ready` deltaP `37.7033` edge `0.3545` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.1259` n `32` status `ready` deltaP `16.7732` edge `0.5008` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.1259` n `32` status `ready` deltaP `16.7732` edge `0.5008` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0235` n `36` status `ready` deltaP `30.4032` edge `0.2403` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0235` n `36` status `ready` deltaP `30.4032` edge `0.2403` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.7368` n `36` status `ready` deltaP `16.4126` edge `0.3283` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.7368` n `36` status `ready` deltaP `16.4126` edge `0.3283` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.3502` n `32` status `ready` deltaP `17.0927` edge `0.2802` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.3502` n `32` status `ready` deltaP `17.0927` edge `0.2802` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.4636` n `36` status `ready` deltaP `22.006` edge `0.0654` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.4636` n `36` status `ready` deltaP `22.006` edge `0.0654` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.7869` n `31` status `ready` deltaP `13.0996` edge `0.2496` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.7869` n `31` status `ready` deltaP `13.0996` edge `0.2496` maxDD `-19.375`
- `risk_on_high->metal_4h` score `0.5998` n `36` status `ready` deltaP `6.8598` edge `0.0866` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.5998` n `36` status `ready` deltaP `6.8598` edge `0.0866` maxDD `-0.5882`
- `risk_on_high->commodity_1h` score `0.5141` n `36` status `ready` deltaP `6.3813` edge `0.0284` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5141` n `36` status `ready` deltaP `6.3813` edge `0.0284` maxDD `-0.2479`
- `risk_on_high->fx_24h` score `0.4834` n `31` status `ready` deltaP `16.4993` edge `-0.0024` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.4834` n `31` status `ready` deltaP `16.4993` edge `-0.0024` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

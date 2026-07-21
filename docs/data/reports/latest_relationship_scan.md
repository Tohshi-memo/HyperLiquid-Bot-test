# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-21T15:07:33.361712+00:00`
- Price records: `672`
- Market context records: `7468`
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

- `risk_on_high->crypto_major_4h` score `7.0475` n `36` status `ready` deltaP `37.7033` edge `0.3552` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.0475` n `36` status `ready` deltaP `37.7033` edge `0.3552` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.1259` n `32` status `ready` deltaP `16.7732` edge `0.5008` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.1259` n `32` status `ready` deltaP `16.7732` edge `0.5008` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0393` n `36` status `ready` deltaP `30.5556` edge `0.2406` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0393` n `36` status `ready` deltaP `30.5556` edge `0.2406` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.7162` n `36` status `ready` deltaP `16.2601` edge `0.3276` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.7162` n `36` status `ready` deltaP `16.2601` edge `0.3276` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.3393` n `32` status `ready` deltaP `17.0927` edge `0.2788` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.3393` n `32` status `ready` deltaP `17.0927` edge `0.2788` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.4776` n `36` status `ready` deltaP `22.1557` edge `0.0662` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.4776` n `36` status `ready` deltaP `22.1557` edge `0.0662` maxDD `-0.957`
- `risk_on_high->equity_24h` score `0.7257` n `31` status `ready` deltaP `13.0996` edge `0.2445` maxDD `-19.375`
- `risk_on_and_context->equity_24h` score `0.7257` n `31` status `ready` deltaP `13.0996` edge `0.2445` maxDD `-19.375`
- `risk_on_high->metal_4h` score `0.5852` n `36` status `ready` deltaP `6.7073` edge `0.0864` maxDD `-0.5882`
- `risk_on_and_context->metal_4h` score `0.5852` n `36` status `ready` deltaP `6.7073` edge `0.0864` maxDD `-0.5882`
- `risk_on_high->commodity_1h` score `0.4973` n `36` status `ready` deltaP `6.2312` edge `0.028` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.4973` n `36` status `ready` deltaP `6.2312` edge `0.028` maxDD `-0.2479`
- `risk_on_high->fx_24h` score `0.4842` n `31` status `ready` deltaP `16.4993` edge `-0.0023` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.4842` n `31` status `ready` deltaP `16.4993` edge `-0.0023` maxDD `-1.3162`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-22T03:52:26.838905+00:00`
- Price records: `672`
- Market context records: `7526`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `14782`

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

- `risk_on_high->crypto_major_4h` score `7.5562` n `36` status `ready` deltaP `40.4472` edge `0.3793` maxDD `-0.8742`
- `risk_on_and_context->crypto_major_4h` score `7.5562` n `36` status `ready` deltaP `40.4472` edge `0.3793` maxDD `-0.8742`
- `risk_on_high->crypto_major_24h` score `6.3829` n `32` status `ready` deltaP `17.4664` edge `0.5176` maxDD `-5.8371`
- `risk_on_and_context->crypto_major_24h` score `6.3829` n `32` status `ready` deltaP `17.4664` edge `0.5176` maxDD `-5.8371`
- `risk_on_high->crypto_alt_4h` score `5.0561` n `36` status `ready` deltaP `30.5556` edge `0.242` maxDD `-0.9492`
- `risk_on_and_context->crypto_alt_4h` score `5.0561` n `36` status `ready` deltaP `30.5556` edge `0.242` maxDD `-0.9492`
- `risk_on_high->unknown_4h` score `4.4927` n `36` status `ready` deltaP `15.0406` edge `0.3171` maxDD `-0.4384`
- `risk_on_and_context->unknown_4h` score `4.4927` n `36` status `ready` deltaP `15.0406` edge `0.3171` maxDD `-0.4384`
- `risk_on_high->crypto_alt_24h` score `2.0119` n `32` status `ready` deltaP `16.2262` edge `0.2426` maxDD `-5.0938`
- `risk_on_and_context->crypto_alt_24h` score `2.0119` n `32` status `ready` deltaP `16.2262` edge `0.2426` maxDD `-5.0938`
- `risk_on_high->crypto_major_1h` score `1.6459` n `36` status `ready` deltaP `24.2515` edge `0.0738` maxDD `-0.957`
- `risk_on_and_context->crypto_major_1h` score `1.6459` n `36` status `ready` deltaP `24.2515` edge `0.0738` maxDD `-0.957`
- `risk_on_high->fx_24h` score `0.5719` n `31` status `ready` deltaP `16.3254` edge `0.0101` maxDD `-1.3162`
- `risk_on_and_context->fx_24h` score `0.5719` n `31` status `ready` deltaP `16.3254` edge `0.0101` maxDD `-1.3162`
- `risk_on_high->equity_1h` score `0.5496` n `36` status `ready` deltaP `9.1592` edge `0.0471` maxDD `-1.3497`
- `risk_on_and_context->equity_1h` score `0.5496` n `36` status `ready` deltaP `9.1592` edge `0.0471` maxDD `-1.3497`
- `risk_on_high->commodity_1h` score `0.5297` n `36` status `ready` deltaP `6.5315` edge `0.0287` maxDD `-0.2479`
- `risk_on_and_context->commodity_1h` score `0.5297` n `36` status `ready` deltaP `6.5315` edge `0.0287` maxDD `-0.2479`
- `risk_on_high->crypto_alt_1h` score `0.289` n `36` status `ready` deltaP `3.0772` edge `0.0536` maxDD `-0.9651`
- `risk_on_and_context->crypto_alt_1h` score `0.289` n `36` status `ready` deltaP `3.0772` edge `0.0536` maxDD `-0.9651`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-15T06:37:30.815154+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9709`

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

- `market_context_high->crypto_alt_4h` score `8.0772` n `118` status `ready` deltaP `19.9669` edge `0.6844` maxDD `-9.2196`
- `risk_on_high->commodity_24h` score `7.8876` n `54` status `ready` deltaP `41.115` edge `0.3832` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.8876` n `54` status `ready` deltaP `41.115` edge `0.3832` maxDD `0.0`
- `risk_on_high->crypto_alt_4h` score `6.8135` n `54` status `ready` deltaP `22.8546` edge `0.4601` maxDD `-1.907`
- `risk_on_and_context->crypto_alt_4h` score `6.8135` n `54` status `ready` deltaP `22.8546` edge `0.4601` maxDD `-1.907`
- `market_context_high->crypto_major_4h` score `6.5662` n `118` status `ready` deltaP `21.9125` edge `0.557` maxDD `-7.4722`
- `risk_on_high->crypto_major_4h` score `4.8762` n `54` status `ready` deltaP `35.5974` edge `0.4731` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `4.8762` n `54` status `ready` deltaP `35.5974` edge `0.4731` maxDD `-4.1548`
- `market_context_high->crypto_alt_1h` score `1.7649` n `121` status `ready` deltaP `13.0376` edge `0.1666` maxDD `-5.8485`
- `market_context_high->crypto_major_1h` score `1.0819` n `121` status `ready` deltaP `4.9228` edge `0.1379` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.3097` n `118` status `ready` deltaP `13.2364` edge `0.0421` maxDD `-1.6961`
- `risk_on_high->crypto_major_1h` score `-0.2829` n `54` status `ready` deltaP `1.4028` edge `0.0266` maxDD `-3.7781`
- `risk_on_and_context->crypto_major_1h` score `-0.2829` n `54` status `ready` deltaP `1.4028` edge `0.0266` maxDD `-3.7781`
- `market_context_high->fx_1h` score `-0.3163` n `121` status `ready` deltaP `-0.2606` edge `-0.0008` maxDD `-0.3742`
- `risk_on_high->crypto_alt_1h` score `-0.3255` n `54` status `ready` deltaP `4.9568` edge `0.0275` maxDD `-5.8485`
- `risk_on_and_context->crypto_alt_1h` score `-0.3255` n `54` status `ready` deltaP `4.9568` edge `0.0275` maxDD `-5.8485`
- `market_context_high->metal_1h` score `-0.3866` n `121` status `ready` deltaP `7.1745` edge `0.0069` maxDD `-0.9556`
- `risk_on_high->metal_1h` score `-0.4407` n `54` status `ready` deltaP `2.0016` edge `0.0033` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4407` n `54` status `ready` deltaP `2.0016` edge `0.0033` maxDD `-0.8513`
- `market_context_high->commodity_24h` score `-0.4629` n `116` status `ready` deltaP `12.6667` edge `0.1447` maxDD `-12.0788`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

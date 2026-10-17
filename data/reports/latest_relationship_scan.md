# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T11:22:28.394247+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9348`

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

- `risk_on_high->commodity_24h` score `7.0281` n `54` status `ready` deltaP `38.5017` edge `0.329` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0281` n `54` status `ready` deltaP `38.5017` edge `0.329` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.6141` n `145` status `ready` deltaP `21.6296` edge `0.4558` maxDD `-5.906`
- `market_context_high->crypto_alt_4h` score `5.5171` n `145` status `ready` deltaP `13.6007` edge `0.5296` maxDD `-7.1743`
- `risk_on_high->crypto_major_4h` score `5.3832` n `71` status `ready` deltaP `29.41` edge `0.3378` maxDD `-4.1548`
- `risk_on_and_context->crypto_major_4h` score `5.3832` n `71` status `ready` deltaP `29.41` edge `0.3378` maxDD `-4.1548`
- `risk_on_high->crypto_alt_4h` score `1.5051` n `71` status `ready` deltaP `6.4904` edge `0.2418` maxDD `-7.1051`
- `risk_on_and_context->crypto_alt_4h` score `1.5051` n `71` status `ready` deltaP `6.4904` edge `0.2418` maxDD `-7.1051`
- `market_context_high->crypto_major_1h` score `0.8373` n `157` status `ready` deltaP `6.6498` edge `0.106` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.5494` n `157` status `ready` deltaP `8.0733` edge `0.1234` maxDD `-5.8485`
- `market_context_high->metal_4h` score `0.3907` n `145` status `ready` deltaP `13.2885` edge `0.0485` maxDD `-1.6961`
- `risk_on_high->index_1h` score `0.2037` n `83` status `ready` deltaP `7.3628` edge `0.0063` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.2037` n `83` status `ready` deltaP `7.3628` edge `0.0063` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1398` n `157` status `ready` deltaP `7.7849` edge `0.005` maxDD `-1.3195`
- `risk_on_high->equity_1h` score `-0.2067` n `83` status `ready` deltaP `12.4788` edge `0.0292` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2067` n `83` status `ready` deltaP `12.4788` edge `0.0292` maxDD `-5.3696`
- `market_context_high->metal_1h` score `-0.3053` n `157` status `ready` deltaP `7.9208` edge `0.0087` maxDD `-0.9556`
- `market_context_high->equity_1h` score `-0.3281` n `157` status `ready` deltaP `10.5603` edge `0.0385` maxDD `-7.0778`
- `risk_on_high->fx_1h` score `-0.3793` n `83` status `ready` deltaP `-1.0493` edge `-0.0036` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.3793` n `83` status `ready` deltaP `-1.0493` edge `-0.0036` maxDD `-0.376`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

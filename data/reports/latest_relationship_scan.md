# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T16:07:26.636913+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9294`

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

- `market_context_high->commodity_24h` score `2.1246` n `126` status `ready` deltaP `19.4093` edge `0.1328` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9838` n `90` status `ready` deltaP `21.314` edge `0.103` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9838` n `90` status `ready` deltaP `21.314` edge `0.103` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.9406` n `127` status `ready` deltaP `14.975` edge `0.3612` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.7107` n `91` status `ready` deltaP `16.048` edge `0.2322` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.7107` n `91` status `ready` deltaP `16.048` edge `0.2322` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4713` n `127` status `ready` deltaP `4.7798` edge `0.0963` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.1257` n `91` status `ready` deltaP `6.3574` edge `0.0065` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.1257` n `91` status `ready` deltaP `6.3574` edge `0.0065` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2562` n `91` status `ready` deltaP `1.1979` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.2602` n `91` status `ready` deltaP `11.06` edge `0.0342` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2602` n `91` status `ready` deltaP `11.06` edge `0.0342` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.3853` n `127` status `ready` deltaP `3.3636` edge `0.003` maxDD `-1.3195`
- `market_context_high->crypto_alt_1h` score `-0.3859` n `127` status `ready` deltaP `2.5225` edge `0.0837` maxDD `-7.3329`
- `risk_on_high->metal_1h` score `-0.4595` n `91` status `ready` deltaP `1.4443` edge `0.0046` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4595` n `91` status `ready` deltaP `1.4443` edge `0.0046` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5078` n `127` status `ready` deltaP `-1.6316` edge `-0.0021` maxDD `-0.503`
- `risk_on_high->crypto_major_1h` score `-0.5959` n `91` status `ready` deltaP `-0.1004` edge `0.0162` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.5959` n `91` status `ready` deltaP `-0.1004` edge `0.0162` maxDD `-4.6876`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

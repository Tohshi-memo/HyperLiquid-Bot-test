# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T15:37:26.798786+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9222`

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

- `market_context_high->commodity_24h` score `2.133` n `128` status `ready` deltaP `19.3342` edge `0.134` maxDD `-1.8119`
- `risk_on_high->commodity_24h` score `1.9332` n `90` status `ready` deltaP `20.9661` edge `0.1011` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.9332` n `90` status `ready` deltaP `20.9661` edge `0.1011` maxDD `-1.7154`
- `market_context_high->crypto_major_4h` score `0.9271` n `129` status `ready` deltaP `15.3171` edge `0.3572` maxDD `-15.2359`
- `risk_on_high->crypto_major_4h` score `0.6481` n `91` status `ready` deltaP `15.7431` edge `0.2262` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.6481` n `91` status `ready` deltaP `15.7431` edge `0.2262` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.6012` n `129` status `ready` deltaP `5.1885` edge `0.1044` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.0993` n `91` status `ready` deltaP `6.0571` edge `0.0063` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0993` n `91` status `ready` deltaP `6.0571` edge `0.0063` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_high->equity_1h` score `-0.2939` n `91` status `ready` deltaP `10.7597` edge `0.0334` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.2939` n `91` status `ready` deltaP `10.7597` edge `0.0334` maxDD `-5.3696`
- `market_context_high->crypto_alt_1h` score `-0.3066` n `129` status `ready` deltaP `3.0288` edge `0.0905` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.3547` n `129` status `ready` deltaP `3.8934` edge `0.0034` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.4759` n `91` status `ready` deltaP `1.1449` edge `0.0045` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.4759` n `91` status `ready` deltaP `1.1449` edge `0.0045` maxDD `-0.8513`
- `risk_on_high->crypto_major_1h` score `-0.6341` n `91` status `ready` deltaP `-0.3998` edge `0.0133` maxDD `-4.6876`
- `risk_on_and_context->crypto_major_1h` score `-0.6341` n `91` status `ready` deltaP `-0.3998` edge `0.0133` maxDD `-4.6876`
- `market_context_high->metal_1h` score `-0.6574` n `129` status `ready` deltaP `3.5046` edge `0.0088` maxDD `-0.9556`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

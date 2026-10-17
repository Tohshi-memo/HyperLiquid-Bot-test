# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-17T13:22:31.390241+00:00`
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

- `risk_on_high->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.0209` n `54` status `ready` deltaP `38.5017` edge `0.3284` maxDD `0.0`
- `market_context_high->crypto_major_4h` score `5.0168` n `153` status `ready` deltaP `19.2791` edge `0.4217` maxDD `-5.906`
- `risk_on_high->crypto_major_4h` score `3.6627` n `79` status `ready` deltaP `22.9276` edge `0.2718` maxDD `-4.8875`
- `risk_on_and_context->crypto_major_4h` score `3.6627` n `79` status `ready` deltaP `22.9276` edge `0.2718` maxDD `-4.8875`
- `market_context_high->crypto_alt_4h` score `3.4275` n `153` status `ready` deltaP `11.5027` edge `0.4856` maxDD `-13.7997`
- `market_context_high->crypto_major_1h` score `0.4749` n `165` status `ready` deltaP `4.8303` edge `0.0921` maxDD `-3.7781`
- `market_context_high->metal_4h` score `0.2529` n `153` status `ready` deltaP `11.8514` edge `0.0466` maxDD `-1.6961`
- `market_context_high->crypto_alt_1h` score `0.0281` n `165` status `ready` deltaP `6.3419` edge `0.1018` maxDD `-6.6726`
- `risk_on_high->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `0.0231` n `90` status `ready` deltaP `5.2553` edge `0.0053` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.228` n `165` status `ready` deltaP `6.1644` edge `0.0045` maxDD `-1.3195`
- `market_context_high->metal_1h` score `-0.2533` n `165` status `ready` deltaP `6.9261` edge `0.0083` maxDD `-0.9556`
- `risk_on_high->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2912` n `90` status `ready` deltaP `0.5705` edge `-0.0031` maxDD `-0.376`
- `market_context_high->equity_4h` score `-0.4056` n `153` status `ready` deltaP `13.3807` edge `0.2014` maxDD `-17.4086`
- `market_context_high->equity_1h` score `-0.417` n `165` status `ready` deltaP `9.1674` edge `0.0364` maxDD `-7.0778`
- `market_context_high->fx_1h` score `-0.4261` n `165` status `ready` deltaP `-0.1365` edge `-0.0016` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.4975` n `90` status `ready` deltaP `9.3694` edge `0.0257` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4975` n `90` status `ready` deltaP `9.3694` edge `0.0257` maxDD `-5.3696`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

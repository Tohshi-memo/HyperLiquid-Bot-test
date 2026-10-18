# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T04:52:26.955872+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10534`

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

- `risk_on_high->commodity_24h` score `4.7207` n `61` status `ready` deltaP `27.8974` edge `0.2468` maxDD `-0.8178`
- `risk_on_and_context->commodity_24h` score `4.7207` n `61` status `ready` deltaP `27.8974` edge `0.2468` maxDD `-0.8178`
- `market_context_high->commodity_24h` score `1.7992` n `116` status `ready` deltaP `15.2349` edge `0.1609` maxDD `-4.3362`
- `market_context_high->crypto_major_4h` score `1.5214` n `157` status `ready` deltaP `15.1099` edge `0.3665` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.473` n `157` status `ready` deltaP `4.0667` edge `0.1012` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.2324` n `157` status `ready` deltaP `7.6595` edge `0.1183` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1507` n `91` status `ready` deltaP `13.3041` edge `0.1787` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1507` n `91` status `ready` deltaP `13.3041` edge `0.1787` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0509` n `91` status `ready` deltaP `4.2553` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0509` n `91` status `ready` deltaP `4.2553` edge `0.0058` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1797` n `157` status `ready` deltaP `7.0341` edge `0.0049` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.4192` n `157` status `ready` deltaP `6.4972` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.438` n `91` status `ready` deltaP `9.4084` edge `0.0304` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.438` n `91` status `ready` deltaP `9.4084` edge `0.0304` maxDD `-5.3696`
- `market_context_high->fx_1h` score `-0.519` n `157` status `ready` deltaP `-1.8927` edge `-0.0018` maxDD `-0.503`
- `risk_on_high->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.5277` n `157` status `ready` deltaP `7.0093` edge `0.043` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

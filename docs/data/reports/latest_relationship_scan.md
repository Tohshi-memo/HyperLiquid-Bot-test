# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T03:52:30.971638+00:00`
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

- `risk_on_high->commodity_24h` score `6.0141` n `57` status `ready` deltaP `34.1096` edge `0.2902` maxDD `-0.3135`
- `risk_on_and_context->commodity_24h` score `6.0141` n `57` status `ready` deltaP `34.1096` edge `0.2902` maxDD `-0.3135`
- `market_context_high->crypto_major_4h` score `1.5383` n `161` status `ready` deltaP `15.6066` edge `0.3646` maxDD `-15.2359`
- `market_context_high->commodity_24h` score `1.2088` n `116` status `ready` deltaP `15.2349` edge `0.1516` maxDD `-6.1943`
- `market_context_high->crypto_major_1h` score `0.5216` n `161` status `ready` deltaP `4.4036` edge `0.103` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.3811` n `161` status `ready` deltaP `8.4678` edge `0.1253` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1813` n `91` status `ready` deltaP `13.4566` edge `0.1816` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1813` n `91` status `ready` deltaP `13.4566` edge `0.1816` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0377` n `91` status `ready` deltaP `4.4055` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0377` n `91` status `ready` deltaP `4.4055` edge `0.0059` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1401` n `161` status `ready` deltaP `7.75` edge `0.0052` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2484` n `91` status `ready` deltaP `1.3481` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.319` n `161` status `ready` deltaP `5.617` edge `0.0086` maxDD `-0.9556`
- `market_context_high->metal_4h` score `-0.4365` n `161` status `ready` deltaP `8.1645` edge `0.0429` maxDD `-1.6961`
- `risk_on_high->equity_1h` score `-0.4368` n `91` status `ready` deltaP `9.4084` edge `0.0305` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4368` n `91` status `ready` deltaP `9.4084` edge `0.0305` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5016` n `91` status `ready` deltaP `0.6958` edge `0.0042` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5162` n `161` status `ready` deltaP `-1.8531` edge `-0.0017` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T12:22:27.388849+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9246`

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

- `market_context_high->commodity_24h` score `2.3651` n `128` status `ready` deltaP `19.6565` edge `0.1512` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.8767` n `139` status `ready` deltaP `16.5961` edge `0.3862` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.8173` n `90` status `ready` deltaP `20.5071` edge `0.0945` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.8173` n `90` status `ready` deltaP `20.5071` edge `0.0945` maxDD `-1.7154`
- `market_context_high->crypto_major_1h` score `0.7367` n `139` status `ready` deltaP `5.4872` edge `0.1137` maxDD `-3.7781`
- `risk_on_high->crypto_major_4h` score `0.2364` n `91` status `ready` deltaP `14.0663` edge `0.1846` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.2364` n `91` status `ready` deltaP `14.0663` edge `0.1846` maxDD `-11.1788`
- `market_context_high->crypto_alt_1h` score `0.027` n `139` status `ready` deltaP `5.512` edge `0.1155` maxDD `-7.3329`
- `risk_on_high->index_1h` score `-0.0172` n `91` status `ready` deltaP `4.7058` edge `0.0056` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0172` n `91` status `ready` deltaP `4.7058` edge `0.0056` maxDD `-0.7394`
- `risk_on_high->fx_1h` score `-0.2398` n `91` status `ready` deltaP `1.4982` edge `-0.0027` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2398` n `91` status `ready` deltaP `1.4982` edge `-0.0027` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3915` n `139` status `ready` deltaP `4.2228` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4247` n `91` status `ready` deltaP `9.7087` edge `0.0295` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4247` n `91` status `ready` deltaP `9.7087` edge `0.0295` maxDD `-5.3696`
- `market_context_high->index_1h` score `-0.4619` n `139` status `ready` deltaP `4.8956` edge `0.0037` maxDD `-1.3195`
- `risk_on_high->metal_1h` score `-0.5179` n `91` status `ready` deltaP `0.3964` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5179` n `91` status `ready` deltaP `0.3964` edge `0.0041` maxDD `-0.8513`
- `market_context_high->metal_4h` score `-0.6144` n `139` status `ready` deltaP `5.6096` edge `0.0451` maxDD `-1.6961`
- `market_context_high->fx_1h` score `-0.6866` n `139` status `ready` deltaP `-0.5099` edge `-0.0017` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

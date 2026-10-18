# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T04:37:28.793576+00:00`
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

- `risk_on_high->commodity_24h` score `5.0332` n `60` status `ready` deltaP `29.3728` edge `0.2572` maxDD `-0.6869`
- `risk_on_and_context->commodity_24h` score `5.0332` n `60` status `ready` deltaP `29.3728` edge `0.2572` maxDD `-0.6869`
- `market_context_high->commodity_24h` score `1.6517` n `116` status `ready` deltaP `15.2349` edge `0.1586` maxDD `-4.8021`
- `market_context_high->crypto_major_4h` score `1.4858` n `158` status `ready` deltaP `14.8754` edge `0.3651` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.433` n `158` status `ready` deltaP `3.716` edge `0.1002` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.2382` n `158` status `ready` deltaP `7.792` edge `0.1179` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1634` n `91` status `ready` deltaP `13.4566` edge `0.1793` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1634` n `91` status `ready` deltaP `13.4566` edge `0.1793` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0497` n `91` status `ready` deltaP `4.2553` edge `0.0059` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0497` n `91` status `ready` deltaP `4.2553` edge `0.0059` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1624` n `158` status `ready` deltaP `7.3364` edge `0.0051` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2406` n `91` status `ready` deltaP `1.4982` edge `-0.0028` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.4475` n `158` status `ready` deltaP `6.1586` edge `0.0086` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4512` n `91` status `ready` deltaP `9.2582` edge `0.0303` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4512` n `91` status `ready` deltaP `9.2582` edge `0.0303` maxDD `-5.3696`
- `market_context_high->metal_4h` score `-0.5053` n `158` status `ready` deltaP `7.3036` edge `0.0429` maxDD `-1.6961`
- `risk_on_high->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5257` n `91` status `ready` deltaP `0.2467` edge `0.0041` maxDD `-0.8513`
- `market_context_high->fx_1h` score `-0.5271` n `158` status `ready` deltaP `-2.0489` edge `-0.0018` maxDD `-0.503`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

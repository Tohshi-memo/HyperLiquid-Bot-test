# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-19T01:07:29.121843+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8622`

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

- `market_context_high->commodity_24h` score `1.8177` n `91` status `ready` deltaP `15.7688` edge `0.1315` maxDD `-1.8119`
- `market_context_high->crypto_major_4h` score `1.4322` n `91` status `ready` deltaP `13.3292` edge `0.4352` maxDD `-15.2359`
- `risk_on_high->commodity_24h` score `1.1428` n `58` status `ready` deltaP `15.1814` edge `0.0738` maxDD `-1.7154`
- `risk_on_and_context->commodity_24h` score `1.1428` n `58` status `ready` deltaP `15.1814` edge `0.0738` maxDD `-1.7154`
- `risk_on_high->crypto_major_4h` score `0.4728` n `58` status `ready` deltaP `10.1082` edge `0.2413` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.4728` n `58` status `ready` deltaP `10.1082` edge `0.2413` maxDD `-11.1788`
- `market_context_high->crypto_major_1h` score `0.4686` n `91` status `ready` deltaP `4.496` edge `0.119` maxDD `-3.7781`
- `risk_on_high->index_1h` score `0.2528` n `58` status `ready` deltaP `8.1806` edge `0.0029` maxDD `-0.5766`
- `risk_on_and_context->index_1h` score `0.2528` n `58` status `ready` deltaP `8.1806` edge `0.0029` maxDD `-0.5766`
- `risk_on_high->fx_1h` score `-0.1386` n `58` status `ready` deltaP `2.6975` edge `-0.0006` maxDD `-0.1456`
- `risk_on_and_context->fx_1h` score `-0.1386` n `58` status `ready` deltaP `2.6975` edge `-0.0006` maxDD `-0.1456`
- `market_context_high->crypto_alt_1h` score `-0.4219` n `91` status `ready` deltaP `0.4951` edge `0.0926` maxDD `-7.3329`
- `market_context_high->index_1h` score `-0.4476` n `91` status `ready` deltaP `2.6103` edge `-0.002` maxDD `-1.1567`
- `risk_on_high->fx_4h` score `-0.516` n `58` status `ready` deltaP `-2.7259` edge `0.0024` maxDD `-0.1781`
- `risk_on_and_context->fx_4h` score `-0.516` n `58` status `ready` deltaP `-2.7259` edge `0.0024` maxDD `-0.1781`
- `market_context_high->fx_1h` score `-0.5375` n `91` status `ready` deltaP `-2.3992` edge `-0.0008` maxDD `-0.503`
- `risk_on_high->equity_1h` score `-0.5389` n `58` status `ready` deltaP `8.6363` edge `-0.0036` maxDD `-4.5775`
- `risk_on_and_context->equity_1h` score `-0.5389` n `58` status `ready` deltaP `8.6363` edge `-0.0036` maxDD `-4.5775`
- `market_context_high->fx_4h` score `-0.5984` n `91` status `ready` deltaP `-2.4986` edge `0.003` maxDD `-0.7115`
- `risk_on_high->commodity_4h` score `-0.7748` n `58` status `ready` deltaP `5.5626` edge `-0.0309` maxDD `-3.4415`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

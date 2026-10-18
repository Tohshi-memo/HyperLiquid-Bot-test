# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-18T05:52:25.791501+00:00`
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

- `risk_on_high->commodity_24h` score `3.5324` n `65` status `ready` deltaP `22.4497` edge `0.2083` maxDD `-1.4212`
- `risk_on_and_context->commodity_24h` score `3.5324` n `65` status `ready` deltaP `22.4497` edge `0.2083` maxDD `-1.4212`
- `market_context_high->commodity_24h` score `2.1419` n `116` status `ready` deltaP `15.2349` edge `0.1654` maxDD `-3.0782`
- `market_context_high->crypto_major_4h` score `1.7377` n `153` status `ready` deltaP `16.4036` edge `0.3759` maxDD `-15.2359`
- `market_context_high->crypto_major_1h` score `0.6657` n `153` status `ready` deltaP `5.5154` edge `0.1076` maxDD `-3.7781`
- `market_context_high->crypto_alt_1h` score `0.1767` n `153` status `ready` deltaP `7.5966` edge `0.122` maxDD `-7.3329`
- `risk_on_high->crypto_major_4h` score `0.1349` n `91` status `ready` deltaP `12.9992` edge `0.1787` maxDD `-11.1788`
- `risk_on_and_context->crypto_major_4h` score `0.1349` n `91` status `ready` deltaP `12.9992` edge `0.1787` maxDD `-11.1788`
- `risk_on_high->index_1h` score `-0.0509` n `91` status `ready` deltaP `4.2553` edge `0.0058` maxDD `-0.7394`
- `risk_on_and_context->index_1h` score `-0.0509` n `91` status `ready` deltaP `4.2553` edge `0.0058` maxDD `-0.7394`
- `market_context_high->index_1h` score `-0.1774` n `153` status `ready` deltaP `7.0924` edge `0.0048` maxDD `-1.3195`
- `risk_on_high->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `risk_on_and_context->fx_1h` score `-0.2726` n `91` status `ready` deltaP `0.8976` edge `-0.0029` maxDD `-0.376`
- `market_context_high->metal_1h` score `-0.3999` n `153` status `ready` deltaP `6.7385` edge `0.0087` maxDD `-0.9556`
- `risk_on_high->equity_1h` score `-0.4632` n `91` status `ready` deltaP `9.1081` edge `0.0303` maxDD `-5.3696`
- `risk_on_and_context->equity_1h` score `-0.4632` n `91` status `ready` deltaP `9.1081` edge `0.0303` maxDD `-5.3696`
- `risk_on_high->metal_1h` score `-0.5179` n `91` status `ready` deltaP `0.3964` edge `0.0041` maxDD `-0.8513`
- `risk_on_and_context->metal_1h` score `-0.5179` n `91` status `ready` deltaP `0.3964` edge `0.0041` maxDD `-0.8513`
- `market_context_high->equity_1h` score `-0.5629` n `153` status `ready` deltaP `10.1926` edge `0.0391` maxDD `-7.3168`
- `market_context_high->metal_4h` score `-0.6213` n `153` status `ready` deltaP `5.7937` edge `0.0433` maxDD `-1.6961`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

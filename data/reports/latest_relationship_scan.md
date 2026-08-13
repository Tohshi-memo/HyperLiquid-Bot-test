# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-13T04:07:24.887568+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11840`

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

- `news_risk_high->equity_4h` score `6.9288` n `36` status `ready` deltaP `37.5` edge `0.3274` maxDD `0.0`
- `risk_on_high->commodity_24h` score `2.483` n `32` status `ready` deltaP `20.3125` edge `0.0715` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.483` n `32` status `ready` deltaP `20.3125` edge `0.0715` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.3205` n `32` status `ready` deltaP `16.0823` edge `0.1044` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.3205` n `32` status `ready` deltaP `16.0823` edge `0.1044` maxDD `-0.1258`
- `news_risk_high->index_4h` score `1.982` n `36` status `ready` deltaP `22.3577` edge `0.0293` maxDD `-0.0546`
- `risk_on_high->crypto_major_24h` score `1.9491` n `32` status `ready` deltaP `15.9722` edge `0.259` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `1.9491` n `32` status `ready` deltaP `15.9722` edge `0.259` maxDD `-6.2481`
- `risk_on_high->fx_24h` score `1.8992` n `32` status `ready` deltaP `21.1806` edge `0.0355` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.8992` n `32` status `ready` deltaP `21.1806` edge `0.0355` maxDD `-0.1418`
- `news_risk_high->equity_1h` score `1.5751` n `36` status `ready` deltaP `7.8344` edge `0.1109` maxDD `-0.5496`
- `risk_on_high->commodity_1h` score `1.146` n `32` status `ready` deltaP `12.6123` edge `0.0347` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.146` n `32` status `ready` deltaP `12.6123` edge `0.0347` maxDD `-0.1957`
- `market_context_high->commodity_4h` score `1.1389` n `161` status `ready` deltaP `13.7337` edge `0.0672` maxDD `-2.1077`
- `risk_on_high->fx_4h` score `1.0656` n `32` status `ready` deltaP `12.2713` edge `0.0211` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `1.0656` n `32` status `ready` deltaP `12.2713` edge `0.0211` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.8721` n `161` status `ready` deltaP `10.943` edge `0.0294` maxDD `-0.3742`
- `market_context_high->commodity_24h` score `0.514` n `161` status `ready` deltaP `10.3746` edge `0.054` maxDD `-2.4263`
- `news_risk_high->fx_4h` score `0.2262` n `36` status `ready` deltaP `7.7574` edge `-0.0008` maxDD `-0.0863`
- `risk_on_high->index_1h` score `0.219` n `32` status `ready` deltaP `8.6078` edge `0.0082` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

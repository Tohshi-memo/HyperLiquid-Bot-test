# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-21T12:37:31.100794+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9102`

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

- `market_context_high->unknown_4h` score `31.7449` n `58` status `ready` deltaP `1.23` edge `2.6522` maxDD `-0.5326`
- `news_risk_high->crypto_major_24h` score `20.6012` n `101` status `ready` deltaP `8.1442` edge `2.3483` maxDD `-46.1999`
- `news_risk_high->crypto_alt_24h` score `14.8159` n `101` status `ready` deltaP `8.5293` edge `1.6659` maxDD `-32.7147`
- `news_risk_high->crypto_alt_4h` score `3.352` n `101` status `ready` deltaP `16.48` edge `0.2904` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `3.0629` n `101` status `ready` deltaP `19.8337` edge `0.2488` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `2.3709` n `101` status `ready` deltaP `14.7344` edge `0.1459` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `1.7571` n `101` status `ready` deltaP `16.5308` edge `0.0885` maxDD `-2.8494`
- `news_risk_high->commodity_24h` score `1.308` n `101` status `ready` deltaP `23.8913` edge `0.139` maxDD `-3.4467`
- `market_context_high->equity_1h` score `0.7144` n `58` status `ready` deltaP `5.4099` edge `0.0488` maxDD `-0.36`
- `market_context_high->index_1h` score `0.6034` n `58` status `ready` deltaP `9.3795` edge `0.0133` maxDD `-0.0435`
- `news_risk_high->metal_1h` score `0.4974` n `101` status `ready` deltaP `13.5501` edge `0.0113` maxDD `-0.8144`
- `market_context_high->fx_1h` score `0.3858` n `58` status `ready` deltaP `9.2247` edge `0.0063` maxDD `-0.1854`
- `news_risk_high->fx_4h` score `0.3658` n `101` status `ready` deltaP `10.3175` edge `0.0253` maxDD `-0.421`
- `news_risk_high->metal_4h` score `0.2787` n `101` status `ready` deltaP `14.6598` edge `0.0309` maxDD `-2.0994`
- `market_context_high->index_4h` score `0.2475` n `58` status `ready` deltaP `13.5618` edge `0.005` maxDD `-1.0949`
- `market_context_high->metal_1h` score `0.2195` n `58` status `ready` deltaP `5.1002` edge `0.0151` maxDD `-0.1314`
- `news_risk_high->fx_1h` score `-0.1633` n `101` status `ready` deltaP `3.5913` edge `0.0068` maxDD `-0.2147`
- `news_risk_high->equity_1h` score `-0.3605` n `101` status `ready` deltaP `1.0227` edge `0.0037` maxDD `-0.9112`
- `market_context_high->fx_4h` score `-0.3981` n `58` status `ready` deltaP `2.1236` edge `-0.0028` maxDD `-0.6588`
- `news_risk_high->metal_24h` score `-0.4788` n `101` status `ready` deltaP `8.7355` edge `-0.0352` maxDD `-2.4203`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

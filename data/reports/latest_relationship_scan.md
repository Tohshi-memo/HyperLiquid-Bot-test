# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T19:07:34.122289+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->metal_24h` score `3.4049` n `93` status `ready` deltaP `15.3502` edge `0.239` maxDD `-2.2743`
- `market_context_high->equity_24h` score `3.2514` n `93` status `ready` deltaP `-2.2444` edge `0.6044` maxDD `-21.1456`
- `market_context_high->fx_24h` score `1.765` n `93` status `ready` deltaP `27.4544` edge `0.0605` maxDD `-2.3821`
- `market_context_high->commodity_4h` score `1.5539` n `109` status `ready` deltaP `15.5977` edge `0.0928` maxDD `-2.7169`
- `market_context_high->index_24h` score `0.9407` n `93` status `ready` deltaP `9.5706` edge `0.1659` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.7565` n `116` status `ready` deltaP `10.9436` edge `0.0277` maxDD `-1.0091`
- `market_context_high->fx_4h` score `0.137` n `109` status `ready` deltaP `9.3113` edge `0.008` maxDD `-1.6928`
- `market_context_high->fx_1h` score `-0.0844` n `116` status `ready` deltaP `6.0345` edge `-0.0015` maxDD `-0.9639`
- `market_context_high->index_4h` score `-0.4145` n `109` status `ready` deltaP `1.3901` edge `-0.0019` maxDD `-1.1743`
- `market_context_high->equity_1h` score `-0.5486` n `116` status `ready` deltaP `4.4704` edge `-0.005` maxDD `-5.611`
- `market_context_high->index_1h` score `-0.6029` n `116` status `ready` deltaP `-1.1924` edge `-0.0073` maxDD `-0.7995`
- `market_context_high->metal_1h` score `-0.8288` n `116` status `ready` deltaP `-2.6533` edge `-0.0018` maxDD `-0.9664`
- `market_context_high->metal_4h` score `-0.871` n `109` status `ready` deltaP `3.7047` edge `0.0036` maxDD `-2.7373`
- `market_context_high->equity_4h` score `-1.1027` n `109` status `ready` deltaP `8.5855` edge `-0.0154` maxDD `-7.6983`
- `market_context_high->crypto_alt_1h` score `-1.3695` n `116` status `ready` deltaP `-5.5802` edge `-0.014` maxDD `-2.3669`
- `market_context_high->crypto_alt_4h` score `-2.6613` n `109` status `ready` deltaP `-2.4376` edge `-0.0457` maxDD `-5.7857`
- `market_context_high->crypto_major_1h` score `-2.7358` n `116` status `ready` deltaP `-7.3095` edge `-0.0553` maxDD `-6.5831`
- `market_context_high->crypto_major_24h` score `-4.4069` n `93` status `ready` deltaP `2.2629` edge `-0.1329` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.5841` n `93` status `ready` deltaP `-16.4697` edge `-0.1279` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-6.6808` n `109` status `ready` deltaP `-7.6485` edge `-0.1857` maxDD `-18.6034`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

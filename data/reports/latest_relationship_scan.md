# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-27T08:52:27.296143+00:00`
- Price records: `672`
- Market context records: `4917`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `9384`

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

- `market_context_high->unknown_1h` score `16.177` n `105` status `ready` deltaP `10.7613` edge `1.3181` maxDD `-1.674`
- `market_context_high->unknown_4h` score `10.6939` n `105` status `ready` deltaP `26.9512` edge `0.7629` maxDD `-1.7801`
- `market_context_high->crypto_alt_4h` score `6.8691` n `105` status `ready` deltaP `22.3432` edge `0.5587` maxDD `-7.8181`
- `market_context_high->crypto_major_4h` score `6.5547` n `105` status `ready` deltaP `18.3058` edge `0.5466` maxDD `-7.1265`
- `market_context_high->unknown_24h` score `5.6887` n `87` status `ready` deltaP `24.6168` edge `0.3442` maxDD `-1.4072`
- `market_context_high->metal_4h` score `1.2603` n `105` status `ready` deltaP `9.2784` edge `0.1094` maxDD `-1.9651`
- `market_context_high->equity_4h` score `0.9938` n `105` status `ready` deltaP `13.3144` edge `0.1768` maxDD `-6.3852`
- `market_context_high->index_4h` score `0.7121` n `105` status `ready` deltaP `9.7344` edge `0.0407` maxDD `-0.7006`
- `market_context_high->crypto_major_1h` score `0.4768` n `105` status `ready` deltaP `5.9196` edge `0.1255` maxDD `-5.6406`
- `market_context_high->equity_1h` score `0.3508` n `105` status `ready` deltaP `5.6872` edge `0.0644` maxDD `-2.5875`
- `market_context_high->crypto_alt_1h` score `0.3117` n `105` status `ready` deltaP `6.5854` edge `0.0983` maxDD `-5.5126`
- `market_context_high->commodity_1h` score `-0.1486` n `105` status `ready` deltaP `4.5181` edge `0.0168` maxDD `-1.278`
- `market_context_high->metal_1h` score `-0.2025` n `105` status `ready` deltaP `1.3074` edge `0.0324` maxDD `-1.3057`
- `market_context_high->index_1h` score `-0.5405` n `105` status `ready` deltaP `-0.7214` edge `0.011` maxDD `-0.7054`
- `market_context_high->commodity_4h` score `-0.6702` n `105` status `ready` deltaP `8.3275` edge `0.0073` maxDD `-4.4933`
- `market_context_high->fx_4h` score `-0.8581` n `105` status `ready` deltaP `-2.381` edge `0.0029` maxDD `-1.0967`
- `market_context_high->fx_1h` score `-0.9186` n `105` status `ready` deltaP `-8.4617` edge `-0.0001` maxDD `-0.5675`
- `market_context_high->fx_24h` score `-1.8307` n `87` status `ready` deltaP `-6.2141` edge `-0.0101` maxDD `-2.749`
- `market_context_high->commodity_24h` score `-4.8523` n `87` status `ready` deltaP `14.6432` edge `0.0089` maxDD `-27.5371`
- `market_context_high->index_24h` score `-4.8701` n `87` status `ready` deltaP `-9.2732` edge `-0.154` maxDD `-24.6845`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

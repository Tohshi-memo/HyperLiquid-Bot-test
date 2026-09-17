# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T22:37:24.230717+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8924`

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

- `news_risk_high->unknown_4h` score `467.9159` n `71` status `ready` deltaP `-12.3218` edge `39.1521` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.202` n `52` status `ready` deltaP `50.0` edge `0.4335` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.202` n `52` status `ready` deltaP `50.0` edge `0.4335` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `7.9538` n `56` status `ready` deltaP `25.744` edge `0.6291` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9029` n `149` status `ready` deltaP `43.2886` edge `0.4225` maxDD `-0.8682`
- `news_risk_high->index_24h` score `4.6319` n `56` status `ready` deltaP `31.9196` edge `0.1908` maxDD `-0.075`
- `news_risk_high->equity_24h` score `3.7895` n `56` status `ready` deltaP `18.6508` edge `0.5389` maxDD `-6.5262`
- `news_risk_high->crypto_major_24h` score `3.5005` n `56` status `ready` deltaP `11.6815` edge `0.5704` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0837` n `52` status `ready` deltaP `33.6069` edge `0.0679` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0837` n `52` status `ready` deltaP `33.6069` edge `0.0679` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9834` n `149` status `ready` deltaP `30.1092` edge `0.0897` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8257` n `52` status `ready` deltaP `26.2019` edge `-0.0183` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8257` n `52` status `ready` deltaP `26.2019` edge `-0.0183` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.6909` n `149` status `ready` deltaP `23.427` edge `0.0063` maxDD `-0.0593`
- `news_risk_high->metal_24h` score `1.617` n `56` status `ready` deltaP `18.2292` edge `0.1312` maxDD `-0.6334`
- `news_risk_high->index_4h` score `1.4285` n `71` status `ready` deltaP `20.3002` edge `0.0303` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2979` n `149` status `ready` deltaP `17.7079` edge `0.0278` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6746` n `52` status `ready` deltaP `10.79` edge `0.0195` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2389` n `149` status `ready` deltaP `10.9531` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

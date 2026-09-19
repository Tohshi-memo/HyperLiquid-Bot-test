# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T05:22:30.420459+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8352`

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

- `news_risk_high->crypto_major_24h` score `59.9194` n `58` status `ready` deltaP `35.2909` edge `4.8472` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `53.8429` n `58` status `ready` deltaP `37.9071` edge `4.3721` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.3019` n `149` status `ready` deltaP `-1.683` edge `3.0597` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `14.0942` n `58` status `ready` deltaP `48.4375` edge `0.8516` maxDD `0.0`
- `risk_on_high->unknown_4h` score `10.1805` n `52` status `ready` deltaP `-8.9236` edge `0.9304` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `10.1805` n `52` status `ready` deltaP `-8.9236` edge `0.9304` maxDD `-0.4694`
- `news_risk_high->crypto_alt_4h` score `8.6301` n `74` status `ready` deltaP `27.7768` edge `0.6466` maxDD `-7.675`
- `risk_on_high->commodity_24h` score `8.2688` n `52` status `ready` deltaP `44.9653` edge `0.3893` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2688` n `52` status `ready` deltaP `44.9653` edge `0.3893` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.9697` n `149` status `ready` deltaP `38.2539` edge `0.3783` maxDD `-0.8682`
- `news_risk_high->crypto_major_4h` score `5.8163` n `74` status `ready` deltaP `24.2007` edge `0.4408` maxDD `-8.0625`
- `news_risk_high->metal_24h` score `4.6457` n `58` status `ready` deltaP `38.2543` edge `0.1479` maxDD `-0.2629`
- `news_risk_high->crypto_alt_1h` score `3.2949` n `81` status `ready` deltaP `17.3006` edge `0.2058` maxDD `-2.058`
- `news_risk_high->crypto_major_1h` score `2.6341` n `81` status `ready` deltaP `20.0691` edge `0.138` maxDD `-2.8494`
- `risk_on_high->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.52` n `52` status `ready` deltaP `30.1008` edge `0.0443` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.4197` n `149` status `ready` deltaP `26.6031` edge `0.0661` maxDD `-0.345`
- `news_risk_high->fx_4h` score `1.4676` n `74` status `ready` deltaP `16.0926` edge `0.0369` maxDD `-0.084`
- `news_risk_high->fx_24h` score `1.2784` n `58` status `ready` deltaP `7.1301` edge `0.0632` maxDD `-0.0029`
- `news_risk_high->equity_4h` score `1.1802` n `74` status `ready` deltaP `10.5966` edge `0.1291` maxDD `-4.4447`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

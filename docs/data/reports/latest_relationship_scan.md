# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T11:37:27.674022+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8658`

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

- `news_risk_high->unknown_4h` score `384.6074` n `83` status `ready` deltaP `-21.6629` edge `32.2845` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.971` n `83` status `ready` deltaP `32.4485` edge `1.0025` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.3484` n `83` status `ready` deltaP `24.5147` edge `1.0651` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.1146` n `52` status `ready` deltaP `49.1319` edge `0.432` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.1146` n `52` status `ready` deltaP `49.1319` edge `0.432` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.8869` n `83` status `ready` deltaP `33.7475` edge `0.693` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `7.8154` n `149` status `ready` deltaP `42.4205` edge `0.421` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.7778` n `83` status `ready` deltaP `39.1776` edge `0.2379` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.9934` n `83` status `ready` deltaP `31.4696` edge `0.1684` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.6377` n `52` status `ready` deltaP `31.1679` edge `0.047` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6377` n `52` status `ready` deltaP `31.1679` edge `0.047` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5375` n `149` status `ready` deltaP `27.6702` edge `0.0688` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.4631` n `52` status `ready` deltaP `32.2783` edge `-0.0057` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.4631` n `52` status `ready` deltaP `32.2783` edge `-0.0057` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.3282` n `149` status `ready` deltaP `29.5034` edge `0.0189` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0678` n `149` status `ready` deltaP `15.9115` edge `0.0206` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4445` n `52` status `ready` deltaP `8.9936` edge `0.0123` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4445` n `52` status `ready` deltaP `8.9936` edge `0.0123` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1892` n `83` status `ready` deltaP `9.4494` edge `0.0241` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0711` n `149` status `ready` deltaP `4.9512` edge `0.0019` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

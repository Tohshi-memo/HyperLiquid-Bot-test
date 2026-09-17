# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T13:22:27.019243+00:00`
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

- `news_risk_high->unknown_4h` score `384.3804` n `83` status `ready` deltaP `-22.73` edge `32.2727` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.0973` n `83` status `ready` deltaP `31.2333` edge `0.9378` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.7352` n `83` status `ready` deltaP `23.2994` edge `1.0221` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3383` n `52` status `ready` deltaP `50.1736` edge `0.4437` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3383` n `52` status `ready` deltaP `50.1736` edge `0.4437` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.4357` n `83` status `ready` deltaP `32.5323` edge `0.6635` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0391` n `149` status `ready` deltaP `43.4622` edge `0.4327` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6675` n `83` status `ready` deltaP `38.3095` edge `0.2345` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.8435` n `83` status `ready` deltaP `30.6016` edge `0.1617` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.8251` n `52` status `ready` deltaP `32.235` edge `0.0555` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8251` n `52` status `ready` deltaP `32.235` edge `0.0555` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7248` n `149` status `ready` deltaP `28.7373` edge `0.0773` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.3454` n `52` status `ready` deltaP `31.063` edge `-0.0074` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3454` n `52` status `ready` deltaP `31.063` edge `-0.0074` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.2106` n `149` status `ready` deltaP `28.2881` edge `0.0172` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1852` n `149` status `ready` deltaP `16.8097` edge `0.0244` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5619` n `52` status `ready` deltaP `9.8918` edge `0.0161` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5619` n `52` status `ready` deltaP `9.8918` edge `0.0161` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1025` n `83` status `ready` deltaP `8.3823` edge `0.0201` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0805` n `149` status `ready` deltaP `5.1009` edge `0.0021` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

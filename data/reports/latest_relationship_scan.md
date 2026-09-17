# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T13:07:28.868716+00:00`
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

- `news_risk_high->unknown_4h` score `384.4106` n `83` status `ready` deltaP `-22.5775` edge `32.2742` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.2264` n `83` status `ready` deltaP `31.4069` edge `0.9474` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.8355` n `83` status `ready` deltaP `23.473` edge `1.0293` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3227` n `52` status `ready` deltaP `50.1736` edge `0.4424` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3227` n `52` status `ready` deltaP `50.1736` edge `0.4424` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.4975` n `83` status `ready` deltaP `32.7059` edge `0.6675` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0235` n `149` status `ready` deltaP `43.4622` edge `0.4314` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6723` n `83` status `ready` deltaP `38.3095` edge `0.2349` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.867` n `83` status `ready` deltaP `30.7752` edge `0.1625` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.7985` n `52` status `ready` deltaP `32.0825` edge `0.0543` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7985` n `52` status `ready` deltaP `32.0825` edge `0.0543` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.6982` n `149` status `ready` deltaP `28.5848` edge `0.0761` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.3629` n `52` status `ready` deltaP `31.2366` edge `-0.0071` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3629` n `52` status `ready` deltaP `31.2366` edge `-0.0071` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.228` n `149` status `ready` deltaP `28.4617` edge `0.0175` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.184` n `149` status `ready` deltaP `16.8097` edge `0.0243` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5607` n `52` status `ready` deltaP `9.8918` edge `0.016` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5607` n `52` status `ready` deltaP `9.8918` edge `0.016` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.1151` n `83` status `ready` deltaP `8.5347` edge `0.0207` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.089` n `149` status `ready` deltaP `5.2506` edge `0.0022` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

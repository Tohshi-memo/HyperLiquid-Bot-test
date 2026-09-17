# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T19:52:29.496626+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9028`

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

- `news_risk_high->unknown_4h` score `429.1224` n `76` status `ready` deltaP `-16.656` edge `35.9482` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2968` n `52` status `ready` deltaP `50.0` edge `0.4414` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2968` n `52` status `ready` deltaP `50.0` edge `0.4414` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2636` n `67` status `ready` deltaP `28.2364` edge `0.6383` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9977` n `149` status `ready` deltaP `43.2886` edge `0.4304` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.1362` n `67` status `ready` deltaP `25.3938` edge `0.6028` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.1695` n `67` status `ready` deltaP `35.1446` edge `0.2141` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.7773` n `67` status `ready` deltaP `17.5451` edge `0.695` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.3235` n `67` status `ready` deltaP `24.3859` edge `0.1598` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `3.0073` n `52` status `ready` deltaP `32.9972` edge `0.0656` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0073` n `52` status `ready` deltaP `32.9972` edge `0.0656` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.907` n `149` status `ready` deltaP `29.4995` edge `0.0874` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8859` n `52` status `ready` deltaP `26.5491` edge `-0.0156` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8859` n `52` status `ready` deltaP `26.5491` edge `-0.0156` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.751` n `149` status `ready` deltaP `23.7742` edge `0.009` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.4754` n `76` status `ready` deltaP `21.0206` edge `0.0294` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.2044` n `149` status `ready` deltaP `16.8097` edge `0.026` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5811` n `52` status `ready` deltaP `9.8918` edge `0.0177` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5811` n `52` status `ready` deltaP `9.8918` edge `0.0177` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

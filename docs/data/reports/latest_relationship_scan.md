# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T20:52:30.356563+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9148`

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

- `news_risk_high->unknown_4h` score `451.7315` n `73` status `ready` deltaP `-12.9218` edge `37.8074` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.274` n `52` status `ready` deltaP `50.0` edge `0.4395` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.274` n `52` status `ready` deltaP `50.0` edge `0.4395` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.2802` n `63` status `ready` deltaP `28.3234` edge `0.6391` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9749` n `149` status `ready` deltaP `43.2886` edge `0.4285` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.741` n `63` status `ready` deltaP `23.2143` edge `0.5844` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.9781` n `63` status `ready` deltaP `34.1022` edge `0.2051` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.4252` n `63` status `ready` deltaP `15.6498` edge `0.6625` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0777` n `52` status `ready` deltaP `33.6069` edge `0.0674` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0777` n `52` status `ready` deltaP `33.6069` edge `0.0674` maxDD `-0.1313`
- `news_risk_high->metal_24h` score `3.0575` n `63` status `ready` deltaP `22.3959` edge `0.1509` maxDD `-0.6334`
- `market_context_high->commodity_4h` score `2.9774` n `149` status `ready` deltaP `30.1092` edge `0.0892` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.8763` n `52` status `ready` deltaP `26.5491` edge `-0.0164` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8763` n `52` status `ready` deltaP `26.5491` edge `-0.0164` maxDD `-0.0054`
- `news_risk_high->index_4h` score `1.7637` n `73` status `ready` deltaP `24.265` edge `0.0318` maxDD `-0.3938`
- `market_context_high->fx_24h` score `1.7414` n `149` status `ready` deltaP `23.7742` edge `0.0082` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2511` n `149` status `ready` deltaP `17.2588` edge `0.0269` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6279` n `52` status `ready` deltaP `10.3409` edge `0.0186` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6279` n `52` status `ready` deltaP `10.3409` edge `0.0186` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2143` n `149` status `ready` deltaP `10.4957` edge `0.0051` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T21:52:30.568071+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8836`

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

- `news_risk_high->unknown_4h` score `467.8943` n `71` status `ready` deltaP `-12.3218` edge `39.1503` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.2392` n `52` status `ready` deltaP `50.0` edge `0.4366` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.2392` n `52` status `ready` deltaP `50.0` edge `0.4366` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.0818` n `59` status `ready` deltaP `26.9244` edge `0.6319` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `7.9401` n `149` status `ready` deltaP `43.2886` edge `0.4256` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `6.2382` n `59` status `ready` deltaP `20.7391` edge `0.559` maxDD `-6.5262`
- `news_risk_high->index_24h` score `4.7874` n `59` status `ready` deltaP `32.9184` edge `0.1971` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `3.9428` n `59` status `ready` deltaP `13.4975` edge `0.615` maxDD `-13.2931`
- `risk_on_high->commodity_4h` score `3.0885` n `52` status `ready` deltaP `33.6069` edge `0.0683` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `3.0885` n `52` status `ready` deltaP `33.6069` edge `0.0683` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.9882` n `149` status `ready` deltaP `30.1092` edge `0.0901` maxDD `-0.345`
- `news_risk_high->metal_24h` score `2.7375` n `59` status `ready` deltaP `20.136` edge `0.1393` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `1.8643` n `52` status `ready` deltaP `26.5491` edge `-0.0174` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.8643` n `52` status `ready` deltaP `26.5491` edge `-0.0174` maxDD `-0.0054`
- `news_risk_high->index_4h` score `1.7588` n `71` status `ready` deltaP `24.0681` edge `0.0327` maxDD `-0.3938`
- `market_context_high->fx_24h` score `1.7294` n `149` status `ready` deltaP `23.7742` edge `0.0072` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.2847` n `149` status `ready` deltaP `17.5582` edge `0.0277` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.6614` n `52` status `ready` deltaP `10.6403` edge `0.0194` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.6614` n `52` status `ready` deltaP `10.6403` edge `0.0194` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2309` n `149` status `ready` deltaP `10.8006` edge `0.0052` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

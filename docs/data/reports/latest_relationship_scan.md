# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T19:37:29.936354+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9026`

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

- `news_risk_high->unknown_4h` score `422.1138` n `77` status `ready` deltaP `-17.4434` edge `35.3694` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.3004` n `52` status `ready` deltaP `50.0` edge `0.4417` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3004` n `52` status `ready` deltaP `50.0` edge `0.4417` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.1112` n `68` status `ready` deltaP `27.2468` edge `0.6322` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0013` n `149` status `ready` deltaP `43.2886` edge `0.4307` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.197` n `68` status `ready` deltaP `25.8987` edge `0.6045` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.2104` n `68` status `ready` deltaP `35.386` edge `0.2159` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `4.8258` n `68` status `ready` deltaP `17.984` edge `0.6983` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.3675` n `68` status `ready` deltaP `24.8468` edge `0.1604` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9879` n `52` status `ready` deltaP `32.8447` edge `0.065` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9879` n `52` status `ready` deltaP `32.8447` edge `0.065` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8876` n `149` status `ready` deltaP `29.347` edge `0.0868` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.9034` n `52` status `ready` deltaP `26.7227` edge `-0.0153` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.9034` n `52` status `ready` deltaP `26.7227` edge `-0.0153` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.7685` n `149` status `ready` deltaP `23.9478` edge `0.0093` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.3947` n `77` status `ready` deltaP `20.1477` edge `0.0285` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.1864` n `149` status `ready` deltaP `16.66` edge `0.0255` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5632` n `52` status `ready` deltaP `9.7421` edge `0.0172` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5632` n `52` status `ready` deltaP `9.7421` edge `0.0172` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

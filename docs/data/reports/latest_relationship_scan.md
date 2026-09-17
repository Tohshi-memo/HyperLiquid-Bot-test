# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T03:52:31.727509+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `120`

- Symbol pattern count: `10533`

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

- `news_risk_high->unknown_4h` score `384.7524` n `83` status `ready` deltaP `-20.9007` edge `32.2915` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `16.2287` n `83` status `ready` deltaP `37.8305` edge `1.2381` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `14.8598` n `83` status `ready` deltaP `29.8967` edge `1.2385` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `11.1042` n `83` status `ready` deltaP `39.1295` edge `0.8419` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `7.838` n `52` status `ready` deltaP `43.75` edge `0.3615` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `7.838` n `52` status `ready` deltaP `43.75` edge `0.3615` maxDD `0.0`
- `market_context_high->commodity_24h` score `6.5389` n `149` status `ready` deltaP `37.0386` edge `0.3505` maxDD `-0.8682`
- `news_risk_high->index_24h` score `6.4267` n `83` status `ready` deltaP `44.5595` edge `0.2561` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.6158` n `83` status `ready` deltaP `31.9905` edge `0.2168` maxDD `-0.6334`
- `risk_on_high->fx_24h` score `2.5934` n `52` status `ready` deltaP `33.6672` edge `-0.0041` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5934` n `52` status `ready` deltaP `33.6672` edge `-0.0041` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.4585` n `149` status `ready` deltaP `30.8923` edge `0.0205` maxDD `-0.0593`
- `risk_on_high->commodity_4h` score `2.1736` n `52` status `ready` deltaP `27.6618` edge `0.0317` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.1736` n `52` status `ready` deltaP `27.6618` edge `0.0317` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.0734` n `149` status `ready` deltaP `24.1641` edge `0.0535` maxDD `-0.345`
- `market_context_high->commodity_1h` score `0.8785` n `149` status `ready` deltaP `13.9654` edge `0.0178` maxDD `-0.3491`
- `news_risk_high->index_4h` score `0.3753` n `83` status `ready` deltaP `11.8884` edge `0.0317` maxDD `-0.6935`
- `risk_on_high->commodity_1h` score `0.2552` n `52` status `ready` deltaP `7.0475` edge `0.0095` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.2552` n `52` status `ready` deltaP `7.0475` edge `0.0095` maxDD `-0.1507`
- `risk_on_high->metal_1h` score `0.1358` n `52` status `ready` deltaP `6.1147` edge `0.0072` maxDD `-0.1115`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

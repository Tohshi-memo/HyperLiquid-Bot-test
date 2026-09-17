# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T10:52:31.371826+00:00`
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

- `news_risk_high->unknown_4h` score `384.6726` n `83` status `ready` deltaP `-21.358` edge `32.2879` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `13.2826` n `83` status `ready` deltaP `32.9694` edge `1.025` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `12.5473` n `83` status `ready` deltaP `25.0355` edge `1.0782` maxDD `-13.2931`
- `news_risk_high->equity_24h` score `9.0713` n `83` status `ready` deltaP `34.2684` edge `0.7049` maxDD `-6.5262`
- `risk_on_high->commodity_24h` score `9.0177` n `52` status `ready` deltaP `48.6111` edge `0.4274` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.0177` n `52` status `ready` deltaP `48.6111` edge `0.4274` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.7185` n `149` status `ready` deltaP `41.8997` edge `0.4164` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.835` n `83` status `ready` deltaP `39.6984` edge `0.2392` maxDD `-0.075`
- `news_risk_high->metal_24h` score `4.0282` n `83` status `ready` deltaP `31.4696` edge `0.1713` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.576` n `52` status `ready` deltaP `30.7106` edge `0.0449` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.576` n `52` status `ready` deltaP `30.7106` edge `0.0449` maxDD `-0.1313`
- `risk_on_high->fx_24h` score `2.5131` n `52` status `ready` deltaP `32.7991` edge `-0.005` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.5131` n `52` status `ready` deltaP `32.7991` edge `-0.005` maxDD `-0.0054`
- `market_context_high->commodity_4h` score `2.4757` n `149` status `ready` deltaP `27.2129` edge `0.0667` maxDD `-0.345`
- `market_context_high->fx_24h` score `2.3782` n `149` status `ready` deltaP `30.0242` edge `0.0196` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.0306` n `149` status `ready` deltaP `15.4624` edge `0.0205` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4074` n `52` status `ready` deltaP `8.5445` edge `0.0122` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4074` n `52` status `ready` deltaP `8.5445` edge `0.0122` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.2247` n `83` status `ready` deltaP `9.9067` edge `0.0256` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0454` n `149` status `ready` deltaP `4.5021` edge `0.0016` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

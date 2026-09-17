# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T13:37:32.440366+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `news_risk_high->unknown_4h` score `384.3142` n `83` status `ready` deltaP `-22.8824` edge `32.2682` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `12.0349` n `83` status `ready` deltaP `31.2333` edge `0.9326` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.6992` n `83` status `ready` deltaP `23.2994` edge `1.0191` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3467` n `52` status `ready` deltaP `50.1736` edge `0.4444` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3467` n `52` status `ready` deltaP `50.1736` edge `0.4444` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.4057` n `83` status `ready` deltaP `32.5323` edge `0.661` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0475` n `149` status `ready` deltaP `43.4622` edge `0.4334` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6651` n `83` status `ready` deltaP `38.3095` edge `0.2343` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.8387` n `83` status `ready` deltaP `30.6016` edge `0.1613` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.8469` n `52` status `ready` deltaP `32.3874` edge `0.0563` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8469` n `52` status `ready` deltaP `32.3874` edge `0.0563` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7466` n `149` status `ready` deltaP `28.8897` edge `0.0781` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.3291` n `52` status `ready` deltaP `30.8894` edge `-0.0076` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.3291` n `52` status `ready` deltaP `30.8894` edge `-0.0076` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.1943` n `149` status `ready` deltaP `28.1145` edge `0.017` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1696` n `149` status `ready` deltaP `16.66` edge `0.0241` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5464` n `52` status `ready` deltaP `9.7421` edge `0.0158` maxDD `-0.1507`
- `news_risk_high->index_4h` score `0.0915` n `83` status `ready` deltaP `8.2299` edge `0.0197` maxDD `-0.6935`
- `market_context_high->fx_1h` score `0.0719` n `149` status `ready` deltaP `4.9512` edge `0.002` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

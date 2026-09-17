# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T14:52:31.604438+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8884`

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

- `news_risk_high->unknown_4h` score `384.1033` n `83` status `ready` deltaP `-23.6446` edge `32.2557` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `11.6761` n `83` status `ready` deltaP `31.2333` edge `0.9027` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.5888` n `83` status `ready` deltaP `23.2994` edge `1.0099` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3815` n `52` status `ready` deltaP `50.1736` edge `0.4473` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3815` n `52` status `ready` deltaP `50.1736` edge `0.4473` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.3169` n `83` status `ready` deltaP `32.5323` edge `0.6536` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0823` n `149` status `ready` deltaP `43.4622` edge `0.4363` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6759` n `83` status `ready` deltaP `38.3095` edge `0.2352` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.8231` n `83` status `ready` deltaP `30.6016` edge `0.16` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.8915` n `52` status `ready` deltaP `32.5399` edge `0.059` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8915` n `52` status `ready` deltaP `32.5399` edge `0.059` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7912` n `149` status `ready` deltaP `29.0422` edge `0.0808` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.2417` n `52` status `ready` deltaP `30.0213` edge `-0.0091` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.2417` n `52` status `ready` deltaP `30.0213` edge `-0.0091` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.1068` n `149` status `ready` deltaP `27.2464` edge `0.0155` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1013` n `149` status `ready` deltaP `16.0612` edge `0.0224` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4781` n `52` status `ready` deltaP `9.1433` edge `0.0141` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4781` n `52` status `ready` deltaP `9.1433` edge `0.0141` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1177` n `149` status `ready` deltaP `8.8189` edge `0.0039` maxDD `-0.1412`
- `market_context_high->fx_1h` score `0.0805` n `149` status `ready` deltaP `5.1009` edge `0.0021` maxDD `-0.063`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

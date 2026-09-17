# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T15:07:31.226253+00:00`
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

- `news_risk_high->unknown_4h` score `390.1486` n `82` status `ready` deltaP `-23.0183` edge `32.7553` maxDD `-4.1571`
- `news_risk_high->crypto_alt_24h` score `11.4257` n `82` status `ready` deltaP `31.0129` edge `0.8833` maxDD `-9.3661`
- `news_risk_high->crypto_major_24h` score `11.1981` n `82` status `ready` deltaP `23.0056` edge `0.9793` maxDD `-13.2931`
- `risk_on_high->commodity_24h` score `9.3839` n `52` status `ready` deltaP `50.1736` edge `0.4475` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3839` n `52` status `ready` deltaP `50.1736` edge `0.4475` maxDD `0.0`
- `news_risk_high->equity_24h` score `8.2754` n `82` status `ready` deltaP `32.1943` edge `0.6524` maxDD `-6.5262`
- `market_context_high->commodity_24h` score `8.0847` n `149` status `ready` deltaP `43.4622` edge `0.4365` maxDD `-0.8682`
- `news_risk_high->index_24h` score `5.6606` n `82` status `ready` deltaP `38.1479` edge `0.235` maxDD `-0.075`
- `news_risk_high->metal_24h` score `3.7936` n `82` status `ready` deltaP `30.293` edge `0.1596` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.8999` n `52` status `ready` deltaP `32.5399` edge `0.0597` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.8999` n `52` status `ready` deltaP `32.5399` edge `0.0597` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.7996` n `149` status `ready` deltaP `29.0422` edge `0.0815` maxDD `-0.345`
- `risk_on_high->fx_24h` score `2.2242` n `52` status `ready` deltaP `29.8477` edge `-0.0094` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `2.2242` n `52` status `ready` deltaP `29.8477` edge `-0.0094` maxDD `-0.0054`
- `market_context_high->fx_24h` score `2.0893` n `149` status `ready` deltaP `27.0728` edge `0.0152` maxDD `-0.0593`
- `market_context_high->commodity_1h` score `1.1025` n `149` status `ready` deltaP `16.0612` edge `0.0225` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.4793` n `52` status `ready` deltaP `9.1433` edge `0.0142` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.4793` n `52` status `ready` deltaP `9.1433` edge `0.0142` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.1272` n `149` status `ready` deltaP `8.9713` edge `0.0041` maxDD `-0.1412`
- `news_risk_high->index_4h` score `0.1156` n `82` status `ready` deltaP `8.2317` edge `0.0185` maxDD `-0.6848`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

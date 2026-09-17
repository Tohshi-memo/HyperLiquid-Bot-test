# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T19:07:09.631316+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9036`

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

- `news_risk_high->unknown_4h` score `421.144` n `77` status `ready` deltaP `-19.7359` edge `35.3122` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.3136` n `52` status `ready` deltaP `50.0` edge `0.4428` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.3136` n `52` status `ready` deltaP `50.0` edge `0.4428` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3044` n `70` status `ready` deltaP `27.877` edge `0.6441` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0145` n `149` status `ready` deltaP `43.2886` edge `0.4318` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.4183` n `70` status `ready` deltaP `26.8651` edge `0.6165` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.3038` n `70` status `ready` deltaP `35.8482` edge `0.2206` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `5.0622` n `70` status `ready` deltaP `18.8244` edge `0.723` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.4681` n `70` status `ready` deltaP `25.7292` edge `0.1629` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9539` n `52` status `ready` deltaP `32.5399` edge `0.0642` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9539` n `52` status `ready` deltaP `32.5399` edge `0.0642` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8536` n `149` status `ready` deltaP `29.0422` edge `0.086` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.9384` n `52` status `ready` deltaP `27.07` edge `-0.0147` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.9384` n `52` status `ready` deltaP `27.07` edge `-0.0147` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.8035` n `149` status `ready` deltaP `24.2951` edge `0.0099` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.2922` n `77` status `ready` deltaP `19.0014` edge `0.0276` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.1673` n `149` status `ready` deltaP `16.5103` edge `0.0249` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.544` n `52` status `ready` deltaP `9.5924` edge `0.0166` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.544` n `52` status `ready` deltaP `9.5924` edge `0.0166` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2135` n `149` status `ready` deltaP `10.4957` edge `0.005` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

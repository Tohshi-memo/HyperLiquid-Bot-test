# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-17T18:52:32.001554+00:00`
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

- `news_risk_high->unknown_4h` score `420.6447` n `77` status `ready` deltaP `-20.8821` edge `35.2824` maxDD `-4.1571`
- `risk_on_high->commodity_24h` score `9.322` n `52` status `ready` deltaP `50.0` edge `0.4435` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `9.322` n `52` status `ready` deltaP `50.0` edge `0.4435` maxDD `0.0`
- `news_risk_high->crypto_alt_24h` score `8.3754` n `71` status `ready` deltaP `28.1788` edge `0.648` maxDD `-9.3661`
- `market_context_high->commodity_24h` score `8.0229` n `149` status `ready` deltaP `43.2886` edge `0.4325` maxDD `-0.8682`
- `news_risk_high->equity_24h` score `7.5201` n `71` status `ready` deltaP `27.3278` edge `0.6219` maxDD `-6.5262`
- `news_risk_high->index_24h` score `5.3491` n `71` status `ready` deltaP `36.0695` edge `0.2229` maxDD `-0.075`
- `news_risk_high->crypto_major_24h` score `5.1494` n `71` status `ready` deltaP `19.2268` edge `0.7315` maxDD `-13.2931`
- `news_risk_high->metal_24h` score `3.5151` n `71` status `ready` deltaP `26.1517` edge `0.164` maxDD `-0.6334`
- `risk_on_high->commodity_4h` score `2.9491` n `52` status `ready` deltaP `32.5399` edge `0.0638` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.9491` n `52` status `ready` deltaP `32.5399` edge `0.0638` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.8488` n `149` status `ready` deltaP `29.0422` edge `0.0856` maxDD `-0.345`
- `risk_on_high->fx_24h` score `1.9559` n `52` status `ready` deltaP `27.2436` edge `-0.0144` maxDD `-0.0054`
- `risk_on_and_context->fx_24h` score `1.9559` n `52` status `ready` deltaP `27.2436` edge `-0.0144` maxDD `-0.0054`
- `market_context_high->fx_24h` score `1.821` n `149` status `ready` deltaP `24.4687` edge `0.0102` maxDD `-0.0593`
- `news_risk_high->index_4h` score `1.1897` n `77` status `ready` deltaP `17.8552` edge `0.0267` maxDD `-0.3938`
- `market_context_high->commodity_1h` score `1.1661` n `149` status `ready` deltaP `16.5103` edge `0.0248` maxDD `-0.3491`
- `risk_on_high->commodity_1h` score `0.5428` n `52` status `ready` deltaP `9.5924` edge `0.0165` maxDD `-0.1507`
- `risk_on_and_context->commodity_1h` score `0.5428` n `52` status `ready` deltaP `9.5924` edge `0.0165` maxDD `-0.1507`
- `market_context_high->fx_4h` score `0.2127` n `149` status `ready` deltaP `10.4957` edge `0.0049` maxDD `-0.1412`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

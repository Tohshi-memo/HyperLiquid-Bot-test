# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T14:52:34.205724+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10084`

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

- `market_context_high->unknown_1h` score `88.6927` n `47` status `ready` deltaP `10.116` edge `7.3307` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `42.6939` n `47` status `ready` deltaP `30.0753` edge `3.3966` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.6132` n `47` status `ready` deltaP `24.782` edge `2.2572` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.0455` n `47` status `ready` deltaP `27.8184` edge `1.8539` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8341` n `47` status `ready` deltaP `34.9364` edge `0.4329` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `6.0137` n `97` status `ready` deltaP `2.4377` edge `1.659` maxDD `-63.6743`
- `news_risk_high->crypto_alt_24h` score `4.1583` n `97` status `ready` deltaP `0.1056` edge `1.2337` maxDD `-49.7699`
- `market_context_high->metal_24h` score `3.5574` n `47` status `ready` deltaP `30.7181` edge `0.1155` maxDD `-0.2401`
- `market_context_high->index_4h` score `3.0822` n `47` status `ready` deltaP `35.0934` edge `0.0383` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.9584` n `118` status `ready` deltaP `13.7497` edge `0.2039` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6395` n `47` status `ready` deltaP `17.7542` edge `0.1434` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.4471` n `118` status `ready` deltaP `16.1449` edge `0.1398` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.7746` n `109` status `ready` deltaP `25.5119` edge `0.0414` maxDD `-0.421`
- `news_risk_high->fx_24h` score `1.2505` n `97` status `ready` deltaP `29.7054` edge `0.1254` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `1.1737` n `97` status `ready` deltaP `25.3222` edge `0.1265` maxDD `-7.2536`
- `news_risk_high->commodity_24h` score `1.0615` n `97` status `ready` deltaP `16.0563` edge `0.0993` maxDD `-2.431`
- `market_context_high->index_1h` score `0.9643` n `47` status `ready` deltaP `14.6101` edge `0.0108` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.8947` n `47` status `ready` deltaP `10.8676` edge `0.0424` maxDD `-1.5564`
- `news_risk_high->crypto_major_4h` score `0.6632` n `109` status `ready` deltaP `14.4118` edge `0.2021` maxDD `-13.719`
- `news_risk_high->metal_1h` score `0.5013` n `118` status `ready` deltaP `15.6069` edge `0.0179` maxDD `-0.6142`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

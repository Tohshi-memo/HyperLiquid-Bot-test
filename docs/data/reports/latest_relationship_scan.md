# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-24T15:37:39.074561+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `10036`

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

- `market_context_high->unknown_1h` score `87.7267` n `47` status `ready` deltaP `10.116` edge `7.2502` maxDD `-0.2334`
- `market_context_high->crypto_major_24h` score `43.1333` n `47` status `ready` deltaP `30.4226` edge `3.4309` maxDD `-2.4756`
- `market_context_high->crypto_alt_24h` score `28.9384` n `47` status `ready` deltaP `24.782` edge `2.2843` maxDD `-2.7051`
- `market_context_high->equity_24h` score `24.2347` n `47` status `ready` deltaP `28.3392` edge `1.8662` maxDD `-2.1786`
- `market_context_high->index_24h` score `7.8473` n `47` status `ready` deltaP `34.9364` edge `0.434` maxDD `-0.3705`
- `news_risk_high->crypto_major_24h` score `5.3802` n `94` status `ready` deltaP `1.6992` edge `1.5827` maxDD `-63.6743`
- `market_context_high->metal_24h` score `3.6255` n `47` status `ready` deltaP `31.2389` edge `0.1177` maxDD `-0.2401`
- `news_risk_high->crypto_alt_24h` score `3.4446` n `94` status `ready` deltaP `-0.7499` edge `1.1479` maxDD `-49.7699`
- `market_context_high->index_4h` score `3.1224` n `47` status `ready` deltaP `35.5507` edge `0.0386` maxDD `-0.2323`
- `news_risk_high->crypto_alt_1h` score `2.8405` n `115` status `ready` deltaP `13.3416` edge `0.1968` maxDD `-1.5895`
- `market_context_high->equity_4h` score `2.6685` n `47` status `ready` deltaP `17.9067` edge `0.1448` maxDD `-1.3444`
- `news_risk_high->crypto_major_1h` score `2.4612` n `115` status `ready` deltaP `16.4567` edge `0.1389` maxDD `-1.8141`
- `news_risk_high->fx_4h` score `1.5862` n `109` status `ready` deltaP `23.2169` edge `0.041` maxDD `-0.421`
- `news_risk_high->crypto_major_4h` score `1.4331` n `109` status `ready` deltaP `15.1768` edge `0.2314` maxDD `-13.719`
- `news_risk_high->fx_24h` score `1.1642` n `94` status `ready` deltaP `28.5867` edge `0.1218` maxDD `-1.7159`
- `news_risk_high->metal_24h` score `1.1448` n `94` status `ready` deltaP `24.8559` edge `0.1259` maxDD `-7.2536`
- `market_context_high->index_1h` score `1.0062` n `47` status `ready` deltaP `15.0592` edge `0.0113` maxDD `-0.2275`
- `market_context_high->equity_1h` score `0.9643` n `47` status `ready` deltaP `11.3167` edge `0.0452` maxDD `-1.5564`
- `news_risk_high->commodity_24h` score `0.9167` n `94` status `ready` deltaP `15.2667` edge `0.0925` maxDD `-2.431`
- `news_risk_high->crypto_alt_4h` score `0.7179` n `109` status `ready` deltaP `7.3884` edge `0.2557` maxDD `-15.9436`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

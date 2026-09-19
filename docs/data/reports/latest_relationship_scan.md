# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T10:52:27.881216+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8522`

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

- `news_risk_high->crypto_major_24h` score `54.408` n `72` status `ready` deltaP `33.8541` edge `4.3975` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `47.6949` n `72` status `ready` deltaP `38.3681` edge `3.8567` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `36.9649` n `144` status `ready` deltaP `-2.185` edge `3.1183` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `11.093` n `72` status `ready` deltaP `43.4028` edge `0.6393` maxDD `-0.0053`
- `risk_on_high->commodity_24h` score `8.2268` n `52` status `ready` deltaP `44.9653` edge `0.3858` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2268` n `52` status `ready` deltaP `44.9653` edge `0.3858` maxDD `0.0`
- `risk_on_high->unknown_4h` score `8.2123` n `52` status `ready` deltaP `-9.076` edge `0.7674` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2123` n `52` status `ready` deltaP `-9.076` edge `0.7674` maxDD `-0.4694`
- `market_context_high->commodity_24h` score `7.0086` n `144` status `ready` deltaP `38.0209` edge `0.3831` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.6161` n `81` status `ready` deltaP `23.0974` edge `0.5183` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6971` n `81` status `ready` deltaP `20.4456` edge `0.3809` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.4294` n `88` status `ready` deltaP `19.1617` edge `0.2046` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.7001` n `52` status `ready` deltaP `32.0825` edge `0.0461` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.548` n `144` status `ready` deltaP `27.8624` edge `0.0684` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.3422` n `88` status `ready` deltaP `18.9848` edge `0.1209` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9041` n `72` status `ready` deltaP `24.4792` edge `0.0799` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1937` n `81` status `ready` deltaP `13.3883` edge `0.0321` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.0908` n `144` status `ready` deltaP `15.9598` edge `0.0222` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.6727` n `88` status `ready` deltaP `8.8527` edge `0.0376` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

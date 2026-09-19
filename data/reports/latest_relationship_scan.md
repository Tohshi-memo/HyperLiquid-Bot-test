# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-19T12:37:30.877705+00:00`
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

- `news_risk_high->crypto_major_24h` score `53.4588` n `72` status `ready` deltaP `32.6388` edge `4.3265` maxDD `-5.8019`
- `news_risk_high->crypto_alt_24h` score `46.8753` n `72` status `ready` deltaP `37.1528` edge `3.7965` maxDD `-9.3661`
- `market_context_high->unknown_4h` score `37.0129` n `144` status `ready` deltaP `-2.185` edge `3.1223` maxDD `-0.5326`
- `news_risk_high->equity_24h` score `10.667` n `72` status `ready` deltaP `42.1875` edge `0.6119` maxDD `-0.0053`
- `risk_on_high->unknown_4h` score `8.2603` n `52` status `ready` deltaP `-9.076` edge `0.7714` maxDD `-0.4694`
- `risk_on_and_context->unknown_4h` score `8.2603` n `52` status `ready` deltaP `-9.076` edge `0.7714` maxDD `-0.4694`
- `risk_on_high->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `8.2328` n `52` status `ready` deltaP `44.9653` edge `0.3863` maxDD `0.0`
- `market_context_high->commodity_24h` score `7.0146` n `144` status `ready` deltaP `38.0209` edge `0.3836` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `6.5882` n `83` status `ready` deltaP `23.5436` edge `0.513` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.6005` n `83` status `ready` deltaP `20.8584` edge `0.3701` maxDD `-8.0625`
- `news_risk_high->crypto_alt_1h` score `3.5613` n `95` status `ready` deltaP `20.7044` edge `0.2053` maxDD `-2.058`
- `risk_on_high->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `risk_on_and_context->commodity_4h` score `2.6745` n `52` status `ready` deltaP `31.7777` edge `0.046` maxDD `-0.1313`
- `market_context_high->commodity_4h` score `2.5225` n `144` status `ready` deltaP `27.5576` edge `0.0683` maxDD `-0.345`
- `news_risk_high->crypto_major_1h` score `2.4982` n `95` status `ready` deltaP `20.6949` edge `0.1225` maxDD `-2.8494`
- `news_risk_high->metal_24h` score `1.9197` n `72` status `ready` deltaP `24.4792` edge `0.0812` maxDD `-2.4203`
- `news_risk_high->fx_4h` score `1.1352` n `83` status `ready` deltaP `12.838` edge `0.0309` maxDD `-0.084`
- `market_context_high->commodity_1h` score `1.1028` n `144` status `ready` deltaP `16.1095` edge `0.0222` maxDD `-0.3491`
- `news_risk_high->equity_1h` score `0.7317` n `95` status `ready` deltaP `9.9953` edge `0.0349` maxDD `-0.9112`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T11:23:02.031021+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9354`

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

- `news_risk_high->crypto_major_24h` score `25.6235` n `94` status `ready` deltaP `8.6251` edge `2.6397` maxDD `-37.6193`
- `news_risk_high->crypto_alt_24h` score `24.1558` n `94` status `ready` deltaP `17.2651` edge `2.2587` maxDD `-23.8655`
- `market_context_high->unknown_4h` score `20.0479` n `60` status `ready` deltaP `1.4024` edge `1.6763` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `5.9211` n `57` status `ready` deltaP `31.7617` edge `0.3342` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.7988` n `101` status `ready` deltaP `22.1202` edge `0.4567` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3283` n `101` status `ready` deltaP `21.2056` edge `0.3451` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0083` n `60` status `ready` deltaP `34.2378` edge `0.1191` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.057` n `101` status `ready` deltaP `16.5308` edge `0.1911` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.289` n `60` status `ready` deltaP `29.6545` edge `0.0104` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2619` n `101` status `ready` deltaP `18.6266` edge `0.1166` maxDD `-2.8494`
- `news_risk_high->equity_24h` score `1.8943` n `94` status `ready` deltaP `19.9579` edge `0.1362` maxDD `-3.9116`
- `market_context_high->fx_24h` score `1.4584` n `57` status `ready` deltaP `17.69` edge `0.0078` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3515` n `68` status `ready` deltaP `16.5727` edge `0.0315` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `0.8855` n `94` status `ready` deltaP `21.646` edge `0.0998` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.5848` n `101` status `ready` deltaP `16.6415` edge `0.0432` maxDD `-2.0994`
- `news_risk_high->metal_24h` score `0.5343` n `94` status `ready` deltaP `18.5875` edge `0.029` maxDD `-2.4203`
- `market_context_high->fx_1h` score `0.4462` n `68` status `ready` deltaP `8.1455` edge `0.0045` maxDD `-0.063`
- `news_risk_high->equity_1h` score `0.2628` n `101` status `ready` deltaP `5.8131` edge `0.0237` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.126` n `68` status `ready` deltaP `4.9842` edge `0.0053` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

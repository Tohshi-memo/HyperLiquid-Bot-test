# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-09-20T11:37:27.663120+00:00`
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

- `news_risk_high->crypto_major_24h` score `24.537` n `95` status `ready` deltaP `8.0372` edge `2.5847` maxDD `-39.8157`
- `news_risk_high->crypto_alt_24h` score `23.0277` n `95` status `ready` deltaP `16.61` edge `2.2015` maxDD `-26.1274`
- `market_context_high->unknown_4h` score `19.6087` n `60` status `ready` deltaP `1.4024` edge `1.6397` maxDD `-0.5326`
- `market_context_high->commodity_24h` score `5.848` n `56` status `ready` deltaP `31.4485` edge `0.3302` maxDD `-0.8682`
- `news_risk_high->crypto_alt_4h` score `5.8206` n `101` status `ready` deltaP `22.2727` edge `0.4575` maxDD `-7.675`
- `news_risk_high->crypto_major_4h` score `4.3489` n `101` status `ready` deltaP `21.358` edge `0.3458` maxDD `-8.0625`
- `market_context_high->commodity_4h` score `4.0047` n `60` status `ready` deltaP `34.2378` edge `0.1188` maxDD `-0.0659`
- `news_risk_high->crypto_alt_1h` score `3.0558` n `101` status `ready` deltaP `16.5308` edge `0.191` maxDD `-2.058`
- `market_context_high->fx_4h` score `2.289` n `60` status `ready` deltaP `29.6545` edge `0.0104` maxDD `-0.0543`
- `news_risk_high->crypto_major_1h` score `2.2451` n `101` status `ready` deltaP `18.4769` edge `0.1162` maxDD `-2.8494`
- `news_risk_high->equity_24h` score `1.6086` n `95` status `ready` deltaP `19.0845` edge `0.1258` maxDD `-4.1853`
- `market_context_high->fx_24h` score `1.4794` n `56` status `ready` deltaP `17.8324` edge `0.0086` maxDD `-0.0027`
- `market_context_high->commodity_1h` score `1.3278` n `67` status `ready` deltaP `16.2615` edge `0.0316` maxDD `-0.3491`
- `news_risk_high->commodity_24h` score `0.9186` n `95` status `ready` deltaP `21.9372` edge `0.1021` maxDD `-3.4467`
- `news_risk_high->metal_1h` score `0.6173` n `101` status `ready` deltaP `14.4483` edge `0.0153` maxDD `-0.8144`
- `news_risk_high->metal_4h` score `0.586` n `101` status `ready` deltaP `16.6415` edge `0.0433` maxDD `-2.0994`
- `market_context_high->fx_1h` score `0.5109` n `67` status `ready` deltaP `8.9396` edge `0.0046` maxDD `-0.063`
- `news_risk_high->metal_24h` score `0.4758` n `95` status `ready` deltaP `17.7924` edge `0.0268` maxDD `-2.4203`
- `news_risk_high->equity_1h` score `0.2484` n `101` status `ready` deltaP `5.6634` edge `0.0235` maxDD `-0.9112`
- `market_context_high->metal_1h` score `0.1709` n `67` status `ready` deltaP `5.8182` edge `0.0055` maxDD `-0.4568`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

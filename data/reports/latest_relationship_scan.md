# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T09:37:26.268272+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11792`

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

- `risk_on_high->equity_24h` score `3.5573` n `32` status `ready` deltaP `9.375` edge `0.5715` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `3.5573` n `32` status `ready` deltaP `9.375` edge `0.5715` maxDD `-11.2348`
- `risk_on_high->crypto_major_24h` score `3.2537` n `32` status `ready` deltaP `22.2222` edge `0.3846` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.2537` n `32` status `ready` deltaP `22.2222` edge `0.3846` maxDD `-6.2481`
- `risk_on_high->commodity_24h` score `2.2332` n `32` status `ready` deltaP `19.9653` edge `0.053` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.2332` n `32` status `ready` deltaP `19.9653` edge `0.053` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.13` n `32` status `ready` deltaP `14.4055` edge `0.0997` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.13` n `32` status `ready` deltaP `14.4055` edge `0.0997` maxDD `-0.1258`
- `risk_on_high->index_24h` score `1.9825` n `32` status `ready` deltaP `16.4931` edge `0.0857` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `1.9825` n `32` status `ready` deltaP `16.4931` edge `0.0857` maxDD `-0.4355`
- `risk_on_high->fx_24h` score `1.9179` n `32` status `ready` deltaP `21.3542` edge `0.0359` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9179` n `32` status `ready` deltaP `21.3542` edge `0.0359` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.0729` n `32` status `ready` deltaP `11.8638` edge `0.0336` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.0729` n `32` status `ready` deltaP `11.8638` edge `0.0336` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8391` n `32` status `ready` deltaP `9.6799` edge `0.0195` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8391` n `32` status `ready` deltaP `9.6799` edge `0.0195` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6662` n `180` status `ready` deltaP `9.7805` edge `0.0225` maxDD `-0.5752`
- `market_context_high->commodity_4h` score `0.3964` n `180` status `ready` deltaP `7.9472` edge `0.0439` maxDD `-2.1077`
- `risk_on_high->index_1h` score `0.3381` n `32` status `ready` deltaP `10.5539` edge `0.0105` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3381` n `32` status `ready` deltaP `10.5539` edge `0.0105` maxDD `-0.3343`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-12T06:07:34.687266+00:00`
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

- `risk_on_high->equity_24h` score `4.1412` n `31` status `ready` deltaP `10.8983` edge `0.6362` maxDD `-11.2348`
- `risk_on_and_context->equity_24h` score `4.1412` n `31` status `ready` deltaP `10.8983` edge `0.6362` maxDD `-11.2348`
- `risk_on_high->crypto_major_24h` score `3.3029` n `31` status `ready` deltaP `22.3566` edge `0.39` maxDD `-6.2481`
- `risk_on_and_context->crypto_major_24h` score `3.3029` n `31` status `ready` deltaP `22.3566` edge `0.39` maxDD `-6.2481`
- `risk_on_high->index_24h` score `2.263` n `31` status `ready` deltaP `18.3188` edge `0.0969` maxDD `-0.4355`
- `risk_on_and_context->index_24h` score `2.263` n `31` status `ready` deltaP `18.3188` edge `0.0969` maxDD `-0.4355`
- `risk_on_high->commodity_24h` score `2.2377` n `31` status `ready` deltaP `19.2708` edge `0.058` maxDD `0.0`
- `risk_on_and_context->commodity_24h` score `2.2377` n `31` status `ready` deltaP `19.2708` edge `0.058` maxDD `0.0`
- `risk_on_high->commodity_4h` score `2.0704` n `32` status `ready` deltaP `13.7957` edge `0.0988` maxDD `-0.1258`
- `risk_on_and_context->commodity_4h` score `2.0704` n `32` status `ready` deltaP `13.7957` edge `0.0988` maxDD `-0.1258`
- `risk_on_high->fx_24h` score `1.9504` n `31` status `ready` deltaP `21.4157` edge `0.0382` maxDD `-0.1418`
- `risk_on_and_context->fx_24h` score `1.9504` n `31` status `ready` deltaP `21.4157` edge `0.0382` maxDD `-0.1418`
- `risk_on_high->commodity_1h` score `1.025` n `32` status `ready` deltaP `11.265` edge `0.0336` maxDD `-0.1957`
- `risk_on_and_context->commodity_1h` score `1.025` n `32` status `ready` deltaP `11.265` edge `0.0336` maxDD `-0.1957`
- `risk_on_high->fx_4h` score `0.8379` n `32` status `ready` deltaP `9.6799` edge `0.0194` maxDD `-0.1285`
- `risk_on_and_context->fx_4h` score `0.8379` n `32` status `ready` deltaP `9.6799` edge `0.0194` maxDD `-0.1285`
- `market_context_high->commodity_1h` score `0.6183` n `180` status `ready` deltaP `9.1817` edge `0.0225` maxDD `-0.5752`
- `risk_on_high->index_1h` score `0.3903` n `32` status `ready` deltaP `11.4521` edge `0.0112` maxDD `-0.3343`
- `risk_on_and_context->index_1h` score `0.3903` n `32` status `ready` deltaP `11.4521` edge `0.0112` maxDD `-0.3343`
- `market_context_high->commodity_4h` score `0.3368` n `180` status `ready` deltaP `7.3374` edge `0.043` maxDD `-2.1077`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

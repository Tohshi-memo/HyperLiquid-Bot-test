# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-19T21:06:37.553531+00:00`
- Price records: `672`
- Market context records: `1256`
- Flow alert records: `5523`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8798`

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

- `market_context_high->crypto_major_24h` score `17.9641` n `128` status `ready` deltaP `41.5798` edge `1.333` maxDD `-8.0553`
- `market_context_high->metal_24h` score `8.6409` n `128` status `ready` deltaP `3.2986` edge `0.8648` maxDD `-6.3373`
- `market_context_high->unknown_4h` score `7.9962` n `128` status `ready` deltaP `5.221` edge `0.7532` maxDD `-6.7322`
- `market_context_high->crypto_alt_24h` score `7.7473` n `128` status `ready` deltaP `22.6562` edge `0.6962` maxDD `-15.1306`
- `market_context_high->index_24h` score `4.2756` n `128` status `ready` deltaP `24.3056` edge `0.3029` maxDD `-5.3574`
- `market_context_high->equity_4h` score `3.372` n `128` status `ready` deltaP `17.8544` edge `0.2283` maxDD `-3.6396`
- `market_context_high->equity_24h` score `3.3323` n `128` status `ready` deltaP `22.3958` edge `0.5106` maxDD `-14.2815`
- `market_context_high->commodity_24h` score `3.0381` n `128` status `ready` deltaP `-9.5486` edge `0.465` maxDD `-6.8535`
- `market_context_high->unknown_24h` score `2.1558` n `128` status `ready` deltaP `1.5625` edge `0.4422` maxDD `-10.1706`
- `market_context_high->index_4h` score `1.5433` n `128` status `ready` deltaP `13.891` edge `0.1043` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.8134` n `128` status `ready` deltaP `11.0966` edge `0.0255` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.762` n `128` status `ready` deltaP `6.9563` edge `0.054` maxDD `-1.2834`
- `market_context_high->metal_4h` score `0.4483` n `128` status `ready` deltaP `16.6731` edge `0.0693` maxDD `-6.4478`
- `market_context_high->metal_1h` score `0.3912` n `128` status `ready` deltaP `11.9152` edge `0.0142` maxDD `-2.2164`
- `market_context_high->fx_24h` score `0.2224` n `128` status `ready` deltaP `4.948` edge `0.032` maxDD `-0.3831`
- `market_context_high->crypto_major_4h` score `0.0595` n `128` status `ready` deltaP `7.2218` edge `0.1516` maxDD `-8.3693`
- `market_context_high->fx_1h` score `-0.1157` n `128` status `ready` deltaP `5.5998` edge `-0.0014` maxDD `-0.3124`
- `market_context_high->crypto_alt_1h` score `-0.2798` n `128` status `ready` deltaP `0.945` edge `0.0421` maxDD `-3.4088`
- `market_context_high->crypto_major_1h` score `-0.4167` n `128` status `ready` deltaP `2.2268` edge `0.0083` maxDD `-4.1256`
- `market_context_high->crypto_alt_4h` score `-0.5754` n `128` status `ready` deltaP `8.4032` edge `0.1667` maxDD `-16.7194`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

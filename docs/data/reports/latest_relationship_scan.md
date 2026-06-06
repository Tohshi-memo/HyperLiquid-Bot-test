# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-06T02:52:24.518969+00:00`
- Price records: `672`
- Market context records: `3031`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `6987`

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

- `market_context_high->crypto_alt_24h` score `22.7568` n `99` status `ready` deltaP `10.8112` edge `2.216` maxDD `-22.6673`
- `market_context_high->unknown_24h` score `12.9271` n `99` status `ready` deltaP `22.7589` edge `0.972` maxDD `-1.7175`
- `market_context_high->commodity_24h` score `12.7445` n `99` status `ready` deltaP `42.3769` edge `0.8036` maxDD `-1.2589`
- `market_context_high->equity_24h` score `7.8439` n `99` status `ready` deltaP `21.8119` edge `1.1354` maxDD `-18.3486`
- `market_context_high->index_24h` score `7.6228` n `99` status `ready` deltaP `21.4015` edge `0.6181` maxDD `-4.7103`
- `market_context_high->commodity_4h` score `2.8439` n `121` status `ready` deltaP `19.2615` edge `0.1733` maxDD `-2.8438`
- `market_context_high->commodity_1h` score `0.0541` n `129` status `ready` deltaP `2.5902` edge `0.0295` maxDD `-1.7142`
- `market_context_high->index_4h` score `-0.0905` n `121` status `ready` deltaP `14.8798` edge `0.0883` maxDD `-11.5945`
- `market_context_high->crypto_alt_4h` score `-0.2214` n `121` status `ready` deltaP `21.0013` edge `0.3864` maxDD `-38.7172`
- `market_context_high->unknown_4h` score `-0.3986` n `121` status `ready` deltaP `1.7134` edge `0.0607` maxDD `-3.7602`
- `market_context_high->index_1h` score `-0.4006` n `129` status `ready` deltaP `3.9375` edge `0.0238` maxDD `-4.1126`
- `market_context_high->equity_1h` score `-0.4723` n `129` status `ready` deltaP `3.7182` edge `0.0362` maxDD `-6.7232`
- `market_context_high->fx_1h` score `-0.533` n `129` status `ready` deltaP `-4.7394` edge `0.0001` maxDD `-0.2801`
- `market_context_high->crypto_alt_1h` score `-0.5662` n `129` status `ready` deltaP `6.3861` edge `0.0978` maxDD `-14.7034`
- `market_context_high->equity_4h` score `-0.8393` n `121` status `ready` deltaP `11.8071` edge `0.1142` maxDD `-21.7084`
- `market_context_high->unknown_1h` score `-0.8729` n `129` status `ready` deltaP `3.6218` edge `-0.0238` maxDD `-3.1801`
- `market_context_high->crypto_major_1h` score `-0.9973` n `129` status `ready` deltaP `4.2798` edge `0.0699` maxDD `-15.1032`
- `market_context_high->fx_4h` score `-1.0522` n `121` status `ready` deltaP `-7.8512` edge `-0.0022` maxDD `-0.7619`
- `market_context_high->metal_1h` score `-1.1404` n `129` status `ready` deltaP `-1.7987` edge `-0.0024` maxDD `-6.8783`
- `market_context_high->fx_24h` score `-1.5569` n `99` status `ready` deltaP `-3.1881` edge `-0.0213` maxDD `-0.6418`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

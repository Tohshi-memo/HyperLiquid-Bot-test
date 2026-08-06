# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-06T09:22:25.499765+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11781`

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

- `market_context_high->unknown_24h` score `11.1008` n `95` status `ready` deltaP `4.3293` edge `0.9005` maxDD `-0.0103`
- `market_context_high->unknown_4h` score `4.1152` n `109` status `ready` deltaP `-0.8881` edge `0.4484` maxDD `-3.6303`
- `market_context_high->commodity_4h` score `1.0772` n `109` status `ready` deltaP `12.9895` edge `0.0878` maxDD `-2.7703`
- `market_context_high->metal_24h` score `0.9491` n `95` status `ready` deltaP `3.8267` edge `0.213` maxDD `-2.6802`
- `market_context_high->fx_24h` score `0.5617` n `95` status `ready` deltaP `21.599` edge `0.0486` maxDD `-4.3126`
- `market_context_high->commodity_1h` score `0.4215` n `109` status `ready` deltaP `7.7597` edge `0.025` maxDD `-1.3282`
- `market_context_high->fx_1h` score `0.0009` n `109` status `ready` deltaP `5.6831` edge `-0.0028` maxDD `-0.8012`
- `market_context_high->fx_4h` score `-0.2458` n `109` status `ready` deltaP `7.3325` edge `0.0056` maxDD `-1.8797`
- `market_context_high->metal_1h` score `-0.5331` n `109` status `ready` deltaP `-1.7099` edge `-0.0075` maxDD `-1.6224`
- `market_context_high->index_1h` score `-0.7245` n `109` status `ready` deltaP `-3.0572` edge `-0.0191` maxDD `-1.6054`
- `market_context_high->metal_4h` score `-0.7493` n `109` status `ready` deltaP `3.2418` edge `0.0058` maxDD `-3.211`
- `market_context_high->index_24h` score `-1.3314` n `95` status `ready` deltaP `-4.0516` edge `0.0758` maxDD `-7.8922`
- `market_context_high->crypto_alt_1h` score `-1.4869` n `109` status `ready` deltaP `-4.9882` edge `-0.0196` maxDD `-3.0178`
- `market_context_high->equity_1h` score `-1.7863` n `109` status `ready` deltaP `1.5685` edge `-0.0859` maxDD `-10.619`
- `market_context_high->index_4h` score `-2.0224` n `109` status `ready` deltaP `-11.6008` edge `-0.0565` maxDD `-4.7021`
- `market_context_high->crypto_alt_24h` score `-2.0532` n `95` status `ready` deltaP `-0.0146` edge `-0.0267` maxDD `-4.5445`
- `market_context_high->crypto_alt_4h` score `-2.1695` n `109` status `ready` deltaP `1.0796` edge `-0.049` maxDD `-5.7857`
- `market_context_high->unknown_1h` score `-2.2108` n `109` status `ready` deltaP `1.1344` edge `-0.1471` maxDD `-1.2421`
- `market_context_high->crypto_major_1h` score `-3.2587` n `109` status `ready` deltaP `-11.1493` edge `-0.0599` maxDD `-7.6533`
- `market_context_high->commodity_24h` score `-6.628` n `95` status `ready` deltaP `6.0051` edge `-0.0357` maxDD `-51.9932`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

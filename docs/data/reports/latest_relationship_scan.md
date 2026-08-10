# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T02:52:24.501597+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `88`

- Symbol pattern count: `10938`

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

- `market_context_high->commodity_4h` score `1.3834` n `161` status `ready` deltaP `15.5062` edge `0.0792` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.7805` n `173` status `ready` deltaP `10.4609` edge `0.0296` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5041` n `139` status `ready` deltaP `18.9161` edge `0.022` maxDD `-1.678`
- `market_context_high->fx_1h` score `-0.1847` n `173` status `ready` deltaP `4.0151` edge `-0.0009` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2643` n `161` status `ready` deltaP `5.7595` edge `0.003` maxDD `-1.6892`
- `market_context_high->index_1h` score `-0.5926` n `173` status `ready` deltaP `-3.4742` edge `-0.0051` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.6193` n `139` status `ready` deltaP `2.1507` edge `0.0872` maxDD `-5.9181`
- `market_context_high->metal_1h` score `-0.8062` n `173` status `ready` deltaP `-4.3724` edge `-0.0106` maxDD `-2.0884`
- `market_context_high->index_4h` score `-0.8576` n `161` status `ready` deltaP `-3.1501` edge `-0.0107` maxDD `-1.26`
- `market_context_high->equity_1h` score `-0.872` n `173` status `ready` deltaP `-2.6963` edge `-0.0068` maxDD `-4.6286`
- `market_context_high->metal_24h` score `-1.2843` n `139` status `ready` deltaP `-3.8507` edge `0.0291` maxDD `-2.503`
- `market_context_high->equity_24h` score `-1.3846` n `139` status `ready` deltaP `-1.4689` edge `0.2004` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.564` n `173` status `ready` deltaP `-9.059` edge `-0.038` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.8041` n `161` status `ready` deltaP `-7.0907` edge `-0.035` maxDD `-5.5884`
- `market_context_high->crypto_major_1h` score `-2.3446` n `173` status `ready` deltaP `-10.3068` edge `-0.0585` maxDD `-10.5372`
- `market_context_high->equity_4h` score `-2.4486` n `161` status `ready` deltaP `-6.6334` edge `-0.0943` maxDD `-7.6983`
- `market_context_high->crypto_alt_24h` score `-4.3373` n `139` status `ready` deltaP `-10.8951` edge `-0.1445` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7698` n `139` status `ready` deltaP `-1.7936` edge `-0.1361` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-6.3282` n `161` status `ready` deltaP `-12.9015` edge `-0.1674` maxDD `-15.2486`
- `market_context_high->unknown_1h` score `-7.4106` n `173` status `ready` deltaP `-4.0566` edge `-0.5448` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

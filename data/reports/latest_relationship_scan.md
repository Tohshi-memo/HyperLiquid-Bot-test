# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-07T20:07:26.938774+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11773`

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

- `market_context_high->equity_24h` score `5.1064` n `90` status `ready` deltaP `0.5727` edge `0.7277` maxDD `-21.1456`
- `market_context_high->metal_24h` score `3.5318` n `90` status `ready` deltaP `15.0172` edge `0.2518` maxDD `-2.2743`
- `market_context_high->fx_24h` score `1.6994` n `90` status `ready` deltaP `26.724` edge `0.0599` maxDD `-2.3821`
- `market_context_high->commodity_4h` score `1.4975` n `109` status `ready` deltaP `15.5977` edge `0.0881` maxDD `-2.7169`
- `market_context_high->index_24h` score `1.279` n `90` status `ready` deltaP `11.4891` edge `0.1813` maxDD `-5.7715`
- `market_context_high->commodity_1h` score `0.8497` n `112` status `ready` deltaP `11.6125` edge `0.0303` maxDD `-0.9524`
- `market_context_high->fx_1h` score `-0.1589` n `112` status `ready` deltaP `5.8062` edge `-0.0024` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2974` n `109` status `ready` deltaP `6.2514` edge `0.0047` maxDD `-1.6928`
- `market_context_high->equity_1h` score `-0.3051` n `112` status `ready` deltaP `5.3144` edge `0.022` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.3708` n `109` status `ready` deltaP `2.1551` edge `-0.0014` maxDD `-1.1743`
- `market_context_high->index_1h` score `-0.5615` n `112` status `ready` deltaP `-1.219` edge `-0.0039` maxDD `-0.7809`
- `market_context_high->metal_1h` score `-0.9301` n `112` status `ready` deltaP `-3.4538` edge `-0.0049` maxDD `-0.9664`
- `market_context_high->crypto_alt_1h` score `-0.9308` n `112` status `ready` deltaP `-5.972` edge `-0.0166` maxDD `-2.3669`
- `market_context_high->equity_4h` score `-0.9755` n `109` status `ready` deltaP `7.8205` edge `0.0003` maxDD `-7.6983`
- `market_context_high->metal_4h` score `-1.0102` n `109` status `ready` deltaP `2.9397` edge `-0.0029` maxDD `-2.7373`
- `market_context_high->crypto_major_1h` score `-2.4561` n `112` status `ready` deltaP `-7.2926` edge `-0.0493` maxDD `-5.2071`
- `market_context_high->crypto_alt_4h` score `-2.9293` n `109` status `ready` deltaP `-3.2026` edge `-0.0671` maxDD `-5.7857`
- `market_context_high->crypto_major_24h` score `-3.7769` n `90` status `ready` deltaP `4.9027` edge `-0.098` maxDD `-14.2873`
- `market_context_high->crypto_alt_24h` score `-4.869` n `90` status `ready` deltaP `-17.8121` edge `-0.1427` maxDD `-4.5445`
- `market_context_high->crypto_major_4h` score `-7.0218` n `109` status `ready` deltaP `-9.1785` edge `-0.1863` maxDD `-18.6796`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

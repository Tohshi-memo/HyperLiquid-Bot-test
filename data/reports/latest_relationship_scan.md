# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-08-10T02:37:31.428291+00:00`
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

- `market_context_high->commodity_4h` score `1.3867` n `160` status `ready` deltaP `15.4878` edge `0.0796` maxDD `-2.7169`
- `market_context_high->commodity_1h` score `0.8194` n `172` status `ready` deltaP `10.8272` edge `0.0304` maxDD `-0.7439`
- `market_context_high->fx_24h` score `0.5186` n `139` status `ready` deltaP `19.0898` edge `0.0227` maxDD `-1.678`
- `market_context_high->fx_1h` score `-0.1767` n `172` status `ready` deltaP `4.1847` edge `-0.001` maxDD `-0.9639`
- `market_context_high->fx_4h` score `-0.2705` n `160` status `ready` deltaP `5.6402` edge `0.003` maxDD `-1.6892`
- `market_context_high->index_1h` score `-0.5842` n `172` status `ready` deltaP `-3.3282` edge `-0.005` maxDD `-0.8168`
- `market_context_high->index_24h` score `-0.6205` n `139` status `ready` deltaP `2.1507` edge `0.0871` maxDD `-5.9181`
- `market_context_high->metal_1h` score `-0.8132` n `172` status `ready` deltaP `-4.5084` edge `-0.0106` maxDD `-2.0884`
- `market_context_high->equity_1h` score `-0.8575` n `172` status `ready` deltaP `-2.5066` edge `-0.0062` maxDD `-4.6286`
- `market_context_high->index_4h` score `-0.8666` n `160` status `ready` deltaP `-3.2927` edge `-0.0109` maxDD `-1.26`
- `market_context_high->metal_24h` score `-1.2819` n `139` status `ready` deltaP `-3.8507` edge `0.0293` maxDD `-2.503`
- `market_context_high->equity_24h` score `-1.444` n `139` status `ready` deltaP `-1.6425` edge `0.1966` maxDD `-21.1456`
- `market_context_high->crypto_alt_1h` score `-1.5526` n `172` status `ready` deltaP `-8.9298` edge `-0.0374` maxDD `-5.5029`
- `market_context_high->metal_4h` score `-1.7348` n `160` status `ready` deltaP `-6.753` edge `-0.034` maxDD `-5.4715`
- `market_context_high->crypto_major_1h` score `-2.3408` n `172` status `ready` deltaP `-10.2179` edge `-0.0586` maxDD `-10.5372`
- `market_context_high->equity_4h` score `-2.401` n `160` status `ready` deltaP `-6.4482` edge `-0.0936` maxDD `-7.6983`
- `market_context_high->crypto_alt_24h` score `-4.3241` n `139` status `ready` deltaP `-10.8951` edge `-0.1434` maxDD `-4.5445`
- `market_context_high->crypto_major_24h` score `-4.7722` n `139` status `ready` deltaP `-1.7936` edge `-0.1363` maxDD `-14.2873`
- `market_context_high->crypto_alt_4h` score `-6.276` n `160` status `ready` deltaP `-12.622` edge `-0.1665` maxDD `-15.1214`
- `market_context_high->unknown_1h` score `-7.456` n `172` status `ready` deltaP `-4.3692` edge `-0.5465` maxDD `-1.323`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

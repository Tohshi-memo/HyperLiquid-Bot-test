# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T02:52:25.332457+00:00`
- Price records: `672`
- Market context records: `5620`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8743`

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

- `market_context_high->equity_24h` score `3.0943` n `174` status `ready` deltaP `15.0084` edge `0.6657` maxDD `-31.6316`
- `market_context_high->fx_24h` score `1.3256` n `174` status `ready` deltaP `22.1325` edge `0.0603` maxDD `-1.457`
- `market_context_high->crypto_major_4h` score `1.0452` n `232` status `ready` deltaP `12.1426` edge `0.2354` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4081` n `232` status `ready` deltaP `6.5812` edge `0.154` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.33` n `232` status `ready` deltaP `6.9123` edge `0.1455` maxDD `-9.46`
- `market_context_high->fx_1h` score `-0.2797` n `237` status `ready` deltaP `1.5993` edge `0.0011` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.3391` n `237` status `ready` deltaP `5.7651` edge `0.034` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.5083` n `237` status `ready` deltaP `0.2924` edge `0.0004` maxDD `-2.0682`
- `market_context_high->crypto_major_1h` score `-0.5306` n `237` status `ready` deltaP `4.8795` edge `0.0478` maxDD `-6.9639`
- `market_context_high->crypto_alt_1h` score `-0.6141` n `237` status `ready` deltaP `1.137` edge `0.0374` maxDD `-5.0257`
- `market_context_high->index_1h` score `-0.9298` n `237` status `ready` deltaP `0.5786` edge `0.0055` maxDD `-0.9472`
- `market_context_high->commodity_1h` score `-1.0824` n `237` status `ready` deltaP `-1.1774` edge `-0.0058` maxDD `-3.7906`
- `market_context_high->fx_4h` score `-1.3199` n `232` status `ready` deltaP `1.0093` edge `0.0066` maxDD `-1.2706`
- `market_context_high->index_4h` score `-1.8195` n `232` status `ready` deltaP `0.0211` edge `0.0098` maxDD `-2.9255`
- `market_context_high->index_24h` score `-2.3832` n `174` status `ready` deltaP `10.0874` edge `0.0259` maxDD `-16.8946`
- `market_context_high->crypto_major_24h` score `-2.6093` n `174` status `ready` deltaP `7.7227` edge `0.1851` maxDD `-29.6555`
- `market_context_high->metal_4h` score `-2.8607` n `232` status `ready` deltaP `-11.1753` edge `-0.0539` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-4.1169` n `232` status `ready` deltaP `-5.3879` edge `-0.0396` maxDD `-14.071`
- `market_context_high->metal_24h` score `-8.2732` n `174` status `ready` deltaP `-10.9315` edge `-0.2517` maxDD `-32.8874`
- `market_context_high->crypto_alt_24h` score `-12.431` n `174` status `ready` deltaP `-2.4904` edge `-0.1496` maxDD `-54.2437`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

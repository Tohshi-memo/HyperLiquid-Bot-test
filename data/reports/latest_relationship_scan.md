# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-17T14:07:13.533450+00:00`
- Price records: `672`
- Market context records: `1018`
- Flow alert records: `4842`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8634`

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

- `market_context_high->crypto_major_24h` score `13.6235` n `194` status `ready` deltaP `32.4662` edge `0.9777` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `4.3884` n `194` status `ready` deltaP `11.1305` edge `0.4149` maxDD `-9.5387`
- `market_context_high->equity_24h` score `0.9879` n `194` status `ready` deltaP `7.7159` edge `0.2088` maxDD `-7.5666`
- `market_context_high->index_24h` score `0.6974` n `194` status `ready` deltaP `7.0452` edge `0.1714` maxDD `-4.4871`
- `market_context_high->fx_1h` score `-0.1631` n `194` status `ready` deltaP `3.6237` edge `0.0005` maxDD `-0.3124`
- `market_context_high->commodity_1h` score `-0.4665` n `194` status `ready` deltaP `2.6113` edge `0.0245` maxDD `-3.7959`
- `market_context_high->equity_1h` score `-0.7829` n `194` status `ready` deltaP `-0.8365` edge `0.0172` maxDD `-4.4826`
- `market_context_high->index_1h` score `-0.7956` n `194` status `ready` deltaP `1.9738` edge `0.0049` maxDD `-2.7485`
- `market_context_high->fx_4h` score `-0.875` n `194` status `ready` deltaP `3.5139` edge `0.0033` maxDD `-1.6381`
- `market_context_high->crypto_major_1h` score `-1.2227` n `194` status `ready` deltaP `4.8213` edge `-0.0166` maxDD `-11.4508`
- `market_context_high->crypto_alt_1h` score `-1.3188` n `194` status `ready` deltaP `-0.9167` edge `-0.019` maxDD `-8.1842`
- `market_context_high->equity_4h` score `-1.3348` n `194` status `ready` deltaP `2.2614` edge `0.0889` maxDD `-10.5498`
- `market_context_high->index_4h` score `-1.4511` n `194` status `ready` deltaP `-0.1634` edge `0.0278` maxDD `-6.1444`
- `market_context_high->metal_1h` score `-1.7858` n `194` status `ready` deltaP `0.3473` edge `-0.0397` maxDD `-8.6583`
- `market_context_high->crypto_major_4h` score `-2.7276` n `194` status `ready` deltaP `7.7398` edge `0.0917` maxDD `-22.648`
- `market_context_high->crypto_alt_4h` score `-2.7306` n `194` status `ready` deltaP `0.4887` edge `0.047` maxDD `-15.2248`
- `market_context_high->fx_24h` score `-3.2871` n `194` status `ready` deltaP `0.9621` edge `-0.0202` maxDD `-19.2774`
- `market_context_high->commodity_4h` score `-3.297` n `194` status `ready` deltaP `-2.8178` edge `0.0608` maxDD `-13.0076`
- `market_context_high->metal_4h` score `-4.2814` n `194` status `ready` deltaP `-2.5034` edge `-0.1621` maxDD `-22.9424`
- `market_context_high->metal_24h` score `-5.7438` n `194` status `ready` deltaP `-8.7164` edge `0.2478` maxDD `-43.1341`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

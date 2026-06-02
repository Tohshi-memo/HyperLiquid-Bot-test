# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-06-02T07:52:23.151813+00:00`
- Price records: `672`
- Market context records: `2643`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9216`

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

- `market_context_high->unknown_24h` score `7.609` n `134` status `ready` deltaP `17.8664` edge `0.5478` maxDD `-1.626`
- `market_context_high->crypto_alt_4h` score `5.3393` n `134` status `ready` deltaP `24.8908` edge `0.5469` maxDD `-15.4319`
- `market_context_high->crypto_alt_24h` score `4.1931` n `134` status `ready` deltaP `7.1854` edge `0.7682` maxDD `-29.3342`
- `market_context_high->crypto_major_4h` score `3.876` n `134` status `ready` deltaP `15.84` edge `0.3984` maxDD `-10.1468`
- `market_context_high->index_24h` score `1.1745` n `134` status `ready` deltaP `11.5879` edge `0.1187` maxDD `-2.5127`
- `market_context_high->unknown_4h` score `1.1005` n `134` status `ready` deltaP `6.837` edge `0.1511` maxDD `-3.7312`
- `market_context_high->crypto_alt_1h` score `1.0899` n `134` status `ready` deltaP `9.9987` edge `0.1429` maxDD `-6.1656`
- `market_context_high->crypto_major_1h` score `0.5547` n `134` status `ready` deltaP `7.1611` edge `0.1179` maxDD `-4.2199`
- `market_context_high->index_4h` score `0.5168` n `134` status `ready` deltaP `11.2669` edge `0.0521` maxDD `-2.3986`
- `market_context_high->unknown_1h` score `0.0287` n `134` status `ready` deltaP `3.1258` edge `0.0357` maxDD `-1.665`
- `market_context_high->index_1h` score `-0.2205` n `134` status `ready` deltaP `2.9739` edge `0.0112` maxDD `-1.2855`
- `market_context_high->metal_4h` score `-0.2885` n `134` status `ready` deltaP `4.5573` edge `0.0272` maxDD `-2.5301`
- `market_context_high->commodity_1h` score `-0.3112` n `134` status `ready` deltaP `6.1198` edge `0.0211` maxDD `-4.3601`
- `market_context_high->fx_1h` score `-0.4308` n `134` status `ready` deltaP `0.7396` edge `0.0038` maxDD `-0.2373`
- `market_context_high->metal_1h` score `-0.4712` n `134` status `ready` deltaP `-0.2972` edge `0.0055` maxDD `-2.114`
- `market_context_high->fx_24h` score `-0.6778` n `134` status `ready` deltaP `4.8741` edge `-0.0005` maxDD `-0.745`
- `market_context_high->fx_4h` score `-0.9188` n `134` status `ready` deltaP `-0.6416` edge `0.0108` maxDD `-0.6474`
- `market_context_high->equity_1h` score `-1.0151` n `134` status `ready` deltaP `-2.27` edge `0.0144` maxDD `-2.7085`
- `market_context_high->commodity_4h` score `-1.1308` n `134` status `ready` deltaP `3.9884` edge `0.0227` maxDD `-10.2078`
- `market_context_high->equity_4h` score `-1.3298` n `134` status `ready` deltaP `2.3298` edge `0.0141` maxDD `-5.9024`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

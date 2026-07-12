# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-12T09:52:29.539356+00:00`
- Price records: `672`
- Market context records: `6486`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5869`

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

- `news_risk_high->crypto_alt_24h` score `12.6703` n `32` status `ready` deltaP `34.2014` edge `0.8426` maxDD `-0.5131`
- `news_risk_high->fx_24h` score `6.483` n `32` status `ready` deltaP `53.9931` edge `0.1803` maxDD `0.0`
- `market_context_high->unknown_24h` score `6.465` n `159` status `ready` deltaP `15.9723` edge `0.7623` maxDD `-15.0689`
- `news_risk_high->crypto_major_24h` score `4.4256` n `32` status `ready` deltaP `17.3611` edge `0.5296` maxDD `-4.2368`
- `news_risk_high->fx_4h` score `3.9788` n `38` status `ready` deltaP `42.37` edge `0.0537` maxDD `-0.0345`
- `news_risk_high->commodity_24h` score `3.0069` n `32` status `ready` deltaP `28.4722` edge `0.0813` maxDD `-0.3101`
- `market_context_high->unknown_1h` score `2.835` n `180` status `ready` deltaP `-3.8922` edge `0.3523` maxDD `-3.2083`
- `news_risk_high->fx_1h` score `1.855` n `38` status `ready` deltaP `23.2115` edge `0.0179` maxDD `-0.1113`
- `news_risk_high->crypto_major_1h` score `0.5777` n `38` status `ready` deltaP `5.0504` edge `0.0941` maxDD `-2.6299`
- `market_context_high->index_4h` score `0.5495` n `169` status `ready` deltaP `12.694` edge `0.0288` maxDD `-0.4108`
- `market_context_high->commodity_24h` score `0.4138` n `159` status `ready` deltaP `6.9903` edge `0.1747` maxDD `-5.2791`
- `market_context_high->crypto_alt_4h` score `0.3572` n `169` status `ready` deltaP `9.2158` edge `0.1237` maxDD `-6.7632`
- `market_context_high->unknown_4h` score `0.2877` n `169` status `ready` deltaP `-15.6986` edge `0.3692` maxDD `-10.5788`
- `market_context_high->metal_4h` score `0.1792` n `169` status `ready` deltaP `11.9336` edge `0.0442` maxDD `-2.7056`
- `news_risk_high->crypto_alt_1h` score `0.0804` n `38` status `ready` deltaP `1.5837` edge `0.0507` maxDD `-2.0756`
- `market_context_high->equity_4h` score `-0.4358` n `169` status `ready` deltaP `8.7323` edge `0.0558` maxDD `-8.2573`
- `news_risk_high->index_24h` score `-0.4532` n `32` status `ready` deltaP `4.6875` edge `-0.0022` maxDD `-2.3058`
- `market_context_high->crypto_alt_1h` score `-0.5322` n `180` status `ready` deltaP `6.7299` edge `0.0182` maxDD `-5.8368`
- `market_context_high->metal_1h` score `-0.5749` n `180` status `ready` deltaP `0.4291` edge `0.0012` maxDD `-1.8877`
- `market_context_high->crypto_major_1h` score `-0.5787` n `180` status `ready` deltaP `6.6001` edge `0.0084` maxDD `-6.7936`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

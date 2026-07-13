# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-13T14:52:30.892767+00:00`
- Price records: `672`
- Market context records: `6613`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `80`

- Symbol pattern count: `9810`

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

- `market_context_high->unknown_24h` score `3.0292` n `174` status `ready` deltaP `1.1435` edge `0.536` maxDD `-13.2952`
- `market_context_high->unknown_1h` score `2.0596` n `206` status `ready` deltaP `-6.129` edge `0.3026` maxDD `-3.2083`
- `market_context_high->commodity_24h` score `0.2039` n `174` status `ready` deltaP `7.4415` edge `0.1542` maxDD `-5.2791`
- `market_context_high->fx_1h` score `-0.2611` n `206` status `ready` deltaP `2.5129` edge `0.0005` maxDD `-0.7249`
- `market_context_high->crypto_major_1h` score `-0.4318` n `206` status `ready` deltaP `7.0548` edge `0.0242` maxDD `-6.7936`
- `market_context_high->commodity_1h` score `-0.5364` n `206` status `ready` deltaP `0.4404` edge `-0.0034` maxDD `-2.1314`
- `market_context_high->index_1h` score `-0.5552` n `206` status `ready` deltaP `-0.4084` edge `0.0035` maxDD `-0.7564`
- `market_context_high->crypto_alt_1h` score `-0.7007` n `206` status `ready` deltaP `4.1785` edge `0.0136` maxDD `-5.8368`
- `market_context_high->index_4h` score `-0.8616` n `206` status `ready` deltaP `10.1261` edge `0.01` maxDD `-5.7046`
- `market_context_high->equity_1h` score `-1.1696` n `206` status `ready` deltaP `1.8284` edge `0.0007` maxDD `-4.1619`
- `market_context_high->commodity_4h` score `-1.1995` n `206` status `ready` deltaP `0.0888` edge `-0.0049` maxDD `-5.6246`
- `market_context_high->metal_1h` score `-1.3002` n `206` status `ready` deltaP `-3.9882` edge `-0.0016` maxDD `-2.0797`
- `market_context_high->fx_4h` score `-1.6136` n `206` status `ready` deltaP `2.2703` edge `-0.0008` maxDD `-3.3635`
- `market_context_high->unknown_4h` score `-1.6178` n `206` status `ready` deltaP `-18.1417` edge `0.2267` maxDD `-10.5788`
- `market_context_high->crypto_major_4h` score `-1.7192` n `206` status `ready` deltaP `7.4621` edge `0.0613` maxDD `-16.8495`
- `market_context_high->crypto_alt_4h` score `-2.0834` n `206` status `ready` deltaP `4.4814` edge `0.0432` maxDD `-19.2145`
- `market_context_high->metal_4h` score `-2.1493` n `206` status `ready` deltaP `-1.2003` edge `0.0185` maxDD `-5.2172`
- `market_context_high->equity_4h` score `-3.0212` n `206` status `ready` deltaP `8.1118` edge `-0.0145` maxDD `-27.1529`
- `market_context_high->metal_24h` score `-3.7909` n `174` status `ready` deltaP `-1.2747` edge `0.0494` maxDD `-13.1534`
- `market_context_high->fx_24h` score `-5.8538` n `174` status `ready` deltaP `-7.33` edge `-0.0013` maxDD `-9.3453`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-18T05:07:13.342435+00:00`
- Price records: `672`
- Market context records: `1086`
- Flow alert records: `5030`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8786`

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

- `market_context_high->crypto_major_24h` score `16.552` n `156` status `ready` deltaP `35.533` edge `1.1888` maxDD `-3.3749`
- `market_context_high->crypto_alt_24h` score `5.8049` n `156` status `ready` deltaP `12.2015` edge `0.5258` maxDD `-9.5387`
- `market_context_high->equity_24h` score `5.5896` n `156` status `ready` deltaP `14.8138` edge `0.4167` maxDD `-3.6396`
- `market_context_high->metal_24h` score `4.6746` n `156` status `ready` deltaP `-2.7046` edge `0.5743` maxDD `-6.3373`
- `market_context_high->index_24h` score `4.5985` n `156` status `ready` deltaP `14.9412` edge `0.3144` maxDD `-2.1308`
- `market_context_high->equity_4h` score `1.8451` n `162` status `ready` deltaP `10.1927` edge `0.1563` maxDD `-3.6396`
- `market_context_high->crypto_major_4h` score `1.208` n `162` status `ready` deltaP `12.0709` edge `0.1888` maxDD `-6.4882`
- `market_context_high->index_4h` score `0.9083` n `162` status `ready` deltaP `7.7086` edge `0.0926` maxDD `-2.1308`
- `market_context_high->index_1h` score `0.6604` n `174` status `ready` deltaP `8.7187` edge `0.0286` maxDD `-0.5353`
- `market_context_high->equity_1h` score `0.509` n `174` status `ready` deltaP `3.2228` edge `0.0587` maxDD `-1.3546`
- `market_context_high->crypto_major_1h` score `0.1895` n `174` status `ready` deltaP `7.5246` edge `0.0422` maxDD `-4.1256`
- `market_context_high->fx_1h` score `0.0417` n `174` status `ready` deltaP `7.177` edge `0.0012` maxDD `-0.3124`
- `market_context_high->metal_1h` score `-0.1199` n `174` status `ready` deltaP `7.0566` edge `0.004` maxDD `-2.2164`
- `market_context_high->crypto_alt_1h` score `-0.2047` n `174` status `ready` deltaP `3.333` edge `0.045` maxDD `-3.4088`
- `market_context_high->crypto_alt_4h` score `-0.3678` n `162` status `ready` deltaP `7.5731` edge `0.1693` maxDD `-13.0347`
- `market_context_high->fx_4h` score `-0.6301` n `162` status `ready` deltaP `2.5143` edge `0.0021` maxDD `-1.6381`
- `market_context_high->commodity_1h` score `-0.6624` n `174` status `ready` deltaP `-0.8019` edge `0.0012` maxDD `-3.7959`
- `market_context_high->metal_4h` score `-1.8429` n `162` status `ready` deltaP `5.2111` edge `-0.0756` maxDD `-9.2991`
- `market_context_high->unknown_4h` score `-2.0675` n `162` status `ready` deltaP `8.6645` edge `-0.1084` maxDD `-6.7322`
- `market_context_high->fx_24h` score `-3.1202` n `156` status `ready` deltaP `4.5618` edge `-0.0228` maxDD `-19.2774`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

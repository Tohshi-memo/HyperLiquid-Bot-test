# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-22T04:07:17.617982+00:00`
- Price records: `672`
- Market context records: `1491`
- Flow alert records: `6202`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `8810`

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

- `market_context_high->metal_24h` score `11.888` n `172` status `ready` deltaP `18.8671` edge `0.9941` maxDD `-6.3373`
- `market_context_high->crypto_alt_24h` score `11.7588` n `172` status `ready` deltaP `28.985` edge `0.9883` maxDD `-15.1306`
- `market_context_high->crypto_major_24h` score `10.7072` n `172` status `ready` deltaP `27.3538` edge `0.8231` maxDD `-8.0553`
- `market_context_high->index_24h` score `3.9626` n `172` status `ready` deltaP `20.3327` edge `0.3033` maxDD `-5.3574`
- `market_context_high->equity_24h` score `3.5001` n `172` status `ready` deltaP `13.6144` edge `0.4336` maxDD `-14.2815`
- `market_context_high->equity_4h` score `1.4161` n `203` status `ready` deltaP `7.441` edge `0.1514` maxDD `-3.6396`
- `market_context_high->fx_24h` score `0.835` n `172` status `ready` deltaP `18.2089` edge `0.0531` maxDD `-1.3925`
- `market_context_high->crypto_alt_4h` score `-0.0097` n `203` status `ready` deltaP `11.1671` edge `0.2567` maxDD `-19.5565`
- `market_context_high->equity_1h` score `-0.0636` n `203` status `ready` deltaP `2.3871` edge `0.0388` maxDD `-2.8014`
- `market_context_high->index_1h` score `-0.1892` n `203` status `ready` deltaP `2.8554` edge `0.0117` maxDD `-1.7205`
- `market_context_high->crypto_alt_1h` score `-0.526` n `203` status `ready` deltaP `1.4299` edge `0.049` maxDD `-4.1892`
- `market_context_high->fx_1h` score `-0.5374` n `203` status `ready` deltaP `-0.3717` edge `-0.0032` maxDD `-0.3914`
- `market_context_high->crypto_major_4h` score `-0.6104` n `203` status `ready` deltaP `7.0385` edge `0.1731` maxDD `-13.3376`
- `market_context_high->metal_1h` score `-0.727` n `203` status `ready` deltaP `6.0566` edge `0.0` maxDD `-6.3532`
- `market_context_high->index_4h` score `-0.824` n `203` status `ready` deltaP `-1.1804` edge `0.0481` maxDD `-3.7119`
- `market_context_high->fx_4h` score `-0.9846` n `203` status `ready` deltaP `-3.6352` edge `-0.0091` maxDD `-1.4313`
- `market_context_high->commodity_1h` score `-1.1098` n `203` status `ready` deltaP `-0.2028` edge `0.001` maxDD `-4.7041`
- `market_context_high->metal_4h` score `-1.3631` n `203` status `ready` deltaP `10.4387` edge `0.086` maxDD `-12.5349`
- `market_context_high->crypto_major_1h` score `-1.581` n `203` status `ready` deltaP `-1.2699` edge `0.0124` maxDD `-6.1883`
- `market_context_high->commodity_4h` score `-4.237` n `203` status `ready` deltaP `-13.5709` edge `-0.0811` maxDD `-17.3969`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

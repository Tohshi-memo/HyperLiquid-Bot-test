# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-27T03:52:27.842497+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `9688`

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

- `market_context_high->unknown_4h` score `90.4718` n `151` status `ready` deltaP `1.9464` edge `7.5599` maxDD `-1.0178`
- `market_context_high->unknown_1h` score `17.6407` n `151` status `ready` deltaP `1.2581` edge `1.5106` maxDD `-1.5807`
- `market_context_high->fx_4h` score `0.3202` n `151` status `ready` deltaP `11.5843` edge `0.0093` maxDD `-0.4545`
- `market_context_high->fx_1h` score `0.3101` n `151` status `ready` deltaP `8.8135` edge `0.0029` maxDD `-0.1986`
- `market_context_high->metal_24h` score `0.1334` n `121` status `ready` deltaP `21.5234` edge `0.1278` maxDD `-6.3348`
- `market_context_high->index_24h` score `0.1251` n `121` status `ready` deltaP `17.6017` edge `0.0149` maxDD `-3.9636`
- `market_context_high->metal_1h` score `-0.0627` n `151` status `ready` deltaP `9.1813` edge `0.0078` maxDD `-1.4974`
- `market_context_high->commodity_1h` score `-0.1504` n `151` status `ready` deltaP `3.1705` edge `0.0164` maxDD `-1.0053`
- `market_context_high->fx_24h` score `-0.1545` n `121` status `ready` deltaP `16.8025` edge `0.0254` maxDD `-1.2451`
- `market_context_high->commodity_4h` score `-0.3103` n `151` status `ready` deltaP `7.1162` edge `0.0496` maxDD `-1.165`
- `market_context_high->index_1h` score `-0.6247` n `151` status `ready` deltaP `-0.6712` edge `-0.0019` maxDD `-1.8971`
- `market_context_high->metal_4h` score `-0.8629` n `151` status `ready` deltaP `8.4578` edge `-0.0005` maxDD `-4.9875`
- `market_context_high->crypto_major_1h` score `-0.8828` n `151` status `ready` deltaP `4.6496` edge `0.0139` maxDD `-9.3126`
- `market_context_high->equity_1h` score `-1.8075` n `151` status `ready` deltaP `1.2115` edge `-0.0122` maxDD `-12.2088`
- `market_context_high->crypto_alt_1h` score `-2.0001` n `151` status `ready` deltaP `-0.2806` edge `-0.0061` maxDD `-13.2099`
- `market_context_high->index_4h` score `-3.521` n `151` status `ready` deltaP `-7.316` edge `-0.027` maxDD `-6.7447`
- `market_context_high->crypto_major_24h` score `-4.1292` n `121` status `ready` deltaP `-0.1003` edge `-0.043` maxDD `-29.1905`
- `market_context_high->crypto_major_4h` score `-4.5583` n `151` status `ready` deltaP `-0.5885` edge `-0.0884` maxDD `-32.0325`
- `market_context_high->equity_24h` score `-5.2278` n `121` status `ready` deltaP `-4.3127` edge `-0.16` maxDD `-30.5188`
- `market_context_high->commodity_24h` score `-5.6081` n `121` status `ready` deltaP `-9.3101` edge `-0.0979` maxDD `-24.0547`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

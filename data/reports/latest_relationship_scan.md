# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-05-08T02:22:10.879896+00:00`
- Price records: `605`
- Market context records: `709`
- Flow alert records: `2003`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `901`

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

- `market_context_high->crypto_major_24h` score `11.0214` n `146` status `ready` deltaP `26.7513` edge `0.7735` maxDD `-1.3382`
- `market_context_high->crypto_alt_24h` score `6.5025` n `146` status `ready` deltaP `8.156` edge `0.4923` maxDD `-0.0508`
- `market_context_high->fx_4h` score `-0.2407` n `149` status `ready` deltaP `6.7779` edge `0.0111` maxDD `-1.6381`
- `market_context_high->fx_1h` score `-0.2901` n `149` status `ready` deltaP `2.7767` edge `0.0021` maxDD `-0.291`
- `market_context_high->commodity_1h` score `-0.464` n `149` status `ready` deltaP `2.4271` edge `0.0426` maxDD `-3.7959`
- `market_context_high->index_1h` score `-0.6315` n `149` status `ready` deltaP `0.2687` edge `0.0026` maxDD `-2.8282`
- `market_context_high->index_24h` score `-0.9579` n `146` status `ready` deltaP `-2.5376` edge `0.1366` maxDD `-5.9609`
- `market_context_high->crypto_major_4h` score `-1.1086` n `149` status `ready` deltaP `16.48` edge `0.1186` maxDD `-22.648`
- `market_context_high->equity_1h` score `-1.1874` n `149` status `ready` deltaP `-1.7425` edge `-0.0063` maxDD `-4.4826`
- `market_context_high->unknown_1h` score `-1.1894` n `149` status `ready` deltaP `-4.2569` edge `-0.0104` maxDD `-2.1602`
- `market_context_high->crypto_alt_1h` score `-1.3288` n `149` status `ready` deltaP `4.8509` edge `-0.0116` maxDD `-8.1842`
- `market_context_high->crypto_major_1h` score `-1.5773` n `149` status `ready` deltaP `6.3094` edge `-0.0012` maxDD `-11.4508`
- `market_context_high->index_4h` score `-1.7317` n `149` status `ready` deltaP `2.049` edge `-0.0057` maxDD `-6.5149`
- `market_context_high->crypto_alt_4h` score `-1.9731` n `149` status `ready` deltaP `3.9083` edge `0.0665` maxDD `-15.2248`
- `market_context_high->equity_24h` score `-2.0293` n `146` status `ready` deltaP `-4.4595` edge `0.1211` maxDD `-10.5047`
- `market_context_high->equity_4h` score `-2.6527` n `149` status `ready` deltaP `-1.0279` edge `0.001` maxDD `-10.5498`
- `market_context_high->metal_1h` score `-3.3957` n `149` status `ready` deltaP `-5.2273` edge `-0.0522` maxDD `-9.0076`
- `market_context_high->commodity_4h` score `-3.7843` n `149` status `ready` deltaP `-6.3098` edge `0.0768` maxDD `-13.0076`
- `market_context_high->unknown_4h` score `-4.2544` n `149` status `ready` deltaP `3.1631` edge `-0.1878` maxDD `-8.3588`
- `market_context_high->fx_24h` score `-5.0682` n `146` status `ready` deltaP `-12.223` edge `-0.0511` maxDD `-21.0414`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

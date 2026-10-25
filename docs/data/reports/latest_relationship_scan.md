# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-10-25T23:22:29.423323+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `5062`

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

- `market_context_high->unknown_4h` score `29.7237` n `113` status `ready` deltaP `-0.7487` edge `2.5155` maxDD `-1.016`
- `market_context_high->crypto_major_24h` score `0.7332` n `84` status `ready` deltaP `7.9117` edge `0.1109` maxDD `-4.5369`
- `market_context_high->fx_1h` score `-0.0747` n `113` status `ready` deltaP `3.41` edge `0.0026` maxDD `-0.1258`
- `market_context_high->fx_4h` score `-0.1108` n `113` status `ready` deltaP `6.3917` edge `0.008` maxDD `-0.4545`
- `market_context_high->fx_24h` score `-0.2514` n `84` status `ready` deltaP `15.6002` edge `0.021` maxDD `-1.2451`
- `market_context_high->commodity_1h` score `-0.4487` n `113` status `ready` deltaP `0.2663` edge `0.0109` maxDD `-1.0053`
- `market_context_high->metal_24h` score `-0.6111` n `84` status `ready` deltaP `12.252` edge `0.107` maxDD `-7.3625`
- `market_context_high->index_1h` score `-0.6705` n `113` status `ready` deltaP `-2.1859` edge `-0.0062` maxDD `-1.2155`
- `market_context_high->metal_1h` score `-0.6958` n `113` status `ready` deltaP `4.0353` edge `-0.0057` maxDD `-1.6682`
- `market_context_high->commodity_4h` score `-0.7362` n `113` status `ready` deltaP `-1.0186` edge `0.0353` maxDD `-1.165`
- `market_context_high->index_24h` score `-0.9325` n `84` status `ready` deltaP `9.8959` edge `-0.0573` maxDD `-4.925`
- `market_context_high->crypto_major_1h` score `-1.3231` n `113` status `ready` deltaP `3.3967` edge `-0.0342` maxDD `-9.3126`
- `market_context_high->metal_4h` score `-2.0278` n `113` status `ready` deltaP `3.3941` edge `-0.0206` maxDD `-5.3474`
- `market_context_high->index_4h` score `-2.1783` n `113` status `ready` deltaP `-8.2249` edge `-0.037` maxDD `-4.3282`
- `market_context_high->commodity_24h` score `-2.5316` n `84` status `ready` deltaP `-7.6885` edge `-0.0414` maxDD `-7.5526`
- `market_context_high->crypto_alt_1h` score `-3.2075` n `113` status `ready` deltaP `-1.7103` edge `-0.0685` maxDD `-11.3243`
- `market_context_high->equity_1h` score `-3.8967` n `113` status `ready` deltaP `-0.6889` edge `-0.0928` maxDD `-12.1865`
- `market_context_high->crypto_alt_24h` score `-7.0389` n `84` status `ready` deltaP `-4.2411` edge `-0.2285` maxDD `-42.3182`
- `market_context_high->equity_24h` score `-7.7301` n `84` status `ready` deltaP `-1.0912` edge `-0.4554` maxDD `-36.6024`
- `market_context_high->crypto_major_4h` score `-10.049` n `113` status `ready` deltaP `-13.2001` edge `-0.2496` maxDD `-32.9851`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

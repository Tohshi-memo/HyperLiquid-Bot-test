# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-03T00:52:28.041712+00:00`
- Price records: `672`
- Market context records: `5509`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `96`

- Symbol pattern count: `11468`

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

- `market_context_high->crypto_major_24h` score `2.8164` n `190` status `ready` deltaP `16.2189` edge `0.5806` maxDD `-29.6555`
- `market_context_high->equity_24h` score `2.631` n `190` status `ready` deltaP `11.272` edge `0.652` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `2.4257` n `193` status `ready` deltaP `14.1887` edge `0.3368` maxDD `-14.0065`
- `market_context_high->equity_4h` score `2.1912` n `193` status `ready` deltaP `11.2299` edge `0.2716` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `1.9083` n `193` status `ready` deltaP `9.6463` edge `0.2588` maxDD `-9.46`
- `market_context_high->equity_1h` score `0.4859` n `193` status `ready` deltaP `8.5834` edge `0.0798` maxDD `-5.0555`
- `market_context_high->fx_24h` score `0.3838` n `190` status `ready` deltaP `12.9312` edge `0.0385` maxDD `-1.0847`
- `market_context_high->index_1h` score `0.1356` n `193` status `ready` deltaP `6.5457` edge `0.017` maxDD `-0.9472`
- `market_context_high->crypto_alt_1h` score `-0.3143` n `193` status `ready` deltaP `1.134` edge `0.0624` maxDD `-5.0257`
- `market_context_high->fx_1h` score `-0.3572` n `193` status `ready` deltaP `0.4778` edge `-0.0001` maxDD `-0.577`
- `market_context_high->crypto_major_1h` score `-0.4535` n `193` status `ready` deltaP `2.7233` edge `0.0686` maxDD `-6.9639`
- `market_context_high->metal_1h` score `-0.5906` n `193` status `ready` deltaP `1.065` edge `0.0112` maxDD `-2.0682`
- `market_context_high->fx_4h` score `-0.809` n `193` status `ready` deltaP `3.6712` edge `0.0062` maxDD `-1.5143`
- `market_context_high->index_4h` score `-0.9718` n `193` status `ready` deltaP `6.1418` edge `0.039` maxDD `-2.874`
- `market_context_high->commodity_1h` score `-1.4979` n `193` status `ready` deltaP `-3.1259` edge `-0.0092` maxDD `-3.5831`
- `market_context_high->index_24h` score `-1.8209` n `190` status `ready` deltaP `14.2708` edge `0.0701` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9417` n `193` status `ready` deltaP `-11.3231` edge `-0.0492` maxDD `-12.8631`
- `market_context_high->commodity_4h` score `-4.5345` n `193` status `ready` deltaP `-8.6385` edge `-0.053` maxDD `-14.0497`
- `market_context_high->crypto_alt_24h` score `-7.2854` n `190` status `ready` deltaP `7.2442` edge `0.2143` maxDD `-54.2437`
- `market_context_high->metal_24h` score `-7.2962` n `190` status `ready` deltaP `-4.2379` edge `-0.1694` maxDD `-33.021`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

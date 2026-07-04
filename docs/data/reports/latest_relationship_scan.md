# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-07-04T13:07:25.036029+00:00`
- Price records: `672`
- Market context records: `5665`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `72`

- Symbol pattern count: `8670`

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

- `market_context_high->equity_24h` score `2.1778` n `193` status `ready` deltaP `15.7167` edge `0.5846` maxDD `-31.6316`
- `market_context_high->crypto_major_4h` score `0.8492` n `243` status `ready` deltaP `11.0728` edge `0.2262` maxDD `-14.0065`
- `market_context_high->equity_4h` score `0.4145` n `243` status `ready` deltaP `7.201` edge `0.1504` maxDD `-7.4425`
- `market_context_high->crypto_alt_4h` score `0.2987` n `243` status `ready` deltaP `8.1157` edge `0.1557` maxDD `-9.46`
- `market_context_high->fx_24h` score `-0.0547` n `193` status `ready` deltaP `16.8529` edge `0.0524` maxDD `-2.5447`
- `market_context_high->fx_1h` score `-0.2593` n `255` status `ready` deltaP `2.0072` edge `0.001` maxDD `-0.4764`
- `market_context_high->equity_1h` score `-0.4651` n `255` status `ready` deltaP `4.6108` edge `0.0312` maxDD `-5.0555`
- `market_context_high->metal_1h` score `-0.514` n `255` status `ready` deltaP `0.2888` edge `-0.0003` maxDD `-2.0682`
- `market_context_high->crypto_alt_1h` score `-0.5162` n `255` status `ready` deltaP `2.3001` edge `0.0378` maxDD `-5.0257`
- `market_context_high->crypto_major_1h` score `-0.7465` n `255` status `ready` deltaP `3.5758` edge `0.0385` maxDD `-6.9639`
- `market_context_high->commodity_1h` score `-0.8539` n `255` status `ready` deltaP `1.244` edge `-0.0029` maxDD `-3.7906`
- `market_context_high->index_1h` score `-0.9195` n `255` status `ready` deltaP `0.7526` edge `0.0052` maxDD `-0.9472`
- `market_context_high->fx_4h` score `-1.2046` n `243` status `ready` deltaP `3.3455` edge `0.0067` maxDD `-1.3415`
- `market_context_high->index_4h` score `-1.2991` n `243` status `ready` deltaP `-1.1969` edge `0.0086` maxDD `-3.04`
- `market_context_high->index_24h` score `-2.3841` n `193` status `ready` deltaP `8.1642` edge `0.0386` maxDD `-16.8946`
- `market_context_high->metal_4h` score `-2.9869` n `243` status `ready` deltaP `-13.5269` edge `-0.0544` maxDD `-11.7351`
- `market_context_high->commodity_4h` score `-3.7304` n `243` status `ready` deltaP `-1.5915` edge `-0.0327` maxDD `-14.071`
- `market_context_high->crypto_major_24h` score `-4.9024` n `193` status `ready` deltaP `3.4336` edge `0.0226` maxDD `-29.6555`
- `market_context_high->metal_24h` score `-8.4372` n `193` status `ready` deltaP `-14.0859` edge `-0.2517` maxDD `-32.8874`
- `market_context_high->commodity_24h` score `-12.3967` n `193` status `ready` deltaP `-12.16` edge `-0.0911` maxDD `-45.8715`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

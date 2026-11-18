# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T01:22:26.615187+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4173`

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

- `market_context_high->unknown_24h` score `1490.2434` n `98` status `ready` deltaP `3.4722` edge `124.1638` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.4496` n `98` status `ready` deltaP `46.5384` edge `1.9975` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.4089` n `98` status `ready` deltaP `32.0791` edge `1.8458` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4579` n `98` status `ready` deltaP `-0.2169` edge `0.0029` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8766` n `98` status `ready` deltaP `-1.2569` edge `0.177` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9169` n `98` status `ready` deltaP `15.3557` edge `0.1437` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0535` n `98` status `ready` deltaP `-5.0196` edge `-0.0029` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.218` n `98` status `ready` deltaP `-2.108` edge `0.0082` maxDD `-7.6911`
- `market_context_high->metal_4h` score `-1.271` n `98` status `ready` deltaP `6.2843` edge `-0.0171` maxDD `-6.1238`
- `market_context_high->fx_1h` score `-1.3173` n `98` status `ready` deltaP `-8.148` edge `-0.0008` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5694` n `98` status `ready` deltaP `-4.0599` edge `0.1841` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3334` n `98` status `ready` deltaP `-2.2852` edge `0.0075` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9275` n `98` status `ready` deltaP `-12.1982` edge `-0.0283` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-3.0121` n `98` status `ready` deltaP `-16.5709` edge `-0.0358` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.5694` n `98` status `ready` deltaP `-1.2373` edge `-0.0706` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6144` n `98` status `ready` deltaP `-25.4542` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.748` n `98` status `ready` deltaP `-18.8138` edge `-0.006` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8171` n `98` status `ready` deltaP `-27.5634` edge `-0.1216` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.549` n `98` status `ready` deltaP `-10.693` edge `-0.0989` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.8024` n `98` status `ready` deltaP `-18.8496` edge `-0.3391` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

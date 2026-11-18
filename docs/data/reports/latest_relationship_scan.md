# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T04:52:25.929301+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `48`

- Symbol pattern count: `4185`

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

- `market_context_high->unknown_24h` score `1464.495` n `98` status `ready` deltaP `3.4722` edge `122.0181` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.306` n `98` status `ready` deltaP `45.3231` edge `1.9872` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.0766` n `98` status `ready` deltaP `30.8638` edge `1.8113` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.3496` n `98` status `ready` deltaP `1.2801` edge `0.0068` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.7251` n `98` status `ready` deltaP `-0.0374` edge `0.1883` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.7825` n `98` status `ready` deltaP `15.3557` edge `0.1549` maxDD `-15.7982`
- `market_context_high->metal_4h` score `-0.9131` n `98` status `ready` deltaP `8.4184` edge `-0.0015` maxDD `-6.1238`
- `market_context_high->index_1h` score `-1.0006` n `98` status `ready` deltaP `-4.2711` edge `-0.0011` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1362` n `98` status `ready` deltaP `-1.3595` edge `0.0137` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3316` n `98` status `ready` deltaP `-8.2977` edge `-0.001` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.4273` n `98` status `ready` deltaP `-2.9928` edge `0.1952` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.2495` n `98` status `ready` deltaP `-1.8361` edge `0.0115` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6752` n `98` status `ready` deltaP `-10.0641` edge `-0.0215` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9211` n `98` status `ready` deltaP `-15.6727` edge `-0.0342` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.278` n `98` status `ready` deltaP `-0.1894` edge `-0.0533` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6108` n `98` status `ready` deltaP `-25.4542` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7672` n `98` status `ready` deltaP `-18.8138` edge `-0.0076` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.6108` n `98` status `ready` deltaP `-25.7342` edge `-0.1166` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.2844` n `98` status `ready` deltaP `-8.4361` edge `-0.0919` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.0417` n `98` status `ready` deltaP `-17.0203` edge `-0.2879` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

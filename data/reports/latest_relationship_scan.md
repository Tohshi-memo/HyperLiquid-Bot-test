# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T14:52:49.205966+00:00`
- Price records: `672`
- Market context records: `8640`
- Flow alert records: `8640`
- Minimum samples: `30`
- Pattern count: `24`

- Symbol pattern count: `2298`

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

- `market_context_high->unknown_24h` score `1363.6888` n `98` status `ready` deltaP `1.9097` edge `113.628` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `14.3349` n `98` status `ready` deltaP `40.462` edge `1.8951` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `12.7332` n `98` status `ready` deltaP `26.5235` edge `1.668` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.2476` n `98` status `ready` deltaP `2.7771` edge `0.0099` maxDD `-2.1461`
- `market_context_high->metal_4h` score `-0.5186` n `98` status `ready` deltaP `11.9245` edge `0.008` maxDD `-6.1238`
- `market_context_high->metal_24h` score `-0.5293` n `98` status `ready` deltaP `15.3557` edge `0.176` maxDD `-15.7982`
- `market_context_high->crypto_alt_4h` score `-0.6738` n `98` status `ready` deltaP `0.7248` edge `0.1898` maxDD `-17.1476`
- `market_context_high->index_1h` score `-0.9398` n `98` status `ready` deltaP `-3.2232` edge `-0.0003` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1721` n `98` status `ready` deltaP `-1.6589` edge `0.0111` maxDD `-7.6911`
- `market_context_high->crypto_major_4h` score `-1.2524` n `98` status `ready` deltaP `-2.6879` edge `0.2156` maxDD `-22.3259`
- `market_context_high->fx_1h` score `-1.37` n `98` status `ready` deltaP `-8.7468` edge `-0.0012` maxDD `-0.3721`
- `market_context_high->crypto_major_1h` score `-2.0997` n `98` status `ready` deltaP `-0.6385` edge `0.016` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.6058` n `98` status `ready` deltaP `-9.3019` edge `-0.0208` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9031` n `98` status `ready` deltaP `-15.6727` edge `-0.0327` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.0393` n `98` status `ready` deltaP `0.8585` edge `-0.0404` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.5986` n `98` status `ready` deltaP `-25.3018` edge `-0.0103` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7852` n `98` status `ready` deltaP `-18.8138` edge `-0.0091` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.2532` n `98` status `ready` deltaP `-22.9902` edge `-0.1051` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6764` n `98` status `ready` deltaP `-12.2555` edge `-0.0991` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-12.3884` n `98` status `ready` deltaP `-14.7337` edge `-0.2487` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

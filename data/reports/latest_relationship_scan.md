# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T01:52:31.605516+00:00`
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

- `market_context_high->unknown_24h` score `1490.0682` n `98` status `ready` deltaP `3.4722` edge `124.1492` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.4104` n `98` status `ready` deltaP `46.1912` edge `1.9948` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.3394` n `98` status `ready` deltaP `31.7319` edge `1.8392` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4665` n `98` status `ready` deltaP `-0.3666` edge `0.0028` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8562` n `98` status `ready` deltaP `-1.1044` edge `0.1786` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9121` n `98` status `ready` deltaP `15.3557` edge `0.1441` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0325` n `98` status `ready` deltaP `-4.7202` edge `-0.0022` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.1993` n `98` status `ready` deltaP `-1.9583` edge `0.0096` maxDD `-7.6911`
- `market_context_high->metal_4h` score `-1.2286` n `98` status `ready` deltaP `6.5891` edge `-0.0156` maxDD `-6.1238`
- `market_context_high->fx_1h` score `-1.3185` n `98` status `ready` deltaP `-8.148` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5599` n `98` status `ready` deltaP `-3.9074` edge `0.1843` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.319` n `98` status `ready` deltaP `-2.2852` edge `0.0087` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.8923` n `98` status `ready` deltaP `-11.8933` edge `-0.0274` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9834` n `98` status `ready` deltaP `-16.2715` edge `-0.0354` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.4855` n `98` status `ready` deltaP `-0.9379` edge `-0.0656` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6144` n `98` status `ready` deltaP `-25.4542` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7516` n `98` status `ready` deltaP `-18.8138` edge `-0.0063` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.7867` n `98` status `ready` deltaP `-27.2585` edge `-0.1211` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.5068` n `98` status `ready` deltaP `-10.3458` edge `-0.0977` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.7436` n `98` status `ready` deltaP `-18.8496` edge `-0.3342` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

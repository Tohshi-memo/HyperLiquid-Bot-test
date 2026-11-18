# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-18T01:37:38.508407+00:00`
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

- `market_context_high->unknown_24h` score `1490.1546` n `98` status `ready` deltaP `3.4722` edge `124.1564` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.4281` n `98` status `ready` deltaP `46.3648` edge `1.9959` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.3718` n `98` status `ready` deltaP `31.9055` edge `1.8422` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.4665` n `98` status `ready` deltaP `-0.3666` edge `0.0028` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8594` n `98` status `ready` deltaP `-1.1044` edge `0.1782` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9157` n `98` status `ready` deltaP `15.3557` edge `0.1438` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0434` n `98` status `ready` deltaP `-4.8699` edge `-0.0026` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2032` n `98` status `ready` deltaP `-1.9583` edge `0.0091` maxDD `-7.6911`
- `market_context_high->metal_4h` score `-1.2504` n `98` status `ready` deltaP `6.4367` edge `-0.0164` maxDD `-6.1238`
- `market_context_high->fx_1h` score `-1.3185` n `98` status `ready` deltaP `-8.148` edge `-0.0009` maxDD `-0.3721`
- `market_context_high->crypto_major_4h` score `-1.5584` n `98` status `ready` deltaP `-3.9074` edge `0.1845` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3226` n `98` status `ready` deltaP `-2.2852` edge `0.0084` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9105` n `98` status `ready` deltaP `-12.0458` edge `-0.0279` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-2.9978` n `98` status `ready` deltaP `-16.4212` edge `-0.0356` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.5322` n `98` status `ready` deltaP `-1.0876` edge `-0.0685` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6144` n `98` status `ready` deltaP `-25.4542` edge `-0.0106` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.7492` n `98` status `ready` deltaP `-18.8138` edge `-0.0061` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8025` n `98` status `ready` deltaP `-27.411` edge `-0.1214` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.5291` n `98` status `ready` deltaP `-10.5194` edge `-0.0984` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.7712` n `98` status `ready` deltaP `-18.8496` edge `-0.3365` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.

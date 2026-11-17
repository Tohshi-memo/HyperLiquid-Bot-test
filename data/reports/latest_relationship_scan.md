# Latest Relationship Scan

Mechanical scan for conditional relationships. This is not a trading signal; it is a candidate generator for private AI review and out-of-sample strategy work.

- Generated: `2026-11-17T23:22:27.341948+00:00`
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

- `market_context_high->unknown_24h` score `1490.9178` n `98` status `ready` deltaP `3.4722` edge `124.22` maxDD `0.0`
- `market_context_high->crypto_major_24h` score `15.6217` n `98` status `ready` deltaP `47.0592` edge `2.0161` maxDD `-22.8301`
- `market_context_high->crypto_alt_24h` score `14.6784` n `98` status `ready` deltaP `33.1208` edge `1.8734` maxDD `-13.3222`
- `market_context_high->metal_1h` score `-0.5109` n `98` status `ready` deltaP `-0.9654` edge `0.0011` maxDD `-2.1461`
- `market_context_high->crypto_alt_4h` score `-0.8032` n `98` status `ready` deltaP `-1.1044` edge `0.1854` maxDD `-17.1476`
- `market_context_high->metal_24h` score `-0.9078` n `98` status `ready` deltaP `15.5293` edge `0.1433` maxDD `-15.7982`
- `market_context_high->index_1h` score `-1.0815` n `98` status `ready` deltaP `-5.4687` edge `-0.0035` maxDD `-1.2295`
- `market_context_high->crypto_alt_1h` score `-1.2695` n `98` status `ready` deltaP `-2.5571` edge `0.0046` maxDD `-7.6911`
- `market_context_high->fx_1h` score `-1.3568` n `98` status `ready` deltaP `-8.5971` edge `-0.0011` maxDD `-0.3721`
- `market_context_high->metal_4h` score `-1.3654` n `98` status `ready` deltaP `5.6745` edge `-0.0209` maxDD `-6.1238`
- `market_context_high->crypto_major_4h` score `-1.4233` n `98` status `ready` deltaP `-3.755` edge `0.2008` maxDD `-22.3259`
- `market_context_high->crypto_major_1h` score `-2.3525` n `98` status `ready` deltaP `-2.5846` edge `0.0079` maxDD `-10.2705`
- `market_context_high->index_4h` score `-2.9203` n `98` status `ready` deltaP `-12.1982` edge `-0.0277` maxDD `-4.7471`
- `market_context_high->commodity_1h` score `-3.0014` n `98` status `ready` deltaP `-16.4212` edge `-0.0359` maxDD `-3.7125`
- `market_context_high->equity_1h` score `-3.6353` n `98` status `ready` deltaP `-1.6864` edge `-0.0731` maxDD `-11.1548`
- `market_context_high->fx_4h` score `-4.6132` n `98` status `ready` deltaP `-25.4542` edge `-0.0105` maxDD `-2.0058`
- `market_context_high->fx_24h` score `-6.6998` n `98` status `ready` deltaP `-18.4666` edge `-0.0043` maxDD `-5.8059`
- `market_context_high->commodity_4h` score `-7.8245` n `98` status `ready` deltaP `-27.7159` edge `-0.1212` maxDD `-14.6855`
- `market_context_high->index_24h` score `-8.6084` n `98` status `ready` deltaP `-10.8666` edge `-0.1027` maxDD `-20.7114`
- `market_context_high->equity_4h` score `-13.6392` n `98` status `ready` deltaP `-18.8496` edge `-0.3255` maxDD `-44.5018`

## Guardrails

- No future leakage: conditions use only data available at or before the price timestamp.
- Treat thin samples as watchlist items only.
- Private strategy code must rerun validation before entry, SL/TP, or sizing decisions.
